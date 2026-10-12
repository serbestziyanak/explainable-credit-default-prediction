# Decision-Aware and Explainable Machine Learning for Credit Risk Prediction

**Reproducible code, cross-validated predictions, and explainability robustness results** accompanying the manuscript:

> **Beyond Discrimination: Interactions of Class Weighting, Probability Calibration, Decision Costs, and Local Explanation Reliability in Credit Risk Prediction**

[Repository](https://github.com/serbestziyanak/explainable-credit-default-prediction) · [Results documentation](results/README.md)

## Overview

This repository provides the analysis notebooks and the **PAPER-mode output archives** for an empirical, two-dataset study of how predictive discrimination, probability calibration, asymmetric classification costs, and local explanation reliability can yield different model preferences.

The analysis is **not** presented as a new classification algorithm or an instance-dependent economic loss estimator. Its contribution is an evaluation protocol that explicitly distinguishes:

1. Class-weighted versus unweighted learning and the effects of sigmoid probability calibration.
2. ROC-AUC and Brier score from threshold-dependent, asymmetric misclassification losses.
3. SHAP–LIME explanation agreement from the fidelity and repeatability of local LIME surrogates.
4. Results from the two historical public credit datasets, without claiming broad contemporary generalization.

## Data sources

| Dataset | Source | Observations | Predictor columns | Positive target (1) |
| --- | --- | ---: | ---: | --- |
| Default of Credit Card Clients | [UCI ID 350](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) | 30,000 | 23 | Default next month (6,636 cases; 22.12%) |
| South German Credit | [UCI ID 573](https://archive.ics.uci.edu/dataset/573/south+german+credit+update) | 1,000 | 20 | Bad credit (300 cases; 30%) |

South German Credit is downloaded **from the official UCI ZIP** rather than `fetch_ucirepo(id=573)`, which does not support direct import for this dataset. The script maps the original label convention so `1` consistently indicates the higher-risk class.

The datasets are **not redistributed** in this repository. Notebook execution requires internet access to the original public sources and remains subject to their availability and conditions of use.

## Repository layout

```text
explainable-credit-default-prediction/
├── README.md
├── CITATION.cff
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   ├── 01_prediction_calibration_cost.ipynb
│   ├── 02_shap_lime_validation.ipynb
│   └── 03_lime_fidelity_robustness.ipynb
├── results/
│   ├── kredi_ek_deney_sonuclari_paper.zip
│   ├── kredi_xai_sonuclari_paper.zip
│   ├── kredi_xai_saglamlik_sonuclari_paper.zip
│   └── README.md
├── figures/
│   ├── fig1_brier.png
│   ├── fig2_xai.png
│   └── fig3_robustness.png
├── environment/
│   └── recorded_versions.json
├── scripts/
│   └── validate_archives.py

```

The three `ipynb` files are the **corrected, experiment-producing versions**. Earlier single-test-split exploratory notebooks are not part of this release and should not be used to recreate the updated paper's tables.

## Reproduce the analysis on Google Colab

**Run in the order listed.** The paper's reported statistics use `MODE = 'PAPER'`; `FAST` is solely a debugging smoke test.

1. **Prediction, calibration, and costs:** Open [`notebooks/01_prediction_calibration_cost.ipynb`](notebooks/01_prediction_calibration_cost.ipynb) in Google Colab. In the settings cell change `MODE = 'FAST'` to `MODE = 'PAPER'` and run all cells. The expected downloadable file is `kredi_ek_deney_sonuclari_paper.zip`. This step uses a five-fold stratified *outer* evaluation and three-fold *inner* hyperparameter search, comparing logistic regression, Random Forest, and weighted/unweighted tree ensembles.
2. **Explainability validation:** Open [`notebooks/02_shap_lime_validation.ipynb`](notebooks/02_shap_lime_validation.ipynb); set `MODE = 'PAPER'` and upload the **first** PAPER ZIP when prompted. It refits matching outer-fold XGBoost models and validates that their predictions reproduce the previously stored probabilities. It then computes probability-scale SHAP–LIME agreement and LIME seed stability. Expected output: `kredi_xai_sonuclari_paper.zip`.
3. **LIME fidelity and robustness:** Open [`notebooks/03_lime_fidelity_robustness.ipynb`](notebooks/03_lime_fidelity_robustness.ipynb); set `MODE = 'PAPER'`, and upload **both earlier PAPER ZIPs** when prompted. This tests LIME discretization and kernel width, in-sample and held-out-neighborhood weighted \(R^2\), sample sensitivity, and seed stability. Expected output: `kredi_xai_saglamlik_sonuclari_paper.zip`.

The existing results archives in [`results/`](results/) contain the **actual completed PAPER-mode outputs**, so it is not necessary to rerun computationally intensive cells merely to inspect or validate the published data tables. For Colab, upload input ZIPs into `/content/` or use the notebooks' file-picker dialog.

### Running locally (optional)

The experiments were conducted in Python 3.13.16 with the principal package versions recorded in [`environment/recorded_versions.json`](environment/recorded_versions.json). For a compatible local environment:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows (cmd.exe): .venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pip install jupyterlab
jupyter lab
```

The notebooks were designed primarily for **Colab**: `%pip` cells install packages independently; file upload/download widgets rely on Colab when the expected ZIPs are not already present. Local execution may require adapting the two input ZIP paths to your local filesystem. Python and package versions, particularly SHAP and scikit-learn, can affect exact output consistency.

## Check released results without retraining

From the repository root:

```bash
python scripts/validate_archives.py
```

This checks the three ZIP archives, study manifests, required output tables, expected PAPER-mode study sizes, and the XAI model-prediction reproduction tolerances. **This is an archive-integrity/schema check, not a claim that training has been rerun in this environment.**

## Selected illustrative findings

For the Taiwan credit-default dataset, the pooled outer-fold results include:

| Model / probabilities | ROC-AUC | Brier score |
| --- | ---: | ---: |
| Unweighted XGBoost, raw | 0.7838 | 0.1337 |
| Unweighted XGBoost, sigmoid-calibrated | 0.7838 | 0.1346 |
| Weighted XGBoost, raw | 0.7831 | 0.1788 |
| Weighted XGBoost, sigmoid-calibrated | 0.7831 | 0.1341 |

The extended LIME experiment also showed that for **weighted XGBoost on Taiwan** the held-out-neighborhood weighted \(R^2\) increased from **0.187 to 0.455** for raw probabilities when continuous variables were left *undiscretized*, while top-five SHAP–LIME Jaccard agreement decreased from **0.548 to 0.351**. Thus fidelity and inter-method agreement should not be treated as interchangeable measures of explanation quality.

These are **descriptive results in the stated experimental protocol**, not universal causal statements. Confidence intervals based on resampling fixed out-of-fold predictions do **not** incorporate model-retraining variability.

## Statistical and interpretive limitations

- Both datasets are historical; the smaller German dataset contains only 1,000 records. Cross-dataset differences alone cannot establish generalization to current lending portfolios.
- Misclassification costs are **fixed hypothetical ratios** (`C_FP = 1`, `C_FN = 1, 2, 3, 5, or 10`); they are not measured currency-denominated losses, nor EAD/LGD-based customer-level costs.
- The SHAP–LIME experiments examine selected, stratified test cases and specific perturbation/background assumptions. Local surrogate fidelity is evaluated on independent synthetic neighborhood samples, *not* on independent real-world borrowers.
- Pooled cross-validation comparisons and paired bootstrap intervals are conditional on the fitted outer-fold models and sampling choices.
- The experiments do not establish non-discrimination, deployability, or model fairness.

## Figures and released outputs

The `figures/` directory contains the **manuscript figure images**. Raw output tables and processing metadata are stored in the three result ZIPs. The figures are supplied as final visual assets; there is no claim that a figure-generation script is included in this release.

For an inventory of each archive's contents, see [`results/README.md`](results/README.md).

## Citation and DOI

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23312634.svg)](https://doi.org/10.5281/zenodo.23312634)

**Version-specific archived release DOI:** [10.5281/zenodo.23312634](https://doi.org/10.5281/zenodo.23312634)  
**GitHub repository:** https://github.com/serbestziyanak/explainable-credit-default-prediction  
**Software version described by this repository:** `v2.0.0`

The Zenodo DOI above was supplied by the author for the released code and results. See [`CITATION.cff`](CITATION.cff) for machine-readable citation information. The earlier DOI [10.5281/zenodo.23010902](https://doi.org/10.5281/zenodo.23010902) identifies an earlier deposit and should **not** be cited for the two-dataset, calibration, XAI, and LIME-fidelity experiments described here.

### Suggested software citation

> Ziyanak, S. (2026). *Decision-aware and explainable machine learning for credit risk prediction: Reproducible experiments* (Version 2.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23312634

**Archived releases are immutable.** Updating this GitHub README or `CITATION.cff` *after* the GitHub release was published does not retroactively alter its associated Zenodo snapshot. Check the record's file list and version before using the DOI in a submission. For an additional archived update, publish a separate new version only if the contents or metadata need to change.

## Authorship and licensing

Code/analysis attribution in this release: **Serbest Ziyanak**. Review and update `CITATION.cff` if the final code has additional contributors. **No software license is declared in this archive** because the rights-holder has not yet selected one. Before public release, explicitly choose a license (e.g., MIT if appropriate) or intentionally retain all rights. Do not assume publicly readable code is automatically open-source licensed.

If submitting the paper to a double-anonymous journal, check that journal's code-sharing and author-identification policy before providing an identifying public repository URL in the blinded manuscript.
