# Import
import random
import time
# Text Colours for Aesthetics
global PURPLE
global CYAN
global DARKCYAN
global BLUE
global GREEN
global RED
global YELLOW
global UNDERLINE
global BOLD
global END
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
# Initial Steps to invite in the game:
print(BOLD + UNDERLINE + "Welcome to Hangman!" + END)
print("By: " + BOLD + GREEN + "Josh Wu" + END)
print("⎯⎯⎯")
# input name
name = input(CYAN + "Hello, what is your name?" + END + "\n → " + RED + BOLD)

while True:
    # Enter Your name, first letter becomes capital if not already
    choice1or2 = input(END + CYAN + "Hello " + BOLD + name.capitalize() + END +
                       CYAN + "! Type 1 to start and 2 for intructions." +
                       END + "\n → " + RED + BOLD)  # Greeting

    while choice1or2 != '1' and choice1or2 != '2':
        print(RED + " ↳ " + UNDERLINE + "Invalid" + END + RED + "!" + "\n" +
              END)
        time.sleep(.1)
        choice1or2 = input(CYAN + "Type 1 to start and 2 for intructions." +
                           END + "\n → " + RED + BOLD)
# asks if they want to play or if they want instructions
    if choice1or2 == "2":
        # instructions
        print(
            CYAN +
            "Hangman is a letter guessing game where the player guesses a word letter by letter. The player gets a set amount of tries before the stick figure gets hanged! Letters can repeat more than once!"
            + "\n" + END + RED + BOLD)
        time.sleep(2)
        break
    if choice1or2 == '1':
        # pass means nothing, if they pass then it goes to the next statement
        break

# Fake loading screen because it looks cool

print(BOLD + PURPLE + "\nLoading", end="\r")
time.sleep(.3)
print("Loading.", end="\r")
time.sleep(.3)
print("Loading..", end="\r")
time.sleep(.3)
print("Loading...", end="\r" + "\n\n")
time.sleep(.3)
time.sleep(.7)
# each string deletes and replaces itself!
print("⬚⬚⬚⬚⬚⬚⬚⬚⬚⬚ 0%", end="\r")
time.sleep(.2)
print("▧⬚⬚⬚⬚⬚⬚⬚⬚⬚ 10%", end="\r")
time.sleep(.1)
print("▧▧⬚⬚⬚⬚⬚⬚⬚⬚ 20%", end="\r")
time.sleep(.1)
print("▧▧▧⬚⬚⬚⬚⬚⬚⬚ 30%", end="\r")
time.sleep(.2)
print("▧▧▧▧⬚⬚⬚⬚⬚⬚ 40%", end="\r")
time.sleep(.2)
print("▧▧▧▧▧⬚⬚⬚⬚⬚ 50%", end="\r")
time.sleep(.1)
print("▧▧▧▧▧▧⬚⬚⬚⬚ 60%", end="\r")
time.sleep(.2)
print("▧▧▧▧▧▧▧⬚⬚⬚ 70%", end="\r")
time.sleep(.2)
print("▧▧▧▧▧▧▧▧⬚⬚ 80%", end="\r")
time.sleep(.3)
print("▧▧▧▧▧▧▧▧▧⬚ 90%", end="\r")
time.sleep(.1)
print(BOLD + "▩▩▩▩▩▩▩▩▩▩ 100%", end="\r")
time.sleep(.05)
print("\n")  # new line
time.sleep(1)  # time.sleep(.2) 3 seconds before next string starts
print(YELLOW + BOLD + "Let the Games Begin! \n" + END)
time.sleep(1.5)


