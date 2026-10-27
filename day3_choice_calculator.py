"""
Day 03 - Choice Calculator
Author: Vishakha Bisht
"""

def calculator():
    try:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        op = input("Choose operation (+, -, *, /): ")

        if op == "+":
            print(f"Add: {num1 + num2}")
        elif op == "-":
            print(f"Sub: {num1 - num2}")
        elif op == "*":
            print(f"Mul: {num1 * num2}")
        elif op == "/":
            if num2 != 0:
                print(f"Div: {num1 / num2}")
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid operation!")

        print("\nMade with love - Day 3")

    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    calculator()
