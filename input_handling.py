
import dice as d
from score import Score

choice = 'done'

#Assign the total rolls and kept rolls to lists in dice file

class Choice(Score):
    
    def __len__(self):
        return len([])

    def die_selection(self):

        #Open the rules file and print it at the top of the terminal each time the user has the option to select dice
        # with open("rules.txt", "r", encoding="utf-8") as rules:
        #     for line in rules:
        #         print(line.strip())

        #Display the current rolls to the player
        print(f'Your roll looks like this {d.rolls}')
        #Allows the user to enter which dice #'s they want to keep, seperated by commas
        keep_input = input('Which dice do you want to keep? ')
        d.kept_rolls.append(keep_input)
        # return d.kept_rolls
    #     return split_input, [keep_input]

    # def appending(split_input,keep_input):
    #     #Adds the user's selection to the kept rolls list
    #     #split_input_int = [int(item) for item in split_input]
    #     for i in range(len(split_input)):
    #         split_input[i] = int(split_input[i])
        
    #     for die in range(len(split_input)):
    #         d.kept_rolls.append(die)    
    #         print(split_input[die])
    #     #remove the selected dice from the current rolls
    #     for i in range(len(split_input)):
    #         d.kept_rolls.pop(split_input[i])
            
    #     print(d.kept_rolls)
        # keep_input = input('Are you done? ')
        # if keep_input == 'done':
        #     return keep_input
        # else:
        #     pass

    # def removal(split_input):
    #     for i in range(len(split_input)):
    #             del d.rolls[i]
    #     #This is where we would want to reroll the remaining die - JW

        
    def show_updates(total_points):
        print(f'Your total score is {Score.total_points}')
        print(f'Your kept rolls are {d.kept_rolls}')

        
        

    


            




# Inputs the player should be allowed to make
# A list of all the choices they have available (like a controls menu)
# See the rules displayed on screen (this will be grabbed from the txt file)
# See the score conditions diplayed on screen
# See their current score
# See what dice they have kept so far
# Choose which die they want to keep (one at a time)
# Finish choosing dice
