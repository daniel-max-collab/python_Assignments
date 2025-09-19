#!/usr/bin/env python3
# multiplication_table.py
# Day 11: Multiplication table

def single_table(n):
    print(f"\n--- Multiplication Table for {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def main():
    try:
        number = int(input("Enter a number: ").strip())
    except ValueError:
        print("Invalid input: enter an integer.")
        return

    # Single table
    single_table(number)

    # Bonus: tables 1–5
    print("\n=== Bonus: Tables from 1 to 5 ===")
    for n in range(1, 6):
        single_table(n)

if __name__ == "__main__":
    main()
