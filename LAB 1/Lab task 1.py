print("===== Lab Task 1: Grade System =====")

marks = int(input("Enter marks of student from 1-100: "))

if marks >= 91 and marks <= 100:
    grade = "A"
elif marks >= 81 and marks <= 90:
    grade = "B"
elif marks >= 71 and marks <= 80:
    grade = "C"
elif marks >= 61 and marks <= 70:
    grade = "D"
elif marks >= 50 and marks <= 60:
    grade = "E"
elif marks >= 0 and marks < 50:
    grade = "F"
else:
    grade = "Invalid marks"

print("Your Grade is:", grade)