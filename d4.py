import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

rock
"""

paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

paper
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

scissors
"""
my_list = [rock, paper, scissors]

choice = int(input("What do you choose? 0-Rocks, 1-Paper, 2-Scissors"))
user_choice = my_list[choice]
comp_choice = random.choice(my_list)
print(user_choice)
print(comp_choice)

if user_choice == comp_choice:
    print("It's a draw!")
elif user_choice == rock:
    if(comp_choice == scissors):
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == paper:
    if(comp_choice == rock):
        print("You win!")
    else:
        print("You loose!")
elif user_choice == scissors:
    if(comp_choice == paper):
        print("You win!")
    else:
        print("You loose!")




