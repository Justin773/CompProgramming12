def calculate():
    operation = input(''' 
                      Please type in the operation you would like to continue:
                      + for addition
                      - for subtraction
                      * for multiplication
                      / for division
                      ''')
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    
    if operation == '+': 
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    
    elif operation == '-': 
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        
    elif operation == '*': 
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        
    elif operation == '/': 
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    
    else:
        print('You have not input the correct operation')

def again():
    calc_again = input('Would you like to calculate again? (Y/N): ')
    
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Goodbye')
    else:
        print('Invalid input, please type Y or N')
        again()

calculate()
