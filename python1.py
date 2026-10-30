```python
# University Scholarship Allocation System

students = []

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

# Input number of students
n = int(input("Enter the number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i + 1}")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    # Subject marks
    subjects = ["English", "Mathematics", "Science"]
    marks = []

    for subject in subjects:
        mark = float(input(f"Enter {subject} marks (out of 100): "))
        marks.append(mark)

    aggregate = sum(marks) / len(marks)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income (Rs.): "))

    # Check eligibility
    eligible = (
        aggregate >= MIN_AGGREGATE
        and all(mark >= MIN_SUBJECT_MARKS for mark in marks)
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_INCOME
    )

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "eligible": eligible
    }

    students.append(student)


# Separate eligible students
eligible_students = [
    student for student in students
    if student["eligible"]
]

# Ranking and tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower annual family income
# 4. Roll number in ascending alphabetical/numerical text order

eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["roll_no"]
    )
)


# Display all student results
print("\n========== SCHOLARSHIP RESULTS ==========")

for student in students:
    print(f"\nName: {student['name']}")
    print(f"Roll Number: {student['roll_no']}")
    print(f"Aggregate Marks: {student['aggregate']:.2f}%")
    print(f"Attendance: {student['attendance']:.2f}%")
    print(f"Annual Family Income: Rs. {student['income']:.2f}")

    if student["eligible"]:
        print("Status: ELIGIBLE")
    else:
        print("Status: NOT ELIGIBLE")


# Display ranked eligible students
print("\n========== SCHOLARSHIP RANK LIST ==========")

if eligible_students:
    for rank, student in enumerate(eligible_students, start=1):
        print(
            f"Rank {rank}: {student['name']} | "
            f"Roll No: {student['roll_no']} | "
            f"Aggregate: {student['aggregate']:.2f}% | "
            f"Attendance: {student['attendance']:.2f}% | "
            f"Income: Rs. {student['income']:.2f}"
        )
else:
    print("No students are eligible for the scholarship.")

print("\nScholarship allocation process completed.")
```