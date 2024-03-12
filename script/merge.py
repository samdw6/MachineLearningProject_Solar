import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib_inline


current_directory = os.getcwd()
print("Current directory:", current_directory)

# Load CSV files
csv1 = pd.read_csv('./course/datasets/solar.csv')
csv2 = pd.read_csv('./course/datasets/weather.csv')

# Load Excel file
xlsx = pd.read_excel('./course/datasets/sunrise-sunset.xlsx')

# convert xlsx to csv
xlsx.to_csv('./course/datasets/sunrise-sunset.csv', index=False)

# Load the new csv file
csv3 = pd.read_csv('./course/datasets/sunrise-sunset.csv')

#create dataframes
df_solar = pd.DataFrame(csv1)
df_weather = pd.DataFrame(csv2)
df_sunrise_sunset = pd.DataFrame(csv3)


def convert_date(df_solar):
  date_format = "%Y-%m-%d %H:%M:%S"
  string = str(df_solar)[:16] + ":00"
  new = datetime.strptime(string,date_format)
  return new

df_solar['timestamp'] = df_solar['timestamp'].apply(convert_date)
df_weather['timestamp'] = pd.to_datetime(df_weather['timestamp'])
df_sunrise_sunset['datum'] = pd.to_datetime(df_sunrise_sunset['datum'])


# Merge the csv files 
df_merged = pd.merge_asof(df_solar,df_weather,on="timestamp",direction="nearest")



# Save the merged dataframe to a new csv file
df_merged.to_csv('./course/datasets/merged.csv', index=False)



#load the new csv file
merged = pd.read_csv('./course/datasets/merged.csv')


# convert timestamp format 
merged['timestamp'] = pd.to_datetime(merged['timestamp'])
merged['timestamp'] = merged['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
#split the timestamp column into date and time
merged['date'] = merged['timestamp'].apply(lambda x: x.split(' ')[0])
#print(merged['date'])
merged['time'] = merged['timestamp'].apply(lambda x: x.split(' ')[1])
#print(merged['time'])

#time column only save hours and minutes
merged['time'] = merged['time'].apply(lambda x: x[:5])
#print(merged['time'])

# Save the new merged dataframe to a new csv file
merged.to_csv('./course/datasets/merged.csv', index=False)

#load the new csv file
merged = pd.read_csv('./course/datasets/merged.csv')



#convert date column to datetime
merged['date'] = pd.to_datetime(merged['date'])
#check dtype of date column
print(merged['date'].dtype)
print(df_sunrise_sunset['datum'].dtype)
# Merge the new csv file with the sunrise-sunset csv file on the date column
df_merged = pd.merge(merged,df_sunrise_sunset,left_on="date",right_on="datum",how="left")

# Save the new merged dataframe to a new csv file
df_merged.to_csv('./course/datasets/merged.csv', index=False)
