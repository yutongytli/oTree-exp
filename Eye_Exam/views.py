from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Introduction(Page):
    pass


class Welcome(Page):
    def before_next_page(self):
        # Retrieve the condition assignments from each participant so far
        conditions_so_far = []
        for p in self.subsession.get_players():
            conditions_so_far.append(p.priming)

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
        self.player.priming = temp


class Wait(WaitPage):
    group_by_arrival_time = True
    players_per_group = 2

    def after_all_players_arrive(self):
        self.subsession.get_priming()


class ResultWait(WaitPage):
    def after_all_players_arrive(self):
        self.group.get_scores()


class Priming(Page):
    form_model = models.Player
    form_fields = ['text']


class Eye1(Page):
    form_model = models.Player
    form_fields = ['feeling1_response']


class Eye2(Page):
    form_model = models.Player
    form_fields = ['feeling2_response']


class Eye3(Page):
    form_model = models.Player
    form_fields = ['feeling3_response']



class Eye4(Page):
    form_model = models.Player
    form_fields = ['feeling4_response']



class Eye5(Page):
    form_model = models.Player
    form_fields = ['feeling5_response']



class Eye6(Page):
    form_model = models.Player
    form_fields = ['feeling6_response']



class Eye7(Page):
    form_model = models.Player
    form_fields = ['feeling7_response']



class Eye8(Page):
    form_model = models.Player
    form_fields = ['feeling8_response']



class Eye9(Page):
    form_model = models.Player
    form_fields = ['feeling9_response']


class Eye10(Page):
    form_model = models.Player
    form_fields = ['feeling10_response']



class Eye11(Page):
    form_model = models.Player
    form_fields = ['feeling11_response']



class Eye12(Page):
    form_model = models.Player
    form_fields = ['feeling12_response']



class Eye13(Page):
    form_model = models.Player
    form_fields = ['feeling13_response']



class Eye14(Page):
    form_model = models.Player
    form_fields = ['feeling14_response']



class Eye15(Page):
    form_model = models.Player
    form_fields = ['feeling15_response']



class Eye16(Page):
    form_model = models.Player
    form_fields = ['feeling16_response']



class Eye17(Page):
    form_model = models.Player
    form_fields = ['feeling17_response']



class Eye18(Page):
    form_model = models.Player
    form_fields = ['feeling18_response']



class Eye19(Page):
    form_model = models.Player
    form_fields = ['feeling19_response']



class Eye20(Page):
    form_model = models.Player
    form_fields = ['feeling20_response']



class Eye21(Page):
    form_model = models.Player
    form_fields = ['feeling21_response']



class Eye22(Page):
    form_model = models.Player
    form_fields = ['feeling22_response']



class Eye23(Page):
    form_model = models.Player
    form_fields = ['feeling23_response']



class Eye24(Page):
    form_model = models.Player
    form_fields = ['feeling24_response']



class Eye25(Page):
    form_model = models.Player
    form_fields = ['feeling25_response']



class Eye26(Page):
    form_model = models.Player
    form_fields = ['feeling26_response']



class Eye27(Page):
    form_model = models.Player
    form_fields = ['feeling27_response']



class Eye28(Page):
    form_model = models.Player
    form_fields = ['feeling28_response']



class Eye29(Page):
    form_model = models.Player
    form_fields = ['feeling29_response']



class Eye30(Page):
    form_model = models.Player
    form_fields = ['feeling30_response']



class Eye31(Page):
    form_model = models.Player
    form_fields = ['feeling31_response']



class Eye32(Page):
    form_model = models.Player
    form_fields = ['feeling32_response']



class Eye33(Page):
    form_model = models.Player
    form_fields = ['feeling33_response']


class Eye34(Page):
    form_model = models.Player
    form_fields = ['feeling34_response']


class Eye35(Page):
    form_model = models.Player
    form_fields = ['feeling35_response']


class Eye36(Page):
    form_model = models.Player
    form_fields = ['feeling36_response']

    def before_next_page(self):
        self.player.get_scores()




page_sequence = [
    # Wait,
    Welcome,
    Priming,
    Introduction,
    Eye1,
    # Eye2,
    # Eye3,
    # Eye4,
    # Eye5,
    # Eye6,
    # Eye7,
    # Eye8,
    # Eye9,
    # Eye10,
    # Eye11,
    # Eye12,
    # Eye13,
    # Eye14,
    # Eye15,
    # Eye16,
    # Eye17,
    # Eye18,
    # Eye19,
    # Eye20,
    # Eye21,
    # Eye22,
    # Eye23,
    # Eye24,
    # Eye25,
    # Eye26,
    # Eye27,
    # Eye28,
    # Eye29,
    # Eye30,
    # Eye31,
    # Eye32,
    # Eye33,
    # Eye34,
    # Eye35,
    # Eye36,
    # ResultWait
]
