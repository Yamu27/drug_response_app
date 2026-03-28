import streamlit as st
import pickle
import pandas as pd

# Load model + column info
model_path = "model/random_forest_model.pkl"
with open(model_path, "rb") as f:
    rf_model_info = pickle.load(f)

rf_model = rf_model_info['model']
gene_list = rf_model_info['columns']

st.title("Cisplatin Drug Response Prediction")
st.write("Enter gene expression values to predict drug response:")

# Create inputs dynamically
input_data = {}
for gene in gene_list:
    input_data[gene] = st.number_input(f"{gene}", value=0.0)

input_df = pd.DataFrame([input_data])

if st.button("Predict"):
    try:
        prediction = rf_model.predict(input_df)[0]
        st.success(f"Predicted Drug Response: {prediction}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")