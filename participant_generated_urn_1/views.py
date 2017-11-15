from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decide(Page):
    form_model = models.Player
    form_fields = ['decision']

class Decide2(Page):

    form_model = models.Player
    form_fields = ['option1', 'option2', 'option3', 'option4']

    def is_displayed(self):
        return self.player.treatment == 'Participant'

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):

    def is_displayed(self):
        return self.player.treatment == 'Participant'

class FirstWait(WaitPage):
    group_by_arrival_time = True
    players_per_group = 8

    def after_all_players_arrive(self):
        self.group.set_treatment()

class Introduction(Page):
    form_model = models.Player
    form_fields = ['decision']

    def vars_for_template(self):
        return {'total': self.group.num_of_par - 1}

    def is_displayed(self):
        return self.player.treatment == 'Participant'

class Decide_exp(Page):

    form_model = models.Player
    form_fields = ['option1', 'option2', 'option3', 'option4']

    def is_displayed(self):
        return self.player.treatment == 'Experimenter'

class Results_2(Page):

    def is_displayed(self):
        return self.player.treatment == 'Experimenter'

class Introduction_2(Page):

    def is_displayed(self):
        return self.player.treatment == 'Experimenter'

    def vars_for_template(self):
        return {'total': self.group.num_of_par - 1}

class belief(Page):
    form_model = models.Player
    form_fields = ['belief']

    def vars_for_template(self):
        return {'sum': self.group.num_of_par - 1}

    def is_displayed(self):
        return self.player.treatment == 'Participant'

page_sequence = [
    FirstWait,
    Introduction,
    Introduction_2,
    Decide2,
    Decide_exp,
    belief,
    ResultsWaitPage,
    Results,
    Results_2
]
