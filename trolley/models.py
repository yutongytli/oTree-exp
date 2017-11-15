from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Yutong LI'

doc = """
Can you run the moral trolley problem on MTurk (oTree presumably)
Run the footbridge question.  I'm curious about something.
"""


class Constants(BaseConstants):
    name_in_url = 'trolley'
    players_per_group = None
    num_rounds = 1

    # treatments = ['control', 'trip3/16', 'trip15/16', 'walk3/16', 'walk15/16']
    treatments = ['control', 'push3/16', 'push15/16']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.CharField()
    choice = models.IntegerField(
        choices=[[1, 'Yes'],
                 [2, 'No']]
    )
    gender = models.IntegerField(
        choices=[[1, 'male'],
                 [2, 'female'],
                 [3, 'It\'s complicated']]
    )
    taken = models.CharField(
        choices=['Yes', 'No']
    )
    nationality = models.CharField()
    age = models.IntegerField(
        max=100, min=10
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
                 [17, 'Others']]
    )