# Paramaters:
def main():  # Function Main
    # global

    global count
    global underscores
    global word
    global alreadyGuessed
    global wordLength
    global playGame
    global mystery
    # words to guess, you can change these
    words_to_guess = [
        "january", "border", "image", "film", "promise", "kids", "lungs",
        "doll", "rhyme", "plants", "apple", "ape", "banana", "python",
        "strong", "fruit", "parrot", "pear", "september", "month", "day",
        "hour", "second", "minute", "decade", "century", "document"
    ]
    # assigning variables
    word = random.choice(words_to_guess)
    wordLength = len(word)
    count = 0
    underscores = '_' * wordLength
    alreadyGuessed = []
    playGame = ""
    mystery = word  # this comes useful around line 233 since the word variable changes values.  This keeps its original value.


# IF the game ends...this code loops again to run it again and again.


def play_loop():  #function loop, this asks if you want to play again
    global playGame
    playGame = input("Do You want to play again? y = yes, n = no \n" + RED +
                     BOLD)
    while playGame not in ["y", "n", "Y", "N"]:
        playGame = input("Do You want to play again? y = yes, n = no \n" +
                         RED + BOLD)
    # plays again
    if playGame == "y":
        main()
    # ends the game, should say "repl process died unexpectedly:"
    elif playGame == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()


# Initializing all the conditions required for the game:
def hangman():  # Function Hangman
    global count
    global underscores
    global word
    global alreadyGuessed
    global playGame

    limit = 5
    guess = input(END + CYAN + "This is the Hangman Word: " + underscores +
                  " Enter your guess: \n" + RED + BOLD)
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print(CYAN + "Invalid Input, Try a letter\n" + RED + BOLD)
        hangman()
# prints the letter in the 'mystery' word
    elif guess in word:
        alreadyGuessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        underscores = underscores[:index] + guess + underscores[index + 1:]
        print(underscores + "\n")
# if its already guessed, then it tells you to try another letter
    elif guess in alreadyGuessed:
        print(END + CYAN + "You already guessed that! Try another letter!\n" + RED)
# fail string
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print(DARKCYAN + """ 
 ____
|/   |
|   
|    
|    
|    
|
|_____

            """ + END)
            print(END+CYAN + "Wrong guess. " + str(limit - count) +
                  " guesses remaining\n " +
                  RED)  #subtraction included --> (limit-count)
# second fail string
        elif count == 2:
            time.sleep(1)
            print(DARKCYAN + """ 
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____

            """ + RED)
            print(END+CYAN + "Wrong guess. " + str(limit - count) +
                  " guesses remaining\n" + RED)
# third fail string
        elif count == 3:
            time.sleep(1)
            print(DARKCYAN + """ 
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____

            """ + RED)
            print(END+CYAN + "Wrong guess. " + str(limit - count) +
                  " guesses remaining\n" + RED)
# fourth fail string
        elif count == 4:
            time.sleep(1)
            print(DARKCYAN + """ 
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____

            """ + RED)
            print(END+CYAN + "Wrong guess. " + str(limit - count) +
                  " last guess remaining\n" + RED)
# 5th fail string
        elif count == 5:
            time.sleep(1)
            print(DARKCYAN + """ 
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \\
|
|_____

            """ + RED)
            # defeat!

            print(CYAN + "Wrong guess. You've been hanged!!!\n")
            # guess word
            print("You guessed: " + RED, alreadyGuessed)
            time.sleep(2)
            # the real word + capitalize
            print(CYAN + "The" , end="\r")
            time.sleep(.3)
            print(CYAN + "The word" , end="\r")
            time.sleep(.7)
            print(CYAN + "The word was:", end="\r")
            time.sleep(.7)
            print(CYAN + "The word was:" + RED, mystery.capitalize() + BLUE, end="\n")
            time.sleep(1)
            play_loop()
