def calculate_tax(status, income):
    # Define the tax brackets for each filing status
    tax_brackets = {
        0: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],
        1: [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)],
        2: [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)],
        3: [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)]
    }

    brackets = tax_brackets[status]
    tax = 0
    last_amount = 0

    for limit, rate in brackets:
        if income > last_amount:
            taxable_amount = min(income - last_amount, limit - last_amount)
            tax += taxable_amount * rate
            last_amount = limit

    return tax

def main():
    while True:
        try:
            status = int(input("Enter the filing status : "))
            income = float(input("Enter the taxable income: "))
            tax = calculate_tax(status, income)
            print(f"Tax is {tax:.2f}")
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
        
        # Ask user if they want to continue
        continue_test = input("Do you want to calculate another tax? (yes/no): ")
        if continue_test.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
