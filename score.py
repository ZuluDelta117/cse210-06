import dice as d
class Score:
    """
    Have the scoring possabilities 
    """
    total_points = 0
    die = ''
    # If it is the d.kept_rollss first turn it will check if the
    # d.kept_rolls has the correct number of points to start the game
    # first_turn = True

    # def entry(turn, score):
    #     if Score.first_turn == True and score <= 450:
    #         Score.first_turn == True
    #         total_score = score - 450
    #     else:
    #         # If they have the correct numebr of points to start they begin
    #         Score.first_turn == False

    # The term d.kept_rolls is deciding if they call the d.kept_rolls list or bot list
    def straight(total_points):
        for i in d.kept_rolls:
            # If the d.kept_rolls has one of each number they get a straight
            if i == '1' and i == '2' and i == '3' and i == '4' and i == '5' and i == '6':
                # If they get a straight they get 4000 points
                points = 4000
                total_points += points
        return total_points

    def three_of_a_kind(total_points):
        pairs = 0
        for i in d.kept_rolls:
            for u in d.kept_rolls:
                # Check to see if the d.kept_rolls has any pairs
                if i == u:
                    # Count the total number of pairs that the d.kept_rolls has
                    pairs += 1
                    # If they get three pairs they get 3000 points
                    if pairs == 3:
                        points = 3000
                        total_points += points
        return total_points

    def ones(total_points):
        points = 0
        for i in d.kept_rolls:
            if i == '1':
                # How many points they get for a single one
                points += 100
                # If they have three ones they get 1000 points
                if points == 300:
                    points = 1000
                # If they get four ones they get 2500 points
                elif points == 400:
                    points = 2500
                # If they get five ones they get 5500 points
                elif points == 500:
                    points = 5500
                # If they get six ones they get 7000 points
                elif points == 600:
                    # d.kept_rolls wins the game if they roll six ones
                    points = 10000
                total_points += points
        return total_points

    def fives(total_points):
        points = 0
        for i in d.kept_rolls:
            if i == '5':
                # How many points they get for a single five
                points += 50
                # If they have three fives they get 1500 points
                if points == 150:
                    points = 1500
                # If they get four fives they get 1000 points
                elif points == 200:
                    points = 2000
                # If they get five fives they get 5000 points
                elif points == 250:
                    points = 5000
                # If they get six fives they get 7000 points
                elif points == 300:
                    points = 7000
                total_points += points
        return total_points

    def all_other_rolls(total_points):
        number_roled = 0
        for i in d.kept_rolls:
            if i != 1 and i != 5:
                points = 0
                number_roled += 1
                # If they have three of a number they get it multilied by 100
                if number_roled == 3:
                    points = 500
                # If they get four of a number they get 1000 points
                elif number_roled == 4:
                    points = 2000
                # If they get five of a number they get 5000 points
                elif number_roled == 5:
                    points = 5000
                # If they get six of a number they get 7000 points
                elif number_roled == 6:
                    points = 7000
                total_points += points
        return total_points

