
    
class UserInterface:
     def __init__(self):
         self.calculator = Calculator()

     def display(self):
         print("Calculator")
         print("Expression:", self.calculator.expression)

     def get_input(self):
         return input("Enter a number or operator (+, -, *, /): ")



