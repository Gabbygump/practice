#Guess-A-Number AI
#
#Grace Gumpert
#September 9,2016

import random
import math

def start_screen():
    print("**//**//**//**//**//**//**//**//**//**//")
    print("**                                    **")
    print("**           Guess-A-Number!          **")
    print("**                                    **")
    print("**        Press ENTER to play!        **")
    print("**                                    **")
    print("**                                    **")
    print("**//**//**//**//**//**//**//**//**//**//")
    input()

def play():

    tries = 0
    print("Please enter your name here.")
    name = input()
    print("Hi," + name)
    print("What do you want your low value to be?")
    low = input()
    low = int(low)
    print("What do you want your high value to be?")
    high = input()
    high = int(high)
    print("Let's play a game!")
    print("Please think of a number from " + str(low) + " to " + str(high) + " and I will try to guess what it is.") 
    print("I will try to guess, and you will tell me if I am right or wrong.")
    print("Please press enter to begin the game.")
    input()

    got_it = False

    while got_it == False:

        guess = (high+low)//2
        print("Is the number " + str(guess)+("?"))
        answer = input ( name + ",say either higher, lower, or yes.")
        if answer == 'higher' or answer =='h':
            low = guess + 1
        elif answer == 'lower' or answer == 'l':
            high = guess -1
        elif answer == 'yes' or answer == 'y':
            got_it = True
            print("Yay! I got it right.")
            print("I guessed the right answer in " + str(tries)+" tries!")
        else:
            print("What? Just say higher, lower , or yes.")
        tries+=1

def play_again():

    while True:
        answer = input("Would you like to play again?")
        
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


print ("____  _   _  ____    ____  _  _  ____   ")
print ("(_  _)( )_( )( ___)  ( ___)( \( )(  _\ ")
print ("  )(   ) _ (  )__)   )__) )  (  )(_))| ")
print ("(__) (_) (_)(____)  (____)(_)\_)(____/  ")
print("Hope you enjoyed the game! Come back soon!")
print("By:Grace Gumpert")
print("Completed on September 9,2016.")
