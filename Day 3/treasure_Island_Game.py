#DAY 3
# print("Welcome to the rollercoaster!")
#
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry, grow taller")



#Program to print if a given number is even or odd

# number = int(input("Enter a whole number: "))
#
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")



#NESTED IF ELSE
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Pay $5")
#     elif age <= 18:
#         print("Pay $7")
#     else:
#         print("Pay $12")
# else:
#     print("Grow taller bruh")



#BMI CALCULATOR EXERCISE
# height = input("Enter your height in metres: ")
# weight = input("Enter your weight in kilograms: ")
#
# bmi = (float(weight) / (float(height) ** 2))
#
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30:
#     print("Overweight")
# elif bmi < 35:
#     print("Obese")
# else:
#     print("Clinically Obese")
#
# print(round(bmi, 2))




#LEAP YEAR EXERCISE
#a year that is divisible by 4 with no remainder is a leap yr
#if it is also divisible by 100 with no remainder, it is not a leap year
#unless that sam year is divisible by 400 with no remainder, its is a leap yr
#USE FLOWCHARTS TO GET THE LOGIC STRAIGHT
# print("LEAP YEAR CALCULATOR")
# year = int(input("Enter a year : "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")



#ROLLERCOASTER EXERCISE
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# bill = 0
#
# if height > 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print(f"Pay $ {bill}")
#     elif age <= 18:
#         bill = 7
#         print(f"Pay $ {bill}")
#     else:
#         bill = 12
#         print(f"Pay $ {bill}")
#
#     answer = input("Or do you want to be given photos after the ride for an additional $3 to your bill? Type yes or no ")
#     if answer == 'yes':
#         print(f"Total bill is {bill + 3}")
#     elif answer == 'no':
#         print(f"Total bill remains as {bill}")
#     else:
#         print("Wrong input. Try again. Enter yes or no")
# else:
#     print("Grow taller bruh")


#PIZZA ORDER SYSTEM -calculating total bill
#if size
#elif
#else

#if peporoni
#elif
#else

#if cheese
#elif
#else

# print("Welcome to python pizza deliveries! ")
# size = input("What size of pizza do you want? S , M , L ")
# add_peperoni = input("Do you want peperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# bill = 0
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
# cheese = 1
# pep_small = 2
# pep_med_large = 3
#
# if size == 'S':
#     if add_peperoni == 'Y':
#         bill = small_pizza + pep_small
#         if extra_cheese == 'Y':
#             bill = small_pizza + pep_small + cheese
#             print(f"Your total bill is: ${bill}")
#         elif extra_cheese == 'N':
#             bill = small_pizza + pep_small
#             print(f"Your total bill is: ${bill}")
#     elif add_peperoni == 'N':
#         if extra_cheese == 'Y':
#             bill = small_pizza + cheese
#             print(f"Your total bill is: ${bill}")
#         elif extra_cheese == 'N':
#             bill = small_pizza
#             print(f"Your total bill is: ${bill}")
#
# if size == 'M':
#     if add_peperoni == 'Y':
#         bill = medium_pizza + pep_med_large
#         if extra_cheese == 'Y':
#             bill = medium_pizza + pep_med_large + cheese
#             print(f"Your total bill is: ${bill}")
#         elif extra_cheese == 'N':
#             bill = medium_pizza + pep_med_large
#             print(f"Your total bill is: ${bill}")
#     elif add_peperoni == 'N':
#         if extra_cheese == 'Y':
#             bill = medium_pizza + cheese
#             print(f"Your total bill is: ${bill}")
#         elif extra_cheese == 'N':
#             bill = medium_pizza
#             print(f"Your total bill is: ${bill}")
#
#
# if size == 'L':
#     if add_peperoni == 'Y':
#         bill = large_pizza + pep_med_large
#         if extra_cheese == 'Y':
#             bill = large_pizza + pep_med_large + cheese
#             print(f"Your total bill is: ${bill}")
#         elif extra_cheese == 'N':
#             bill = large_pizza + pep_med_large
#             print(f"Your total bill is: ${bill}")
#     elif add_peperoni == 'N':
#         if extra_cheese == 'Y':
#             bill = large_pizza + cheese
#             print(f"Your total bill is: ${bill}")
#         elif extra_cheese == 'N':
#             bill = large_pizza
#             print(f"Your total bill is: ${bill}")



