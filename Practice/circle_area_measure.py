import numpy as np

radii = np.array([2, 8, 15, 26])
area_of_circle = np.pi * radii ** 2

for radius, area in zip(radii, area_of_circle):
    print (f"In radius {radius}, area of circle is {area:.2f} SQKM")