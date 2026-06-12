

# This program multiplies two numbers entered by the user.

def multiply_numbers(a, b):
    return a * b


def main():
    try:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        result = multiply_numbers(num1, num2)
        print(f'The product of {num1} and {num2} is {result}')
    except ValueError:
        print('Please enter valid numeric values.')


if __name__ == '__main__':
    main()
