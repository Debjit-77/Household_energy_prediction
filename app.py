import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("energy_prediction.pkl")

st.title("⚡ Energy Consumption Prediction")
st.write("Enter the household and environmental details to predict energy usage (kWh).")

# Input fields based exactly on model features
household_size = st.number_input("Household Size", min_value=1, max_value=20, step=1)
avg_temperature = st.number_input("Average Temperature (°C)", step=0.1)
has_ac = st.selectbox("Has Air Conditioner?", ["No", "Yes"])
peak_usage = st.number_input("Peak Hours Usage (kWh)", step=0.1)

month = st.number_input("Month (1-12)", min_value=1, max_value=12, step=1)
day = st.number_input("Day (1-31)", min_value=1, max_value=31, step=1)
day_of_week = st.number_input("Day of Week (0 = Monday, 6 = Sunday)", min_value=0, max_value=6, step=1)
is_weekend = st.selectbox("Is Weekend?", ["No", "Yes"])

# Convert categorical values
has_ac = 1 if has_ac == "Yes" else 0
is_weekend = 1 if is_weekend == "Yes" else 0

if st.button("Predict Energy Consumption"):
    # Create input DataFrame with correct columns
    input_df = pd.DataFrame([{
        "Household_Size": household_size,
        "Avg_Temperature_C": avg_temperature,
        "Has_AC": has_ac,
        "Peak_Hours_Usage_kWh": peak_usage,
        "Month": month,
        "Day": day,
        "DayOfWeek": day_of_week,
        "Is_Weekend": is_weekend
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Energy Consumption: **{prediction:.2f} kWh**")
