from score import Score as s


class player_score:
    """
    add points for the player score
    """
    def total_score(player):
        total_points = 0
        total_points += s.straight(s.total_points)
        total_points += s.three_of_a_kind(s.total_points)
        total_points += s.ones(s.total_points)
        total_points += s.fives(s.total_points)
        total_points += s.all_other_rolls(s.total_points)
        player_score = total_points
        return player_score