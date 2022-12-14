import dice as d
import input_handling as ih
import player_score as ps
import computer as c
import score as s

playing = True
# Run introduction
print('Welcome to Zilch: The Dice Game.')
# Show rules
print('Here are the rules:')
with open('rules.txt') as f:
    lines = f.read()
    print(lines)

print('Let\'s play!')
while playing:
    finished = ''
    d.kept_rolls.clear()
    while finished.lower() != "y":
        # Roll dice
        d.D.roll(d.rolls, d.kept_rolls, d.choice)
        # Ask for input
        inputs = ih.Choice()
        inputs.die_selection()
        finished = input('Are you done? Y/N ')



    # Show current scores
    current_player_score = ps.player_score.total_score(player=d.kept_rolls)

    print(f'Your score is {current_player_score}')


    # Check if there are winners
    print(f'Congrats! You got {current_player_score} points')
    playing = False


print('Game Over')
print('Thank you for playing!')