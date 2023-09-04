class Calculator:
     def __init__(self):
         self.expression = ""

     def add(self, num):
         self.expression += "+" + str(num)

     def subtract(self, num):
         self.expression += "-" + str(num)

     def multiply(self, num):
         self.expression += "*" + str(num)

     def divide(self, num):
         self.expression += "/" + str(num)

     def clear(self):
         self.expression = ""

     def backspace(self):
         if self.expression:
             self.expression = self.expression[:-1]                    

     def calculate(self):
         
         #add a function to the calculator class
         # the function should return the expression
         # the function should return the expression
         return self.expression