
from user_interface import UserInterface

        
def main():
    ui = UserInterface()

    while True:
        ui.display()
        user_input = ui.get_input()

        if user_input.isdigit():
            num = float(user_input)
            ui.calculator.add(num)
        elif user_input == "+":
            ui.calculator.add(0)
        elif user_input == "-":
            ui.calculator.subtract(0)
        elif user_input == "*":
            ui.calculator.multiply(1)
        elif user_input == "/":
            ui.calculator.divide(1)
        elif user_input == "clear":
            ui.calculator.clear()
        elif user_input == "backspace":
            ui.calculator.backspace()
        elif user_input == "calculate":
            result = ui.calculator.calculate()
            print("Result:", result)
            break
        else:
            print("Invalid input. Please try again.")
            continue
        
        #find the error in this code
        #the error is that the main function is calling itself
        #this is an example of recursion
        #the main function is calling itself
        #this is an example of recursion

        #how to fix this error
        #remove the main() function call from the main function
        #this will fix the error

        #what is the error now?
        #the error now is that the program is not running
        #this is because the main function is not being called
        #the main function is not being called
        #this is because the main function is not being called

    
        #run the program
        #the program is running
        #this is because the main function is being called
        #the main function is being called


        #add a function to the calculator class
        # the function should return the expression
        # the function should return the expression
        # the function should return the expression
        # write the function in the calculator.py file 

