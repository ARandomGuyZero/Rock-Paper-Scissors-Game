"""
Rock, Paper, Scissors Game

This script is a simple implementation of the classic Rock, Paper, Scissors game. 
The player chooses between Rock, Paper, or Scissors, and the computer randomly selects one as well. 
The game then compares the choices and determines the winner.
"""

from random import randint

# ASCII art for the game options
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Get the player's choice
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))

# Get the computer's choice (randomly selected)
computer_choice = randint(0, 2)

# List to map choices to their corresponding ASCII art
options = [rock, paper, scissors]

# Ensure the player's choice is valid
if 0 <= player_choice <= 2:
    # Display the player's choice
    print(f"Your choice:\n{options[player_choice]}")

    # Display the computer's choice
    print(f"Computer choice:\n{options[computer_choice]}")

    # Determine the outcome of the game
    if player_choice == computer_choice:
        print("Whoops! That's a draw!")
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
else:
    # Handle invalid input
    print("Sorry, that's not an option. You lose!")