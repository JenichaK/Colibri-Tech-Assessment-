import pandas as pd

# Loading all three files into one dataset

file1 = pd.read_csv("data_group_1.csv")
file2 = pd.read_csv("data_group_2.csv")
file3 = pd.read_csv("data_group_3.csv")

all_data = pd.concat([file1, file2, file3], ignore_index=True)


print(all_data.shape)

print(all_data.head())

# Checking any missing values

print(all_data.isnull().sum())

# Checking for duplicate rows

print(all_data.duplicated().sum())

print(all_data.duplicated(subset=["timestamp", "turbine_id"]).sum())

# checking wind speed to see if there is any negative value 

print((all_data["wind_speed"] < 0).sum())

# checking wind direction between 0 and 359

print(((all_data["wind_direction"] < 0) | (all_data["wind_direction"] > 359)).sum())

# checking for negative power output value 

print((all_data["power_output"] < 0).sum())

# checking for min and max value to see if there's any impossible values

print(all_data["power_output"].min())
print(all_data["power_output"].max())

# checking timestamps

all_data["timestamp"] = pd.to_datetime(all_data["timestamp"])

print(all_data["timestamp"].dtype)

# checking ealiest and latest timestamp
print(all_data["timestamp"].min())
print(all_data["timestamp"].max())

# checking readings for each turbine
print(all_data["turbine_id"].value_counts().sort_index())

#checking each hour is recorded per turbine
print(all_data.groupby("turbine_id")["timestamp"].nunique())

#checking turbines performance by power output

all_data["date"] = all_data["timestamp"].dt.date

print(all_data[["timestamp", "date"]].head())

daily_data = all_data.groupby(["date", "turbine_id"])["power_output"].agg(["min", "max", "mean"]).reset_index()

print(daily_data.head())

# finding avearge 

daily_data["daily_mean"] = daily_data.groupby("date")["mean"].transform("mean")

# working out standard deviation 

daily_data["daily_std"] = daily_data.groupby("date")["mean"].transform("std")

# finding any anomalies

daily_data["is_anomaly"] = abs(daily_data["mean"] - daily_data["daily_mean"]) > 2 * daily_data["daily_std"]

print(daily_data[daily_data["is_anomaly"]])

daily_data.to_csv("daily_summary1.csv", index=False)

all_data.to_csv("cleaned_data1.csv", index=False)

























