#!/usr/bin/env python3
# calculator.py
# Day 8: Simple calculator

def main():
    try:
        a = float(input("Enter first number: ").strip())
        b = float(input("Enter second number: ").strip())
    except ValueError:
        print("Invalid input: enter numeric values.")
        return

    op = input("Operator (+, -, *, /, %, **): ").strip()

    try:
        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            res = a / b
        elif op == "%":
            res = a % b
        elif op == "**":
            res = a ** b
        else:
            print("Unsupported operator.")
            return
    except ZeroDivisionError:
        print("Error: division by zero.")
        return

    print(f"\nResult: {a} {op} {b} = {res}")

if __name__ == "__main__":
    main()
