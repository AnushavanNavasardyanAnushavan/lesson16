# N2 ///////Calculator
# def calc(num1, num2, arg, argMin = '+'):
#     try:
#         if argMin == "-":
#             print(-num1 + num2)
#         else:
#             # print(num1 + num2)
#             if arg == "-":
#                 print(num1 - num2)
#             elif arg == "*":
#                 print(num1 * num2)
#             elif arg == "/":
#                 print(num1 / num2)
#             elif arg == "+":
#                 print(num1 + num2)
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
# calcInput = input("Enter number --- ")
# calcInputList = [] 
# for i in calcInput:
#     if i == " ":
#         del i
#     else:
#         calcInputList.append(i)

# # if len(calcInputList) > 3:
# #     del calcInputList[3:]
# print(calcInputList)

# try:
#     calc(int(calcInputList[1]), int(calcInputList[3]), calcInputList[2], calcInputList[0])
# except ValueError:
#     print("Value Error")


# N1 /////PASSWORD
# def password(parol):
#     charList = ["!", "@", "#", "$"]
#     charListCoutn = 0
#     numCount = 0
#     strCount = 0
#     while True:
#         if len(parol) < 8:
#             continue
#         for i in parol:
#             if i in charList:
#                 charListCoutn += 1
#             if i.isdigit():
#                 numCount += 1
#             if i.isalpha():
#                 strCount += 1
        
#         if numCount  >= 2 and strCount >= 2 and charListCoutn >= 1:
#             print("your password is strong!!!!")
#             break
# passwordInput = input("Enter password --> ")
# password(passwordInput)
            
                




# N1 /// IF--ELSE-ի խնդիրներից   dog's age in human years
# def dogAge(age):
    
#     if age <= 2:
#         dogYear = age * 10.5
#         print(dogYear)
#     elif age > 2:
#         dogYear = 21 + ((age - 2) * 4)
#         print(dogYear)
#     elif age < 0:
#         print("0")
# dogAge(3)


# N5 /// IF--ELSE-ի խնդիրներից  Write a python program which will say whowin in game
# import random as r
# def point():
#     userPoint = 0
#     pcPoint = 0
#     while True:
#         pcRandom = r.randint(0, 5)
#         userInput = int(input("Enter number [0, 5] ---> "))
#         if userInput == pcRandom:
#             userPoint += 1
#             print("user point = ", userPoint, "pc point = ", pcPoint)
#         else:
#             pcPoint += 1
#             print("user point = ", userPoint, "pc point = ", pcPoint)
#         if userPoint == 2 or pcPoint == 2:
#             break
# point()


# import random
# while True:
#     choices = ["rock","paper","scissors"]

#     computer = random.choice(choices)
#     player = None

#     while player not in choices:
#         player = input("rock, paper, or scissors?: ").lower()

#     if player == computer:
#         print("computer: ",computer)
#         print("player: ",player)
#         print("Tie!")

#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     elif player == "scissors":
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     elif player == "paper":
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     play_again = input("Play again? (yes/no): ").lower()

#     if play_again != "yes":
#         break

# print("Bye!")



# ///Lesson 11  exercises N1
# def smallest(num1, num2):
#     smalList = []
#     for i in range(1, ((num1 * num2) + 1)):
#         if i % num1 == 0 and i % num2 == 0:
#             smalList.append(i)
#     print(smalList)
    
# userInput = input("ENTER numbers --> ")
# user = userInput.split(" ")
# smallest(int(user[0]), int(user[1]))


# ///Lesson 11  exercises N5
# def fanc(arg):
#     res = 0
#     for i in arg:
#         res += int(i)
#     print( res)
# user = input("Enter numbers ----> ")
# fanc(user)


# Lesson 11  exercises N6  Factorial
# def factorial1(a):
#     result = 1
#     for i in range(1, a + 1):
#         result = result * i
#     return result
# a = input("ur number please ")
# y = factorial1(int(a))
# print(y, "is ur answer")











