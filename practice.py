import random

message = """
SNAKE WATER GUN GAME :
[1] Snake
[2] Water
[3] Gun
"""

def snakeWaterGun():
    print(message)
    game_list = ["Snake", "Water", "Gun"]
    user = input("Choose one: ").capitalize()  # Convert user input to capitalize

    computer = random.choice(game_list)

    if user == "Snake":
        if computer == "Snake":
            print(f"user choice {user} and computer choice {computer} - Game is tie!")
        elif computer == "Water":
            print(f"user choice {user} and computer choice {computer} - You Won!")
        elif computer == "Gun":
            print(f"user choice {user} and computer choice {computer} - You lose!")
    elif user == "Water":
        if computer == "Water":
            print(f"user choice {user} and computer choice {computer} - Game is tie!")
        elif computer == "Snake":
            print(f"user choice {user} and computer choice {computer} - You lose!")
        elif computer == "Gun":
            print(f"user choice {user} and computer choice {computer} - You won!")
    elif user == "Gun":
        if computer == "Gun":
            print(f"user choice {user} and computer choice {computer} - Game is tie!")
        elif computer == "Snake":
            print(f"user choice {user} and computer choice {computer} - You won!")
        elif computer == "Water":
            print(f"user choice {user} and computer choice {computer} - You lose!")
    else:
        print("Oops! Please try again :(")

snakeWaterGun()
