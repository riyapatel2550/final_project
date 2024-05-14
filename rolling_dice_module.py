# rolling_dice_module
import random

def rolling_dice():
    """Roll three dice and return the result."""
    return [random.randint(1, 6) for _ in range(3)]

def score(dice):
    """Calculate the score based on the rolled dice."""
    if len(set(dice)) == 1:  
        return 0
    else:
        return sum(dice)