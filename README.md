# Explainable Machine Learning for Credit Card Default Prediction

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23010902.svg)](https://doi.org/10.5281/zenodo.23010902)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Reproducible machine-learning analysis of discrimination, probability calibration, decision costs, and explanation reliability in credit default prediction.

This repository contains the complete Python/Google Colab notebook accompanying the study:

> **Explainable Machine Learning for Credit Default Prediction: A Joint Evaluation of Discrimination, Calibration, Cost, and Explanation Reliability**

The study compares Logistic Regression, Random Forest, and XGBoost using the UCI *Default of Credit Card Clients* dataset. The analysis evaluates not only predictive discrimination, but also probability calibration, cost-sensitive decision thresholds, and the reliability of post-hoc explanations produced by SHAP and LIME.

---

## Repository Contents

| File | Description |
|---|---|
| `explainable_credit_default_prediction.ipynb` | Complete reproducible analysis notebook, including model training, evaluation, calibration, cost-sensitive analysis, SHAP, LIME, and explanation-stability experiments |
| `LICENSE` | MIT License covering the original source code and repository documentation |
| `README.md` | Repository documentation |

The notebook automatically generates result tables and figures during execution.

Generated tables are saved using the pattern:

```text
Table_*.csv
```

Generated figures are saved using the pattern:

```text
Figure_*.png
```

These files can be regenerated directly by executing the notebook.

---

## Data Source

The analysis uses the **Default of Credit Card Clients** dataset from the UCI Machine Learning Repository.

The notebook retrieves the dataset automatically using:

```python
fetch_ucirepo(id=350)
```

Dataset characteristics:

- Number of observations: **30,000**
- Prediction task: binary classification
- Target: credit-card default
- The `ID` variable is excluded from model inputs

The dataset itself is **not included in this repository**.

Internet access is therefore required when the data-loading cell is executed.

Dataset source:

https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients

The UCI dataset is third-party material and is not covered by the MIT License of this repository. Users should consult the UCI Machine Learning Repository for the dataset's citation and usage conditions.

---

## Machine Learning Models

The following models are evaluated:

- Logistic Regression
- Random Forest
- XGBoost

The models are compared using several complementary evaluation perspectives rather than relying on accuracy alone.

---

## Evaluation Metrics

Predictive performance is evaluated using metrics including:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Brier score
- Confusion matrix
- False-positive rate
- False-negative rate

The study also examines model behavior under alternative classification thresholds.

---

## Cost-Sensitive Evaluation

In addition to conventional predictive-performance metrics, the notebook evaluates models using an assumed classification-error cost function:

```text
Total Cost = C_FP × FP + C_FN × FN
```

where:

- `C_FP` is the assumed cost of a false positive,
- `C_FN` is the assumed cost of a false negative,
- `FP` is the number of false-positive predictions,
- `FN` is the number of false-negative predictions.

Decision thresholds are optimized using training data rather than fixed exclusively at `0.50`.

Multiple false-negative/false-positive cost ratios are examined to determine how operational assumptions affect model selection and threshold choice.

---

## Probability Calibration

Probability calibration is evaluated for Random Forest and XGBoost.

The notebook compares:

- raw model probabilities,
- sigmoid calibration,
- isotonic calibration.

Calibration methods are selected using training data and evaluated on the independent test set.

The analysis includes:

- Brier scores,
- ROC-AUC values,
- calibration curves,
- cost-sensitive thresholds after calibration.

This allows the study to distinguish between:

1. ranking ability,
2. probability quality,
3. decision usefulness.

---

## Explainable Artificial Intelligence

Two post-hoc explanation methods are used:

### SHAP

SHAP is used to quantify feature contributions based on Shapley-value principles.

The notebook includes analyses of:

- global feature importance,
- local explanations,
- feature rankings,
- explanation direction.

### LIME

LIME is used to generate local surrogate explanations for individual predictions.

The notebook evaluates:

- local feature importance,
- feature rankings,
- explanation direction,
- explanation stability across repeated runs.

---

## SHAP–LIME Agreement

The study goes beyond displaying SHAP and LIME visualizations and quantitatively investigates agreement between the two explanation techniques.

The notebook evaluates:

- top-feature overlap,
- Jaccard similarity,
- full-feature rank agreement,
- Spearman rank correlation,
- directional agreement for shared important features.

This analysis helps assess whether different explanation methods provide consistent interpretations of the same prediction.

---

## LIME Stability Analysis

Because LIME contains stochastic components, explanation stability is explicitly evaluated.

Selected observations are repeatedly explained using different random seeds.

The analysis examines:

- feature-set stability,
- ranking stability,
- directional stability,
- variation across repeated explanations.

The main experiments include repeated LIME explanations across **30 random seeds for 10 selected observations**.

---

## Analysis Workflow

The main experimental workflow is:

1. Retrieve the UCI dataset.
2. Remove the `ID` variable from model inputs.
3. Split the data using a stratified:
   - 80% training set
   - 20% independent test set
4. Perform hyperparameter optimization using five-fold stratified cross-validation.
5. Optimize models using ROC-AUC.
6. Generate out-of-fold training predictions.
7. Determine F1-optimal classification thresholds.
8. Determine cost-sensitive optimal thresholds.
9. Evaluate the final models on the independent test set.
10. Compare ROC-AUC and Brier scores.
11. Evaluate alternative cost assumptions.
12. Apply probability calibration to Random Forest and XGBoost.
13. Recalculate optimal thresholds after calibration.
14. Generate SHAP explanations.
15. Generate LIME explanations.
16. Measure SHAP–LIME agreement.
17. Analyze LIME explanation stability.
18. Perform descriptive subgroup error analysis.

The test set is not used for hyperparameter selection, calibration-method selection, or decision-threshold optimization.

---

## Main Generated Outputs

Important reviewer-revision outputs include:

| Output | Description |
|---|---|
| `Table_Calibration_Review.csv` | Selected calibration method and raw/calibrated test-set Brier score and ROC-AUC |
| `Table_Calibration_Cost_Review.csv` | Raw/calibrated thresholds and test costs under alternative false-negative/false-positive cost ratios |
| `Table_Explanation_Rank_Direction_Review.csv` | Top-feature overlap, full-feature rank agreement, and directional agreement |
| `Table_LIME_Rank_Stability_Review.csv` | LIME rank and direction stability across repeated random seeds |
| `Figure_Calibration_Curves.png` | Calibration curves for the evaluated model probabilities |

Additional tables and figures are generated throughout the notebook.

---

## Running the Analysis in Google Colab

The easiest way to reproduce the analysis is with Google Colab.

### Step 1

Open:

```text
explainable_credit_default_prediction.ipynb
```

in Google Colab.

### Step 2

Select:

```text
Runtime → Run all
```

### Step 3

The first cells install the required additional packages, including:

```text
ucimlrepo
xgboost
shap
lime
openpyxl
```

The notebook also uses:

- NumPy
- pandas
- Matplotlib
- SciPy
- scikit-learn

### Step 4

Allow all cells to finish execution.

Hyperparameter optimization and repeated LIME explanation experiments can require more computation than the standard model-evaluation sections.

### Step 5

Generated CSV and PNG files can be downloaded from the Colab Files panel.

Because the Colab working directory is temporary, generated files should be downloaded before the runtime session is terminated.

---

## Reproducibility

The main random seed used in the analysis is:

```python
random_state = 42
```

However, exact numerical results may vary slightly depending on:

- package versions,
- execution environment,
- XGBoost implementation differences,
- stochastic behavior in LIME.

The notebook was developed and tested using Google Colab.

Dependency versions are not currently pinned to a fixed environment.

---

## Interpretation and Limitations

Several methodological considerations should be kept in mind when interpreting the results.

### Hyperparameter tuning

Hyperparameters are selected using the complete training set before some out-of-fold predictions are generated.

Therefore, the procedure should not be interpreted as fully nested cross-validation.

The independent test set is not used for hyperparameter selection.

### Cost analysis

The cost function:

```text
C_FP × FP + C_FN × FN
```

uses assumed constant error costs.

It should not be interpreted as an estimate of actual monetary credit losses based on quantities such as:

- exposure at default,
- loss given default,
- outstanding balance,
- customer-level financial impact.

### Brier score

The Brier score measures overall squared probability error.

It reflects probability quality but should not be interpreted as a pure measure of calibration alone.

### SHAP and LIME

SHAP and LIME operate using different explanation mechanisms and output scales.

Their raw contribution magnitudes should therefore not be compared directly.

Directional agreement analyses are performed only for features appearing in both relevant explanation sets.

### External validity

The study uses a single publicly available credit-card dataset.

The results have not been externally validated using an independent financial-institution portfolio.

---

## Citation

If you use this code, notebook, or methodology in academic work, please cite the archived Zenodo release.

### Zenodo DOI

**https://doi.org/10.5281/zenodo.23010902**

Suggested citation:

> Ziyanak, S. (2026). *Explainable Machine Learning for Credit Card Default Prediction: A Joint Evaluation of Discrimination, Calibration, Cost, and Explanation Reliability* (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23010902

### BibTeX

```bibtex
@software{ziyanak_2026_credit_default,
  author    = {Ziyanak, Serbest},
  title     = {Explainable Machine Learning for Credit Card Default Prediction: A Joint Evaluation of Discrimination, Calibration, Cost, and Explanation Reliability},
  year      = {2026},
  version   = {1.0.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.23010902},
  url       = {https://doi.org/10.5281/zenodo.23010902}
}
```

---

## Code Availability

The complete analysis code is publicly available through both GitHub and Zenodo.

**GitHub**

https://github.com/serbestziyanak/explainable-credit-default-prediction

**Permanent Zenodo archive**

https://doi.org/10.5281/zenodo.23010902

For reproducibility, researchers are encouraged to cite and use the archived Zenodo release corresponding to the version used in the study rather than relying exclusively on the continuously updated GitHub default branch.

---

## License

The original source code and repository documentation are distributed under the **MIT License**.

See:

```text
LICENSE
```

for details.

The license does not apply to:

- the UCI dataset,
- third-party Python libraries,
- other externally licensed resources.

These materials retain their respective licenses and usage conditions.

---

## Author

**Serbest Ziyanak**

GitHub:  
https://github.com/serbestziyanak

---

## Permanent Archive

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23010902.svg)](https://doi.org/10.5281/zenodo.23010902)

**DOI:** https://doi.org/10.5281/zenodo.23010902
