def factorial(num):
    # Base case: factorial of 0 or 1 is 1
    if num == 0 or num == 1:
        return 1
    else:
        # Recursive case: num! = num * (num-1)!
        return num * factorial(num - 1)

# Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
