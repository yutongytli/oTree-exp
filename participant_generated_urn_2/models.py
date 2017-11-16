from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Yutong LI'

doc = """
Reference:
Chen, Daniel L., and Martin Schonger. "Is Ambiguity Aversion a Preference?." (2016).

Wait Page Package:
https://github.com/chapkovski/custom-waiting-page-for-mturk
"""


class Constants(BaseConstants):
    name_in_url = 'participant_generate_urn_2'
    players_per_group = 5
    num_rounds = 1
    conditions = ['Participant', 'Experimenter']
    symbols = ['uparrow', 'downarrow', 'heart', 'circle', 'downzhe', 'upzhe', 'square', 'line', 'arrow', 'circle2',
               'theta', 'question', '11']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    symbol_exp = models.IntegerField()
    treatment = models.CharField()
    symbol_pair = models.CharField()
    a = models.IntegerField()
    b = models.IntegerField()
    coin = models.CharField()

    def set_payoffs(self):
        # result of first coin
        self.coin = random.choice(['Head', 'Tail'])

        self.symbol_exp = random.randint(1, 29)
        if self.treatment == 'Experimenter':
            self.a = random.randint(0, 29)
            self.b = 29 - self.a
        else:
            pass

        for player in self.get_players():

            result_a = []
            option_temp = [player.option1, player.option2, player.option3, player.option4]
            player.option = option_temp.index(max(option_temp)) + 1

            # for those choose second coin
            if self.treatment == 'Participant':
                for p in self.get_players():
                    if p.id_in_group != player.id_in_group:
                        if p.decision == 'A':
                            result_a.extend([p.decision])
                        else:
                            pass
                    else:
                        pass
                player.a = len(result_a)
                player.b = 29 - player.a
            else:
                pass

            player.symbol_par = random.randint(1, 29)

            if self.treatment == 'Participant':
                if player.option == 4:
                    if player.symbol_par <= player.a:
                        player.result = 'A'
                        player.payoff = 1
                    else:
                        player.result = 'B'
                        player.payoff = 0
                elif player.option == 3:
                    if player.symbol_par <= player.a:
                        player.result = 'A'
                        player.payoff = 0
                    else:
                        player.result = 'B'
                        player.payoff = 1
                elif player.option == 1:
                    if self.coin == 'Head':
                        player.payoff = 0
                        if player.symbol_par <= player.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                    else:
                        player.payoff = 1
                        if player.symbol_par <= player.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                else:
                    if self.coin == 'Head':
                        player.payoff = 1
                        if player.symbol_par <= player.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                    else:
                        player.payoff = 0
                        if player.symbol_par <= player.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
            else:
                if player.option == 4:
                    if self.symbol_exp <= self.a:
                        player.result = 'A'
                        player.payoff = 1
                    else:
                        player.result = 'B'
                        player.payoff = 0
                elif player.option == 3:
                    if self.symbol_exp <= self.a:
                        player.result = 'A'
                        player.payoff = 0
                    else:
                        player.result = 'B'
                        player.payoff = 1
                elif player.option == 1:
                    if self.coin == 'Head':
                        player.payoff = 0
                        if self.symbol_exp <= self.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                    else:
                        player.payoff = 1
                        if self.symbol_exp <= self.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                else:
                    if self.coin == 'Head':
                        player.payoff = 1
                        if self.symbol_exp <= self.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                    else:
                        player.payoff = 0
                        if self.symbol_exp <= self.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'


class Player(BasePlayer):
    decision = models.CharField(
        widget=widgets.RadioSelect()
    )

    option1 = models.CurrencyField(
        choices=currency_range(0, 1, c(0.01))
    )

    option2 = models.CurrencyField(
        choices=currency_range(0, 1, c(0.01))
    )

    option3 = models.CurrencyField(
        choices=currency_range(0, 1, c(0.01))
    )

    option4 = models.CurrencyField(
        choices=currency_range(0, 1, c(0.01))
    )

    treatment = models.CharField()

    option = models.IntegerField()

    # 抽出来的结果
    result = models.CharField()

    belief = models.IntegerField(
        doc="""Please choose one of the options"""
    )

    a = models.IntegerField()
    b = models.IntegerField()
    symbol_par = models.IntegerField()

    citizenship = models.CharField()
    language = models.CharField()
    age = models.IntegerField(
        max=100, min=10
    )
    gender = models.CharField(
        choices=['Female', 'Male', 'Other'],
        widget=widgets.RadioSelectHorizontal()
    )
    educ = models.IntegerField(
        choices=[[1, 'Less than 1st grade'],
                 [2, '1st, 2nd, 3rd or 4th grade'],
                 [3, '5th or 6th grade'],
                 [4, '7th or 8th grade'],
                 [5, '9th grade'],
                 [6, '10th grade'],
                 [7, '1th grade'],
                 [8, '12th grade no diploma'],
                 [9, 'High school graduate - high school diploma or equivalent (for example: GED)'],
                 [10, 'Some college but no degree'],
                 [11, 'Associate degree in college - Occupational/vocational program'],
                 [12, 'Associate degree in college -- Academic program'],
                 [13, 'Bachelor\'s degree (For example: BA, AB, BS)'],
                 [14, 'Master\'s degree (For example: MA, MS, MEng, MEd, MSW, MBA)'],
                 [15, 'Professional School Degree (For example: MD,DDS,DVM,LLB,JD)'],
                 [16, 'Doctorate degree (For example: PhD, EdD)'],
                 [95, 'Others']]
    )
    time = models.CharField(
        choices=['Never', 'Once', '2 times', '3 times', 'More than 3 times'],
        widget=widgets.RadioSelectHorizontal()
    )
    religion = models.CharField()
    income = models.CharField(
        choices=['Less than $20000', 'Between $20000 to $40000', 'Between $40001 to $60000', 'Between $60001 to $80000',
                 'More than $80000'],
        doc="""Please choose one of the choices""",
    )
    timeout_decide = models.IntegerField(
        blank=True
    )
    timeout_intro = models.IntegerField(
        blank=True
    )
    timeout_belief = models.IntegerField(
        blank=True
    )
    timeout_demo = models.IntegerField(
        blank=True
    )
    compensate = models.IntegerField(
        blank=True
    )


