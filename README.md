
# Canadian Credit Risk Prediction & Insights Dashboard

End-to-End Credit Risk Analysis | Streamlit UI | SHAP Explainability | Power BI Dashboard

## Project Overview

This project demonstrates **complete end-to-end execution** of a Canadian credit risk analytics solution. From **raw data cleaning** to  **predictive modeling** ,  **explainable AI** , and  **interactive dashboards** , this project showcases my ability to deliver actionable insights for financial institutions.

**Key Achievements:**

* Built a **credit risk prediction model** using Canadian lending and macroeconomic data
* Designed **interactive Streamlit UI** for business users to upload datasets and get predictions instantly
* Integrated **SHAP explainability** to show which features drive risk predictions
* Developed a **Power BI dashboard** to monitor credit risk trends, distributions, and feature impacts

---

## Business Problem

Financial institutions need **early warning indicators** to identify rising credit risk driven by:

* Credit expansion or contraction
* Volatility in lending behavior
* Sudden macroeconomic shifts

This project answers:

> *Can publicly available Canadian credit data be transformed into a transparent and explainable credit risk framework?*

---

## Solution Approach (End-to-End)

### 1. Data Collection

* Source: **Bank of Canada / Statistics Canada**
* Data Type: Monthly aggregate credit measures (business & household)

---

### 2. Data Cleaning

* Handled missing values
* Standardized column names
* Converted date fields
* Removed non-numeric noise for modeling

Notebook: `01_data_cleaning.ipynb`

---

### 3. Exploratory Data Analysis (EDA)

* Credit growth trends
* Volatility patterns
* Distribution analysis
* Correlation insights

Notebook: `02_exploratory_data_analysis.ipynb`

---

### 4. Feature Engineering (Core Strength of This Project)

Created **risk-relevant features** such as:

* Rolling averages
* Credit growth rates
* Credit volatility (rolling std)
* Trend indicators
* Created derived features: `Credit_Type`, rolling averages, month-over-month changes
* Handled categorical and numeric features for modeling

Notebook: `03_feature_engineering.ipynb`

---

### 5. Target Definition & Modeling

* Engineered a **credit risk target** using a composite risk score
* Converted into:
  * Binary Risk (Low / High)
* Models used:
  * Logistic Regression (interpretable baseline)

Key challenges addressed:

* Class imbalance
* Small macroeconomic dataset
* Stratified validation constraints

Saved artifacts for deployment:

* `credit_risk_model.pkl`
* `label_encoder.pkl`
* `feature_names.pkl`

Notebook: `04_target_definition_and_modeling.ipynb`

---

### 6. Model Evaluation & Explainability

* Performance metrics:
  * Accuracy
  * Precision / Recall
* **Explainability using SHAP**
  * Identified key drivers of high credit risk
  * Explained model behavior to non-technical stakeholders

Notebook: `05_model_evaluation_and_explainability.ipynb`

---

### 7. Results & Business Insights

Translated model outputs into  **business-ready insights** :

* What increases credit risk?
* How volatility acts as an early warning signal
* How this model can support decision-making

Notebook: `06_results_and_business_insights.ipynb`

## Streamlit UI

* Interactive web interface for **predicting credit risk** from new datasets
* Visualizes **SHAP feature importance**
* Exports predictions and SHAP summary for dashboard integration
* Run locally:

  `streamlit run Credit_Risk_App.py`

---

## Power BI Dashboard

* **Credit Risk Overview:** Total accounts, % High/Low risk, risk distribution
* **Credit Trends Over Time:** Total balances, growth, and volatility
* **Model Explainability:** Top features driving risk predictions
* Filters: **Month, Credit Type, Predicted Risk**
* Fully interactive and suitable for executive decision-making

## **Business Impact**

* **High volatility and rapid credit growth** identified as key risk drivers
* **Stable credit trends** linked to lower predicted risk
* **Early interventions** recommended for high-risk segments
* Visualizations and KPIs enable **real-time monitoring** of credit portfolios

## **Output**

* **`predicted_credit_risk.csv`** – Predictions per account
* **`shap_summary.csv`** – Feature impact per prediction
* **Power BI Dashboard** – Executive insights and trend monitoring
* **Streamlit App** – Interactive UI for real-time credit risk predictions and SHAP-based explainability

## Business Applications

### For Banks

* Portfolio risk monitoring
* Credit policy support
* Early warning dashboards

### For Regulators

* Systemic risk surveillance
* Macroprudential analysis

### For Risk & Analytics Teams

* Scenario analysis
* Stress testing frameworks
* Model explainability demonstrations

---

## Limitations

* Uses **aggregate macroeconomic data**
* Target variable is  **engineered** , not default-based
* Intended as a  **framework demonstration** , not production scoring

---

## Future Enhancements

* Add borrower-level or sector-level data
* Incorporate interest rates, CPI, unemployment
* Time-series models (LSTM / ARIMA)

---

## Tech Stack

* **Languages & Libraries:** Python 3.11, pandas, numpy, scikit-learn, matplotlib, seaborn, shap, joblib, streamlit
* **Machine Learning Models:** Logistic Regression, XGBoost, LightGBM
* **Visualization:** Power BI for interactive dashboards

---

## **Project Highlights**

* End-to-end **data science lifecycle execution**
* Integration of **AI explainability (SHAP)** for business trust
* Deployment-ready **Streamlit UI** for user interaction
* Actionable insights via **Power BI dashboard**

---

## **How to Use**

1. Run all Jupyter notebooks sequentially (`01 → 06`) to process data and train the model
2. Open **Streamlit App** to test predictions and visualize SHAP features:
   `streamlit run Credit_Risk_App.py`
3. Load `predicted_credit_risk.csv` and `shap_summary.csv` in **Power BI** for interactive dashboards

## Author

**Kirti Sinha** – Data & AI Specialist | Agile Practitioner | Dashboard Developer | Canada

Connect to discuss how I can help your organization make  **data-driven credit decisions** .
