def add(a, b):
    result = a + b
    return result

def sum_two_numbers(a, b):  # Duplicación
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

# Inyección insegura (Security issue)
def eval_user_input():
    user_input = input("Enter expression: ")  # ⚠️ Esto es inseguro
    result = eval(user_input)  # ⚠️ Eval de input sin validación
    print("Result:", result)
