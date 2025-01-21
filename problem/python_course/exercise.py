# # Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" 
# # where players use hand gestures to represent a snake, water, or a gun. 
# # The gun beats the snake, the water beats the gun, and the snake beats the water. 
# # Write a python program to create a Snake Water Gun game in Python using if-else 
# # statements. 
# # Do not create any fancy GUI. Use proper functions to check for win.

# def game(n):
#     if n == "water":
#         return "snake"
#     if n == "snake":
#         return "gun"
#     if n == "gun":
#         return "water"
#     else :
#         return "Invalid Input"
    

# n = input("enter the move :")

    
    

# print(game(n))

import random

# Function to determine the winner
def check_win(user_move, computer_move):
    if user_move == computer_move:
        return "It's a tie!"
    elif (user_move == "snake" and computer_move == "water") or \
         (user_move == "water" and computer_move == "gun") or \
         (user_move == "gun" and computer_move == "snake"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game function
def game():
    moves = ["snake", "water", "gun"]
    
    # Take user input
    user_move = input("Enter your move (snake, water, gun): ").lower()
    
    # Check for invalid input
    if user_move not in moves:
        return "Invalid input. Please choose snake, water, or gun."
    
    # Computer makes a random move
    computer_move = random.choice(moves)
    
    print(f"Computer's move: {computer_move}")
    
    # Determine and return the result
    return check_win(user_move, computer_move)

# Run the game
print(game())
