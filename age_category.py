#!/usr/bin/env python3
# age_category.py
# Day 10: Age category assignment

def main():
    name = input("Enter your name: ").strip()
    try:
        age = int(input("Enter your age: ").strip())
    except ValueError:
        print("Invalid input: enter a number for age.")
        return

    if age < 0:
        print("Age cannot be negative.")
        return

    if 0 <= age <= 12:
        category = "Child"
    elif 13 <= age <= 19:
        category = "Teen"
    elif 20 <= age <= 59:
        category = "Adult"
    else:
        category = "Senior"

    print(f"\nName: {name}\nAge: {age}\nCategory: {category}")

if __name__ == "__main__":
    main()
