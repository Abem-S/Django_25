def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

number1 = float(input("Enter the first number: "))
number2 = float(input("Ente the second number: "))
print("Select operation: ")
operand = input("Enter operation(+, -, *, /): ")

if operand == '+':
    print(f"{number1} + {number2} = {add(number1, number2)}")
elif operand == '-':
    print(f"{number1} - {number2} = {subtract(number1, number2)}")
elif operand == '*':
    print(f"{number1} * {number2} = {multiply(number1, number2)}")
elif operand == '/':
    print(f"{number1} / {number2} = {divide(number1, number2)}")
else:
    print("please select only from +, -, *, / and make sure there are no spaces.")