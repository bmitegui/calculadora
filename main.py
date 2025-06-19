import calculator
import utils
import os

def main():
    # Eval input controlado con manejo de excepciones
    try:
        calculator.eval_user_input()
    except Exception as e:
        print("Error during user input evaluation:", e)

    print("Add:", calculator.add(2, 3))

    division_result = calculator.divide(5, 0)
    if division_result is not None:
        print("Divide:", division_result)
    else:
        print("Cannot divide by zero.")

    # Usar bucle para evitar duplicación de llamadas
    for _ in range(3):
        utils.greet_again("Alice")

    # Manejo seguro de apertura de archivo
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file 'nonexistent.txt' was not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")

if __name__ == "__main__":
    main()
