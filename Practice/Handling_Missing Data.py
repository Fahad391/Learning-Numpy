import numpy as np

# Imaginary Sensor reading matrix failed to capture some data points
sensor_readings = np.array(
    [
        [24.1, 26.5, np.nan, np.nan, 25],
        [np.nan, 28.4, 26.8, 27.0, np.nan]
    ]
)

# Creating a boolean mask to locate where the missing values are
# If found shows False meaning not missing
# If not found shows True meaning is missing
locate_missing_values = np.isnan(sensor_readings)
print(f"Located missing values\n{locate_missing_values}")

#Replace all NaN values with 0
cleaned_readings = sensor_readings.copy()
cleaned_readings[locate_missing_values] = 0.0

print("\nCleaned Matrix (NaNs replaced with 0.0):")
print(cleaned_readings)