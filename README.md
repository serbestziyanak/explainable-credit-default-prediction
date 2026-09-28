# Explainable Machine Learning for Credit Card Default Prediction

**Reproducible analysis of discrimination, probability calibration, classification costs, and explanation reliability.**

This repository contains the Python notebook accompanying the article **“Kredi Temerrüt Tahmininde Açıklanabilir Makine Öğrenmesi: Ayrım Gücü, Kalibrasyon, Maliyet ve Açıklama Güvenilirliğinin Birlikte Değerlendirilmesi”** (*Explainable Machine Learning for Credit Default Prediction: A Joint Evaluation of Discrimination, Calibration, Cost, and Explanation Reliability*).

The study compares Logistic Regression, Random Forest, and XGBoost on the UCI **Default of Credit Card Clients** dataset. Its purpose is to show how the preferred model changes with the evaluation objective and with post-hoc probability calibration.

## Repository contents

| File | Description |
| --- | --- |
| [`makale_kredi_hakem_revizyonu.ipynb`](makale_kredi_hakem_revizyonu.ipynb) | Complete analysis, including the reviewer-requested calibration and explanation analyses. |
| [`LICENSE`](LICENSE) | MIT license for the code and repository documentation. |

The notebook writes result tables as `Table_*.csv` and figures as `Figure_*.png` to its working directory. These files can be regenerated from the notebook.

## Data source

The notebook retrieves the [Default of Credit Card Clients dataset](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) from the UCI Machine Learning Repository with `fetch_ucirepo(id=350)`. The dataset has 30,000 observations. The `ID` column is excluded from the model inputs.

The data are **not included** in this repository. Internet access is required when the data-loading cell runs. Consult the UCI record for the dataset's citation and usage terms; the MIT license in this repository does not cover the third-party dataset.

## Run in Google Colab

1. Open [`makale_kredi_hakem_revizyonu.ipynb`](makale_kredi_hakem_revizyonu.ipynb) in Google Colab.
2. Select **Runtime → Run all**. The first cell installs `ucimlrepo`, `xgboost`, `shap`, `lime`, and `openpyxl`. The notebook also uses NumPy, pandas, Matplotlib, SciPy, and scikit-learn.
3. Wait for every cell to finish and check for errors. Hyperparameter search and repeated LIME explanations may take time.
4. Save the executed notebook if the cell outputs should remain visible. Download generated CSV and PNG files from the Colab **Files** panel before the session ends; its working directory is temporary.

The notebook has been run in Colab, but dependency versions are not pinned. Results may vary with library versions and LIME's stochastic explanations. The main random seed is `42`.

## Analysis workflow

1. Split the data into stratified training (80%) and independent test (20%) sets.
2. Tune the three models on training data with five-fold stratified cross-validation using ROC-AUC.
3. Select F1-optimal and assumed-cost-optimal thresholds from training cross-validation predictions; evaluate them on the test set.
4. Compare ROC-AUC, Brier score, error costs, SHAP and LIME explanations, and descriptive subgroup error rates.
5. Compare sigmoid and isotonic probability calibration for Random Forest and XGBoost using training predictions; evaluate the selected method and reselected cost thresholds on the test set.
6. Measure SHAP–LIME feature-set overlap, full-feature rank agreement, direction agreement on shared top-five features, and LIME stability across 30 seeds for 10 observations.

### Reviewer-revision outputs

| Output | Contents |
| --- | --- |
| `Table_Calibration_Review.csv` | Selected calibration method and raw/calibrated test Brier and ROC-AUC. |
| `Table_Calibration_Cost_Review.csv` | Raw/calibrated thresholds and test costs for five false-negative/false-positive cost ratios. |
| `Table_Explanation_Rank_Direction_Review.csv` | Top-five overlap, full-feature rank correlation, and direction agreement for 100 test observations. |
| `Table_LIME_Rank_Stability_Review.csv` | Rank and direction stability across 30 LIME seeds for 10 observations. |

`Figure_Calibration_Curves.png` shows the **raw** model probabilities; it is not a plot of the post-calibration probabilities.

## Interpretation and limitations

- Hyperparameters are selected using the full training set before out-of-fold predictions are generated. This is **not fully nested cross-validation**. The test set is not used to select hyperparameters, calibration methods, or decision thresholds.
- The cost expression `C_FP × FP + C_FN × FN` uses assumed, constant error costs. It is not a measured monetary loss based on exposure at default, loss given default, or individual loan amounts.
- The Brier score measures overall squared probability error, not calibration alone. The small difference between calibrated models has not been subjected to a separate significance test.
- SHAP and LIME operate on different output scales in this notebook. Their contribution magnitudes should not be directly compared. Direction agreement applies only to features shared by both top-five lists.
- Results come from one public credit-card dataset and have not been externally validated on another portfolio.

## Citing this code

Cite the **specific tagged release** used for the paper, rather than the changing default branch. Once a release and, optionally, a Zenodo archive are available, replace this section with the actual release URL and DOI. A suggested reference format is:

> Ziyanak, S. (2026). *Explainable machine learning for credit card default prediction: Analysis code* (Version 1.0) [Computer software]. GitHub. URL of the tagged release

Until the release exists, do not cite a placeholder URL or DOI as if it were published.

## License

The original code and repository documentation are available under the [MIT License](LICENSE). The UCI dataset and third-party dependencies retain their respective terms.
