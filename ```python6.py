```python
# Retail Billing with Multiple Discount Rules

def calculate_discount(subtotal):
    # Threshold-based discount rules
    if subtotal >= 10000:
        discount_rate = 0.20
    elif subtotal >= 5000:
        discount_rate = 0.15
    elif subtotal >= 2000:
        discount_rate = 0.10
    elif subtotal >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = subtotal * discount_rate

    # Maximum concession limit: Rs. 2000
    maximum_discount = 2000
    discount = min(discount, maximum_discount)

    return discount, discount_rate


def get_tax_rate(category):
    # Category-specific tax rates (example rates)
    tax_rates = {
        "FOOD": 0.05,
        "CLOTHING": 0.05,
        "ELECTRONICS": 0.18,
        "FURNITURE": 0.12,
        "BOOKS": 0.00
    }

    return tax_rates.get(category.upper(), -1)


def main():
    print("=" * 55)
    print("       RETAIL BILLING SYSTEM")
    print("=" * 55)

    try:
        customer_name = input("Enter customer name: ").strip()

        if not customer_name:
            print("Error: Customer name cannot be empty.")
            return

        number_of_products = int(input("Enter number of products: "))

        if number_of_products <= 0:
            print("Error: Enter at least one product.")
            return

        invoice = []
        subtotal = 0
        total_tax = 0

        for i in range(number_of_products):
            print(f"\n--- Product {i + 1} ---")

            product_name = input("Enter product name: ").strip()

            if not product_name:
                print("Error: Product name cannot be empty.")
                return

            category = input(
                "Enter category (FOOD/CLOTHING/ELECTRONICS/"
                "FURNITURE/BOOKS): "
            ).strip().upper()

            tax_rate = get_tax_rate(category)

            if tax_rate < 0:
                print("Error: Invalid product category.")
                return

            price = float(input("Enter price per unit (Rs.): "))
            quantity = int(input("Enter quantity: "))

            if price < 0 or quantity <= 0:
                print("Error: Price cannot be negative and quantity "
                      "must be greater than zero.")
                return

            item_total = price * quantity
            item_tax = item_total * tax_rate

            subtotal += item_total
            total_tax += item_tax

            invoice.append({
                "name": product_name,
                "category": category,
                "price": price,
                "quantity": quantity,
                "item_total": item_total,
                "tax_rate": tax_rate,
                "tax": item_tax
            })

        # Calculate threshold discount
        discount, discount_rate = calculate_discount(subtotal)

        # Allocate discount proportionally across items
        print("\n" + "=" * 75)
        print("                         ITEMIZED INVOICE")
        print("=" * 75)
        print(f"Customer Name: {customer_name}")
        print("-" * 75)

        print(
            f"{'Product':<15}{'Qty':>5}{'Price':>10}"
            f"{'Subtotal':>12}{'Tax':>10}{'Total':>12}"
        )

        print("-" * 75)

        for item in invoice:
            # Proportional allocation of overall discount
            if subtotal > 0:
                item_discount = (
                    item["item_total"] / subtotal
                ) * discount
            else:
                item_discount = 0

            discounted_amount = item["item_total"] - item_discount

            # Calculate tax after discount
            item_tax = discounted_amount * item["tax_rate"]

            item_final = discounted_amount + item_tax

            print(
                f"{item['name'][:15]:<15}"
                f"{item['quantity']:>5}"
                f"{item['price']:>10.2f}"
                f"{item['item_total']:>12.2f}"
                f"{item_tax:>10.2f}"
                f"{item_final:>12.2f}"
            )

        # Recalculate tax after discount
        total_tax_after_discount = 0

        for item in invoice:
            if subtotal > 0:
                item_discount = (
                    item["item_total"] / subtotal
                ) * discount
            else:
                item_discount = 0

            discounted_amount = item["item_total"] - item_discount
            total_tax_after_discount += (
                discounted_amount * item["tax_rate"]
            )

        final_amount = (
            subtotal - discount + total_tax_after_discount
        )

        print("-" * 75)
        print(f"Subtotal Before Discount: Rs. {subtotal:.2f}")
        print(f"Discount Rate: {discount_rate * 100:.0f}%")
        print(f"Total Discount: Rs. {discount:.2f}")
        print(f"Maximum Discount Limit: Rs. 2000.00")
        print(
            f"Tax After Discount: Rs. "
            f"{total_tax_after_discount:.2f}"
        )
        print("-" * 75)
        print(f"FINAL AMOUNT: Rs. {final_amount:.2f}")
        print("=" * 75)
        print("Thank you for shopping!")

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()
```