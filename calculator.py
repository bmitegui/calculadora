def add(a, b):
    result = a + b
    return result

def sum_two_numbers(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
        return None
    return a / b

def eval_user_input():
    user_input = input("Enter expression: ") 
    result = eval(user_input)
    print("Result:", result)


print("This is a calculator module.This is a calculator module. This is a calculator module. This is a calculator module. This is a calculator module. This is a calculator module. This is a calculator module.This is a calculator module. This is a calculator module. This is a calculator module.")