##LOGICAL OPERATORS

# num = 1000
# if num > 1000 or num < 100:
#     print("Yes")
# else:
#     print("No")
#
# age = int(input("Enter your age "))
#
# if age > 12 and age <= 18:
#     print("Allowed entry")
# elif age <= 12:
#     print("Enter with parent")
# else:
#     print("Not allowed")


##EXERCISE
# name1 = 'KEVIN'
# print(name1.lower())
#
# print()
#
# name ='Kevin Kimutai Tarus'
# print(name.count('i'))

##LOVE CALCULATOR
# name1 = input("What is your name? ")
# name2 = input("What is the other person's name? ")
#
# name_c = name1.lower() + name2.lower()
#
# t = name_c.count("t")
# r = name_c.count("r")
# u = name_c.count("u")
# e = name_c.count("e")
#
# l = name_c.count("l")
# o = name_c.count("o")
# v = name_c.count("v")
# e = name_c.count("e")
#
# true = t + r + u + e
# love = l + o + v + e
# score = str(true) + str(love)
#
# if int(score) < 10 or int(score) > 90:
#
#   print(f"Your score is {score}, you go together like coke and mentos.")
#
# elif 40 < int(score) < 50:
#
#   print(f"Your score is {score}, you are alright together.")
#
# else:
#
#   print(f"Your score is {score}.")

#print('You\'re right')                           --use backslash to ignore the apostrophe in you're


##TREASURE ISLAND GAME
print('''  __         ##3 single quotes to print multiple lines
     /  l
   .'   :               __.....__..._  ____
  /  /   \          _.-"        "-.  ""    "-.
 (`-: .---:    .--.'          _....J.         "-.             
  """y     \,.'    \  __..--""       `+""--.     `.           
    :     .'/    .-"""-. _.            `.   "-.    `._.._
    ;  _.'.'  .-j       `.               \     "-.   "-._`.
    :    / .-" :          \  `-.          `-      "-.      \
     ;  /.'    ;          :;               ."        \      `,
     :_:/      ::\        ;:     (        /   .-"   .')      ;
       ;-"      ; "-.    /  ;           .^. .'    .' /    .-"
      /     .-  :    `. '.  : .- / __.-j.'.'   .-"  /.---'
     /  /      `,\.  .'   "":'  /-"   .'       \__.'
    :  :         ,\""       ; .'    .'      .-""
   _J  ;         ; `.      /.'    _/    \.-"
  /  "-:        /"--.b-..-'     .'       ;
 /     /  ""-..'            .--'.-'/  ,  :
:`.   :     / : bug         `-i" ,',_:  _ \
:  \  '._  :__;             .'.-"; ; ; j `.l
 \  \          "-._         `"  :_/ :_/
  `.;\             "-._
    :_"-._             "-.
      `.  l "-.     )     `.
        ""^--""^-. :        \
                  ";         \
                  :           `._
                  ; /    \ `._   ""---.
                 / /   _      `.--.__.'
                : :   / ;  :".  \
                ; ;  :  :  ;  `. `.
               /  ;  :   ; :    `. `.
              /  /:  ;   :  ;     "-'
             :_.' ;  ;    ; :
                 /  /     :_l
                 `-'
''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
print()

choice1 = input("You are at a crossroad, where do you want to go? 'left' or 'right' ?".lower())
if choice1 == 'left':
    choice2 = input("You've come to a lake. There is an island on the lake. Type 'wait' to wait for the boat, type 'swim' to swim across the lake ".lower())
    if choice2 == 'wait':
        choice3 = input("You arrive at the island. There is a red, blue and green door. Choose one to enter. Type 'red' or 'green' or 'blue' ".lower())
        if choice3 == 'red':
            print("You fell into lava bruh")
        elif choice3 == 'blue':
            print("Congratulations blud. You got 10 million won")
        elif choice3 == 'green':
            print("You fell into a room with poisonous snakes and died bruh")
        else:
            print("Wrong input")
    elif choice2 == 'swim':
        print("Game over. Sharks ate you")
    else:
        print("Wrong input")
elif choice1 == 'right':
    print("Game over.You fell into a hole")
else:
    print("Wrong input")



















