import numpy as np 

# 3 rows and 5 columns representing quantity of items sold
item_Quantity = np.array([
    [100, 115, 150, 110, 90],
    [500, 400, 450, 680, 190],
    [255, 245, 350, 120, 398]
])

# A 1D array for price of products of 5 categories
price_of_items = np.array([25, 45, 80, 500, 170])

# Caluculating total revenue (using Broadcasting)
total_revenue = item_Quantity * price_of_items
print("Total Revenue in BDT:")
for revenue in total_revenue:
    print(revenue)

# Calculating total revenue each branch(row) [using aggregate functions]
revenue_each_branch = np.sum(total_revenue, axis=1)
print("\nRevenue each Branch:")
branch = 0
for branch_revenue in revenue_each_branch:
    print(f"Branch {branch + 1}: {branch_revenue} BDT")
    branch += 1

# Using filter to distinct the low performing products on sale vs high performing products on sale

threshold = 12000

low_performance_on_revenue = total_revenue < threshold

under_performing_items_revenue = total_revenue[low_performance_on_revenue]

print(f"\nRed Alert: Targets Below {threshold} in BDT:")
print(under_performing_items_revenue)

print('\n')

high_performance_on_revenue = total_revenue > threshold
better_performing_items_revenue = total_revenue[high_performance_on_revenue]
print(f"Targets above {threshold} in BDT:")
print(better_performing_items_revenue)