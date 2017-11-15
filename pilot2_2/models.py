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
    name_in_url = 'pilot2_2'
    players_per_group = None
    num_rounds = 1

    questions = [[1, 'requiring employers to offer paid leave to the parents of new children'],
                 [2, 'building a wall on the US Border with Mexico'],
                 [3, 'increasing income taxes on people making over one million dollars per year'],
                 [4, 'making it more difficult for people to buy a gun'],
                 [5, 'the US sending ground troops to fight Islamic militants, such as ISIS, in Iraq and Syria'],
                 [6, 'allowing Syrian refugees to come to the United States'],
                 [7, 'laws to protect gays and lesbians against job discrimination'],
                 [8, 'requiring employers to pay women and men the same amount for the same work']]

    last_three = [[9, 'laws to protect gays and lesbians against job discrimination'],
                  [10, 'making it more difficult for people to buy a gun'],
                  [11, 'the government trying to reduce the difference in income between the richest and the poorest households']]


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.treatment = random.choice(['prime', 'deprime'])


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treatment = models.CharField()

    partisan_1 = models.IntegerField()
    partisan_2 = models.IntegerField()

    internet_1 = models.IntegerField()
    internet_2 = models.IntegerField()
    internet_3 = models.IntegerField()
    internet_4 = models.IntegerField()

    pic1 = models.TextField()
    pic2_like = models.TextField()
    pic2_dislike = models.TextField()

    question_1 = models.IntegerField()
    answer_1 = models.IntegerField()
    question_2 = models.IntegerField()
    answer_2 = models.IntegerField()
    question_3 = models.IntegerField()
    answer_3 = models.IntegerField()
    question_4 = models.IntegerField()
    answer_4 = models.IntegerField()
    question_5 = models.IntegerField()
    answer_5 = models.IntegerField()
    question_6 = models.IntegerField()
    answer_6 = models.IntegerField()
    question_7 = models.IntegerField()
    answer_7 = models.IntegerField()
    question_8 = models.IntegerField()
    answer_8 = models.IntegerField()
    question_9 = models.IntegerField()
    answer_9 = models.IntegerField()
    importance_9 = models.IntegerField()
    question_10 = models.IntegerField()
    answer_10 = models.IntegerField()
    importance_10 = models.IntegerField()
    question_11 = models.IntegerField()
    answer_11 = models.IntegerField()
    importance_11 = models.IntegerField()

    employ = models.IntegerField(
        max=100, min=0
    )
    trump = models.IntegerField(
        max=100, min=0
    )

    partisan_3 = models.IntegerField()
    partisan_4 = models.IntegerField()
    partisan_5 = models.IntegerField()
    partisan_6 = models.IntegerField()




