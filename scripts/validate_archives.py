#!/usr/bin/env python3
"""Validate the shipped PAPER-mode ZIPs using the Python standard library.

Not a full rerun of training or a proof of statistical validity.
"""
from __future__ import annotations
from pathlib import Path
import csv
import io
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
EXPECTED = {
    "kredi_ek_deney_sonuclari_paper.zip": (
        "manifest.json",
        {
            "tuning.csv", "fold_metrics.csv", "pooled_metrics.csv",
            "pooled_predictions.csv", "decisions.csv", "cost_summary.csv",
            "paired_brier_bootstrap.csv", "paired_cost_bootstrap.csv",
        },
    ),
    "kredi_xai_sonuclari_paper.zip": (
        "xai_manifest.json",
        {
            "xai_cases.csv", "xai_summary.csv", "xai_paired_comparisons.csv",
            "lime_stability.csv", "prediction_reproducibility.csv",
        },
    ),
    "kredi_xai_saglamlik_sonuclari_paper.zip": (
        "robustness_manifest.json",
        {
            "lime_case_repeats.csv", "summary_by_config.csv", "summary_by_cohort.csv",
            "paired_config_comparisons.csv", "paired_calibration_comparisons.csv",
            "lime_seed_stability.csv", "lime_seed_stability_summary.csv",
            "prediction_reproducibility.csv",
        },
    ),
}


def read_rows(archive: zipfile.ZipFile, file: str):
    with archive.open(file) as raw:
        yield from csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig"))


def main() -> None:
    for filename, (manifest, required) in EXPECTED.items():
        path = RESULTS / filename
        assert path.is_file(), f"Archive missing: {path}"
        with zipfile.ZipFile(path) as archive:
            assert archive.testzip() is None, f"Bad ZIP member: {filename}"
            assert {manifest, *required}.issubset(set(archive.namelist())), filename
            metadata = json.loads(archive.read(manifest))
            assert metadata.get("mode") == "PAPER", (filename, metadata.get("mode"))
            print(f"OK: {filename}; {len(archive.namelist())} members; PAPER mode")
            if manifest == "manifest.json":
                assert metadata["outer_folds"] == 5
                assert metadata["datasets"]["Taiwan_Credit_Default"]["n"] == 30000
                assert metadata["datasets"]["South_German_Credit"]["n"] == 1000
                total = 0
                for row in read_rows(archive, "pooled_predictions.csv"):
                    assert row["Probability"] in ("raw", "calibrated")
                    assert 0 <= float(row["P"]) <= 1
                    total += 1
                assert total == 310000, f"Unexpected pooled predictions: {total}"
                print(f"    pooled_predictions.csv: {total} rows")
            elif manifest == "xai_manifest.json":
                assert metadata["n_cases"] == 320
                assert metadata["n_stability"] == 240
                assert metadata["reproducibility_max_error"] < 1e-8
                cases = sum(1 for _ in read_rows(archive, "xai_cases.csv"))
                assert cases == 320
                print(f"    xai_cases.csv: {cases} rows")
            else:
                assert metadata["case_repeats"] == 1920
                assert metadata["unique_explained_cases"] == 960
                assert metadata["reproducibility_max_error"] < 1e-8
                cases = sum(1 for _ in read_rows(archive, "lime_case_repeats.csv"))
                assert cases == 1920
                print(f"    lime_case_repeats.csv: {cases} rows")
    print("PASS: All three PAPER archives, expected schemas, counts, and manifests validated.")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, KeyError, zipfile.BadZipFile, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
