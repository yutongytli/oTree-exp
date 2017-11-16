from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'petition'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    petition_1 = models.CharField(
        blank=True
    )

    petition_2 = models.CharField(
        blank=True
    )

    petition_3 = models.CharField(
        blank=True
    )

    petition_4 = models.CharField(
        blank=True
    )

    petition_5 = models.CharField(
        blank=True
    )

    petition_6 = models.CharField(
        blank=True
    )

    petition_7 = models.CharField(
        blank=True
    )

    petition_8 = models.CharField(
        blank=True
    )

    petition_9 = models.CharField(
        blank=True
    )

    petition_10 = models.CharField(
        blank=True
    )

    email_petition = models.CharField(
        blank=True
    )

    click = models.CharField(
        blank=True
    )
