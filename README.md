# cse210-06
Team Project
# Zilch - Dice Game
Zilch is a dice roller game based on risk-reward principles below are how you are able to play.

Player turns

-A player starts by rolling 6 6-sided dice. The player may keep any combination of dice that correlates with the point sheet.

-Once the player "locks in" at least one die, the player can re-roll the remaining dice.

-If the player cannot lock in any dice, at any time, the player busts and must end their turn.

-If a player is able to lock in all their dice, they may re-roll all their dice. (A player theoretically
can roll numerous times without busting).

Reading the Point Sheet

-With the multiple dice combinations, you must collect a combination on one roll/re-roll. For example,
a player must roll 3 ones in one roll in order to get 1000 points. The player cannot collect 3 ones over
several rolls to get 1000 points (the player only would earn 300 points because the ones are 100 points each).

-Rolling 6 ones in one roll automatically makes the player win the game, regardless of how many points they have left (or if
they have to still "buy in"). The chance of this occurring is a 1 in 46656.

-Straight is at least 4 numbers in consecutive order. For example, a player can roll a 1, 2, 3, 4 and the player has earned a 
straight.

Point System

-Players have to first "buy in" with a minimum of 450 points before they can start collecting points. If a player fails to get
at least 450 points to "buy in", they bust. If a player earns more than 450 points, they subtract 450 points from what they
earned and can now collect as many points as they want.

-All players are going to try to achieve exactly 10000 points. If a player has the abilty to earn more points
than what they can have (for example, player only needs 100 points, but they can take 200 points) they bust. This makes it so that eventually a player will have to rely solely on luck.


## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
python3 cse210-06
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- zilch               (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Zack Doxey (zack13@byui.edu)
* Jordan Waite (jman1819@byui.edu)
* Logan Simmons
* Seth Hartman (har20099@byui.edu)
* Damion Davis

Individual Assignments:
Die rolling - Logan
Scores - Zack
Put together logic gates for robo player - Seth
Handling player input - Jordan
