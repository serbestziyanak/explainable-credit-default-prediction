# Released PAPER-mode experiment results

The data here are the **archived outputs provided by the researcher**, not values regenerated at packaging time.

| Archive | Source notebook | Contents |
| --- | --- | --- |
| `kredi_ek_deney_sonuclari_paper.zip` | `01_prediction_calibration_cost.ipynb` | `manifest.json`, `tuning.csv`, `fold_metrics.csv`, `pooled_metrics.csv`, `pooled_predictions.csv`, `decisions.csv`, `cost_summary.csv`, `paired_brier_bootstrap.csv`, `paired_cost_bootstrap.csv` |
| `kredi_xai_sonuclari_paper.zip` | `02_shap_lime_validation.ipynb` | `xai_manifest.json`, `xai_cases.csv`, `xai_summary.csv`, `xai_paired_comparisons.csv`, `lime_stability.csv`, `prediction_reproducibility.csv` |
| `kredi_xai_saglamlik_sonuclari_paper.zip` | `03_lime_fidelity_robustness.ipynb` | `robustness_manifest.json`, `lime_case_repeats.csv`, `summary_by_config.csv`, `summary_by_cohort.csv`, `paired_config_comparisons.csv`, `paired_calibration_comparisons.csv`, `lime_seed_stability.csv`, `lime_seed_stability_summary.csv`, `prediction_reproducibility.csv` |

All three archives were generated with `MODE = PAPER`; run `python scripts/validate_archives.py` to check archive structure and metadata without training models.

**Data caution:** `pooled_predictions.csv` includes record indices, public-dataset binary class labels, and fitted predicted probabilities. The source raw credit records are *not* included. Bootstrap uncertainty is conditional on fixed fitted models.
