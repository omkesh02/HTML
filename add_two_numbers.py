#!/usr/bin/env python3

def add(a, b):
    return a + b


def main():
    try:
        a = float(input("Enter first number: ").strip())
        b = float(input("Enter second number: ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    result = add(a, b)
    # Print as integer if both inputs were integers
    if result.is_integer():
        print("Sum:", int(result))
    else:
        print("Sum:", result)


if __name__ == "__main__":
    main()
