import random 
def show_start_screen():
    print("Let's play Hangman!")

def show_credits():
    print ( "by Grace Gumpert")

def get_puzzle():
    words = ["patriots","soccer","french fries","greenville","mann" "lemon","cucumber","watch","phone", "computer","ice cubes","cab","cats","dogs","violet","orange","blue green"]
    return random.choice(words)

def check(word,solved, guesses):
    for i in range(len(word)):
        if word[i] in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]
    return solved 

def get_guess():
     guess = input("Guess a letter: ")
     return guess

def confirm():
    pass

def play():

    word = get_puzzle()
    
    solved = "-" * len(word)
    guesses = ""
    
    solved = check(word, solved, guesses)
    print(solved)

    while word != solved:
        guesses += get_guess ()
        solved = check(word, solved, guesses)
        print(solved)

    print("You win!")


def main():
    show_start_screen()
    play()
    show_credits()


# code execution begins here
if __name__ == "__main__":
    main()
