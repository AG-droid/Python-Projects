#Taking the input from the user
calc = input('Pls enter the type of calculation you want to do --> ')
num1 = float(input('Pls enter the first number --> '))
num2 = float(input('Pls enter the second number -->'))

def sum():
    #Sorting the info
    global a
    if calc == 'Divide' or 'divide':
        a = num1 / num2
    if calc == 'Multiply' or calc =='multiply':
        a = num1 * num2
    if calc == "Addition" or calc =='Add' or calc == 'addition' or  calc =='add':
        a = num1 + num2
    if calc == 'Subtract' or calc =='subtract' or calc =='Subtraction' or calc =='subtraction':
        a = num1 - num2

    #Displaying the final output
    print('Your final answer is {}'.format(a))

#Initialisng the function
sum()