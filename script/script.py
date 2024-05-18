import pandas as pd
import joblib
from datetime import datetime

# Load your regression model
model = joblib.load("C:/HoGent/Jaar2/ML/Project/MachineLearningProject_Solar/script/best_model.joblib")

# Read forecast data from CSV
forecast_df = pd.read_csv("C:/HoGent/Jaar2/ML/Project/MachineLearningProject_Solar/data/forecast.csv")
sunset_df = pd.read_csv("C:/HoGent/Jaar2/ML/Project/MachineLearningProject_Solar/data/sunset.csv")

# Merge the forecast data with the sunset data
merged_forecast_df = pd.merge(forecast_df, sunset_df, on='timestamp')

# save merged data to csv
merged_forecast_df.to_csv("C:/HoGent/Jaar2/ML/Project/MachineLearningProject_Solar/data/forecast_merged.csv", index=False)




""" def predict_kwh(forecast_df):
    # Preprocess your forecast data
    # Ensure the columns are in the same order as they were during training
    forecast_features = forecast_df[['temp', 'pressure', 'cloudiness', 'humidity_relative']]

    # Use the model to make predictions
    predictions = model.predict(forecast_features)

    return predictions



# Extract day of the year from timestamp column
forecast_df['day_of_year'] = pd.to_datetime(forecast_df['timestamp']).dt.dayofyear

# Predict the kWh for the next 48 hours
predictions = predict_kwh(forecast_df)

# Output the predictions with corresponding hour
for hour, prediction in zip(forecast_df['hour'], predictions):
    print(f"Voorspelling voor {hour}u: {prediction:.2f} kWh")
 """