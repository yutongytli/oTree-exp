from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Introduction(Page):
    def before_next_page(self):
        treatments_so_far = []
        for p in self.subsession.get_players():
            treatments_so_far.append(p.treatment)

        treatments_n = {}
        for c in Constants.treatments:
            treatments_n[c] = treatments_so_far.count(c)

        treatments = []
        for c, n in treatments_n.items():
            if n == min(treatments_n.values()):
                treatments.append(c)

        temp = random.choice(treatments)
        self.player.treatment = temp


class MyPage(Page):
    form_model = models.Player
    form_fields = ['choice']

    def vars_for_template(self):
        if self.player.treatment == 'walk3/16' or self.player.treatment == 'push3/16':
            N1 = '3/16'
            N2 = '13/16'
        elif self.player.treatment == 'walk15/16' or self.player.treatment == 'push15/16':
            N1 = '15/16'
            N2 = '1/16'
        else:
            N1 = '0'
            N2 = '0'
        return {'N1': N1,
                'N2': N2}


class Demo(Page):
    form_model = models.Player
    form_fields = ['gender', 'educ', 'age', 'taken', 'nationality']


class Results(Page):
    pass


page_sequence = [
    Introduction,
    MyPage,
    Demo,
    Results
]
