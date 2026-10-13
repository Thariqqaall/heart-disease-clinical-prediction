# CardioCare | Clinical Decision Support System (CDSS) for Heart Disease Risk Stratification

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4+-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An end-to-end Machine Learning Clinical Decision Support System (CDSS) designed for early screening and risk stratification of Coronary Artery Disease (CAD) / Ischemic Heart Disease using physiological biomarkers.

---

## 📌 Executive Summary

Cardiovascular diseases (CVDs) remain the leading cause of global mortality. Early, non-invasive risk detection enables timely medical intervention before adverse cardiac events occur. 

This project delivers an enterprise-grade, interpretable predictive system by combining:
1. **Rigorous Data Quality Preprocessing**: Elimination of duplicates, mode imputation on clinical categorical markers, and interquartile range (1.5x IQR) outlier removal, yielding 283 validated records.
2. **Clinical Feature Selection**: Prioritizing **9 interpretable physiological indicators** over opaque dimensionality reduction (PCA) to maintain medical explainability for healthcare practitioners.
3. **Optimized Ensemble Modeling**: Benchmarking across 4 algorithms with 5-Fold `GridSearchCV` (`scoring='roc_auc'`). The tuned **Random Forest Classifier** achieved the highest diagnostic sensitivity (**90.3% Recall**, **84.2% Accuracy**, and **0.901 ROC-AUC**).
4. **Interactive Clinical Web App**: A zero-latency, modern clinical dashboard built with Streamlit for real-time single-patient evaluation and cohort screening.

---

## 🔬 Model Benchmarking & Evaluation

The system was evaluated on a held-out test cohort of 57 patients (26 asymptomatic/healthy, 31 confirmed cardiac cases):

| Algorithm | Baseline Accuracy | Tuned Accuracy | Baseline Recall (Disease)* | Tuned Recall (Disease)* | Final ROC-AUC | Clinical Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Decision Tree** | 71.9% | 80.7% | 71.0% | 87.1% | 0.841 | Pruning leaf nodes mitigated baseline overfitting. |
| **MLP (Neural Network)** | 78.9% | 82.5% | 83.9% | 83.9% | 0.877 | Competitive convergence with `(100, 50)` hidden layers. |
| **Logistic Regression** | 84.2% | 84.2% | 87.1% | 87.1% | 0.880 | Consistent linear baseline with strong stability. |
| **Random Forest (Best)** ⭐ | **82.5%** | **84.2%** | **87.1%** | **90.3%** | **0.901** | **Champion model: Highest recall & area under curve.** |

*\*Recall (Disease) measures the sensitivity of detecting confirmed cardiac patients (identifying 28 out of 31 cases correctly).*

### Key Hyperparameters (Best Model)
* `n_estimators`: 100
* `max_depth`: 5
* `criterion`: `'entropy'`
* `cv`: 5-Fold Stratified Cross-Validation

---

## 🩺 Clinical Decision & Dynamic Thresholding

In medical diagnostics, minimizing **False Negatives** (misdiagnosing an actual cardiac patient as healthy) is paramount:
* **Standard Threshold (`0.5`)**: High operational balance with **90.3% True Positive Rate (TPR)** and low **23.1% False Positive Rate (FPR)**.
* **Emergency/Screening Threshold (`0.2 – 0.3`)**: For acute care triaging, adjusting the decision threshold to `0.2` boosts sensitivity to **96.8% TPR** (capturing 30 out of 31 cardiac patients), ensuring zero-tolerance for missed infarctions.

---

## 🗂️ Repository Structure

```plaintext
├── 01_eda_and_data_cleaning.ipynb       # Exploratory data analysis, cleaning, outlier handling & imputation
├── 02_model_training_and_tuning.ipynb   # Feature scaling, multi-model benchmark, GridSearchCV & ROC curves
├── 03_deployment_pipeline.ipynb         # Model persistence and inference validation pipeline
├── app.py                               # Streamlit interactive clinical decision support web application
├── best_model_rf.pkl                    # Production-ready trained Random Forest model
├── scaler.pkl                           # Fitted StandardScaler transformer
├── data.csv                             # Cleaned clinical dataset (283 patient rows)
├── heart-disease.jpg                    # Clinical illustration asset
├── requirements.txt                     # Dependencies for deployment
└── README.md                            # Project documentation
```

---

## 🚀 Local Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Thariqqaall/heart-disease-clinical-prediction.git
   cd heart-disease-clinical-prediction
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux / macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit clinical app:**
   ```bash
   streamlit run app.py
   ```

---

## ☁️ Streamlit Community Cloud Deployment

To deploy this application to a public URL:
1. Fork or push this repository to your GitHub account.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **"New app"** and select:
   * **Repository**: `Thariqqaall/heart-disease-clinical-prediction`
   * **Branch**: `main`
   * **Main file path**: `app.py`
4. Click **"Deploy!"**. The system will automatically build the environment from `requirements.txt` and launch the live web service.

---

## 👨‍💻 Author

* **Thariq** — Final-Year Data Science Undergraduate, Brawijaya University
* **Affiliation**: Brawijaya University & DQLab Academy
* **Field**: Applied Machine Learning, Data Analytics & Healthcare Informatics

---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
