import random

change = 0

def snakeWaterGum():
    message = """
    GAME:  Snake, Water, Gun
    [1] Snake
    [2] Water
    [3] Gun
    """


    try:
        while True:
            print(message)
            user_choice = int(input("Enter your choice: "))
            computer_choice = random.randint(1,3)

            if user_choice == computer_choice:
                print(f"It's a tie! You choice: {user_choice} and computer choice: {computer_choice}")
            elif user_choice == 1 and computer_choice == 2:
                print(f"You won! You choice: {user_choice} and computer choice: {computer_choice}")
            elif user_choice == 1 and computer_choice == 3:
                print(f"You lost! You choice: {user_choice} and computer choice: {computer_choice}")
            elif user_choice == 2 and computer_choice == 1:
                print(f"You lost! You choice: {user_choice} and computer choice: {computer_choice}")
            elif user_choice == 2 and computer_choice == 3:
                print(f"You won! You choice: {user_choice} and computer choice: {computer_choice}")
            elif user_choice == 3 and computer_choice == 1:
                print(f"You won! You choice: {user_choice} and computer choice: {computer_choice}")
            elif user_choice == 3 and computer_choice == 2:
                print(f"You lost! You choice: {user_choice} and computer choice: {computer_choice}")
            else:
                print("Invalid choice!")
    except:
        print("Oops! Invalid choice. Please try again.")

snakeWaterGum()