# if you won, this statement plays
    if word == '_' * wordLength:
      
        print(GREEN + "✩ Congrats! You have guessed the word correctly! ✩" + BLUE, end="\r")
        time.sleep(.5)
        print(PURPLE + "✭ Congrats! You have guessed the word correctly! ✭" + BLUE, end="\r")
        time.sleep(.5)
        print(GREEN + "✩ Congrats! You have guessed the word correctly! ✩" + BLUE, end="\r")
        time.sleep(.5)
        print(PURPLE + "✭ Congrats! You have guessed the word correctly! ✭" + BLUE, end="\r")
        time.sleep(.5)
        print(GREEN + "✩ Congrats! You have guessed the word correctly! ✩" + BLUE, end="\r")
        time.sleep(.5)
        print(PURPLE + "✭ Congrats! You have guessed the word correctly! ✭" + BLUE, end="\r")
        time.sleep(.5)
        print(GREEN + "✩ Congrats! You have guessed the word correctly! ✩" + BLUE, end="\r")
        time.sleep(.5)
        print(PURPLE + "✭ Congrats! You have guessed the word correctly! ✭" + BLUE, end="\r")
        time.sleep(.5)
        print(GREEN + "✩ Congrats! You have guessed the word correctly! ✩" + BLUE, end="\r")
        time.sleep(.5)
        print(PURPLE + "✭ Congrats! You have guessed the word correctly! ✭" + BLUE, end="\r")
        time.sleep(.5)
        print(GREEN + "✩ Congrats! You have guessed the word correctly! ✩" + BLUE, end="\r")
        time.sleep(.5)
        print(PURPLE + "✭ Congrats! You have guessed the word correctly! ✭" + BLUE, end="\r")
        time.sleep(.5)
        print(GREEN + "✩ Congrats! You have guessed the word correctly! ✩" + BLUE + "\n")
        time.sleep(.5)
        
        
        play_loop()
# if count is not at limit
    elif count != limit:
        hangman()


# back to main function
main()
# back to hangman function
hangman()

# Game 2 *fail
# --------------------------------------------------
# def main1():
#     global number
#     global count
#     global underscores
#     global word
#     global alreadyGuessed
#     global wordLength
#     global playGame

#     words_to_guess = [
#         "january", "border", "image", "film", "promise", "kids", "lungs",
#         "doll", "rhyme", "plants", "apple", "ape", "banana", "python",
#         "strong", "fruit", "parrot", "pear", "september", "month", "day",
#         "hour", "second", "minute", "decade", "century", "document"
#     ]
#     word = random.choice(words_to_guess)
#     wordLength = len(word)
#     count = 0
#     underscores = '_' * wordLength
#     alreadyGuessed = []
#     playGame = ""

# def play_loop1(): #function loop
#     global playGame
#     playGame = input("Do You want to play again? y = yes, n = no \n")
#     while playGame not in ["y", "n","Y","N"]:
#         playGame = input("Do You want to play again? y = yes, n = no \n")
#     if playGame == "y":
#         number_guessing()
#     elif playGame == "n":
#         print("Thanks For Playing! We expect you back again!")
#         exit()

# def number_guessing():
#     import random
#     # random number from 1 to 100
#     number = random.randint(1, 100)
#     # print(number)
#     # start ammount of guesses
#     number_of_guesses = 1
#     print('I am Guessing a number between 1 and 100:'
#           '\nEnter guess #' + str(number_of_guesses))
#     # while loop
#     while number_of_guesses < 8:
#         guess = input()
#         number_of_guesses += 1
#         if int(guess) == number:
#             break

#     # If it's invalid
#         if (int(guess) > 100) or (int(guess) < 1):
#             print('Invalid guess. Try again.')
#             print('Enter guess #' + str(number_of_guesses))
#     # if its too low
#         elif int(guess) < number:
#             print('Higher!')
#             # print('Enter guess #' + str(number_of_guesses) )
#     # if its too high
#         elif int(guess) > number:
#             print('Lower!')

#             # print('Enter guess #' + str(number_of_guesses) )
#         if int(number_of_guesses) == 8:
#             print('Better luck next time. The number was ' + str(number) + ".")
#         else:
#             print('Enter guess #' + str(number_of_guesses))
#     # if it is correct

#     # break redirects to this
#     if int(guess) == number:
#         print('You won in ' + str(number_of_guesses - 1) +
#               ' guesses!  The number was ' + str(number) + '.')
#     # if it isnt right, it prints this:
