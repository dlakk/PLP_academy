# Basic Calculator Program

# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

def calculator():
  def get_operand(prompt):
    while True:
      try:
        return int(input(prompt))
      except ValueError:
        print("Invalid input! Please enter an integer.")

  def get_operation():
    while True:
      operation = input("Enter the operation (+, -, *, /): ")
      if operation in ["+", "-", "*", "/"]:
        return operation
      else:
        print("Invalid operation! Please enter one of +, -, *, /.")

  def arithmetic(num1, num2, operation):
    if operation == "+":
      return "{num1} + {num2} = {result}".format(num1=num1, num2=num2, result=num1 + num2)
    elif operation == "-":
      return "{num1} - {num2} = {result}".format(num1=num1, num2=num2, result=num1 - num2)
    elif operation == "*":
      return "{num1} * {num2} = {result}".format(num1=num1, num2=num2, result=num1 * num2)
    elif operation == "/":
      if num2 == 0:
        return "Cannot divide by zero!"
      return "{num1} / {num2} = {result}".format(num1=num1, num2=num2, result=num1 / num2)

  def repeat():
    while True:
      num1 = get_operand("Enter the first operand: ")
      num2 = get_operand("Enter the second operand: ")
      operation = get_operation()
      result = arithmetic(num1, num2, operation)
      print(result)
      feedback = input("Do you want to perform another calculation? (y/n): ").lower()
      if feedback != "y":
        print("Great doing Math with you!")
        break

  repeat()
  

print(calculator())     

#Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again.

# Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡
