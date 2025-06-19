def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
        return None
    return a / b

def eval_user_input():
    user_input = input("Enter expression: ") 
    result = eval(user_input)  # ⚠️ Aún es inseguro, pero lo dejamos si estás haciendo pruebas
    print("Result:", result)

# Mensaje informativo único
print(
    "This is a calculator module. " * 5  # imprime el mensaje 5 veces sin duplicarlo manualmente
)
