#DAY 4

#IMPORTING YOUR OWN CREATED MODULE
# import my_module     #Crested my_module python file
#
# example = my_module.pi * 12
# print(example)


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
import random

print("Welcome to the virtual coin toss generator")
print()
input("Press any key to start the generator ")
print()

coin = random.randint(0,1)
print(coin)
if coin == 0:
    print("Heads")
elif coin == 1:
    print("Tails")
