# Importing Numpy library as numerical
import numpy as numerical

# Creating an Array of Integer numbers from 1-10
Array_of_letter_Single_Dim = numerical.array(['A', 'B', 'C', 'D', 'E'])

# printing the Array
print("Before Slice: ", Array_of_letter_Single_Dim)

print("After Slice: ", Array_of_letter_Single_Dim[2:0:-1])

print('\n')

Array_of_Integer_numbers_Multi_Dim = numerical.array([[1,2,3,4,5,6,7,8,9,10], 
                                           [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])
print("Before Slice\n", Array_of_Integer_numbers_Multi_Dim)
# Slicing Multi-Dimensional Array
print("After Slicing: ", Array_of_Integer_numbers_Multi_Dim[0:2, 8])