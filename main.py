#this program does simple arithmatic calculations 

operation = ''

while True:  #using this loop to keep askign for input until user enters a valid int/float
    try:
        number1 = float(input('Enter the first number: '))
        break
    except ValueError: 
        print('This is not a valid number.')

operations_list = ['+', '-', 'x', '\\' ] #using this list to check if users enter a valid operation
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

if operation == '+':
    result = (number1) - (number2)
elif operation == '-':
    result = (number1) - (number2)
elif operation == 'x':
    result = (number1) - (number2)
else: 
    result = (number1) - (number2)

print(str(number1) + ' ' + operation + ' ' + str(number2) + ' = ' + str(result))
