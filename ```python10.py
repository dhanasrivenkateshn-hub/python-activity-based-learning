```python
import math

# Examination Result and Grace-Mark Validation System

PASS_PERCENTAGE = 35
MAX_GRACE_PER_SUBJECT = 5
MAX_TOTAL_GRACE = 10


def get_valid_number(prompt, minimum, maximum):
    """Read and validate a numeric input."""
    while True:
        try:
            value = float(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def classify_result(percentage, failed_subjects):
    """Determine the student's final classification."""
    if failed_subjects > 0:
        return "FAIL"

    if percentage >= 75:
        return "DISTINCTION"
    elif percentage >= 60:
        return "FIRST CLASS"
    elif percentage >= 50:
        return "SECOND CLASS"
    else:
        return "PASS"


def main():
    print("=" * 55)
    print(" EXAMINATION RESULT AND GRACE-MARK VALIDATION")
    print("=" * 55)

    student_name = input("Enter student name: ").strip()

    while not student_name:
        print("Student name cannot be empty.")
        student_name = input("Enter student name: ").strip()

    number_of_subjects = int(
        get_valid_number("Enter number of subjects (1-20): ", 1, 20)
    )

    subjects = []
    total_maximum = 0
    total_original = 0
    total_grace = 0

    for i in range(1, number_of_subjects + 1):
        print(f"\n--- Subject {i} ---")

        subject_name = input("Enter subject name: ").strip()

        while not subject_name:
            print("Subject name cannot be empty.")
            subject_name = input("Enter subject name: ").strip()

        maximum_marks = get_valid_number(
            "Enter maximum marks: ", 1, 1000
        )

        pass_marks = get_valid_number(
            "Enter minimum pass marks: ", 0, maximum_marks
        )

        marks_obtained = get_valid_number(
            "Enter marks obtained: ", 0, maximum_marks
        )

        subjects.append({
            "name": subject_name,
            "maximum": maximum_marks,
            "pass_marks": pass_marks,
            "original": marks_obtained,
            "final": marks_obtained,
            "grace": 0
        })

        total_maximum += maximum_marks
        total_original += marks_obtained

    print("\nApplying grace-mark policy...")

    # Grace marks are applied only to subjects where the student
    # narrowly misses the pass mark.
    for subject in