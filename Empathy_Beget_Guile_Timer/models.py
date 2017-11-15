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
    name_in_url = 'Empathy_Timer'
    players_per_group = 2
    num_rounds = 1
    conditions = ['Treatment A', 'Treatment B', 'Treatment C', 'Treatment D']

    startwp_timer = 10


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for g in self.get_groups():
            g.treatment = 'None'


class Group(BaseGroup):

    def set_payoffs(self):

        p1 = self.get_player_by_role('Player 1')
        p2 = self.get_player_by_role('Player 2')

        if self.treatment == 'Treatment A':
            if p2.option_AB == 'Option A':
                p1.payoff = 1
                p2.payoff = 1.04
            else:
                p1.payoff = 1.04
                p2.payoff = 1
        elif self.treatment == 'Treatment B':
            if p2.option_AB == 'Option A':
                p1.payoff = 1
                p2.payoff = 1.4
            else:
                p1.payoff = 1.04
                p2.payoff = 1
        elif self.treatment == 'Treatment C':
            if p2.option_AB == 'Option A':
                p1.payoff = 1
                p2.payoff = 1.4
            else:
                p1.payoff = 1.4
                p2.payoff = 1
        else:
            p1.payoff = 1.2
            p2.payoff = 1.2

    treatment = models.CharField()

class Player(BasePlayer):

    # Decision for Treatment 1-3
    message = models.CharField(
        choices=['Message 1', 'Message 2'],
        doc="""Either 'Message 1' or 'Message 2'""",
        widget=widgets.RadioSelect()
    )
    option_AB = models.CharField(
        choices=['Option A', 'Option B'],
        doc="""Either 'Option A' or 'Option B'""",
        widget=widgets.RadioSelect()
    )

    # Decision for Treatment 4
    D_Q39_1 = models.CharField(
        choices=['Completely Fair', 'Fair', 'Unfair', 'Very Unfair'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    D_Q39_2 = models.CharField(
        choices=['Completely Fair', 'Fair', 'Unfair', 'Very Unfair'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    def role(self):
        if self.id_in_group == 1:
            return 'Player 1'
        if self.id_in_group == 2:
            return 'Player 2'

    def other_player(self):
        """Returns other player in group"""
        return self.get_others_in_group()[0]

    gender = models.CharField(
        choices=['Male', 'Female', 'Other'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    age = models.PositiveIntegerField()

    religion = models.CharField(
        # doc="""Please fill in the blank with, e.x.: Christian, Hindu.""",
        # widget=widgets.RadioSelect()
    )

    services = models.CharField(
        choices=['Never', 'Once a year', 'Once a month', 'Once a week', 'More than once a week'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    # Is treatment 4
    is_4 = models.IntegerField()

    startwp_timer_set = models.BooleanField(default=False)
    startwp_time = models.PositiveIntegerField()
    outofthegame = models.BooleanField()

    bonus_wait = models.CurrencyField(
        blank=True,
        default=0
    )

