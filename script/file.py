import joblib
import os
import pandas as pd

# Define the absolute path to the model
model_path = 'C:/HoGent/Jaar2/ML/Project/MachineLearningProject_Solar/script/best_model.joblib'

# Check if the model file exists
if os.path.exists(model_path):
    # Load the model
    model = joblib.load(model_path)
    print("Model loaded successfully")

    # Define the path to the forecast CSV file
    forecast_path = 'C:/HoGent/Jaar2/ML/Project/MachineLearningProject_Solar/data/forecast.csv'

    # Check if the forecast file exists
    if os.path.exists(forecast_path):
        # Load the forecast data
        forecast_data = pd.read_csv(forecast_path)
        print("Forecast data loaded successfully")

        # Ensure the forecast data is in the correct format for prediction
        # Assuming the data needs to be in the same format as the training data
        # (e.g., selecting necessary features and preprocessing)

        # Make a prediction
        prediction = model.predict(forecast_data)
        print(f"Prediction: {prediction}")
    else:
        print(f"Forecast file not found at: {forecast_path}")
else:
    print(f"Model file not found at: {model_path}")
