# Energy Consumption Prediction Using Machine Learning

This project predicts **household energy consumption (kWh)** based on various factors such as temperature, AC usage, household size, and peak-hour consumption.  

##  Project Overview

Traditional manual methods of estimating household energy consumption are inaccurate and unreliable.  
This project uses **Machine Learning** to build a predictive model that helps forecast energy usage more efficiently.

The main objectives were:

- Perform data cleaning & preprocessing  
- Train multiple ML models  
- Compare model performance  
- Save the best model using `joblib`  
- Deploy the model through a Streamlit Web App

##  Dataset

The dataset contains features such as:

- Household_Size  
- Avg_Temperature_C  
- Has_AC  
- Peak_Hours_Usage_kWh  
- Month  
- Day  
- DayOfWeek  
- Is_Weekend  
- Energy_Consumption_kWh (Target)

##  Machine Learning Models Tested

The following ML algorithms were trained and evaluated:

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- Support Vector Regressor (SVR)  
- Gradient Boosting Regressor  

###  Best Performing Model: **Gradient Boosting Regressor**

### Run Streamlit App - https://household-energy-prediction-gzpnx6jburbbmpdoqj93ea.streamlit.app/

How to Use the Web App

Enter details:
Household size,
Temperature,
Peak Hours Usage,
Month, Day,
DayOfWeek,
Weekend or not,
AC availability,

Click Predict

The app displays predicted Energy Consumption (kWh)
