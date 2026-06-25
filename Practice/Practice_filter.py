import numpy as np

# Array of Exam Scores
scores = np.array([[80, 85, 90, 55, 40, 75, 60, 58, 77, 98, 50, 55]])
# Putting a condition for pass
pass_mark = scores > 60 # Shows in Boolean [True, False...]
#passed = scores[pass_mark] # Only Trues shows up

# inline (shorthand, same result) ---
passed = scores[scores > 70] 

# compound conditions (use & | ~, NOT and/or) ---
good = scores[(scores > 70) & (scores < 90)]  # [72, 85, 78]
extreme = scores[(scores < 60) | (scores > 88)] # [91, 55]
not_low = scores[~(scores < 65)]               # [72, 85, 91, 78]

# np.where → conditional replacement (if-else on arrays) ---
# np.where(condition, value_if_true, value_if_false)
grade = np.where(scores >= 70, "Pass", "Fail")
# ['Pass' 'Pass' 'Fail' 'Pass' 'Fail' 'Pass']

# np.where with numeric replacement ---
# Cap scores at 80 (clip outliers)
capped = np.where(scores > 80, 80, scores)  # [72, 80, 60, 80, 55, 78]

# np.argwhere → gives INDICES not values ---
idx = np.argwhere(scores > 70)   # [[0],[1],[3],[5]] — row indices
flat_idx = np.where(scores > 70)[0]  # [0, 1, 3, 5] flat

# filter on 2D array (row-wise) ---
students = np.array([[1, 72], [2, 85], [3, 60], [4, 91]])
# Filter rows where column 1 (score) > 70
top_students = students[students[:, 1] > 70]   # [[1,72],[2,85],[4,91]]

#print(passed, '\n', good, '\n', extreme, '\n', not_low)
#print(grade)
#print(capped)
#print(idx)
#print(flat_idx)
#print(students)
#print(top_students)