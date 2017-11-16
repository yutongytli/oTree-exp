from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'all_likert'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    submitted_answer_1 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_2 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_3 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_4 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_5 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_6 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_7 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_8 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_9 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_10 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )

    likert_1 = models.IntegerField()
    likert_2 = models.IntegerField()
    likert_3 = models.IntegerField()
    likert_4 = models.IntegerField()
    likert_5 = models.IntegerField()
    likert_6 = models.IntegerField()
    likert_7 = models.IntegerField()
    likert_8 = models.IntegerField()
    likert_9 = models.IntegerField()
    likert_10 = models.IntegerField()

    important_1 = models.IntegerField()
    important_2 = models.IntegerField()
    important_3 = models.IntegerField()
    important_4 = models.IntegerField()
    important_5 = models.IntegerField()
    important_6 = models.IntegerField()
    important_7 = models.IntegerField()
    important_8 = models.IntegerField()
    important_9 = models.IntegerField()
    important_10 = models.IntegerField()

    # likertquest
    care1f = models.IntegerField(
        widget=widgets.RadioSelect()
    )

    care1o = models.IntegerField(
        widget=widgets.RadioSelect()
    )

    care2f = models.IntegerField(
        widget=widgets.RadioSelect(),
    )

    care2o = models.IntegerField(
        widget=widgets.RadioSelect(),
    )

    care3f = models.IntegerField(
        widget=widgets.RadioSelect(),
    )

    care3o = models.IntegerField(
        widget=widgets.RadioSelect(),
    )
