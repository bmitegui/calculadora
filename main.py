import calculator
import utils

def main():
    calculator.eval_user_input()

    print("Add:", calculator.add(2, 3))
    print("Divide:", calculator.divide(5, 0))

    utils.greet("Alice")
    utils.greet_again("Alice")
    utils.greet_again("Alice")
    utils.greet_again("Alice")

    # No uso try/catch
    file = open("nonexistent.txt", "r")

if __name__ == "__main__":
    main()
