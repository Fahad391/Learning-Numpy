import numpy as np

# Taking 2 imaginary sales data for 2 different arrays
B1_sales = np.array([100, 150, 200])
B2_sales = np.array([300, 350, 400])

# Without combination
print("If they are printed separately\n", B1_sales, '\n', B2_sales)

# Using Vertical Stack for new rows
vertical_stack = np.vstack((B1_sales, B2_sales))
print("\nVertical Stack (Rows added):")
print(vertical_stack)

# Using Horizontal stack
horizontal_stack = np.hstack((B1_sales, B2_sales))
print("\nHorizontal Stack (Joined end-to-end):")
print(horizontal_stack)