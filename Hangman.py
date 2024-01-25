import random

word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)
print(chosen_word)

word_len = len(chosen_word)

for i in range(word_len):
    display += "_"

while display != list(chosen_word):  
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
        for pos in range(word_len):
            letter = chosen_word[pos]
            if letter == guess:
                display[pos] = letter
        print(display)
    else:
        print("Incorrect guess. Try again.")

print("Congratulations! You guessed the word:", chosen_word)
