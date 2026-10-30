```python
# Hospital Billing and Patient Classification System

def calculate_consultation(consultation_fee, visits):
    return consultation_fee * visits


def calculate_diagnostic(diagnostic_charges):
    return sum(diagnostic_charges)


def calculate_treatment(treatment_charges):
    return sum(treatment_charges)


def calculate_concession(total, patient_type, senior_citizen):
    concession = 0

    # Apply concession based on patient category
    if patient_type == "BPL":
        concession = total * 0.20
    elif patient_type == "INSURED":
        concession = total * 0.10

    # Additional senior citizen concession
    if senior_citizen:
        concession += total * 0.05

    # Maximum concession is 25% of the bill
    maximum_concession = total * 0.25
    concession = min(concession, maximum_concession)

    return concession


def classify_patient(final_bill):
    # Example payment classification policy
    if final_bill == 0:
        return "Fully Concession-Based"
    elif final_bill <= 5000:
        return "Low Payment Category"
    elif final_bill <= 20000:
        return "Medium Payment Category"
    else:
        return "High Payment Category"


def main():
    print("======================================")
    print(" HOSPITAL BILLING SYSTEM")
    print("======================================")

    patient_name = input("Enter patient name: ").strip()

    if not patient_name:
        print("Error: Patient name cannot be empty.")
        return

    try:
        age = int(input("Enter patient age: "))

        if age < 0 or age > 130:
            print("Error: Enter a valid age between 0 and 130.")
            return

        patient_type = input(
            "Enter patient type (GENERAL/BPL/INSURED): "
        ).strip().upper()

        if patient_type not in ["GENERAL", "BPL", "INSURED"]:
            print("Error: Invalid patient type.")
            return

        senior_citizen = age >= 60

        consultation_fee = float(
            input("Enter consultation fee per visit: ")
        )
        visits = int(input("Enter number of consultation visits: "))

        if consultation_fee < 0 or visits < 0:
            print("Error: Charges and visits cannot be negative.")
            return

        # Diagnostic charges
        diagnostic_charges = []
        diagnostic_count = int(
            input("Enter number of diagnostic tests: ")
        )

        if diagnostic_count < 0:
            print("Error: Number of tests cannot be negative.")
            return

        for i in range(diagnostic_count):
            charge = float(
                input(f"Enter charge for diagnostic test {i + 1}: ")
            )

            if charge < 0:
                print("Error: Diagnostic charges cannot be negative.")
                return

            diagnostic_charges.append(charge)

        # Treatment charges
        treatment_charges = []
        treatment_count = int(
            input("Enter number of treatments: ")
        )

        if treatment_count < 0:
            print("Error: Number of treatments cannot be negative.")
            return

        for i in range(t