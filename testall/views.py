from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ['mouse_x', 'mouse_y']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


class Onepage(Page):
    form_model = models.Player
    form_fields = ['text', 'submit']

page_sequence = [
    # MyPage,
    # ResultsWaitPage,
    # Results
    Onepage
]
