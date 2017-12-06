from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mysurvey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.PositiveIntegerField(
        choices=[
            [0, 'Female'],
            [1, 'Male'],
        ]
    )  # Will ask yes or no (Boolean) {horizontaly}
    age = models.IntegerField(min=1900,max=2000) #Is an integer free value
    is_student = models.BooleanField()
    level = models.PositiveIntegerField(
        choices=[
            [0, 'Bac'],
            [1, 'classe préparatoire'],
            [2, 'L 1'],
            [3, 'L 2'],
            [4, 'L 3'],
            [5, 'M 1'],
            [6, 'M 2'],
            [7, 'PhD'],
        ]
    )
    income = models.PositiveIntegerField(
        choices=[
            [1, '<1,200€'],
            [2, '1,201€ to 1,800€'],
            [3, '1,800€ to 2,500€'],
            [4, '2,501€ to 3,500€'],
            [5, '>3,500€'],

        ]
    )