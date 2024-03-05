#this program does simple arithmatic calculations 

def calculate(x, y, operator): # This function takes two numbers and a symbol
    if operator == '+':
        result = (x) + (y)
        return result
    elif operation == '-':
        result = (x) - (y)
        return result
    elif operation == 'x':
        result = (x) * (y)
        return result
    else: 
        result = (x) / (y)
        return result

operation = '' # To but inputed by user

while True:  # Using while loop to keep asking until a valid number is given
    try:
        number1 = float(input('Enter the first number: '))
        break  # If the input can be converted into float then it is valid, loop ends
    except ValueError: 
        print('This is not a valid number.')

operations_list = ['+', '-', 'x', '\\' ] # Using this list to check that use inputs valid symbol
while True: 
    operation = input('Enter an operation (+, -, x, \): ')
    if operation in operations_list:
        break
    else:
        print('This is not a valid operation.')

while True: 
    try:
        number2 = float(input('Enter the second number: '))
        break
    except ValueError: 
        print('This is not a valid number.')

calc = calculate(number1, number2, operation)  # Calling calulator function with user inputs

print(str(number1) + ' ' + operation + ' ' + str(number2) + ' = ' + str(calc))
