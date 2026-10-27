import pandas as pd 
print("Colibri assessment starting!")

file1 = pd.read_csv("data_group_1.csv")
file2 = pd.read_csv("data_group_2.csv")
file3 = pd.read_csv("data_group_3.csv")

all_data = pd.concat([file1, file2, file3], ignore_index=True)

print(all_data.head())
print(all_data.shape)

print(all_data.info())
print(all_data.isnull().sum())

print("Duplicate rows:", all_data.duplicated().sum())
print("Duplicate turbine-time readings:", all_data.duplicated(subset=["timestamp", "turbine_id"]).sum())

print("Minimum wind speed:", all_data["wind_speed"].min())
print("Maximum wind speed:", all_data["wind_speed"].max())

print("Minimum wind direction:", all_data["wind_direction"].min())
print("Maximum wind direction:", all_data["wind_direction"].max())

print("Minimum power output:", all_data["power_output"].min())
print("Maximum power output:", all_data["power_output"].max())


# Check the date range covered by the data
all_data["timestamp"] = pd.to_datetime(all_data["timestamp"])

print("Earliest timestamp:", all_data["timestamp"].min())
print("Latest timestamp:", all_data["timestamp"].max())


# Count how many readings each turbine has
print(all_data["turbine_id"].value_counts().sort_index())


# Check for physically impossible wind measurements
print("Negative wind speeds:", (all_data["wind_speed"] < 0).sum())

print(
    "Invalid wind directions:",
    ((all_data["wind_direction"] < 0) |
     (all_data["wind_direction"] > 359)).sum()
)


# Check for negative power output
print(
    "Negative power readings:",
    (all_data["power_output"] < 0).sum()
)


# Calculate the average power output for each turbine
print(all_data.groupby("turbine_id")["power_output"].mean())


# Extract the date from each timestamp
all_data["date"] = all_data["timestamp"].dt.date

# Calculate daily power statistics for each turbine
daily_summary = all_data.groupby(
    ["date", "turbine_id"]
)["power_output"].agg(
    ["min", "max", "mean"]
).reset_index()

print(daily_summary.head(10))
print("Number of daily turbine summaries:", len(daily_summary))


# Calculate the daily mean and standard deviation across turbines
daily_summary["daily_mean"] = daily_summary.groupby("date")["mean"].transform("mean")

daily_summary["daily_std"] = daily_summary.groupby("date")["mean"].transform("std")

print(daily_summary.head(10))


# Flag turbine averages that are more than 2 standard deviations from the daily mean
daily_summary["is_anomaly"] = (
    (daily_summary["mean"] - daily_summary["daily_mean"]).abs()
    > 2 * daily_summary["daily_std"]
)

# Display the number of flagged anomalies
print("Number of flagged anomalies:", daily_summary["is_anomaly"].sum())

# Display the rows that were flagged
print(daily_summary[daily_summary["is_anomaly"]])


# Save the combined dataset to a CSV file
all_data.to_csv("cleaned_data.csv", index=False)

# Save the daily statistics and anomaly flags to a CSV file
daily_summary.to_csv("daily_summary.csv", index=False)

print("Files saved successfully!")


# Check for missing hourly timestamps for each turbine
expected_hours = 31 * 24

hourly_counts = all_data.groupby("turbine_id")["timestamp"].nunique()

print("Expected hourly readings per turbine:", expected_hours)
print("Actual unique hourly readings per turbine:")
print(hourly_counts)

print("Turbines with missing hourly readings:", (hourly_counts < expected_hours).sum())


# Check that the saved CSV files can be opened
saved_data = pd.read_csv("cleaned_data.csv")
saved_summary = pd.read_csv("daily_summary.csv")

print("Saved data shape:", saved_data.shape)
print("Saved data columns:", saved_data.columns.tolist())

print("Saved summary shape:", saved_summary.shape)
print("Saved summary columns:", saved_summary.columns.tolist())





