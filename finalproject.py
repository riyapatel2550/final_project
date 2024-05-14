# "Tuple Out" Dice Game (Code)
# Install dependenes if needed (conda install)

import random
import os
import rolling_dice_module

def main():
    print("Welcome to the 'Tuple Out' Dice Game! There will be two rounds!")
    print("You lose if you have three of the same number.")
    print("Do not re-roll any dice that are of the same number.")
    players_number = int((input("Enter number of players: ")))
    scores = [0] * players_number
    rounds = 0
    while rounds < 2:
        for player in range(players_number):
            print(f"Player {player + 1}'s turn:")
            turns = 0
            dice = rolling_dice_module.rolling_dice() # Rolling dice function from other module (3.2 requirement)
            print("You rolled: ", dice)

            if len(set(dice)) == 1:
                print("This is a tuple! You receive 0 points.")
                break
            else:
                fixed_dice = set()
                while True:
                    choose = input("Do you want to re-roll any dice? (yes/no): ").lower()
                    if choose != 'yes':
                        break
                    else:
                        fixing_dice = input("Enter the dice you want to fix (1, 2, or 3), or input '0' to stop: ")
                        if fixing_dice == '0':
                            print("0 points scored the turn.")
                            break
                        elif fixing_dice in ['1', '2', '3']:
                            fixed_dice.add(int(fixing_dice))
                            dice[int(fixing_dice) - 1] = random.randint(1, 6)
                            print("Dice", fixing_dice, "re-rolled:", dice[int(fixing_dice) - 1])
                        else:
                            print("Invalid choice.")
                
                turns = rolling_dice_module(dice) # Score function from other module (3.2 requirement)
                print("Score for the turn:", turns)
            
            if turns == 0:
                print("0 points scored the turn.")
            else:
                scores[player] += turns
            
            print("Score for Player", player + 1, ":", scores[player])
            rounds +=1

def test_cases():
    """Test cases for the rolling_dice and score functions."""
    print("Testing roll_dice function:")
    for _ in range(5):
        print("Roll result:", rolling_dice_module.rolling_dice())

    print("\nTesting score function:")
    test_scores = [[1, 1, 1], [1, 2, 3], [4, 4, 4], [5, 5, 6], [2, 3, 3]]
    for dice in test_scores:
        print("Dice:", dice, "Score:", rolling_dice_module(dice))

def write_to_file(score):
    try:
        with open("scores.txt", "a") as file:
            file.write(str(score) + "\n")
        print("Score written to file successfully.")
    except Exception as e:
        print("Error writing score to file:", e)

if __name__ == "__main__":
    main()