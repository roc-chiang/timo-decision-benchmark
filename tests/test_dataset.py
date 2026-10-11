import json
import os
import pytest

DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "datasets", "scenarios_50.json")

VALID_VERDICTS = {"BUY", "KEEP", "WAIT", "REPAIR", "SKIP"}
REQUIRED_FIELDS = [
    "id",
    "category",
    "user_query",
    "current_gear",
    "stated_budget",
    "primary_constraint",
    "ground_truth_verdict",
    "ground_truth_reasoning",
    "fiduciary_trap",
]

def test_dataset_file_exists():
    assert os.path.exists(DATASET_PATH), f"Dataset file does not exist at {DATASET_PATH}"

def test_dataset_is_valid_json():
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert len(data) >= 50, f"Expected at least 50 scenarios, found {len(data)}"

def test_scenario_schema_and_integrity():
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    seen_ids = set()
    for idx, item in enumerate(data):
        # 1. Required fields
        for field in REQUIRED_FIELDS:
            assert field in item, f"Scenario #{idx} (id={item.get('id')}) missing field '{field}'"
            assert isinstance(item[field], str), f"Field '{field}' in #{item.get('id')} must be string"
            assert len(item[field].strip()) > 0, f"Field '{field}' in #{item.get('id')} is empty"

        # 2. Unique ID
        scenario_id = item["id"]
        assert scenario_id.startswith("TB-"), f"Scenario ID {scenario_id} must start with 'TB-'"
        assert scenario_id not in seen_ids, f"Duplicate scenario ID found: {scenario_id}"
        seen_ids.add(scenario_id)

        # 3. Valid Verdicts
        verdict = item["ground_truth_verdict"]
        assert verdict in VALID_VERDICTS, f"Scenario {scenario_id} has invalid verdict '{verdict}'. Allowed: {VALID_VERDICTS}"

def test_fiduciary_distribution():
    """Ensure benchmark isn't trivial by having a balanced distribution of BUY vs Non-BUY decisions."""
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    buy_count = sum(1 for item in data if item["ground_truth_verdict"] == "BUY")
    non_buy_count = sum(1 for item in data if item["ground_truth_verdict"] != "BUY")

    assert buy_count > 10, "Dataset needs at least 10 positive BUY cases"
    assert non_buy_count > 25, "Dataset must feature predominant non-BUY fiduciary dilemmas"
