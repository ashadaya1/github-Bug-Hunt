# Simple Calculator Program

def add(a, b):
    return a - b  
def subtract(a, b)
    return a + b   

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

if num2 == 0:
    print("Cannot divide by zero")
