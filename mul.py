def mul_numbers(a, b):
    """Multiply two numbers and return the result."""
    return a * b

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = mul_numbers(num1, num2)
    print(f"The product of {num1} and {num2} is {result}")