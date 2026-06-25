import numpy as np
      
# 1D array OP scalar
# Numpy stretches the scalar to match every element
product_prices = np.array([1000, 1200, 800, 950])
with_Tax = product_prices * 1.15  # scalar broadcasts → shape (4,)


#Now, 2D array OP 1D array (shapes must align from RIGHT) 
# (3, 4) shape
# (4,) shape  ← aligns on the right column axis
# (3, 4) result  ← 1D row repeats for each of 3 rows
sales = np.array([[100, 200, 150, 300],
                   [120, 180, 90,  260],
                   [90,  210, 110, 280]])

discount = np.array([10, 5, 20, 15])  # one discount per product
final = sales + discount              # discount row applied to ALL weeks

# Column vector broadcast (reshape trick)
# Want to add a per-week bonus (3 values) to each column
bonus = np.array([50, 30, 70])        # shape (3,) — won't broadcast on its own
bonus_column = bonus.reshape(3, 1)      # shape (3,1) → NOW it stretches across columns
boosted = sales + bonus_column          # (3,4) + (3,1) → (3,4) ✓

## Print values
print(f"Prices of products: {product_prices}", "\n", 
      f"with Tax: {with_Tax}\n")

print(f"Sales: {final}\n")

print(boosted)