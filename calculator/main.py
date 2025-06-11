import sys

def addition(a,b):
	return a + b

def subtraction(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    return a / b
    
def show_options():
    print("Please choose an operation:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiply")
    print("4) Division")
    print("5) Exit the calculator")    

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("You didn't entered a correct number.")

def menu():
    operation_option = 6
    a = None
    b = None      
    while operation_option not in range(1,6):
        show_options()
        try:
            operation_option = int(input())
        except ValueError:
            print("The option entered is not correct.")
    if operation_option != 5:
        a = get_valid_float("Please enter the first number you want to calculate with: ")
        if operation_option == 4:
            b = 0
            while b == 0:
                b = get_valid_float("Remember that you can't divide by zero. Please enter the second number you want to calculate with: ")
        else:
            b = get_valid_float("Please enter the second number you want to calculate with: ")
    return operation_option,a,b

def do_the_math(operation_option,a,b):
    match operation_option:
        case 1:
            print("You chose addition. Result of " + str(a) + " + " + str(b) + " is: " + str(addition(a,b)))
        case 2:
            print("You chose subtraction. Result of " + str(a) + " - " + str(b) + " is: " + str(subtraction(a,b)))
        case 3:
            print("You chose multiply. Result of " + str(a) + " * " + str(b) + " is: " + str(multiply(a,b)))
        case 4:
            print("You chose division. Result of " + str(a) + " / " + str(b) + " is: " + str(division(a,b)))

def main():
    continue_option = 'Y'
    print("Welcome to Brenda's calculator!")  
    while continue_option.lower() == 'y':
        operation_option,a,b = menu()
        if operation_option == 5:
            sys.exit()
        do_the_math(operation_option,a,b)
        print("Do you want to use the calculator again? (Y/N)")
        continue_option = input()
            
if __name__ == "__main__":
    main()