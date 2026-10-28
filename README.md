# Wind Turbine Data Analysis

## What This Project Checks

This project checks wind turbine data for March 2022 to see if there are any missing readings, duplicate records or values that don't look correct. It combines data from three CSV files into one dataset and checks the wind speed, wind direction and power output.

It also looks at each turbine's power output each day by calculating the minimum, maximum and average. It then compares each turbine's daily average with the overall average for that day to identify turbines with unusually high or low power output. The results are saved into CSV files for further review.

## Requirements

- Python 3
- pandas

## How to Run

1. Download the project files from GitHub.
2. Make sure the three CSV files are in the same folder as `main.py`.
3. Open the folder in Terminal.
4. Install pandas if you haven't already:
5. Run the code:

The results will be saved as CSV files in the same folder.

## Output Files

1. cleaned_data1.csv contains the combined data from all three files, including the new date column.
2. daily_summary1.csv contains each turbine's daily minimum, maximum and average power output, plus the daily mean, standard deviation and anomaly flag.



## Problems Found and how I dealt with them

I checked the data for the following problems 

1. Missing values: no missing values were found, so I did not need to remove or fill any data.
2. Duplicate data: no duplicate rows or repeated for the same turbine and timestamp were found, so no records were removed
3. Negative wind speed: no negative speed was found 
4. Invalid wind direction: I checked the wind direction was between 0 and 359 degrees and no invalid values were found.
5. Power output: I checked for negative power output and looked at the minimum and maximum values. The values ranged from 1.5 MW to 4.5 MW. No negative values were found however, the turbines full capacity was not defined so I could not cofirm the maximum physically possible output. 
6. Timestamps: I converted the timestamps (str) into a date and time format so I could group the readings by day. I also verified the date range and the number of readings for each one.
7. Unusual power output: I compared each turbines daily average power output with the average of all turbines for that day. If a turbines output was two standard deviations away from the daily average, I flagged it. I found 17 anomalies and kept them in the summary for further investigation rather than deleting them.

### Flagged Turbine & Day Combinations

These are the 17 anomalies in March 2022 with their date and turbine id: 

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

These results does not mean that the turbines are faulty. They show which turbines had an average power output that was unusually different from the others on that day.


## Limitations 

1. Wind direction should be between 0 degrees and 359 degrees. 
2. Negative wind speed and negative power output were treated as invalid if found. 
3. Turbines with the unusual power output were flagged for further testing rather than deleted.
4. The maximum possible power output of the turbines could not be confirmed because the tubines capacity output was not provided.


## Future Improvements

If I had more time I would:
1. Investigate the flagged results to see why their power output was different.
2. Check the tubine capacity limits to identify any physically impossible output values. 
3. Check that every hourly reading is present for each turbine.

