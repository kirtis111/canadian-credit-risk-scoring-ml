import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Canadian Credit Risk Dashboard",
    layout="wide"
)

st.title("Canadian Credit Risk Analysis & Explainability")
st.markdown("""
This dashboard predicts **Credit Risk** using Canadian macroeconomic credit data and explains the predictions using SHAP values.
""")

# -----------------------------
# Load Trained Artifacts
# -----------------------------
model = joblib.load("Models/credit_risk_model.pkl")
le = joblib.load("Models/label_encoder.pkl")
feature_names = joblib.load("Models/feature_names.pkl")

# -----------------------------
# Upload CSV
# -----------------------------
uploaded_file = st.file_uploader("Upload a Feature-Engineered CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # -----------------------------
    # Preprocessing / Feature Alignment
    # -----------------------------
    # Drop target-related columns if present
    drop_cols = ["risk_score", "credit_risk", "credit_risk_binary"]
    X = df.drop(columns=[c for c in drop_cols if c in df.columns], errors='ignore')

    # Keep only numeric columns
    X = X.select_dtypes(include=["float64", "int64"])

    # Add missing columns and reorder
    for col in feature_names:
        if col not in X.columns:
            X[col] = 0
    X = X[feature_names]

    st.subheader("Aligned Model Features")
    st.write(X.head())

    # -----------------------------
    # Make Predictions
    # -----------------------------
    predictions = model.predict(X)
    risk_labels = le.inverse_transform(predictions)
    df["Predicted Credit Risk"] = risk_labels

    st.subheader("Predictions")
    st.dataframe(df[["Predicted Credit Risk"]])

    #------------------------------
    #Require a single column: Credit_Type for Dashboard creation
    #------------------------------
    
    credit_type_cols = [
    "Credit_Type_Consumer credit",
    "Credit_Type_Household credit",
    "Credit_Type_Residential mortgage credit",
    "Credit_Type_Total business and household credit"
]

    df["Credit_Type"] = df[credit_type_cols].idxmax(axis=1)
    df["Credit_Type"] = df["Credit_Type"].str.replace("Credit_Type_", "")

    #------------------------------
    # Save the DataFrame with predictions to CSV for Power BI / Tableau
    #------------------------------
    output_path = r"C:\Users\kirti\VS Code Projects\VS Code\33. Canadian-Credit-Risk-Model\Output\predicted_credit_risk.csv"
    df.to_csv(output_path, index=False)

    st.success(f"Predicted CSV saved at: {output_path}")
    
    # -----------------------------
    # ---- ADDITION: Generate SHAP Summary CSV ----
    # -----------------------------
    try:
        explainer = shap.LinearExplainer(model, X)  # Use TreeExplainer for tree-based models
        shap_values = explainer.shap_values(X)

        shap_df_wide = pd.DataFrame(shap_values, columns=X.columns)
        shap_df_wide['Predicted Credit Risk'] = risk_labels
        shap_df_long = shap_df_wide.melt(
            id_vars=['Predicted Credit Risk'],
            var_name='Feature',
            value_name='SHAP_value'
        )

        shap_path = r"C:\Users\kirti\VS Code Projects\VS Code\33. Canadian-Credit-Risk-Model\Output\shap_summary.csv"
        shap_df_long.to_csv(shap_path, index=False)
        st.success(f"SHAP summary CSV saved at: {shap_path}")
    except Exception as e:
        st.error(f"SHAP summary generation failed: {e}")

    
    #-----------------------------
    # Compute SHAP values --------
    #-----------------------------
    
    #explainer = shap.LinearExplainer(model, X)  # use TreeExplainer for tree-based models
    #shap_values = explainer.shap_values(X)

    #shap_df = pd.DataFrame(shap_values, columns=X.columns)
    #shap_df['Predicted Risk'] = risk_labels

    #shap_path = r"C:\Users\kirti\VS Code Projects\VS Code\33. Canadian-Credit-Risk-Model\Output\shap_summary.csv"
    #shap_df.to_csv(shap_path, index=False)
    #st.success(f"SHAP summary CSV saved at: {shap_path}")
    
    # -----------------------------
    # SHAP Explainability
    # -----------------------------
    st.subheader("Model Explainability (SHAP)")

    try:
        explainer = shap.LinearExplainer(model, X)
        shap_values = explainer.shap_values(X)

        # SHAP Summary Plot
        fig, ax = plt.subplots()
        shap.summary_plot(shap_values, X, show=False)
        st.pyplot(fig)

        # Optional: Display top 5 features for each prediction
        st.subheader("Top 5 Features Impacting Risk Prediction")
        shap_df = pd.DataFrame(shap_values, columns=X.columns)
        top_features = shap_df.abs().mean().sort_values(ascending=False).head(5)
        st.write(top_features)
    except Exception as e:
        st.error(f"SHAP plotting failed: {e}")
        st.info("SHAP explainability requires numeric input only and aligned features.")

    # -----------------------------
    # Business Insights Section
    # -----------------------------
    st.subheader("Business Insights")
    st.markdown("""
    - High volatility and rapid credit growth increase risk probability.
    - Stable trends in credit reduce predicted risk.
    - Use this dashboard to monitor emerging risk in credit portfolios.
    """)