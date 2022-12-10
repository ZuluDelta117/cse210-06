
import dice as d
from score import Score

choice = 'done'

#Assign the total rolls and kept rolls to lists in dice file

class Choice(Score):
    
    def __len__(self):
        return len([])

    def die_selection(self):

        #Display the current rolls to the player
        print(f'Your roll looks like this {d.rolls}')
        #Allows the user to enter which dice #'s they want to keep, seperated by commas
        keep_input = input('Which dice do you want to keep? ')
        d.kept_rolls.append(keep_input)

    def show_updates(total_points):
        print(f'Your total score is {Score.total_points}')
        print(f'Your kept rolls are {d.kept_rolls}')