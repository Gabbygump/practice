import random
import os 
def show_start_screen():
    print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
    print("_     _   _      ___ _             _  _  ")                               
    print("| |___| |_( )___ | _ \ |__ _ _  _  | || |__ _ _ _  __ _ _ __  __ _ _ _ ")  
    print("| / -_)  _|/(_-< |  _/ / _` | || | | __ / _` | ' \/ _` | '  \/ _` | ' \ ") 
    print("|_\___|\__| /__/ |_| |_\__,_|\_, | |_||_\__,_|_||_\__, |_|_|_\__,_|_||_| ")
    print("                             |__/                 |___/    ")             
    print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
    print(" Press enter to play")
    print()
def show_credits():
    print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
    print("  _______  _______  __   __  _______    _______  __   __  _______  ______  ") 
    print(" |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ")
    print(" |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ")
    print(" |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ")
    print(" |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |")
    print(" |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |")
    print(" |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|")
    print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
    print ( "by Grace Gumpert")
def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate(files):
        print(str(i) + ") " + f)

    choice = input("Enter selection: ")
    choice = int(choice)

    return path + "/" + files[choice]

    
def get_puzzle(file):
    words = ["patriots","soccer","french fries","greenville","mann" "lemon","cucumber","watch","phone", "computer","ice cubes","cab","cats","dogs","violet","orange","blue green"]

    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words)

def check(word,solved, guesses):
    for i in range(len(word)):
        if word[i] in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]
    return solved 

def get_guess():
    while True:
         guess = input("Guess a letter: ")
         if len(guess) == 1 and guess.isalpha():
            return guess
         else:
            print("Invalid. Enter just 1 letter.")
         
def display_board(solved, guesses, strikes):

    if strikes == 0:
        pass
    elif strikes == 1:
        print("O")
    elif strikes == 2:
        print("O")
        print("|")
    elif strikes == 3:
        print("O")
        print("|/")
    elif strikes == 4:
        print(" O ")
        print("\|/")
    elif strikes == 5:
        print(" O")
        print("\|/")
        print("/")
    elif strikes == 6:
        print(" O")
        print("\|/")
        print("//")
        
        
    print(solved + " [" + guesses +"]")

def play_again():

    while True:
        answer = input("Would you like to play again?")
        
        if answer == 'no' or answer == 'n' or answer =='No' or answer == 'N':
            return False
        elif answer == 'yes' or answer == 'Yes' or answer == 'Y' or answer == 'y' :
            return True
        


def play():
    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)
    
    guesses = ""
    strikes = 0
    limit = 6
    
    solved = check(word, solved, guesses)
    display_board(solved, guesses, strikes)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
            strikes += 1
            
        guesses += letter
        
        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)

    if word == solved:
        print("You win!")
    else:
        print("You lose!")
    


def main():
    show_start_screen()
    
    playing = True
    
    while playing:
        play()
        playing = play_again()
    show_credits()


# code execution begins here
if __name__ == "__main__":
    main()
