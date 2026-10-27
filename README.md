# Wind Turbine Data Analysis

## Project Overview
This project analyses hourly wind turbine data for 15 turbines over March 2022. The data is provided across three CSV files, which are combined into a single dataset using Python and pandas.

The project checks data quality, calculates daily power output statistics for each turbine, identifies potential anomalies using a two-standard-deviation rule, and exports the results to CSV files.

## Requirements

- Python 3
- pandas

## How to Run

1. Download or clone the project repository.
2. Ensure the three input CSV files are in the same folder as `main.py`.
3. Ensure Python and pandas are installed.
4. Run the script using VS Code or a terminal.

The script reads the three input CSV files, combines them, performs data quality checks, calculates daily statistics, identifies potential anomalies, and saves the output files.

## Output Files

- `cleaned_data.csv`: Combined hourly turbine data with an additional date column.
- `daily_summary.csv`: Daily minimum, maximum, and average power output for each turbine, daily mean and standard deviation, and anomaly flags.



## Problems Found and Actions Taken

The dataset was checked for data quality issues before analysis.

| Check | Problem found | Action taken |
|---|---|---|
| Missing values | None found | No action required |
| Duplicate rows | None found | No action required |
| Duplicate turbine-time readings | None found | No action required |
| Missing hourly timestamps | None found | No action required |
| Negative wind speeds | None found | No action required |
| Invalid wind directions | None found | No action required |
| Negative power output | None found | No action required |
| Unusual daily power averages | 17 potential anomalies flagged | Flagged for further investigation; not removed |

The timestamp column was converted into a datetime format, and a separate date column was created to support daily analysis.

The recorded power output ranged from 1.5 to 4.5. The maximum rated capacity of the turbines was not provided, so an upper physical limit could not be verified.


## Daily Statistics and Anomaly Detection

Daily statistics were calculated for each turbine using the hourly power output readings. The minimum, maximum, and mean power output were calculated for each turbine on each day.

For anomaly detection, the mean and standard deviation of the 15 turbines' daily average power outputs were calculated separately for each day.

A turbine day was flagged as a potential anomaly when its daily average power output was more than two standard deviations away from that day's overall mean. Absolute differences were used so that unusually high and unusually low averages could both be identified.

This method identified 17 potential anomalies during March 2022. These were flagged for further investigation rather than automatically removed from the dataset.


### Flagged Turbine-Day Combinations

The following turbine-day combinations were flagged as potential anomalies:

| Date | Turbine ID |
|---|---:|
| 1 March 2022 | 15 |
| 2 March 2022 | 2 |
| 3 March 2022 | 12 |
| 4 March 2022 | 8 |
| 6 March 2022 | 3 |
| 7 March 2022 | 1 |
| 8 March 2022 | 11 |
| 11 March 2022 | 4 |
| 12 March 2022 | 12 |
| 13 March 2022 | 7 |
| 15 March 2022 | 9 |
| 18 March 2022 | 15 |
| 20 March 2022 | 4 |
| 22 March 2022 | 11 |
| 26 March 2022 | 4 |
| 28 March 2022 | 3 |
| 29 March 2022 | 9 |

These observations exceeded the two-standard-deviation threshold. They were retained in the dataset because a statistical anomaly does not necessarily indicate faulty sensor readings.


## Limitations and Assumptions

- The dataset covers March 2022 and contains hourly readings for 15 turbines.
- Each turbine was expected to have 744 hourly readings, and the checks confirmed that all expected hourly timestamps were present.
- The two standard deviation rule was used to identify potential anomalies. Flagged values are not necessarily errors and require further investigation.
- The turbines' rated power capacity was not provided, so the maximum physically possible power output could not be verified.
- The analysis uses the available data and does not establish the cause of any flagged anomaly.

## Future Improvements

- Confirm the rated capacity of each turbine and validate power output against it.
- Investigate the 17 flagged turbine day combinations using additional operational information.
- Add automated tests to check data quality and validate the analysis.


