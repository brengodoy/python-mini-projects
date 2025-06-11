# this is the game where the computer picks a random number and the user must guess what it is.
import random

def generate_number():
	number = random.randint(0,9)
	return number
	
def enter_number(): 
	number_guessed = int(input())
	return number_guessed
	
def verify_correct_number(number,number_guessed): 
	if number == number_guessed:
		return True
	else:
		return False

def enter_option():
    return input()
  
def number_game():
    lifes_left = 5
    option = 'Y'
    while option == 'Y':
        number = generate_number()
        print("I've already chosen a number, now you have to guess it.")
        print("Guess the number between 0 and 9: ")
        number_guessed = enter_number()
        result = verify_correct_number(number,number_guessed)
        if result:
            print("Correct! The number I chose was: " + str(number))
        else:
            print("Wrong, the number I chose was: " + str(number))
            lifes_left = lifes_left - 1
            if lifes_left == 0: 
                print("You don't have any more attempts.")
                break
        print("You still have " + str(lifes_left) + " attempts left.")
        print("Do you want to try again? Y/N")
        option = enter_option()
    
    
if __name__ == "__main__":
    number_game()