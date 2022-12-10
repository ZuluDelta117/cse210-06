import random as r
from input_handling import choice

die_value = 0
die_numbers = [1,2,3,4,5,6]

# Player values
rolls = []
kept_rolls = []

# Bot values
bot_rolls = []
bot_kept_rolls = []
calc_it = (6 - len(kept_rolls))

class D:
    def roll(rolls,kept_rolls,choice):
        rolls.clear()
        if len(kept_rolls) == 6:
            print('You have no more dice to roll.')
            choice = 'done'
        else:
            while len(rolls) < (6 - len(kept_rolls)):
                rolls.append(r.randint(1,6))

    
    def bot_roll(bot_rolls,bot_kept_rolls):
        if len(bot_kept_rolls) == 6:
            print('no more dice for bot')
        else:
            while len(bot_rolls) < (6 - bot_kept_rolls.count()):
                bot_rolls.append(r.randint(1,6))
