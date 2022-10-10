# #DAY 2
# # Ctrl + /     --comment out code
#
# print("Hello"[0])  #Will print the 1st char in the str
#
# print(123_456_789)   #output will join the numbers
#
# #Float 3.12
# #Boolean True or False
#
# num = 12.34
# example = True
# print(type(num))
# print(type(example))
#
# #Type conversion
# # string = str(num)
# # print(string)
# # print(type(string))
# a = str(123)
# print(type(a))
# print(70 + float("30"))

#Exercise
# two_digit_number =input("Type a two digit number: ")
#
# print(type(two_digit_number))
#
# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])
#
# print(num1 + num2)

#print(6/3)  #will print out a floating num


##POwer of a number

#num = 2**3
#print(num)  ##Python follows BODMAS


#BMI CALCULATOR EXERCISE
# height = input("Enter your height in metres: ")
# weight = input("Enter your weight in kilograms: ")
#
# bmi = (float(weight) / (float(height) ** 2))
#
# print(int(bmi))


#Round off numbers
# print(8/3)
# print(round(8/3))
# print(round(8/3, 2))             #decimal places
# print(round(23.56786543, 4))
#
# print(8 // 3)  # // will turn from decimal num to int
# print(type(8 / 3))
# print(type(8 // 3))
#
# result = 4 / 2
# result /= 2
#
# print(result)

#score = 0
#score += 1   #score = score + 1;
#score -= 1   #score = score - 1;

#You cannot print two datatypes at the same time
#print("Your score is : " + score)    wrong
#print("Your score is : " + str(score))   right


#F-string           --be able to print multiple datatypes in a line
#marks = 76
#grade = "A+"
#print(f"Your marks is: {marks} and your grade is : {grade}")


#YOUR LIFE IN WEEKS

#age = input("What is your current age? ")

# age_in_int = int(age)
#
# years_remaining = 90 - age_in_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
#
# print(f"You have {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks, {days_remaining} days")

#TIP CALCULATOR

print("WELCOME TO THE SPLIT BILL CALCULATOR")
bill = float(input("What is your total bill? $"))

tip = float(input("What percentage would you like to give? 10, 12, 15 "))

people = int(input("How many people are there to split the bill? "))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people

print(f"Each person should pay : {round(bill_per_person, 2)} dollars")    #bill_per_person = "{:.2f}".format(bill_per_person)  #otput will be in 2 decimal places













