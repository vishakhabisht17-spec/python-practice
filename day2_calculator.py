"""
Day 02 - Simple Calculator
Author: Vishakha Bisht 
Description: Basic arithmetic operations
"""

def calculator():
    try:
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        
        print(f"Add: {num1 + num2}")
        print(f"Sub: {num1 - num2}")
        print(f"Mul: {num1 * num2}")
        print(f"Div: {num1 / num2 if num2 != 0 else 'Cannot divide by zero'}")
        
        print("\nMade with ❤️ by Vishakha - Day 2")
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    calculator()
