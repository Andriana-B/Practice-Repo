#this program does simple arithmatic calculations 

def calculate(x, y, operator):
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

operation = ''

while True:  
    try:
        number1 = float(input('Enter the first number: '))
        break
    except ValueError: 
        print('This is not a valid number.')

operations_list = ['+', '-', 'x', '\\' ] 
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

calc = calculate(number1, number2, operation)

print(str(number1) + ' ' + operation + ' ' + str(number2) + ' = ' + str(calc))
