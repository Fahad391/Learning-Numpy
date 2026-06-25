import numpy as np

# 1D Array of 12 elements
flat_data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

# Reshape 1D array into 2D array (2 rows and 3 columns)
matrix = flat_data.reshape(3, 4)

print("Flat Data\n", flat_data)

print("\nReshaped Matrix (3x4):")
print(matrix)

# Transpose the matrix
transposed_matrix = matrix.T
print("\nTransposed Matrix (4x3):")
print(transposed_matrix)