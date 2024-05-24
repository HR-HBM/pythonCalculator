print("Welcome!")

x = 0
y = 0

x = int(input("Enter the first number: "))
operator = input("Enter the operator +, -, *, /: ")
y = int(input("Enter the next number: "))

#calculator functions

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y


#calculator operator dictionary

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

if operator in operations:
    print(f"Operator: {operator},  value: {operations[operator]}")

else:
    print("invalid operator!")

calculation = operations[operator](x,y)

print(f"{x} {operator} {y} = " + str(calculation))


