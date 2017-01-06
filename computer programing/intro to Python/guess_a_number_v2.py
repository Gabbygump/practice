import random
import math

def start_screen():
    print("**//**//**//**//**//**//**//**//**//**//")
    print("**                                    **")
    print("**           Guess-A-Number!          **")
    print("**                                    **")
    print("**           Press ENTER to play!     **")
    print("**                                    **")
    print("**                                    **")
    print("**//**//**//**//**//**//**//**//**//**//")
    print()
    
def play():

    low = 1
    high = 100
    limit = int(math.log(high-low,2)) + 1
    tries = 0
    
    print("Let's play a game!")
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".")
    print("You try to guess, and I'll tell you if you're right.")
    print("You have " + str(limit) + " attempts to get it.")

    num = random.randint(1,100)

    got_it = False
    

    while got_it == False and tries < limit:
        
        guess = input("What number am I thinking of? ")
        guess = int(guess)
        input ()
        if guess < num:
            print("Sorry try again. Your guess is too low.")
        elif guess > num:
            print("Sorry try again. Your guess is too high.")
        else:
            got_it = True

        tries += 1

    if got_it == True:
        print("You're a winner!")
    else:
        print("You're a loser! The right answer is " + str(num) + ".")
        input()
def play_again():

    while True:
        answer = input("Would you like to play again? ")
        
        if answer == 'no' or answer == 'n' or answer =='No' or answer == 'N':
            return False
        elif answer == 'yes' or answer == 'Yes' or answer == 'Y' or answer == 'y' :
            return True
        
        print ("What?!!! Just say yes or no!")
            
    

        
# games begins     
start_screen()       
again = True
while again == True:
    play ()
    again = play_again()
    

  
input ()
print ("____  _   _  ____    ____  _  _  ____   ")
print ("(_  _)( )_( )( ___)  ( ___)( \( )(  _\ ")
print ("  )(   ) _ (  )__)   )__) )  (  )(_))")
print ("(__) (_) (_)(____)  (____)(_)\_)(____/  ")
input()
print("Hope you enjoyed the game! come back soon!")
print ("BY:Grace Gumpert")










