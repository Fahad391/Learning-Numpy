import numpy as npy 
try:
    number_of_courses = int(input("Total Courses: "))
    if number_of_courses <= 0:
        raise ValueError("Number of courses must be at least 1.")

    all_courses = [] 
    all_credits = []
    all_Marks = []

    for n in range(number_of_courses):
        course_name = input(f"Course {n + 1}: ")
        if not course_name.strip():
            raise ValueError("Course name cannot be blank.")
        
        credit = int(input("Course Credit: "))
        if credit <= 0: 
            raise ValueError("Credit must be positive (greater than 0).")
        
        course_marks = float(input(f"Marks in {course_name}: "))
        if course_marks < 0 or course_marks > 100:
            raise ValueError("Marks must be between 0 and 100.")

        all_courses.append(course_name)
        all_credits.append(credit)
        all_Marks.append(course_marks)
    

    courses = npy.array(all_courses, dtype=str)
    credits = npy.array(all_credits, dtype=int)
    marks = npy.array(all_Marks, dtype=float)

    conditions = [
        (marks < 50),
        (marks >= 50) & (marks < 60),
        (marks >= 60) & (marks < 65),
        (marks >= 65) & (marks < 70),
        (marks >= 70) & (marks < 75),
        (marks >= 75) & (marks < 80),
        (marks >= 80) & (marks < 85),
        (marks >= 85) & (marks < 90),
        (marks >= 90)
    ]

    CGPA_on_Marks = [0.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00]


    CGPA_each_course = npy.select(conditions, CGPA_on_Marks)
    points_each_course = CGPA_each_course * credits
    Overall_CGPA = points_each_course.sum() / credits.sum()
    print('\n')
    print(f"Courses: {courses}")
    print(f"Credits: {credits}")
    print(f"Marks: {marks}")
    npy.set_printoptions(formatter={'float': '{:.2f}'.format})
    print(f"\nPoints Each course: {points_each_course}")
    print(f"\nOverall CGPA: {Overall_CGPA:.2f}")

    
except ValueError as error:
    print(f"Value Error: {error}")
except TypeError as error:
    print(f"Type Error: {error}")
except ZeroDivisionError as error:
    print(f"Zero Division Error: {error}")
except Exception as error:
    print(f"Unknown Error: {error}")