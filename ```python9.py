```python
# Campus Event Financial Planning System

import math


def calculate_total_cost(
    venue_cost,
    equipment_cost,
    catering_per_person,
    transport_per_person,
    certificate_per_person,
    participants
):
    catering_cost = catering_per_person * participants
    transport_cost = transport_per_person * participants
    certificate_cost = certificate_per_person * participants

    total_cost = (
        venue_cost
        + equipment_cost
        + catering_cost
        + transport_cost
        + certificate_cost
    )

    return {
        "venue": venue_cost,
        "equipment": equipment_cost,
        "catering": catering_cost,
        "transport": transport_cost,
        "certificates": certificate_cost,
        "total_cost": total_cost
    }


def calculate_break_even(
    fixed_cost,
    variable_cost_per_person,
    registration_fee,
    sponsorship
):
    # Sponsorship reduces the amount that registrations must cover.
    remaining_fixed_cost = max(0, fixed_cost - sponsorship)

    contribution_per_person = (
        registration_fee - variable_cost_per_person
    )

    if contribution_per_person <= 0:
        return None

    return math.ceil(
        remaining_fixed_cost / contribution_per_person
    )


def main():
    print("=" * 60)
    print("       CAMPUS EVENT FINANCIAL PLANNING")
    print("=" * 60)

    try:
        # Event details
        event_name = input("Enter event name: ").strip()

        if not event_name:
            print("Error: Event name cannot be empty.")
            return

        participants = int(
            input("Enter expected number of participants: ")
        )

        if participants <= 0:
            print("Error: Participants must be greater than zero.")
            return

        # Fixed costs
        print("\n--- Fixed Expenses ---")

        venue_cost = float(
            input("Enter venue cost (Rs.): ")
        )

        equipment_cost = float(
            input("Enter equipment cost (Rs.): ")
        )

        # Variable costs per participant
        print("\n--- Per-Participant Expenses ---")

        catering_per_person = float(
            input("Enter catering cost per participant (Rs.): ")
        )

        transport_per_person = float(
            input("Enter transport cost per participant (Rs.): ")
        )

        certificate_per_person = float(
            input("Enter certificate cost per participant (Rs.): ")
        )

        # Funding
        print("\n--- Funding Details ---")

        registration_fee = float(
            input("Enter registration fee per participant (Rs.): ")
        )

        sponsorship = float(
            input("Enter confirmed sponsorship amount (Rs.): ")
        )

        # Validate financial inputs
        financial_values = [
            venue_cost,
            equipment_cost,
            catering_per_person,
            transport_per_person,
            certificate_per_person,
            registration_fee,
            sponsorship
        ]

        if any(value < 0 for value in financial_values):
            print("Error: Costs, fees, and sponsorship cannot be negative.")
            return

        # Calculate expenses
        expenses = calculate_total_cost(
            venue_cost,
            equipment_cost,
            catering_per_person,
            transport_per_person,
            certificate_per_person,
            participants
        )

        total_cost = expenses["total_cost"]

        # Calculate funding and shortfall
        registration_income = participants * registration_fee
        total_funding = registration_income + sponsorship

        sponsorship_needed = max(
            0, total_cost - registration_income
        )

        sponsorship_shortfall = max(
            0, sponsorship_needed - sponsorship
        )

        surplus = total_funding - total_cost

        # Calculate per-participant cost
        cost_per_participant = total_cost / participants

        # Break-even calculation
        fixed_cost = venue_cost + equipment_cost

        variable_cost_per_person = (
            catering_per_person
            + transport_per_person
            + certificate_per_person
        )

        break_even_count = calculate_break_even(
            fixed_cost,
            variable_cost_per_person,
            registration_fee,
            sponsorship
        )

        # Display financial report
        print("\n" + "=" * 60)
        print("                 EVENT FINANCIAL REPORT")
        print("=" * 60)

        print(f"Event Name: {event_name}")
        print(f"Expected Participants: {participants}")

        print("\n--- Expense Breakdown ---")
        print(f"Venue Cost: Rs. {expenses['venue']:.2f}")
        print(f"Equipment Cost: Rs. {expenses['equipment']:.2f}")
        print(f"Catering Cost: Rs. {expenses['catering']:.2f}")
        print(f"Transport Cost: Rs. {expenses['transport']:.2f}")
        print(f"Certificate Cost: Rs. {expenses['certificates']:.2f}")

        print("-" * 60)
        print(f"Total Event Cost: Rs. {total_cost:.2f}")
        print(
            f"Cost Per Participant: Rs. "
            f"{cost_per_participant:.2f}"
        )

        print("\n--- Funding Breakdown ---")
        print(f"Registration Income: Rs. {registration_income:.2f}")
        print(f"Confirmed Sponsorship: Rs. {sponsorship:.2f}")
        print(f"Total Available Funding: Rs. {total_funding:.2f}")

        print("-" * 60)
        print(
            f"Additional Sponsorship Needed: "
            f"Rs. {sponsorship_needed:.2f}"
        )
        print(
            f"Sponsorship Shortfall: "
            f"Rs. {sponsorship_shortfall:.2f}"
        )

        if surplus > 0:
            print(f"Expected Surplus: Rs. {surplus:.2f}")
            print("Financial Status: EVENT IS IN SURPLUS")
        elif surplus < 0:
            print(f"Expected Deficit: Rs. {abs(surplus):.2f}")
            print("Financial Status: ADDITIONAL FUNDING REQUIRED")
        else:
            print("Financial Status: BREAK-EVEN")

        print("\n--- Break-Even Analysis ---")

        if break_even_count is None:
            print(
                "Break-even is not possible with the current "
                "registration fee and variable costs."
            )
            print(
                "Increase the registration fee or reduce "
                "per-participant expenses."
            )
        else:
            print(
                f"Minimum Registrations Needed: {break_even_count}"
            )

            if break_even_count <= participants:
                print(
                    "Status: Expected registrations can cover "
                    "the event costs."
                )
            else:
                print(
                    "Warning: Expected registrations are insufficient "
                    "to reach break-even."
                )

        print("=" * 60)

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()
```