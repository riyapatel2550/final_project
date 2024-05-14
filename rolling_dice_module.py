# rolling_dice_module
import random

def rolling_dice(dice_number =3):
    """Roll three dice and return the result."""
    return [random.randint(1, 6) for _ in range(dice_number)]

def score(dice):
    """Calculate the score based on the rolled dice."""
    if len(set(dice)) == 1:  
        return 0
    else:
        return sum(dice)
    
def test_rolling_dice():
    """Test rolling_dice()"""
    print("Test rolling_dice():")
    for _ in range(5):
        dice_number = random.randint(1, 6)
        print(f"Number of dice: {dice_number}, Roll result: {rolling_dice(dice_number)}")

def test_score():
    """Test score()"""
    print("\nTest score():")
    test_scores = [[1, 1, 1], [1, 2, 3], [4, 4, 4], [5, 5, 6], [2, 3, 3]]
    for dice in test_scores:
        print("dice:", dice, "score:", score(dice))

if __name__ == "__main__":
    test_rolling_dice()
    test_score()