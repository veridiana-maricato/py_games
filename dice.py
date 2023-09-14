# age = input("whats your age? ")

# yearsLeft = 90 - int(age) 

# monthsLeft = yearsLeft * 12

# weeksLeft = yearsLeft * 52


# if int(age) > 5:
#     print(f"you still have {yearsLeft} years, {monthsLeft} months and {weeksLeft} weeks left, congrats!")

# someArray = [1,2,3,4]

# someTuple = 1,2,3

# someArray.extend([1])

# print(someArray)

# for nums in someArray:
#     if nums != 1:
#         print(f"this nums is dif then 1: {nums}")

import random
import time

def play_dice():    
    player = random.randint(1,6)

    ai = random.randint(1,6)

    print("************** GAME ON **************")

    time.sleep(1)

    print(f"You: {player}")
    time.sleep(1)
    print(f"Computer: {ai}")
    time.sleep(1)

    if player > ai:
        print("Congrats! You won!")

    elif ai > player:
        print("Sorry! You lost...")

    else:
        print("It's a tie!")

    anwser = input("Press enter to play again or type 'exit' to exit game ")   

    if anwser.lower() == "exit":
        return
    else:
        play_dice()

answer = input("Press enter to start")

play_dice()

