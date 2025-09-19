#!/usr/bin/env python3
# grade_evaluator.py
# Day 9: Grade evaluator

def main():
    name = input("Enter student name: ").strip()
    try:
        score = int(input("Enter score (0–100): ").strip())
    except ValueError:
        print("Invalid input: enter a number between 0 and 100.")
        return

    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        return

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"\nStudent: {name}\nScore: {score}\nGrade: {grade}")

if __name__ == "__main__":
    main()
