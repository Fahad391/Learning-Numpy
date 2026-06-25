import numpy as np

sales = np.array(
    [
            [100, 200, 150, 300],
            [120, 180, 90,  260],
            [90,  210, 110, 280]
]
)

# Collapsing everything to one number
total = np.sum(sales)
avg = np.mean(sales)
highest_sold_unit_num = np.max(sales)
lowest_sold_unit_num = np.min(sales)

# Showing rows values only
row_value_sum = np.sum(sales, axis=1) # shows total value per row
row_max_values = np.max(sales, axis=1) # shows max value in each row

# Doing the same with Column
column_value_sum = np.sum(sales, axis=0) # shows total value per column
column_max_values = np.max(sales, axis=0) # shows max value in each column

# using argmax / argmin [Index of the extreme]
best_product_idx = np.argmax(column_value_sum)   # 3 — product at column 3 sold most
worst_week_idx   = np.argmin(row_value_sum)   # 1 — week 1 had lowest total

# using cumsum [running total (great for growth charts)]
running = np.cumsum(row_value_sum)

# using std 
spread = np.std(sales, axis=1)  # variability per week

print(f"Total: {total}")
print(f"Average: {avg:.2f}")
print(f"Number of Highest Sold Unit: {highest_sold_unit_num}")
print(f"Number of Lowest Sold Unit: {lowest_sold_unit_num}")

print(f"Total Value Per Row: {row_value_sum}")
print(f"Max Value each Row: {row_max_values}")
print(f"Total Value Per Column: {column_value_sum}")
print(f"Max Value each Column: {column_max_values}")

print('\n')
print("Values after using arg max/min\n")
print("Best Product Index\n",best_product_idx)
print("Wrost Week Index\n", worst_week_idx)
print('\n')
print("Values After using std\n")
print(spread)