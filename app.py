import streamlit as st
from src.predict import predict_covid, FEATURES

st.set_page_config(page_title="COVID_19 Prediction", page_icon="Φ", layout="centered")

st.title("Φ COVID-19 Prediction App made by Anuj Karan")
st.markdown("Select your symptoms below")

#taking inputs
inputs = []
for feature in FEATURES:
    choice = st.selectbox(f"{feature}: ", ["No", "Yes"])
    inputs.append(1 if choice == "Yes" else 0)

#submit button
if st.button("Check"):
    result = predict_covid(inputs)
    if result == 1:
        st.error("⚠️ You may have COVID-19. Please consult a doctor immediately.")
    else:
        st.success("✅ You are likely safe. Stay cautious and follow safety measures.")