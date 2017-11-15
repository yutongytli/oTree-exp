from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import time


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def is_displayed(self):
        return self.player.is_4 == 0 and not self.player.outofthegame



class Player1(Page):
    form_model = models.Player
    form_fields = ['message']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.player.is_4 == 0 and not self.player.outofthegame

    timeout_seconds = 420
    timeout_submission = {'message': 'Message 1'}


class Player2(Page):
    form_model = models.Player
    form_fields = ['option_AB']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.is_4 == 0 and not self.player.outofthegame

    timeout_seconds = 420
    timeout_submission = {'option_AB': 'Option A'}


class treatment_4(Page):
    form_model = models.Player
    form_fields = ['D_Q39_1', 'D_Q39_2']

    def before_next_page(self):
        self.player.payoff = 1.2

    def is_displayed(self):
        return self.player.is_4 == 1 and not self.player.outofthegame



class Result_123(Page):
    def vars_for_template(self):
        money_o = 0.80 + self.player.bonus_wait
        return {'task2': self.player.payoff - 0.80,
                'money_o': money_o}



class Demographic(Page):
    form_model = models.Player
    form_fields = ['gender', 'age', 'religion', 'services']

    timeout_seconds = 300
    timeout_submission = {'gender': 'Other',
                          'age': 100,
                          'religion': 'qwertyuiop',
                          'services': 'Never'}

    def before_next_page(self):
        if self.player.outofthegame:
            self.player.bonus_wait = 0.05



class WaitforP1(WaitPage):
    def is_displayed(self):
        return self.player.is_4 == 0 and not self.player.outofthegame


class Task3(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.is_4 == 0 and not self.player.outofthegame

    timeout_seconds = 420


class CustomWaitPage(WaitPage):
    template_name = 'Empathy_Beget_Guile_Timer/CustomWaitPage.html'


class CustomPage(Page):
    timeout_seconds = 60
    def is_displayed(self):
        return not self.player.outofthegame and self.extra_is_displayed()

    def extra_is_displayed(self):
        return True


class StartWP(CustomWaitPage):
    group_by_arrival_time = True
    template_name = 'Empathy_Beget_Guile_Timer/FirstWaitPage.html'
    players_per_group = 2

    def get_mturk_group_name(self):
        return 'mturkchannel_{}_{}'.format(self.session.pk, self._index_in_pages)

    # def is_displayed(self):
    #     return self.subsession.round_number == 1

    def vars_for_template(self):
        now = time.time()
        if not self.player.startwp_timer_set:
            self.player.startwp_timer_set = True
            self.player.startwp_time = time.time()
        time_left = self.player.startwp_time + Constants.startwp_timer - now

        return {'time_left': round(time_left)}

    def get_players_for_group(self, waiting_players):
        post_dict = self.request.POST.dict()
        endofgame = post_dict.get('endofgame')
        if endofgame:
            curplayer = [p for p in waiting_players if p.pk == int(endofgame)][0]
            curplayer.outofthegame = True
            return [curplayer]
        if len(waiting_players) == Constants.players_per_group:
            return waiting_players


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




page_sequence = [
    StartWP,
    Player1,
    Task3,
    WaitforP1,
    Player2,
    treatment_4,
    Demographic,
    ResultsWaitPage,
    Result_123
]
