import random

word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)
print(chosen_word)

guess = (input("guess a letter: ")).lower()

word_len = len(chosen_word)

for i in range(word_len - 1):
    display += "_"
    
for i in range(5):
    for pos in range(word_len):
        letter = chosen_word[pos]
        if letter == guess:
    display[pos] = letter

# print("".join(display))
print(display)
