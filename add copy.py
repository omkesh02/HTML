
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
    print("Sum:", int(result) if result.is_integer() else result)

if __name__ == "__main__":
    main()