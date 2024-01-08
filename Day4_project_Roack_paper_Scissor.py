# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# import random
# c=0
# u=0

# print_list=[rock,paper,scissors]
# print(f"user score: {u}")
# print(f"computer score: {c}")
# print(f"THE GAME BEGINS :\n")

# for i in range(5):
#     computer=random.randint(0,2)
#     user=int(input("CHOOSE :\n0-ROCK\n1-PAPER\n2-SCISSOR"))

#     if computer==user:
#         continue
#     elif computer==0 and user==1:
#         print(f"User puts :\n {print_list[user]}")
#         print(f"User puts :\n {print_list[user]}")
#         print("Oh no!")
#         c+=1
#         print(f"user score: {u}\n")
#         print(f"computer score: {c}\n")
#     elif computer==0 and user==2:
#         print(f"User puts :\n {print_list[user]}")
#         print(f"User puts :\n {print_list[user]}")
#         print("Oh no!")
#         c+=1
#         print(f"user score: {u}\n")
#         print(f"computer score: {c}\n")
#     elif computer==1 and user==0:
#         print(f"User puts :\n {print_list[user]}")
#         print(f"User puts :\n {print_list[user]}")
#         print("Oh no Bro!")
#         c+=1
#         print(f"user score: {u}\n")
#         print(f"computer score: {c}\n")
#     elif computer==2 and user==1:
#         print(f"User puts :\n {print_list[user]}")
#         print(f"User puts :\n {print_list[user]}")
#         print("Oh no Bro!")
#         c+=1
#         print(f"user score: {u}\n")
#         print(f"computer score: {c}\n")
#     elif computer==1 and user==2:
#         print(f"User puts :\n {print_list[user]}")
#         print(f"User puts :\n {print_list[user]}")
#         print("Oh Yeah Baby!")
#         u+=1
#         print(f"user score: {u}\n")
#         print(f"computer score: {c}\n")
#     elif computer==2 and user==0:
#         print(f"User puts :\n {print_list[user]}")
#         print(f"User puts :\n {print_list[user]}")
#         print("Oh Yeah Baby!")
#         u+=1
#         print(f"user score: {u}\n")
#         print(f"computer score: {c}\n")
    
# if u > c:
#     print("CONGRATULATIONS! You win!")
# elif u < c:
#     print("GAME OVER BRO. Computer wins!")
# else:
#     print("It's a tie!")

    

rock = '''
    _______
---'   ____)
      (_____)
      (____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print_list = [rock, paper, scissors]
user_score = 0
computer_score = 0

print(f"user score: {user_score}")
print(f"computer_score: {computer_score}")
print("THE GAME BEGINS:\n")

for i in range(5):
    computer_choice = random.randint(0, 2)
    user_choice = int(input("CHOOSE:\n0-ROCK\n1-PAPER\n2-SCISSORS"))

    print(f"User puts:\n {print_list[user_choice]}")
    print(f"Computer puts:\n {print_list[computer_choice]}")

    if computer_choice == user_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        user_score += 1
        print("You win!")
    else:
        computer_score += 1
        print("Computer wins!")

    print(f"user score: {user_score}")
    print(f"computer_score: {computer_score}\n")

if user_score > computer_score:
    print("CONGRATULATIONS! You win!")
elif user_score < computer_score:
    print("GAME OVER. Computer wins!")
else:
    print("It's a tie!")


