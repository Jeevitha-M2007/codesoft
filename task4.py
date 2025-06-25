import random

#Initialize score
user_score = 0
computer_score = 0

while True:
    user_input = input("enter your choice : Type 0 for Rock ,1 for Paper ,2 for Scissors.")
    
    if user_input == 'quit':
            print("Game Over.")
            print(f"Final Score — You: {user_score}, Computer: {computer_score}")
            break
        
    if not user_input.isdigit() or int(user_input) not in [0, 1, 2]:
        print("Invalid number. Please enter 0, 1, or 2.")
        continue
    user_choice = int(user_input)
    computer_choice = random.randint(0,2)
    
    print("Computer choice :")
    print(computer_choice)
    print("User choice :")
    print(user_choice)
    if computer_choice == user_choice:
        print("It's a draw.")
    elif computer_choice == 0 and user_choice == 2 or computer_choice > user_choice:
        print("Computer win")
        computer_score += 1
    else :
        print("you win")
        user_score += 1
    print(f"Score — You: {user_score}, Computer: {computer_score}\n")
