
import random
import words

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
                                                                    
                                                                       




stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


chosen_word  = random.choice(words.word_list)
display = []
life=6

print(f"Total Life: {life}")

#print(chosen_word)

word_len = len(chosen_word)

for i in range(word_len):
    display += "_"

while (life!=0):  
    guess = input("Guess a letter: ").lower()
    if(display != list(chosen_word)):
        if guess in chosen_word:
            for pos in range(word_len):
                letter = chosen_word[pos]
                if letter == guess:
                    display[pos] = letter
            print(display)
        else:
            life=life-1
            print(stages[life])
            print("Incorrect guess. Try again.")
            print(f"Total Life left: {life}")

    else:
        print("Congratulations! You guessed the word:", chosen_word)
        
else:
    print("You Lost!  the word is :", chosen_word)




    


