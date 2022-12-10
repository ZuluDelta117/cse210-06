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

question = input('Ready to play? Y/N ')
if question.lower() == 'y':
    print('Let\'s play')
else:
    print('Too bad')
while playing:
    keep_input = ''
    while keep_input != "done":
        # Roll dice
        d.D.roll(d.rolls, d.kept_rolls, d.choice)

        # Ask for input
        input = ih.Choice()
        keep_input, split_input = input.die_selection()
        input.appending(split_input)
        input.removal(split_input)

    # Bot turn
    d.D.bot_roll()
    c.Computer.risk_control()
    c.Computer.logic_determine()

    # Show current scores
    current_player_score = ps.player_score.total_score(player=d.kept_rolls)
    print('Your score is' + current_player_score)
    # CHANGE ME!!
    current_bot_score = ps.player_score.total_score(player=d.bot_kept_rolls)
    print('Your oponent\'s score is' + current_bot_score)

    # Check if there are winners
    if current_player_score == 10000:
        print('Congrats! You won!')
        playing = False
    elif current_bot_score == 10000:
        print('You lose! Good day, sir.')
        print(f'BOB:' + c.Computer.return_message(3))
        playing = False

print('Game Over')
print('Thank you for playing!')