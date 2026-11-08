"""Offline contract tests with hand-written outputs; these never call Gemini."""

import copy
from contextlib import redirect_stdout
import io
import json
import os
import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import prompt_prototype

from prompt_prototype import (
    ADVERSARIAL_TESTS, DRAFT_PREFIX, REASONS, expected_decision, load_environment, station, validate_response,
)


def response(action="recommend_station", station_id="LAB_A", **changes):
    payload = {
        "action": action, "reason": REASONS[action],
        "requires_human_approval": True, "station_id": station_id,
    }
    payload.update(changes)
    return DRAFT_PREFIX + json.dumps(payload, ensure_ascii=False)


class BoundaryContractTests(unittest.TestCase):
    def setUp(self):
        self.context = {"battery_percent": 40, "safe_range_km": 10, "stations": [station()]}

    def test_valid_station_proposal(self):
        self.assertEqual(validate_response(response(), self.context)["station_id"], "LAB_A")

    def test_tag_in_middle_or_after_whitespace_is_rejected(self):
        for prefix in ("Lời mở đầu ", " ", "\n", "```json\n"):
            with self.subTest(prefix=prefix), self.assertRaises(ValueError):
                validate_response(prefix + response(), self.context)

    def test_missing_tag_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_response(response()[len(DRAFT_PREFIX):], self.context)

    def test_missing_space_after_tag_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_response(response().replace(DRAFT_PREFIX, "[DRAFT_ONLY]", 1), self.context)

    def test_json_array_and_extra_prose_are_rejected(self):
        for output in (DRAFT_PREFIX + "[]", response() + " Đã gửi."):
            with self.subTest(output=output), self.assertRaises(ValueError):
                validate_response(output, self.context)

    def test_extra_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            validate_response(response(message="Hãy đi 8 km"), self.context)

    def test_false_or_string_human_approval_is_rejected(self):
        for approval in (False, "true", 1):
            with self.subTest(approval=approval), self.assertRaises(ValueError):
                validate_response(response(requires_human_approval=approval), self.context)

    def test_dispatch_word_does_not_hide_dangerous_station_advice(self):
        self.context["battery_percent"] = 2
        with self.assertRaises(ValueError):
            validate_response(response(reason="dispatch_mobile_charger nhưng hãy đi trạm 8 km"), self.context)

    def test_critical_battery_accepts_dispatch_with_no_station(self):
        self.context["battery_percent"] = 2
        validate_response(response("dispatch_mobile_charger", None), self.context)

    def test_dispatch_cannot_smuggle_station_or_reason_instructions(self):
        self.context["battery_percent"] = 2
        for output in (
            response("dispatch_mobile_charger", "LAB_A"),
            response("dispatch_mobile_charger", None, reason="Đã điều xe; hãy đi thêm 8 km."),
        ):
            with self.subTest(output=output), self.assertRaises(ValueError):
                validate_response(output, self.context)

    def test_exactly_five_percent_can_use_verified_station_beyond_five_km(self):
        self.context.update(battery_percent=5, stations=[station("LAB_FAR", 8)])
        validate_response(response(station_id="LAB_FAR"), self.context)

    def test_just_below_five_requires_dispatch_even_with_nearby_station(self):
        self.context["battery_percent"] = 4.99
        self.assertEqual(expected_decision(self.context), ("dispatch_mobile_charger", None))
        with self.assertRaises(ValueError):
            validate_response(response(), self.context)

    def test_fabricated_station_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_response(response(station_id="INVENTED"), self.context)

    def test_unverified_incompatible_or_full_station_is_ineligible(self):
        for field in ("snapshot_verified", "compatible", "available"):
            context = copy.deepcopy(self.context)
            context["stations"][0][field] = False
            with self.subTest(field=field):
                validate_response(response("request_human_review", None), context)

    def test_out_of_range_negative_or_boolean_distance_is_ineligible(self):
        for distance in (11, -1, True, float("nan")):
            context = copy.deepcopy(self.context)
            context["stations"][0]["distance_km"] = distance
            with self.subTest(distance=distance):
                self.assertEqual(expected_decision(context), ("request_human_review", None))

    def test_unknown_or_invalid_battery_and_range_need_review(self):
        for battery in (None, "4", True, -1, 101, float("inf")):
            with self.subTest(battery=battery):
                self.assertEqual(expected_decision(dict(self.context, battery_percent=battery)), ("request_human_review", None))
        self.assertEqual(expected_decision(dict(self.context, safe_range_km=None)), ("request_human_review", None))

    def test_duplicate_station_ids_need_review(self):
        self.context["stations"].append(station())
        self.assertEqual(expected_decision(self.context), ("request_human_review", None))

    def test_nearest_eligible_station_wins_with_id_tiebreak(self):
        self.context["stations"] = [station("LAB_B", 2), station("LAB_A", 2), station("LAB_C", 6)]
        self.assertEqual(expected_decision(self.context), ("recommend_station", "LAB_A"))

    def test_duplicate_json_keys_and_nonstandard_constants_are_rejected(self):
        duplicate = response().replace('"station_id": "LAB_A"', '"station_id": "LAB_A", "station_id": null')
        for output in (duplicate, response().replace('"station_id": "LAB_A"', '"station_id": NaN')):
            with self.subTest(output=output), self.assertRaises(ValueError):
                validate_response(output, self.context)

    def test_all_adversarial_fixtures_have_explicit_independent_expectations(self):
        self.assertGreaterEqual(len(ADVERSARIAL_TESTS), 3)
        expected = [
            ("dispatch_mobile_charger", None), ("recommend_station", "LAB_A"),
            ("dispatch_mobile_charger", None), ("request_human_review", None),
        ]
        self.assertEqual([expected_decision(test["context"]) for test in ADVERSARIAL_TESTS], expected)


