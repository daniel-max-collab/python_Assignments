#!/usr/bin/env python3
# user_profile.py
# Day 7: ask user for info and print a formatted summary

def main():
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    language = input("Favorite programming language: ").strip()
    hobby = input("Hobby: ").strip()

    print()  # blank line for nicer output
    print(f"Hello {name}!")
    print(f"You are: {age}.")
    print(f"Your favorite programming language is {language} and your hobby is {hobby}.")

if __name__ == "__main__":
    main()
