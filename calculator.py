
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculator():
    print("\n--- Basic Calculator ---")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Choose operation (1-4): ")

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b == 0:
            print("Error! Cannot divide by zero.")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operation!")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometres to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose conversion (1-2): ")
    value = get_number("Enter value: ")

    if choice == "1":
        print("Miles:", value * 0.621371)
    elif choice == "2":
        print("Fahrenheit:", (value * 9 / 5) + 32)
    else:
        print("Invalid conversion!")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("Enter the exchange rate for your currencies.")
    amount = get_number("Enter amount: ")

    while True:
        rate = get_number("Enter exchange rate: ")
        if rate > 0:
            break
        print("Exchange rate must be greater than zero.")

    result = amount * rate
    print("Converted amount:", round(result, 2))


while True:
    print("\n===== MAIN MENU =====")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Currency Converter")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        calculator()
    elif choice == "2":
        unit_converter()
    elif choice == "3":
        currency_converter()
    elif choice == "4":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice! Please select 1-4.")
sss