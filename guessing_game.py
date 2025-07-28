# Guessing game -Emari, Aiden, Erika
import random


def generate_random_number(): 
    return random.randint(1, 100) #this returns the random number that is generated



def get_user_guess():
    guess_number = int(input("guess a number: "))
    user_try = False
    while user_try == False:
        if not type(guess_number) is int:
            raise ValueError("The number is not an integer")
        elif guess_number < 1 or guess_number > 100:
            print("The number is not in the range")
        else:
            return guess_number

def play_guessing_game():
    secret_number=generate_random_number()
    user_input = False
    tries = 0
    while user_input==False:
        user_number = get_user_guess()
        print(user_number)
        tries += 1
        if user_number == secret_number:
            print("you are correct")
            return tries
        elif user_number < secret_number:
            print("you are too low")
        else:
            print("you are too high")
        



def game_loop():
    user_tries = False
    while user_tries == False: 
        user_tries = play_guessing_game()
if __name__ == "__main__": 
    game_loop()






    
          
   
