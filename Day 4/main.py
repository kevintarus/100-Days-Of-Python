#DAY 4

#IMPORTING YOUR OWN CREATED MODULE
# import my_module     #Crested my_module python file
#
# example = my_module.pi * 12
# print(example)
import random


#RANDOM
# import random   #module
#
# num = random.randint(12,22)    #will run anything between and including those numbers
# print(num)
#
# random_float = random.random()   #will print a random float btwn [0 and 1)
# print(random_float)
#
# random_num = random.random() * 5   #Between 1 and 5
# print(random_num)
#
# lovescore = random.randint(1,100)
# print(f"Your love score is {lovescore} ")



#HEADS OR TAILS GENERATOR
# import random

# print("Welcome to the virtual coin toss generator")
# print()
# input("Press any key to start the generator ")
# print()

# coin = random.randint(0,1)
# print(coin)
# if coin == 0:
#     print("Heads")
# elif coin == 1:
#     print("Tails")




#LISTS
#fruits = [item1, item2]

# courses_in_strathmore = ["law", "computer science", "cyber security"]

# print(courses_in_strathmore[1])
# example = courses_in_strathmore[2]
# print(courses_in_strathmore[-1])  #will start from the end of the list

# courses_in_strathmore[0] = "electrical"
# print(courses_in_strathmore) 

# courses_in_strathmore.append("Kenya")
# print(courses_in_strathmore)

# courses_in_strathmore.extend(["Nairobi", "Omegle", "Linux"])
# print(courses_in_strathmore)

# names = ["Kevin", "Tarus", "Leone", "Owen"]
# guess = random.choice(names)
# print(guess)

# city = ["Lodwar", "Nairobi"]
# country = ["Kenya", "Uganda"]

# nation = [city, country]

# print(nation)


#WHO IS PAYING THE BILL
# names_string = input("Give me everybody's name separated by commas")
# names = names_string.split(", ")              #will store the input as a list
# guess = random.randint(0, len(names) - 1)
# print(f"{names[guess]} is going to pay") 





#TREASURE MAP
#row1 = ["⬜️","⬜️","⬜️"]
#row2 = ["⬜️","⬜️","⬜️"]
#row3 = ["⬜️","⬜️","⬜️"]
#map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}")
#position = input("Where do you want to put the treasure? ")

#horizontal = int(position[0])
#vertical = int(position[1])

#map[vertical - 1][horizontal - 1] = "X"

#print(f"{row1}\n{row2}\n{row3}")





#ROCK PAPER AND SCISSORS               ascii art
rock = '''        
    _______
---'   ____)
      (_____)
      (_____)
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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

       




