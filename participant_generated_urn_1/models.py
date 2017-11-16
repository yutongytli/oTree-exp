from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Yutong LI'

doc = """
Reference:
Chen, Daniel L., and Martin Schonger. "Is Ambiguity Aversion a Preference?." (2016).
"""


class Constants(BaseConstants):
    name_in_url = 'participant_generate_urn'
    players_per_group = 8
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    num_of_exp = models.IntegerField()
    num_of_par = models.IntegerField()
    symbol = models.CharField()

    coin = models.CharField()
    a = models.IntegerField()
    b = models.IntegerField()

    def set_treatment(self):
        # l = []
        # for p in self.get_players():
        #     p.treatment = random.choice(['Experimenter', 'Participant'])
        #
        #     if p.treatment == 'Experimenter':
        #         l.append(p)
        #     else:
        #         pass
        # self.num_of_exp = len(l)
        # self.num_of_par = Constants.players_per_group - self.num_of_exp
        self.num_of_par = 4
        self.num_of_exp = 4

        participant = random.sample(self.get_players(), self.num_of_par)
        id = [p.id_in_group for p in participant]

        for p in self.get_players():
            if p.id_in_group in id:
                p.treatment = 'Participant'
            else:
                p.treatment = 'Experimenter'

    def set_payoffs(self):

        # result of first coin
        self.coin = random.choice(['head', 'tail'])

        for player in self.get_players():

            result_a = []
            option_temp = [player.option1, player.option2, player.option3, player.option4]
            player.option = option_temp.index(max(option_temp)) + 1

            # for those choose second coin
            if player.treatment == 'Participant':
                for i in self.get_players():
                    if i.id_in_group != player.id_in_group and i.treatment == 'Participant':
                        if i.decision == '↗':
                            result_a.extend([i.decision])
                        else:
                            pass
                    else:
                        pass
                self.a = len(result_a)
            else:
                self.a = random.randint(0, (self.num_of_par - 1))
                self.b = self.num_of_par - 1 - self.a

            self.symbol = random.randint(1, (self.num_of_par - 1))

            if player.option == 3 or player.option == 4:

                if self.symbol <= self.a:
                    player.result = '↗'
                    player.yourresult = bool(player.option == 4)
                else:
                    player.result = '↖'
                    player.yourresult = bool(player.option == 3)
            else:
                if self.coin == 'head':
                    player.yourresult = bool(player.option == 2)
                    if self.symbol <= self.a:
                        player.result = '↗'
                    else:
                        player.result = '↖'

                else:
                    player.yourresult = bool(player.option == 1)
                    if self.symbol <= self.a:
                        player.result = '↗'
                    else:
                        player.result = '↖'

            player.payoff = player.yourresult * 4


class Player(BasePlayer):
    decision = models.CharField(
        choices=['↗', '↖'],
        doc="""Either ↗ or ↖""",
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

    belief = models.CharField(
        choices=['0 chose ↗ and 3 chose ↖', '1 chose ↗ and 2 chose ↖',
                 '2 chose ↗ and 1 chose ↖', '3 chose ↗ and 0 chose ↖'],
        doc="""Please choose one of the options"""
    )

