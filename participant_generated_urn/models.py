from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'majority_determine'
    players_per_group = 4
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    num_of_exp = models.IntegerField()
    num_of_par = models.IntegerField()
    symbol = models.CharField()

    coin = models.CharField()
    black = models.IntegerField()
    white = models.IntegerField()

    def set_treatment(self):
        for p in self.get_players():
            p.treatment = random.choice(['Experimenter', 'Participant'])

        self.num_of_exp = sum(p for p in self.get_players() if p.treatment == 'Experimenter')
        self.num_of_par = Constants.players_per_group - self.num_of_exp

    def set_payoffs(self):

        # result of first coin
        self.coin = random.choice(['head', 'tail'])

        for player in self.get_players():

            result_black = []
            option_temp = [player.option1, player.option2, player.option3, player.option4]
            player.option = option_temp.index(max(option_temp)) + 1

            # for those choose second coin
            if player.option == 3 or player.option == 4:
                if player.treatment == 'Participant':
                    for i in self.get_players():
                        if i.id_in_group != player.id_in_group and i.treatment == 'Participant':
                            if i.decision == 'Black':
                                result_black.extend([i.decision])
                            else:
                                pass
                        else:
                            pass
                    self.black = len(result_black)
                else:
                    self.black = random.randint(0, (self.num_of_par - 1))
                    self.white = self.num_of_par - 1 - self.black

                self.symbol = random.randint(1, (self.num_of_par - 1))

                if self.symbol <= self.black:
                    player.result = 'Black'
                    player.yourresult = bool(player.option == 3)
                else:
                    player.result = 'White'
                    player.yourresult = bool(player.option == 4)
            else:
                if self.coin == 'head':
                    player.yourresult = bool(player.option == 2)
                else:
                    player.yourresult = bool(player.option == 1)

            player.payoff = player.yourresult * 4


class Player(BasePlayer):
    decision = models.CharField(
        choices=['Black', 'White'],
        doc="""Either 'Black' or 'White'""",
        widget=widgets.RadioSelect()
    )
    option1 = models.CurrencyField(
        choices=currency_range(0, 4, c(0.01))
    )
    option2 = models.CurrencyField(
        choices=currency_range(0, 4, c(0.01))
    )
    option3 = models.CurrencyField(
        choices=currency_range(0, 4, c(0.01))
    )
    option4 = models.CurrencyField(
        choices=currency_range(0, 4, c(0.01))
    )

    option = models.IntegerField()

    treatment = models.CharField()

    result = models.CharField()
