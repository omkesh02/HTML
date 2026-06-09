# add_two_numbers_cli.py
import argparse

def add(a, b):
    return a + b

def main():
    p = argparse.ArgumentParser(description="Add two numbers")
    p.add_argument("a", type=float, help="First number")
    p.add_argument("b", type=float, help="Second number")
    args = p.parse_args()

    result = add(args.a, args.b)
    print("Sum:", int(result) if result.is_integer() else result)

if __name__ == "__main__":
    main()