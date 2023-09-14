import time

def mad_libs():
    print("************** GAME ON **************")
    time.sleep(0.5)
    print("Type 'exit' at any time to quit the game")

    while True:
        animal = input("Write here the name of an animal: ")
        if animal == "exit":
            break

        adjective = input("Now an adjective: ")
        if adjective == "exit":
            break

        place = input("Write the name of a place you like: ")
        if place == "exit":
            break

        action = input("Write an action in the present continuous: ")
        if action == "exit":
            break

        print("Generating your story...")
        time.sleep(1.5)

        print(f"Hey, there! Would you be so kind to adopt this {adjective} {animal}? I saw it when I was coming back from work just {action} in the middle of the street. I wish I could keep it, but I have three {animal}s already. I'm so late to meet my wife at the {place}, but please take it. Look how adorable, how... {adjective}!")

        answer = input("Press Enter to play again or type 'exit' to exit the game: ").lower()
        
        if answer == "exit":
            break

input("Press Enter to start")
mad_libs()

print("Exiting game")

time.sleep(.5)

# import time

# playing = True

# def exitGame(var):
#     global playing
#     if(var == "exit"):       
#         playing = False
#         print("Exiting game")
#         time.sleep(.5)
#     return

# def mad_libs():
#     print("************** GAME ON **************")
#     time.sleep(.5)
#     print("Type exit at any time to quit the game")

#     time.sleep(1)

#     animal = input("Write here the name of an animal: ")
#     exitGame(animal)
#     if not playing:
#         return

#     adjective = input("Now an adjective: ")
#     exitGame(adjective)
#     if not playing:
#         return

#     place = input("Write the name of a place you like: ")
#     exitGame(place)
#     if not playing:
#         return

#     action = input("Write an action in the present continuous: ")
#     exitGame(action)
#     if not playing:
#         return

#     print("Generating your story...")

#     time.sleep(1.5)

#     print(f"Hey, there! Would you be so kind to adopt this {adjective} {animal}? I saw it when I was comming back from work just {action} in the middle of the street. I wish I could keep it, but I have three {animal}s already. I'm so late to meet my wife at the {place}, but please take it. Look how adorable, how... {adjective}!")

#     anwser = input("Press enter to play again or type 'exit' to exit game ")   

#     if anwser.lower() == "exit":
#         return
#     else:
#         mad_libs()

# answer = input("Press enter to start")

# mad_libs()