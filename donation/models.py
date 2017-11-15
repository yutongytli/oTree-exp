from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'donation'
    players_per_group = None
    num_rounds = 1

    amount_allocated = c(10)

    organization = ['organization 1', 'organization 2', 'The American Chamber of Commerce', 'organization 4',
                    'organization 5', 'Center for Immigration Studies', 'organization 7', 'organization 8',
                    'organization 9', 'organization 10']

    description = ['description 1', 'description 2',
                   'The ACC is a non-partisan association that lobbies Congress to maintain low tariffs on imports because an increase would raise consumer prices and hurt American exports',
                   'description 4',
                   'description 5',
                   'The CIS is a conservative non-profit research organization "that favors far lower immigration numbers and produces research to further those views.” It also lobbies congress for policies in that direction',
                   'description 7',
                   'description 8',
                   'description 9',
                   'description 10']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donation = models.CurrencyField(
        blank=True,
        min=0, max=Constants.amount_allocated,
        doc='Please choose from $0 to $10'
    )

    org = models.IntegerField(
        blank=True,
        doc='Please enter the number of organization you want',
        min=0, max=3
    )

    org_option1 = models.CharField()
    org_option2 = models.CharField()
    org_option3 = models.CharField()

    email = models.CharField(
        blank=True,
        doc='For example: XXXX@gmail.com'
    )

    annotation = models.CharField()
