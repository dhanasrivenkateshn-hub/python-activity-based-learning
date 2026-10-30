```python
# Manufacturing Cost and Profitability Analysis

def calculate_material_cost(quantity, material_cost):
    return quantity * material_cost


def calculate_wastage_cost(material_cost, wastage_percentage):
    return material_cost * wastage_percentage / 100


def calculate_labour_cost(workers, hours, hourly_rate):
    return workers * hours * hourly_rate


def calculate_machine_cost(machine_hours, hourly_machine_rate):
    return machine_hours * hourly_machine_rate


def analyze_profitability(
    material_cost,
    wastage_cost,
    labour_cost,
    machine_cost,
    other_cost,
    production_quantity,
    selling_price,
    profit_target
):
    total_cost = (
        material_cost
        + wastage_cost
        + labour_cost
        + machine_cost
        + other_cost
    )

    cost_per_unit = total_cost / production_quantity
    total_revenue = selling_price * production_quantity
    total_profit = total_revenue - total_cost

    if total_revenue > 0:
        profit_margin = (total_profit / total_revenue) * 100
    else:
        profit_margin = 0

    profit_per_unit = selling_price - cost_per_unit

    meets_target = profit_margin >= profit_target

    return {
        "total_cost": total_cost,
        "cost_per_unit": cost_per_unit,
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "profit_per_unit": profit_per_unit,
        "profit_margin": profit_margin,
        "meets_target": meets_target
    }


def main():
    print("=" * 55)
    print(" MANUFACTURING COST AND PROFITABILITY ANALYSIS")
    print("=" * 55)

    try:
        product_name = input("Enter product name: ").strip()

        if not product_name:
            print("Error: Product name cannot be empty.")
            return

        production_quantity = int(
            input("Enter number of units produced: ")
        )

        if production_quantity <= 0:
            print("Error: Production quantity must be positive.")
            return

        # Material costs
        material_quantity = float(
            input("Enter total material quantity used: ")
        )

        material_rate = float(
            input("Enter cost per material unit (Rs.): ")
        )

        if material_quantity < 0 or material_rate < 0:
            print("Error: Material values cannot be negative.")
            return

        material_cost = calculate_material_cost(
            material_quantity, material_rate
        )

        wastage_percentage = float(
            input("Enter material wastage percentage: ")
        )

        if not 0 <= wastage_percentage <= 100:
            print("Error: Wastage percentage must be between 0 and 100.")
            return

        wastage_cost = calculate_wastage_cost(
            material_cost, wastage_percentage
        )

        # Labour costs
        workers = int(input("Enter number of workers: "))
        labour_hours = float(input("Enter working hours per worker: "))
        hourly_labour_rate = float(
            input("Enter labour cost per hour (Rs.): ")
        )

        if workers < 0 or labour_hours < 0 or hourly_labour_rate < 0:
            print("Error: Labour values cannot be negative.")
            return

        labour_cost = calculate_labour_cost(
            workers, labour_hours, hourly_labour_rate
        )

        # Machine costs
        machine_hours = float(input("Enter machine operating hours: "))
        machine_rate = float(
            input("Enter machine cost per hour (Rs.): ")
        )

        if machine_hours < 0 or machine_rate < 0:
            print("Error: Machine values cannot be negative.")
            return

        machine_cost = calculate_machine_cost(
            machine_hours, machine_rate
        )

        # Other production expenses
        other_cost = float(
            input("Enter other production expenses (Rs.): ")
        )

        if other_cost < 0:
            print("Error: Other expenses cannot be negative.")
            return

        # Selling price and profit target
        selling_price = float(
            input("Enter selling price per unit (Rs.): ")
        )

        profit_target = float(
            input("Enter target profit margin percentage: ")
        )

        if selling_price < 0:
            print("Error: Selling price cannot be negative.")
            return

        if not 0 <= profit_target <= 100:
            print("Error: Profit target must be between 0 and 100.")
            return

        # Perform profitability analysis
        result = analyze_profitability(
            material_cost,
            wastage_cost,
            labour_cost,
            machine_cost,
            other_cost,
            production_quantity,
            selling_price,
            profit_target
        )

        # Display report
        print("\n" + "=" * 55)
        print("             PRODUCTION COST REPORT")
        print("=" * 55)

        print(f"Product Name           : {product_name}")
        print(f"Units Produced         : {production_quantity}")
        print("-" * 55)

        print(f"Material Cost          : Rs. {material_cost:.2f}")
        print(f"Wastage Cost           : Rs. {wastage_cost:.2f}")
        print(f"Labour Cost            : Rs. {labour_cost:.2f}")
        print(f"Machine Cost           : Rs