import random

def word_creation():
    words = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']
    x = int(random.random() * 10)
    return words[x]

secret_word = word_creation()
len_of_random_word = len(secret_word)

def process_of_game():
    tries = 6

    print("Welcome to Wordle!")
    print(f"Guess the {len_of_random_word} - letter word. You have {tries} tries.")
    
    while tries!=0:
        try:
            guess = input(f"Attempt {7 - tries}/6 - Enter guess: ").lower().strip()
        except ValueError:
            print("Wrong value, please, write a number")
        
        if len(guess)!=len_of_random_word:
            print(f"Wrong length. Expected {len_of_random_word}")
            continue

        elif guess==secret_word:
            print("You win!!!")
            break
        
        result=[]
        def character_finding():
            i=0
            while i<len_of_random_word:
                character = guess[i]
                if character==secret_word[i]:
                    result.append('correct')
                elif character in secret_word:
                    result.append('present')
                else:
                    result.append('absent')
                i+=1
        character_finding()

        display=[]
        def displaying_character():
            j=0
            while j<len_of_random_word:
                s = guess[j]
                res = result[j]
                if res=='correct':
                    display.append("["+s.upper()+"]")
                elif res=='present':
                    display.append("("+s+")")
                else:
                    display.append(" "+s+" ")
                j+=1
        displaying_character()

        junk = ''.join([c for c in display if c])
        print("Result:", ' '.join(display))
        tries+=-1
    else:
        print(f"You lose! The word was: {secret_word}")

process_of_game()

def loop_without_rerunning_code():
    choice = input("Your game is over, do you want to play again (yes/no)?").lower()
    if choice == "yes":
        process_of_game()
    else:
        print("Thank you for playing! Good day and a good life!")
loop_without_rerunning_code()