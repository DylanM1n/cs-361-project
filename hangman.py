#######################################################################  
# Program Filename:  Homewrok#5.py
# Author:   Dylan Miner
# Date: 6/4/2022
# Description: Hangman game
# Input: letters from user
# Output:  statement of correct letter in word or a hangman image popping up in a text file.
#######################################################################  
  
import matplotlib.pyplot as plt
import random 

guess_list = []
full_letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word_list = ['dead','happy','chill','human','terminal','balls','homework','work','money','drake','mountain','blanket']
the_word = []
correctletters = []

####################################################################### 
# Function:  main
# Description: my main function where everything is ran from
# Parameters:  none
# Return values: none
# Pre-Conditions: none
# Post-Conditions:  none
#######################################################################  
def main():
    
    guess_word = word_get()
    input_get()
    
####################################################################### 
# Function:  word_get
# Description: gets word from the global list of words.
# Parameters:  none
# Return values: none
# Pre-Conditions: none
# Post-Conditions: none
#######################################################################  
def word_get():
    guess_word = random.choice(tuple(word_list))
    for i in guess_word:
        the_word.append(i)
    
    print(' _ ' * len(guess_word))
    return guess_word
    
####################################################################### 
# Function:  input_get
# Description: This function gets input from the user and counts the amount of times
#               that the user has left and then if they get a wrong letter then a 
#               hangman image is printed onto the text file
# Parameters:  none
# Return values: none
# Pre-Conditions: none
# Post-Conditions:  none
#######################################################################  
def input_get():
    joe = 6
    james = False
    while joe >= 0:
        print('You have ', joe, 'body parts left')
        user_input1 = input('Enter the LETTER you want to guess: ')
        
        james = check(user_input1)
        if james == True:
            joe -= 1
        if joe == 5:
            myfile = open('hangman1.txt', 'w')
            myfile.write('  O')
            myfile.close()
        elif joe == 4:
            myfile = open('hangman1.txt', 'w')
            myfile.write('  O\n  |')
            myfile.close()
        elif joe == 3:
            myfile = open('hangman1.txt', 'w')
            myfile.write('  O\n /|')
            myfile.close()
        elif joe == 2:
            myfile = open('hangman1.txt', 'w')
            myfile.write('  O\n /|\\')
            myfile.close()
        elif joe == 1:
            myfile = open('hangman1.txt', 'w')
            myfile.write("  O\n /|\\ \n /")
            myfile.close()
        elif joe == 0:
            myfile = open('hangman1.txt', 'w')
            myfile.write("  O\n /|\\ \n / \\ \n*********************\nYOU LOST!!!\n*********************")
            myfile.close()
            exit()
####################################################################### 
# Function:  check
# Description: its checks the user input to see if the letter is in the word and if it is a letter at all
#              it also checks if the user got the correct letter 
# Parameters:  u1 (userinput)
# Return values: False, True
# Pre-Conditions: none
# Post-Conditions:  none
#######################################################################  
def check(u1):
   
    #if u1 in full_letter_list:
        #check for letters in list then go from there.

    u1 

   
main()