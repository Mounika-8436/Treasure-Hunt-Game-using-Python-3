def start():
    print("You are in a dark room. There is a door to your left and right.")
    print("Which one do you take? (l or r)")
    
    choice = input("> ").lower()
    if choice == "l":
        snake_room()
    elif choice == "r":
        monster_room()
    else:
        game_over("You wander around until you starve.")

def snake_room():
    print("You enter a room with a snake!")
    print("The snake is guarding the treasure. What do you do?")
    print("1. Try to fight the snake.")
    print("2. Sneak past the snake.")
    
    choice = input("> ")
    if choice == "1":
        game_over("The snake bites you. You lose!")
    elif choice == "2":
        treasure_room()
    else:
        game_over("The snake attacks you out of confusion!")

def monster_room():
    print("You enter a room with a monster!")
    print("The monster is blocking the exit. What do you do?")
    print("1. Fight the monster.")
    print("2. Distract the monster.")
    
    choice = input("> ")
    if choice == "1":
        game_over("The monster overpowers you. You lose!")
    elif choice == "2":
        treasure_room()
    else:
        game_over("The monster gets angry and attacks you!")

def treasure_room():
    print("Congratulations! You've found the treasure room!")
    print("The treasure is yours. You win!")
    play_again()

def game_over(reason):
    print(reason)
    print("Game Over!")
    play_again()

def play_again():
    print("Do you want to play again? (yes or no)")
    choice = input("> ").lower()
    if choice == "yes":
        start()
    elif choice == "no":
        print("Thanks for playing!")
    else:
        print("I didn't understand that. Exiting the game.")

# Start the game
start()
