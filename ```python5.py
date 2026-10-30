```python
# Railway Fare and Reservation Calculator

def calculate_base_fare(distance, rate_per_km):
    # Distance-based fare slabs
    if distance <= 100:
        fare = distance * rate_per_km
    elif distance <= 300:
        fare = (100 * rate_per_km) + (
            (distance - 100) * rate_per_km * 0.90
        )
    else:
        fare = (
            (100 * rate_per_km)
            + (200 * rate_per_km * 0.90)
            + ((distance - 300) * rate_per_km * 0.80)
        )

    return fare


def calculate_age_concession(age, fare):
    # Example age-based concession policy
    if age < 5:
        return fare       # Free fare for children below 5
    elif age <= 12:
        return fare * 0.50
    elif age >= 60:
        return fare * 0.40
    else:
        return 0


def calculate_passenger_fare(distance, travel_class, age):
    # Travel class rates per kilometre
    class_rates = {
        "SLEEPER": 1.00,
        "AC3": 2.00,
        "AC2": 3.00,
        "AC1": 4.00
    }

    # Reservation fees
    reservation_fees = {
        "SLEEPER": 20,
        "AC3": 40,
        "AC2": 50,
        "AC1": 60
    }

    rate = class_rates[travel_class]
    reservation_fee = reservation_fees[travel_class]

    base_fare = calculate_base_fare(distance, rate)
    concession = calculate_age_concession(age, base_fare)

    # Children below 5 are assumed not to occupy a separate seat
    if age < 5:
        reservation_fee = 0

    final_fare = base_fare - concession + reservation_fee

    return {
        "base_fare": base_fare,
        "concession": concession,
        "reservation_fee": reservation_fee,
        "final_fare": final_fare
    }


def calculate_cancellation_refund(fare, penalty_percent):
    penalty = fare * penalty_percent / 100
    refund = fare - penalty

    return penalty, refund


def main():
    print("========================================")
    print(" RAILWAY FARE AND RESERVATION CALCULATOR")
    print("========================================")

    try:
        distance = float(input("Enter journey distance in km: "))

        if distance <= 0:
            print("Error: Distance must be greater than zero.")
            return

        passengers = int(input("Enter number of passengers: "))

        if passengers <= 0:
            print("Error: At least one passenger is required.")
            return

        print("\nTravel Classes:")
        print("SLEEPER - Sleeper Class")
        print("AC3     - AC 3-Tier")
        print("AC2     - AC 2-Tier")
        print("AC1     - AC First Class")

        passenger_details = []
        total_fare = 0

        for i in range(passengers):
            print(f"\n--- Passenger {i + 1} ---")

            name = input("Enter passenger name: ").strip()

            if not name:
                print("Error: Passenger name cannot be empty.")
                return

            age = int(input("Enter passenger age: "))

            if age < 0 or age > 120:
                print("Error: Enter a valid age between 0 and 120.")
                return

            travel_class = input(
                "Enter travel class (SLEEPER/AC3/AC2/AC1): "
            ).strip().upper()

            if travel_class not in ["SLEEPER", "AC3", "AC2", "AC1"]:
                print("Error: Invalid travel class.")
                return

            fare_details = calculate_passenger_fare(
                distance, travel_class, age
            )

            passenger_details.append({
                "name": name,
                "age": age,
                "travel_class": travel_class,
                **fare_details
            })

            total_fare += fare_details["final_fare"]

        # Display reservation details
        print("\n========================================")
        print("          RESERVATION SUMMARY")
        print("========================================")

        for i, passenger in enumerate(passenger_details, start=1):
            print(f"\nPassenger {i}: {passenger['name']}")
            print(f"Age: {passenger['age']}")
            print(f"Travel Class: {passenger['travel_class']}")
            print(f"Base Fare: Rs. {passenger['base_fare']:.2f}")
            print(f"Age Concession: Rs. {passenger['concession']:.2f}")
            print(
                f"Reservation Fee: "
                f"Rs. {passenger['reservation_fee']:.2f}"
            )
            print(f"Final Fare: Rs. {passenger['final_fare']:.2f}")

        print("\n========================================")
        print(f"Total Passengers: {passengers}")
        print(f"Journey Distance: {distance:.2f} km")
        print(f"Total Reservation Fare: Rs. {total_fare:.2f}")
        print("========================================")

        # Cancellation calculation
        cancel = input(
            "\nDo you want to calculate cancellation charges? (yes/no): "
        ).strip().lower()

        if cancel == "yes":
            penalty_percent = float(
                input("Enter cancellation penalty percentage: ")
            )

            if not 0 <= penalty_percent <= 100:
                print("Error: Penalty must be between 0 and 100.")
                return

            penalty, refund = calculate_cancellation_refund(
                total_fare, penalty_percent
            )

            print("\n========== CANCELLATION DETAILS ==========")
            print(f"Original Fare: Rs. {total_fare:.2f}")
            print(f"Cancellation Penalty: Rs. {penalty:.2f}")
            print(f"Refund Amount: Rs. {refund:.2f}")

        print("\nThank you for using the Railway Calculator!")

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()
```