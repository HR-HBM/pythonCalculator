repeat = True
while repeat:

    print("Welcome!")

    # x = 0
    # y = 0
    # calculation = 0

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




    x = int(input("Enter the first number: "))
    def continue_calculation():
        global x

        operator = input("Select the operator +, -, *, /: ")
        y = int(input("Enter the next number: "))

        if operator in operations:
            print(f"Operator: {operator},  value: {operations[operator]}")

        else:
            print("invalid operator!")

        calculation = operations[operator](x,y)
        # print(calculation)

        print(f"{x} {operator} {y} = " + str(calculation))

        x = calculation

    continue_calculation()


    user_choice = input("Enter 'yes' to continue calculating or enter 'no' to exit.")

    while user_choice.lower() == "yes":
        continue_calculation()
        user_choice = input("Enter 'yes' to continue calculating or enter 'no' to exit.")
    if user_choice.lower() == "no":
        repeat = True
        continue


