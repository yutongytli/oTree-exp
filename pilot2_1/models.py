from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Yutong LI'

doc = """
Reference:
Who Cares? Measuring Policy Preferences in a Polarized Environment
"""


class Constants(BaseConstants):
    name_in_url = 'pilot2_1'
    players_per_group = None
    num_rounds = 1

    first_two = [[1, 'increasing income taxes on people making over one million dollars per year'],
                 [2, 'building a wall on the US Border with Mexico']]

    questions = [[3, 'the government trying to reduce the difference in income between the richest and the poorest households'],
                 [4, 'laws to protect gays and lesbians against job discrimination'],
                 [5, 'allowing Syrian refugees to come to the United States'],
                 [6, 'making it more difficult for people to buy a gun']]


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.treatment = random.choice(['polarized', 'depolarized', 'control'])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.CharField()

    question_1 = models.IntegerField()
    answer_1 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    importance_1 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    question_2 = models.IntegerField()
    answer_2 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    importance_2 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    question_3 = models.IntegerField()
    answer_3 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    importance_3 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    question_4 = models.IntegerField()
    answer_4 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    importance_4 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    question_5 = models.IntegerField()
    answer_5 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    importance_5 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    question_6 = models.IntegerField()
    answer_6 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    importance_6 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    internet_1 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    internet_2 = models.IntegerField(
        widget=widgets.RadioSelect
    )
    freq = models.IntegerField()
    partisan_1 = models.IntegerField()
    partisan_2 = models.IntegerField()

    def set_payoff(self):

        payoff_matrix = {
            True:
                {
                    True: Constants.both_cooperate_payoff,
                    False: Constants.betrayed_payoff
                },
            False:
                {
                    True: Constants.betray_payoff,
                    False: Constants.both_defect_payoff
                }
        }