# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero!"

# Main calculator function
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations: 1) Add  2) Subtract  3) Multiply  4) Divide")

    while True:
        try:
            choice = int(input("Enter operation number (1-4) or 0 to exit: "))
            if choice == 0:
                print("Goodbye!")
                break
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")

        print()  # Blank line for readability

# Run the calculator
if __name__ == "__main__":
    calculator()