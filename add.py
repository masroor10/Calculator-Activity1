
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")