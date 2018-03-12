from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Wait(WaitPage):
    group_by_arrival_time = True
    players_per_group = 2

    def after_all_players_arrive(self):
        # if self.group.treatment == 'None':
            # Retrieve the condition assignments from each participant so far
            conditions_so_far = []
            for g in self.subsession.get_groups():
                conditions_so_far.append(g.treatment)

            # Count how often each condition has been run
            conditions_n = {}
            for c in Constants.conditions:
                conditions_n[c] = conditions_so_far.count(c)

            # Create a new array containing the conditions that have been run the least amount of times
            conditions = []
            for c, n in conditions_n.items():
                if n == min(conditions_n.values()):
                    conditions.append(c)

            # Randomly assign the participant to one of these conditions
            temp = random.choice(conditions)
            self.group.treatment = temp
            if temp == 'Treatment D':
                for p in self.group.get_players():
                    p.is_4 = 1
            else:
                for p in self.group.get_players():
                    p.is_4 = 0
        # else:
        #     pass



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def is_displayed(self):
        return self.player.is_4 == 0


class Player1(Page):
    form_model = models.Player
    form_fields = ['message']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.player.is_4 == 0

    timeout_seconds = 420
    timeout_submission = {'message': 'Message 1'}


class Player2(Page):
    form_model = models.Player
    form_fields = ['option_AB']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.is_4 == 0

    timeout_seconds = 420
    timeout_submission = {'option_AB': 'Option A'}


class treatment_4(Page):
    form_model = models.Player
    form_fields = ['D_Q39_1', 'D_Q39_2']

    def before_next_page(self):
        self.player.payoff = 1.20

    def is_displayed(self):
        return self.player.is_4 == 1



class Result_123(Page):

    def vars_for_template(self):
        return {'task2': self.player.payoff - 0.80}


class Demographic(Page):
    form_model = models.Player
    form_fields = ['gender', 'age', 'religion', 'services']

    timeout_seconds = 300
    timeout_submission = {'gender': 'Other',
                          'age': 100,
                          'religion': 'qwertyuiop',
                          'services': 'Never'}



class WaitforP1(WaitPage):
    def is_displayed(self):
        return self.player.is_4 == 0


class Task3(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.is_4 == 0

    timeout_seconds = 420


page_sequence = [
    Wait,
    Player1,
    Task3,
    WaitforP1,
    Player2,
    treatment_4,
    Demographic,
    ResultsWaitPage,
    Result_123
]
