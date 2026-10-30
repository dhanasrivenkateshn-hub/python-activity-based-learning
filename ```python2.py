```python
# Progressive Electricity Billing System

def calculate_bill(units):
    # Electricity charges based on consumption slabs
    bill = 0

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed charge
    fixed_charge = 50

    # Surcharge: 5% of energy charges
    surcharge = bill * 0.05

    # Total before rebate
    total = bill + fixed_charge + surcharge

    # Rebate: 10% if consumption is below 100 units
    rebate = 0
    if units < 100:
        rebate = total * 0.10

    # Final bill
    final_bill = total - rebate

    return round(final_bill, 2)


# Main program
months = int(input("Enter the number of months: "))

monthly_bills = []

for i in range(months):
    month = input(f"\nEnter month {i + 1} name: ")
    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Units cannot be negative. Please restart the program.")
        exit()

    bill = calculate_bill(units)

    monthly_bills.append({
        "month": month,
        "units": units,
        "bill": bill
    })

# Display monthly bills
print("\n========== ELECTRICITY BILL REPORT ==========")

for record in monthly_bills:
    print(f"Month: {record['month']}")
    print(f"Units Consumed: {record['units']}")
    print(f"Electricity Bill: Rs. {record['bill']:.2f}")
    print("---------------------------------------------")

# Compare bills and identify unusual increases
print("\n========== MONTHLY BILL COMPARISON ==========")

threshold = 20  # Flag increases greater than 20%

for i in range(1, len(monthly_bills)):
    previous = monthly_bills[i - 1]
    current = monthly_bills[i]

    increase = current["bill"] - previous["bill"]

    if previous["bill"] > 0:
        percentage = (increase / previous["bill"]) * 100
    else:
        percentage = 0

    print(f"\n{previous['month']} -> {current['month']}")
    print(f"Previous Bill: Rs. {previous['bill']:.2f}")
    print(f"Current Bill: Rs. {current['bill']:.2f}")

    if increase > 0:
        print(f"Bill Increased By: Rs. {increase:.2f}")
        print(f"Percentage Increase: {percentage:.2f}%")
    elif increase < 0:
        print(f"Bill Decreased By: Rs. {abs(increase):.2f}")
    else:
        print("Bill Remained the Same.")

    if percentage > threshold:
        print("WARNING: Unusual bill increase detected!")
    else:
        print("No unusual increase detected.")

print("\n========== REPORT COMPLETED ==========")
```