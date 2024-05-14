# "Tuple Out" Dice Game Consolidation Project
Riya Patel

The Rules of Word Guessing Game and how it works:

1. Each player rolls three dice
2. If all three dice show the same number, the player tuples out and gets a score of 0 for that round.
3. Players can then fix certain dice that have the same member to not have to re-roll them.
4. Players then decide when they want to stop rolling to add the points or when they tuple out.
5. When a player decides to stop, they sum up points equal and calculate their score.
6. If a player tuples out they score 0 points for that turn.


How the Program Works (technological aspect):

1. Run the Python program 'consolidation_project_2.py'
2. Prompted with an Introduction and some rules along with asking to input how many palyers there are.
3. Players will then take turns rolling dice and inputting which dice they want to fix and when to stop.
4. The game stops and quits once the two rounds are over.


Important Key Notes:

1. import os and import random are used in the beginning in order for it to be an interactive operating system and for the word from the word bank to be random.
2. The format method in the print statements are useful to easily implement certain values from variables into outputs and messages.
3. The indexes and for loops are used to re-roll certain dice.


Future Goals:

1. Creating a target score to determine when the game ends.
2. To be able to record a high school and tally up how many games the players have won.
3. Create AI to compete against a player.

Add-ons:

1. There is a separate module for rolling_dice() and scores() which is then implemented in the main file using "import" (3.2 requirement).
2. There are also arguments and test cases in this separate module which covers the "Five-step" process (2.2 requirement).
3. Included a Graph for the scores of each player using matplotlib. (Advanced Topics).