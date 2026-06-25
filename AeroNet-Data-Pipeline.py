import numpy as np

# 2 variables containing 1D arrays with 12 elements each containing air Quality rate
zone_1_sensor_data = np.array([20.1, 28.4, np.nan, 31.7, 22.6, np.nan, 25.5, 26.8, 29.1, np.nan, 23.5, 27.7])
zone_2_sensor_data = np.array([19.8, 22.4, 21.0, np.nan, 20.5, 33.1, np.nan, 25.4, 18.9, 22.5, 24.2, np.nan])

# Getting them into a 3x4 matrix
matrix_1 = zone_1_sensor_data.reshape(3,4)
matrix_2 = zone_2_sensor_data.reshape(3,4)
# Combining these data in a vertical stack
combined_zone_data = np.vstack((matrix_1, matrix_2))
print(f"Presnting Data of zone 1&2:\n{combined_zone_data}")

# Replacing missing numbers with 0 after locating them
# Step-1: Locate the missing values
locate_missing_values = np.isnan(combined_zone_data)

# Step-2: Replace them with 0
cleaned_readings = combined_zone_data.copy() # Copies the variable's data
cleaned_readings[locate_missing_values] = 0 # Replaces with 0

print(f"\nCleaned Matrix (after replacing missing values with 0)")
print(cleaned_readings)

# Doing a calibration adjustment
calibration_adjustment = np.array([+1.5, -0.5, +2.0, -1.0])

final_reading = cleaned_readings + calibration_adjustment
print(f"\nFinal Reading:\n{final_reading}")

# Time to find maximum pollution level from the data
threshold_for_max_pollution = 30.0
threshold_for_avg_pollution = 27.0
# for maximum pollution level
max_pollution_level = final_reading >= threshold_for_max_pollution
worse_air_quality = final_reading[max_pollution_level]
print(f"\nWorse Air Quality\n.Levels:\n{worse_air_quality}")

avg_pollution_level = (
    (final_reading <= threshold_for_avg_pollution) &
    (final_reading > 25.0)
)
avg_air_quality = final_reading[avg_pollution_level]
print(f"\nAverage Air Quality\n.Levels:\n{avg_air_quality}")

