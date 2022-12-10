from player_score import player_score as ps
import dice as d

class Computer:
    def __init__(self):
        self._base_risk = .5
        self._messages = ['Drat! I busted', 'Yay! I scored over 1000 points', 'Haha, you busted']
        #self._total_points = int(0)
        #self._round_points = int(0)

    def return_risk(self):
        return self._base_risk

    def return_message(self, num):
        return self._messages[num-1]

   # def return_total_points(self):
    #    return self._total_points

    #def modify_total_points(self, value):
     #   self._total_points =+ value

    def modify_risk(self, change):
        self._base_risk = self._base_risk * change
        if self._base_risk > 1:
            self._base_risk = 1

    def risk_control(self):
        # The Computer will raise/lower its risk based upon whether it is further ahead or further behind.
        _player_points = ps.total_score(player=d.kept_rolls)
        if self._total_points - _player_points >= 2000:
            self.modify_risk(1.2)
        elif self._total_points - _player_points >= 1000:
            self.modify_risk(1.1)
        elif _player_points - self._total_points >= 1000:
            self.modify_risk(.9)
        elif _player_points - self._total_points >= 2000:
            self.modify_risk(.8)

    def logic_determine(self):
        risk = self.return_risk()

        # The Computer gets riskier as its risk level is higher and vice versa
        if risk <= .4:
            if self._round_points >= 1000:
                return "stop"
            elif self._round_points < 1000:
                return "roll"
        elif risk > .4 and risk <= .6:
            if self._round_points >= 1250:
                return "stop"
            elif self._round_points < 1250:
                return "roll"
        elif risk > .6 and risk <= .8:
            if self._round_points >= 1750:
                return "stop"
            elif self._round_points < 1750:
                return "roll"
        else:
            if self._round_points >= 2500:
                return "stop"
            elif self._round_points < 2500:
                return "roll"