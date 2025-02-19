# lab2.py

# Starter code for lab 2 in ICS 32 Programming with Software Libraries in Python

# Jordan
# jnetz#uci.edu
# 56628532

from pathlib import Path

def pycalc(operand1, operand2, operation, file_name):
    """
    Perform a calculation based on two operands and an operator.

    Parameters:
    operand1 (int): The first operand.
    operand2 (int): The second operand.
    operation (str): The operation ('+', '-', 'x', '/', 'q').

    Returns tuple of msg, running:
    msg: The result of the calculation as a string.
    running: Boolean value to indicate whether the program should continue to run.
    """
    error = None
    try:
        operand1 = int(operand1)
        operand2 = int(operand2)
    except ValueError:
        error = "ValueError"
        
    try:
        my_path = Path.cwd() / file_name
        my_file = my_path.open('a')
    except IOError as e:
        error = "IOError"
    try:
        if operation == '+':
            result = operand1 + operand2
        elif operation == '-':
            result = operand1 - operand2
        elif operation == 'x':
            result = operand1 * operand2
        elif operation == "/":
            result = operand1 / operand2
        elif operation == "q":
            my_file.close()
            return "Finished", False
        else:
            return "Invalid operator! Please use one of the following: +, -, x, /, or q.", True
    except ZeroDivisionError:
        error = "ZeroDivisionError"
    
    if error == None:
        msg = f"{operand1} {operation} {operand2} = {result}\n"
        my_file.write(msg)
        my_file.close()
    else:
        msg = error

    return msg, True

def main():
    """
    Main function to run the PyCalc program.
    """
    print("Welcome to ICS 32 PyCalc! \n")
    file_name = input("Enter the log file name: ")
    
    running = True
    while running:
        # Collect user input
        operand1 = input("Enter your first operand: ")
        operand2 = input("Enter your second operand: ")
        operation = input("Enter your desired operator (+, -, x, /, or q): ")
        
        # Perform calculation and print result
        result, running = pycalc(operand1, operand2, operation, file_name)
        print(result)

if __name__ == "__main__":
    main()