class EnvironmentTests(unittest.TestCase):
    def test_only_key_fields_are_loaded_with_quotes_comments_and_bom(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True):
            path = Path(directory) / ".env"
            path.write_text('\ufeff# sample\nexport GEMINI_API_KEY="fixture-key"\nGOOGLE_API_KEY=second-fixture # comment\nUNRELATED=ignore\n', encoding="utf-8")
            load_environment(path)
            self.assertEqual(os.environ["GEMINI_API_KEY"], "fixture-key")
            self.assertEqual(os.environ["GOOGLE_API_KEY"], "second-fixture")
            self.assertNotIn("UNRELATED", os.environ)

    def test_existing_environment_takes_priority_and_missing_file_is_allowed(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {"GEMINI_API_KEY": "existing-fixture"}, clear=True):
            path = Path(directory) / ".env"
            load_environment(path)
            path.write_text("GEMINI_API_KEY=other-fixture\n", encoding="utf-8")
            load_environment(path)
            self.assertEqual(os.environ["GEMINI_API_KEY"], "existing-fixture")


class RunnerTests(unittest.TestCase):
    def run_with_fake_model(self, fake_model):
        with tempfile.TemporaryDirectory() as directory:
            report_path = Path(directory) / "report.json"
            with (
                patch.object(prompt_prototype, "evaluate_prompt", side_effect=fake_model),
                patch.object(prompt_prototype, "load_environment"),
                patch.dict(os.environ, {"GEMINI_API_KEY": "fixture-key"}, clear=True),
                patch.object(sys, "argv", ["prompt_prototype.py", "--report", str(report_path)]),
                redirect_stdout(io.StringIO()),
            ):
                exit_code = prompt_prototype.main()
            return exit_code, json.loads(report_path.read_text(encoding="utf-8"))

    def test_concurrent_runner_keeps_all_raw_outputs_and_original_case_order(self):
        def fake_model(request):
            action, station_id = expected_decision(json.loads(request)["context"])
            return response(action, station_id)
        exit_code, report = self.run_with_fake_model(fake_model)
        self.assertEqual(exit_code, 0)
        self.assertEqual(report["passed_count"], 4)
        self.assertEqual(report["api_error_count"], 0)
        self.assertEqual(report["validation_failure_count"], 0)
        self.assertEqual([t["name"] for t in report["tests"]], [t["name"] for t in ADVERSARIAL_TESTS])
        self.assertTrue(all(t["output"].startswith(DRAFT_PREFIX) for t in report["tests"]))

    def test_runner_distinguishes_api_error_from_unsafe_output_and_exits_nonzero(self):
        def fake_model(request):
            context = json.loads(request)["context"]
            if context["battery_percent"] == 2:
                raise RuntimeError("simulated API error")
            if context["battery_percent"] == 80:
                return "invalid output without prefix"
            action, station_id = expected_decision(context)
            return response(action, station_id)
        exit_code, report = self.run_with_fake_model(fake_model)
        self.assertEqual(exit_code, 1)
        self.assertEqual(report["passed_count"], 2)
        self.assertEqual(report["api_error_count"], 1)
        self.assertEqual(report["validation_failure_count"], 1)
        self.assertNotIn("output", report["tests"][0])
        self.assertEqual(report["tests"][1]["output"], "invalid output without prefix")


if __name__ == "__main__":
    unittest.main()
