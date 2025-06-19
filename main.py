import calculator

def main():
    print("Add:", calculator.add(5, 3))
    print("Subtract:", calculator.subtract(10, 4))
    print("Multiply:", calculator.multiply(2, 6))
    print("Divide:", calculator.divide(10, 0))

    # bad indentation
    for i in range(3):
        print("Number", i)
      print("Looping...")

    x = 10 # unused variable

if __name__ == "__main__":
    main()
