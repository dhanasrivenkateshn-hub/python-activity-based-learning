```python
# Multi-Plan Telecommunications Cost Optimization

def calculate_plan_cost(plan, data_used, call_minutes, sms_used, days_used):
    # Calculate excess usage
    extra_data = max(0, data_used - plan["data"])
    extra_calls = max(0, call_minutes - plan["calls"])
    extra_sms = max(0, sms_used - plan["sms"])

    # Calculate excess charges
    data_charge = extra_data * plan["extra_data_rate"]
    call_charge = extra_calls * plan["extra_call_rate"]
    sms_charge = extra_sms * plan["extra_sms_rate"]

    excess_charges = data_charge + call_charge + sms_charge

    # Total plan cost
    total_cost = plan["price"] + excess_charges

    # Check validity and budget constraints
    validity_ok = plan["validity"] >= days_used
    budget_ok = total_cost <= budget

    eligible = validity_ok and budget_ok

    return {
        "name": plan["name"],
        "base_price": plan["price"],
        "data_charge": data_charge,
        "call_charge": call_charge,
        "sms_charge": sms_charge,
        "excess_charges": excess_charges,
        "total_cost": total_cost,
        "validity_ok": validity_ok,
        "budget_ok": budget_ok,
        "eligible": eligible
    }


# Example mobile plans
plans = [
    {
        "name": "Basic Plan",
        "price": 199,
        "data": 10,
        "calls": 200,
        "sms": 100,
        "validity": 28,
        "extra_data_rate": 10,
        "extra_call_rate": 0.50,
        "extra_sms_rate": 0.25
    },
    {
        "name": "Standard Plan",
        "price": 299,
        "data": 30,
        "calls": 500,
        "sms": 200,
        "validity": 28,
        "extra_data_rate": 8,
        "extra_call_rate": 0.40,
        "extra_sms_rate": 0.20
    },
    {
        "name": "Premium Plan",
        "price": 399,
        "data": 60,
        "calls": 1000,
        "sms": 500,
        "validity": 56,
        "extra_data_rate": 5,
        "extra_call_rate": 0.30,
        "extra_sms_rate": 0.10
    },
    {
        "name": "Unlimited Plan",
        "price": 499,
        "data": 100,
        "calls": 1500,
        "sms": 1000,
        "validity": 84,
        "extra_data_rate": 3,
        "extra_call_rate": 0.20,
        "extra_sms_rate": 0.05
    }
]


# Get user requirements
print("===== MOBILE PLAN COST OPTIMIZER =====")

try:
    data_used = float(input("Enter data usage in GB: "))
    call_minutes = int(input("Enter call minutes required: "))
    sms_used = int(input("Enter number of SMS required: "))
    days_used = int(input("Enter required validity in days: "))
    budget = float(input("Enter your budget in Rs: "))

    if (
        data_used < 0
        or call_minutes < 0
        or sms_used < 0
        or days_used <= 0
        or budget < 0
    ):
        print("Error: Usage and budget cannot be negative.")
        print("Validity must be greater than zero.")

    else:
        results = []

        # Evaluate all plans
        for plan in plans:
            result = calculate_plan_cost(
                plan,
                data_used,
                call_minutes,
                sms_used,
                days_used
            )
            results.append(result)

        # Display comparison
        print("\n========== PLAN COMPARISON ==========")

        for result in results:
            print(f"\nPlan: {result['name']}")
            print(f"Base Price: Rs. {result['base_price']:.2f}")
            print(f"Extra Data Charges: Rs. {result['data_charge']:.2f}")
            print(f"Extra Call Charges: Rs. {result['call_charge']:.2f}")
            print(f"Extra SMS Charges: Rs. {result['sms_charge']:.2f}")
            print(f"Total Extra Charges: Rs. {result['excess_charges']:.2f}")
            print(f"Total Cost: Rs. {result['total_cost']:.2f}")

            print(
                "Validity: "
                + ("Satisfied" if result["validity_ok"] else "Insufficient")
            )

            print(
                "Budget: "
                + ("Satisfied" if result["budget_ok"] else "Exceeded")
            )

            print(
                "Status: "
                + ("Eligible" if result["eligible"] else "Not Eligible")
            )

        # Find the most economical eligible plan
        eligible_plans = [
            result for result in results if result["eligible"]
        ]

        print("\n========== BEST PLAN ==========")

        if eligible_plans:
            best_plan = min(
                eligible_plans,
                key=lambda result: result["total_cost"]
            )

            print(f"Recommended Plan: {best_plan['name']}")
            print(f"Total Cost: Rs. {best_plan['total_cost']:.2f}")
            print(f"Base Price: Rs. {best_plan['base_price']:.2f}")
            print(
                f"Excess Charges: Rs. "
                f"{best_plan['excess_charges']:.2f}"
            )
        else:
            print("No plan satisfies all your requirements.")
            print("Try increasing your budget or reducing usage.")

except ValueError:
    print("Error: Please enter valid numeric values.")
```