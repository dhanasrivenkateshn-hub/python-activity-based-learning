```python
# Multi-Currency Travel Budget Analysis

def convert_currency(amount, exchange_rate, fee_percentage):
    converted_amount = amount * exchange_rate
    conversion_fee = converted_amount * fee_percentage / 100
    total_amount = converted_amount + conversion_fee

    return converted_amount, conversion_fee, total_amount


def main():
    print("=" * 60)
    print("       MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")
    print("=" * 60)

    base_currency = input(
        "Enter base currency (e.g., INR, USD, EUR): "
    ).strip().upper()

    try:
        budget = float(input("Enter total travel budget: "))
        fee_percentage = float(
            input("Enter currency conversion fee percentage: ")
        )
        number_of_expenses = int(
            input("Enter number of travel expenses: ")
        )

        # Validate initial inputs
        if budget < 0:
            print("Error: Budget cannot be negative.")
            return

        if not 0 <= fee_percentage <= 100:
            print("Error: Fee must be between 0 and 100%.")
            return

        if number_of_expenses <= 0:
            print("Error: Enter at least one expense.")
            return

        expenses = []
        total_spending = 0

        # Collect expense information
        for i in range(number_of_expenses):
            print(f"\n--- Expense {i + 1} ---")

            category = input(
                "Enter category (Hotel/Food/Transport/Shopping/Other): "
            ).strip().title()

            if not category:
                print("Error: Category cannot be empty.")
                return

            currency = input(
                "Enter expense currency (e.g., USD, EUR, INR): "
            ).strip().upper()

            if not currency:
                print("Error: Currency cannot be empty.")
                return

            amount = float(input("Enter expense amount: "))

            if amount < 0:
                print("Error: Expense amount cannot be negative.")
                return

            # Exchange rate means units of base currency
            # received for one unit of the expense currency.
            if currency == base_currency:
                exchange_rate = 1.0
            else:
                exchange_rate = float(
                    input(
                        f"Enter exchange rate (1 {currency} = "
                        f"how many {base_currency}?): "
                    )
                )

                if exchange_rate <= 0:
                    print("Error: Exchange rate must be positive.")
                    return

            converted, fee, total = convert_currency(
                amount, exchange_rate, fee_percentage
            )

            expenses.append({
                "category": category,
                "currency": currency,
                "original_amount": amount,
                "exchange_rate": exchange_rate,
                "converted_amount": converted,
                "conversion_fee": fee,
                "total": total
            })

            total_spending += total

        # Display itemized expense report
        print("\n" + "=" * 90)
        print("                  TRAVEL EXPENSE REPORT")
        print("=" * 90)

        print(
            f"{'Category