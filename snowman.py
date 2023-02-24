import random
from wonderwords import RandomWord


SNOWMAN_GRAPHIC = [
    '*   *   *  ', # index 0
    ' *   _ *   ', # index 1
    '   _[_]_ * ', # index 2
    '  * (")    ', # index 3
    '  \( : )/ *', # index 4
    '* (_ : _)  ', # index 5
    '-----------'  # index 6
]

SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5

SNOWMAN_WRONG_GUESSES = 7

def get_letter_from_user(wrong_guesses_list, snowman_dict):
    valid_input = False
    user_input_string = None
    
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in wrong_guesses_list:
            print("You have already guessed that letter, and it's not in the word.")
        elif user_input_string in snowman_dict and snowman_dict[user_input_string]:
            print("You have already guessed that letter, and it is in the word.")
        else:
            valid_input = True

    return user_input_string

def wrong_count(wrong_guesses):
    # Build snowman for every wrong guess
    for i in range(SNOWMAN_WRONG_GUESSES + 1 - wrong_guesses, SNOWMAN_WRONG_GUESSES + 1):
        print(SNOWMAN_GRAPHIC[i - 1])

def build_word_dict(snowman_word):
    # Create a dictionary of all letters in randomized words
    snowman_word_dict = {}
    
    for letter in range(len(snowman_word)):
        snowman_word_dict[snowman_word[letter]] = False
    
    return snowman_word_dict

def generate_word_progress_string(snowman_word, snowman_dict):
    # Create a string with the amount of letters in each word and change dashed line to correctly guessed letter
    word_progress_list = []

    for letter in range(len(snowman_word)):
        word_progress_list.append('_ ')

        if snowman_dict[snowman_word[letter]] == True:
            word_progress_list[letter] = (f"{snowman_word[letter]} ")
    
    word_progress_string = ''.join(word_progress_list)

    return word_progress_string.strip()

def get_word_progress(snowman_word, snowman_dict):
    # Tell user when word has been completed
    count = 0 
    
    for letter in snowman_dict:

        if snowman_dict[snowman_word[count]] == False:
            count += 1
            return False
            
        elif snowman_dict[snowman_word[count]] == True:
            count += 1
    
    return True
    
def snowman():
    r = RandomWord()

    snowman_word = r.word(
    word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
    word_max_length=SNOWMAN_MAX_WORD_LENGTH)

    # print(snowman_word)

    snowman_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []


    while not len(wrong_guesses_list) == SNOWMAN_WRONG_GUESSES or get_word_progress(snowman_word, snowman_dict):
        print("\n",generate_word_progress_string(snowman_word, snowman_dict),"\n")
        
        user_letter = get_letter_from_user(wrong_guesses_list, snowman_dict)

        if user_letter in snowman_word:
            snowman_dict[user_letter] = True
            
            if get_word_progress(snowman_word, snowman_dict):
                print("You guessed the word!")
                break

        else:
            print(f"The letter '{user_letter}' is not in the word.")
            wrong_guesses_list.append(user_letter)
            
            if len(wrong_guesses_list) == SNOWMAN_WRONG_GUESSES:
                print("You ran out of guesses.")
                print(f"The word was '{snowman_word}'.")  

        wrong_count(len(wrong_guesses_list))    
    
snowman()