# calculater
while True:
    print("welcome to calculater")
    print("opyions")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers ")
    print("Enter 'mutiply'to multiply two numbers")
    print("ENter 'divide' to divide two numbers")
    print("Enter 'quit' to exit from calculate ")
    user_input = input(": ")
    if user_input == "quit":
        print("exit")
        break
    elif user_input == "add":
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        result = str(num1 + num2)
        print("The answer:" + result)
    elif user_input == "subtract":
        num1 = float (input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        result = str(num1 - num2)
        print("The answer:" + result)
    elif user_input == "multiply":
        num1 = float (input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        result = str(num1 * num2)
        print("The answer:" + result)
    elif user_input == "divide":
        num1 = float (input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        result = str(num1 / num2)
        print("The answer:" + result)
    else:
        print("Unknown input")
        




# calculate
while True:
  o = input("if do you want to exit, Enter quit. but if you dont want, Enter your operators: ")
  if o == "quit":
    print("Thank you for your trust.")
    break  
  else:  
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

  if o == "multiply" or o == "MULTIPLY":
    print(int(num1) * int(num2))
  elif o == "divide" or o == "DIVIDE":
    print(int(num1) / int(num2))
  elif o == "add" or o == "ADD":
    print(int(num1) + int(num2))
  elif o == "minus" or o == "MINUS":
    print(int(num1) - int(num2))
  else: 
    print("Your input is not true, Enter the right operator.")

