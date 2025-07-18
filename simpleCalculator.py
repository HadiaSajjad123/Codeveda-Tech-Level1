def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2): 
    return num1*num2

def divide(num1,num2): 
    if num2 != 0:
        return num1/num2
    else:
        return "Division by zero error" 
    
while True:
    choice = input("Do you want to perform a calculation? (yes/no): ").strip().lower()
    if choice != 'yes':
        break
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            print("Result:", add(number1, number2))
        elif operation == "-":
            print("Result:", subtract(number1, number2))
        elif operation == "*":
            print("Result:", multiply(number1, number2))
        elif operation == "/":
            print("Result:", divide(number1, number2))
        else:
            print("Invalid operation")

    except ValueError:
        print("Invalid input")