def add(n1, n2):
    return n1 + n2

# TOD0: Write out the other 3 funcitons -subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Can't divide by zero"

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+" ,"-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations: Multiply 4 * 8 using the dictionary

print(operations["*"](4,8))

# TODO: user input

first_number = int(input("What's the first number?: "))
print("+" + "\n" + "-" + "\n" + "*" + "\n" + "/")
select_operation = input("Pick an operation: ")
next_number = int(input("What's the next number?: "))

def operation(first_number, next_number, select_operation):
    if select_operation in operations:
        result = operations[select_operation](first_number, next_number)
        return result
    else:
        return "Invalid"

result = operation(first_number, next_number, select_operation)
print(result)

continue_text = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

while continue_text == "y":
    first_number = result
    print("+" + "\n" + "-" + "\n" + "*" + "\n" + "/")
    select_operation = input("Pick an operation: ")
    next_number = int(input("What's the next number?"))
    operation(first_number, next_number, select_operation)
    result = operation(first_number, next_number, select_operation)
    print(result)
    continue_text = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

if continue_text == "n":
    print(result)



