number_of_words = 3319

import sys
import random
import time
import os

os.system('cls')

os.system('color a')

start_time = time.time()

global random_word

#Bug - if random word has 'e' in it then every 'e' in the result is shown (Test by "queek" as random word and "Eerie" as input)
#      only the number of 'e' in random word should be shown is the deirable result    ----Patched(used different algo)

def comparison_func(user_input, random_word):
    assert len(user_input) == len(random_word), "Sizes differ"
    
    letters = list(random_word.lower())
    result = ""

    for l, l_guess in zip(user_input, random_word):
        if l in letters:
            result += l.upper() if l == l_guess else l.lower()
            letters.remove(l)
        else:
            result += "_"

    return result

def random_word_generator():

    file = open("five_letter_words.txt",'r')
    content = file.readlines()

    rand_int = random.randint(0,number_of_words-1)
    return content[rand_int].strip()        #strip() removes spaces from the string

def typeWrite(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

typeWrite("               W O R D L E              \n\n")                  #Instructions and intro

print("Wordle is basically a word guessing game in which a\nrandom 5 letter word is selected from the dictionary and\nthe goal is to guess that word using 6 or less attempts.\n\n")
print("Here -->\n1)A capital case letter indicates the letter is in the correct position.\n2)A lower case letter means the letter is in the word but currently not in the correct position.\n3)An underscore(_) represents the letter is absent from the random word.\n\n")
input("<<Press Enter to start the game>>\n\n")

random_word = random_word_generator()

typeWrite("The random word has been selected.\n")
#Main loop
y = 0
while y < 6:

    user_input = input("Enter your guess: ").strip().lower()
    x=0
    #length check
    if len(user_input) == 5:
        with open("five_letter_words.txt",'r') as file:             #Checking for the user_input in txt file
            for l_no,line in enumerate(file):
                x += 1            
                if user_input in line:
                    final_result = comparison_func(user_input,random_word)

                    if final_result == random_word.upper():
                        typeWrite("You won!!!!")
                        y = 7                        #Win condition
                    else:
                        print("Output: ",final_result,"\n")
                        y = y+1    
                    break    
                    # call the comparison with output function
                    
                    
                if x >= number_of_words:
                    typeWrite("Enter a valid word!!!\n\n")
                    # return to previous state
    else:
        typeWrite("Please enter a 5 letter word!!!\n\n")
        # return to previous state


end_time = time.time()

word_declaration = "The word was: " + random_word.upper()
typeWrite(word_declaration)
time.sleep(1)

os.system('color f')

print("\nThe program took",str(round(float(end_time-start_time),2)).strip(),"s to execute.")
