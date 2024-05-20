import pandas as pd
import joblib
from datetime import datetime
model = joblib.load("C:/HoGent/Jaar2/ML/Project/MachineLearningProject_Solar/script/best_model.joblib")
forecast_df = pd.read_csv(r"C:/HoGent/Jaar2/ML/Project/MachineLearningProject_Solar/data/forecast.csv")
sunset_df = pd.read_csv(r"C:/HoGent/Jaar2/ML/Project/MachineLearningProject_Solar/data/sunrise-sunset.csv")
# day of the year
forecast_df['timestamp'] = pd.to_datetime(forecast_df['timestamp'])
forecast_df['day_of_year'] = forecast_df['timestamp'].dt.dayofyear

# sunrise and sunset
sunset_df['datum'] = pd.to_datetime(sunset_df['datum'])
sunset_df['day_of_year'] = sunset_df['datum'].dt.dayofyear
# merge the two dataframes
merged_forecast_df = pd.merge(forecast_df, sunset_df, on='day_of_year', how='left')
merged_forecast_df.drop_duplicates(subset=['timestamp'], inplace=True)
merged_forecast_df['hour'] = merged_forecast_df['timestamp'].dt.hour
# convert to floats (Ondergang, Opkomst, Op ware middag)
merged_forecast_df['Ondergang'] = merged_forecast_df['Ondergang'].astype(str).str.replace(':', '').astype(float)
merged_forecast_df['Opkomst'] = merged_forecast_df['Opkomst'].astype(str).str.replace(':','').astype(float)
merged_forecast_df['Op ware middag'] = merged_forecast_df['Op ware middag'].astype(str).str.replace(':','').astype(float)
# drop columns
merged_forecast_df = merged_forecast_df.drop(columns=['timestamp', 'datum'])
merged_forecast_df = merged_forecast_df[['temp', 'humidity_relative', 'pressure', 'cloudiness', 'Opkomst', 'Op ware middag', 'Ondergang', 'hour', 'day_of_year']]
# run model on forecast data
predictions = model.predict(merged_forecast_df)
# save predictions
output_df = pd.DataFrame({'prediction': predictions})

print(output_df)

# bar chart
import matplotlib.pyplot as plt
import numpy as np
hours = merged_forecast_df["hour"]


hours = np.arange(0, 48, 1)
plt.bar(hours, predictions)
plt.xlabel('hour')
plt.ylabel('prediction')
plt.title('Prediction per hour')
plt.show()
