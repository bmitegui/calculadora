def add(a, b):
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
        print("Can't divide by zero")
        return
    return a / b

def unused_function(x):
    y = x * x

def long_function():
    print("This is a very long function" +
          " that does not need to be this long" +
          " but we keep going to test complexity" +
          " and also the code smell of long expressions.")
    print("Still printing...")
    print("Maybe we should break this.")
