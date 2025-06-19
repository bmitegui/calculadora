import calculator
import utils

def main():
    calculator.eval_user_input()  # Security

    print("Add:", calculator.add(2, 3))
    print("Divide:", calculator.divide(5, 0))  # Reliability: no manejo adecuado del error

    utils.greet("Alice")
    utils.greet_again("Alice")

    # No uso try/catch
    file = open("nonexistent.txt", "r")  # Reliability: puede lanzar error y fallar app

if __name__ == "__main__":
    main()
