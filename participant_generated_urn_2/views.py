from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import time
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage

# class Decide(Page):
#     form_model = models.Player
#     form_fields = ['decision']
#
#     def vars_for_template(self):
#         if self.group.symbol_pair == 'uparrow':
#             htmla = '↗'
#             htmlb = '↖'
#         elif self.group.symbol_pair == 'downarrow':
#             htmla = '↙'
#             htmlb = '↘︎'
#         elif self.group.symbol_pair == 'heart':
#             htmla = '♡'
#             htmlb = '☺︎'
#         elif self.group.symbol_pair == 'circle':
#             htmla = '◯'
#             htmlb = '•'
#         elif self.group.symbol_pair == 'downzhe':
#             htmla = '┓'
#             htmlb = '┏︎'
#         elif self.group.symbol_pair == 'upzhe':
#             htmla = '┗'
#             htmlb = '┛'
#         elif self.group.symbol_pair == 'square':
#             htmla = '■'
#             htmlb = '□'
#         elif self.group.symbol_pair == 'line':
#             htmla = '—'
#             htmlb = '|'
#         elif self.group.symbol_pair == 'arrow':
#             htmla = '↔'
#             htmlb = '↕'
#         elif self.group.symbol_pair == 'circle2':
#             htmla = '◌'
#             htmlb = '●'
#         elif self.group.symbol_pair == 'theta':
#             htmla = 'φ'
#             htmlb = 'θ'
#         elif self.group.symbol_pair == 'question':
#             htmla = 'ʔ'
#             htmlb = 'ʕ'
#         else:
#             htmla = '⑪'
#             htmlb = '⓫'
#         return {'htmla': htmla,
#                 'htmlb': htmlb}
#
#     def decision_choices(self):
#         if self.group.symbol_pair == 'uparrow':
#             htmla = '↗'
#             htmlb = '↖'
#         elif self.group.symbol_pair == 'downarrow':
#             htmla = '↙'
#             htmlb = '↘︎'
#         elif self.group.symbol_pair == 'heart':
#             htmla = '♡'
#             htmlb = '☺︎'
#         elif self.group.symbol_pair == 'circle':
#             htmla = '◯'
#             htmlb = '•'
#         elif self.group.symbol_pair == 'downzhe':
#             htmla = '┓'
#             htmlb = '┏︎'
#         elif self.group.symbol_pair == 'upzhe':
#             htmla = '┗'
#             htmlb = '┛'
#         elif self.group.symbol_pair == 'square':
#             htmla = '■'
#             htmlb = '□'
#         elif self.group.symbol_pair == 'line':
#             htmla = '—'
#             htmlb = '|'
#         elif self.group.symbol_pair == 'arrow':
#             htmla = '↔'
#             htmlb = '↕'
#         elif self.group.symbol_pair == 'circle2':
#             htmla = '◌'
#             htmlb = '●'
#         elif self.group.symbol_pair == 'theta':
#             htmla = 'φ'
#             htmlb = 'θ'
#         elif self.group.symbol_pair == 'question':
#             htmla = 'ʔ'
#             htmlb = 'ʕ'
#         else:
#             htmla = '⑪'
#             htmlb = '⓫'
#         return [['A', htmla],
#                 ['B', htmlb]]
#
#     timeout_seconds = 210
#     timeout_submission = ['A']


class Decide2(Page):

    form_model = models.Player
    form_fields = ['option1', 'option2', 'option3', 'option4']

    def is_displayed(self):
        return self.player.treatment == 'Participant'

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return {'htmla': htmla,
                'htmlb': htmlb}

    timeout_seconds = 360
    timeout_submission = {'option1': 0.01,
                          'option2': 0.01,
                          'option3': 0.01,
                          'option4': 0.01}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_decide = 1


class ResultsWaitPage(WaitPage):
    # template_name = 'participant_generated_urn_2/CustomWaitPage.html'

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        for p in self.group.get_players():
            p.participant.vars['fourthtime'] = time.time()


class Results(Page):

    def vars_for_template(self):
        id_num = []
        other_result = []
        for p in self.player.get_others_in_group():
            id_num.append(p.id_in_group)
            if self.group.symbol_pair == 'uparrow':
                if p.decision == 'A':
                    decision = '↗'
                else:
                    decision = '↖'
            elif self.group.symbol_pair == 'downarrow':
                if p.decision == 'A':
                    decision = '↙'
                else:
                    decision = '↘︎'
            elif self.group.symbol_pair == 'heart':
                if p.decision == 'A':
                    decision = '♡'
                else:
                    decision = '☺︎'
            elif self.group.symbol_pair == 'circle':
                if p.decision == 'A':
                    decision = '◯'
                else:
                    decision = '•'
            elif self.group.symbol_pair == 'downzhe':
                if p.decision == 'A':
                    decision = '┓'
                else:
                    decision = '┏︎'
            elif self.group.symbol_pair == 'upzhe':
                if p.decision == 'A':
                    decision = '┗'
                else:
                    decision = '┛'
            elif self.group.symbol_pair == 'square':
                if p.decision == 'A':
                    decision = '■'
                else:
                    decision = '□'
            elif self.group.symbol_pair == 'arrow':
                if p.decision == 'A':
                    decision = '↔'
                else:
                    decision = '↕'
            elif self.group.symbol_pair == 'line':
                if p.decision == 'A':
                    decision = '—'
                else:
                    decision = '|︎'
            elif self.group.symbol_pair == 'circle2':
                if p.decision == 'A':
                    decision = '◌'
                else:
                    decision = '●'
            elif self.group.symbol_pair == 'theta':
                if p.decision == 'A':
                    decision = 'φ'
                else:
                    decision = 'θ︎'
            elif self.group.symbol_pair == 'question':
                if p.decision == 'A':
                    decision = 'ʔ'
                else:
                    decision = 'ʕ'
            else:
                if p.decision == 'A':
                    decision = '⑪'
                else:
                    decision = '⓫'

            other_result.append(decision)

        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
            if self.player.result == 'A':
                result = '↗'
            else:
                result = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
            if self.player.result == 'A':
                result = '↙'
            else:
                result = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
            if self.player.result == 'A':
                result = '♡'
            else:
                result = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
            if self.player.result == 'A':
                result = '◯'
            else:
                result = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏'
            if self.player.result == 'A':
                result = '┓'
            else:
                result = '┏'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛︎'
            if self.player.result == 'A':
                result = '┗'
            else:
                result = '┛︎'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
            if self.player.result == 'A':
                result = '■'
            else:
                result = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
            if self.player.result == 'A':
                result = '—'
            else:
                result = '|︎'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
            if self.player.result == 'A':
                result = '↔'
            else:
                result = '↕︎'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
            if self.player.result == 'A':
                result = '◌'
            else:
                result = '●'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ︎'
            if self.player.result == 'A':
                result = 'ʔ'
            else:
                result = 'ʕ︎'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
            if self.player.result == 'A':
                result = 'φ'
            else:
                result = 'θ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
            if self.player.result == 'A':
                result = '⑪'
            else:
                result = '⓫'

        mylist = zip(id_num, other_result)

        comp = (self.participant.vars['secondtime'] - self.participant.vars['firsttime']) / 60 + \
               (self.participant.vars['fourthtime'] - self.participant.vars['thirdtime']) / 60

        self.player.compensate = round(comp)

        return {'list': mylist,
                'result': result,
                'htmla': htmla,
                'htmlb': htmlb,
                'comp': self.player.compensate}

    def is_displayed(self):
        return self.player.treatment == 'Participant'


class FirstWait(CustomMturkWaitPage):
    group_by_arrival_time = True
    # template_name = 'participant_generated_urn_2/CustomWaitPage.html'

    def after_all_players_arrive(self):
        # Retrieve the condition assignments from each participant so far
        conditions_so_far = []
        symbols_so_far = []
        for g in self.subsession.get_groups():
            conditions_so_far.append(g.treatment)
            symbols_so_far.append(g.symbol_pair)

        # Count how often each condition has been run
        conditions_n = {}
        symbols_n = {}
        for c in Constants.conditions:
            conditions_n[c] = conditions_so_far.count(c)
        for s in Constants.symbols:
            symbols_n[s] = symbols_so_far.count(s)

        # Create a new array containing the conditions that have been run the least amount of times
        conditions = []
        symbols = []
        for c, n in conditions_n.items():
            if n == min(conditions_n.values()):
                conditions.append(c)
        for s, n in symbols_n.items():
            if n == min(symbols_n.values()):
                symbols.append(s)

        # Randomly assign the participant to one of these conditions
        self.group.treatment = random.choice(conditions)
        self.group.symbol_pair = random.choice(symbols)

        for p in self.group.get_players():
            p.treatment = self.group.treatment
            p.participant.vars['secondtime'] = time.time()


class Introduction(Page):
    form_model = models.Player
    form_fields = ['decision']

    def decision_choices(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        elif self.group.symbol_pair == '11':
            htmla = '⑪'
            htmlb = '⓫'
        else:
            htmla = 'bots'
            htmlb = 'bots'
        return [['A', htmla],
                ['B', htmlb]]

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return {'total': 30,
                'htmla': htmla,
                'htmlb': htmlb}

    def is_displayed(self):
        return self.player.treatment == 'Participant'

    timeout_seconds = 200
    timeout_submission = {'decision': 'A'}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_decide_0 = 1


class Decide_exp(Page):

    form_model = models.Player
    form_fields = ['option1', 'option2', 'option3', 'option4']

    def is_displayed(self):
        return self.player.treatment == 'Experimenter'

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return {'htmla': htmla,
                'htmlb': htmlb}

    timeout_seconds = 360
    timeout_submission = {'option1': 0.01,
                          'option2': 0.01,
                          'option3': 0.01,
                          'option4': 0.01}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_decide = 1


class Results_2(Page):

    def is_displayed(self):
        return self.player.treatment == 'Experimenter'

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'

        if self.group.symbol_pair == 'uparrow':
            if self.player.result == 'A':
                result = '↗'
            else:
                result = '↖'
        elif self.group.symbol_pair == 'downarrow':
            if self.player.result == 'A':
                result = '↙'
            else:
                result = '↘︎'
        elif self.group.symbol_pair == 'heart':
            if self.player.result == 'A':
                result = '♡'
            else:
                result = '☺︎'
        elif self.group.symbol_pair == 'circle':
            if self.player.result == 'A':
                result = '◯'
            else:
                result = '•'
        elif self.group.symbol_pair == 'downzhe':
            if self.player.result == 'A':
                result = '┓'
            else:
                result = '┏'
        elif self.group.symbol_pair == 'upzhe':
            if self.player.result == 'A':
                result = '┗'
            else:
                result = '┛'
        elif self.group.symbol_pair == 'square':
            if self.player.result == 'A':
                result = '■'
            else:
                result = '□'
        elif self.group.symbol_pair == 'line':
            if self.player.result == 'A':
                result = '—'
            else:
                result = '|︎'
        elif self.group.symbol_pair == 'arrow':
            if self.player.result == 'A':
                result = '↔'
            else:
                result = '↕'
        elif self.group.symbol_pair == 'circle2':
            if self.player.result == 'A':
                result = '◌'
            else:
                result = '●'
        elif self.group.symbol_pair == 'theta':
            if self.player.result == 'A':
                result = 'φ'
            else:
                result = 'θ'
        elif self.group.symbol_pair == 'question':
            if self.player.result == 'A':
                result = 'ʔ'
            else:
                result = 'ʕ︎'
        else:
            if self.player.result == 'A':
                result = '⑪'
            else:
                result = '⓫'

        comp = (self.participant.vars['secondtime'] - self.participant.vars['firsttime'])/60 + \
               (self.participant.vars['fourthtime'] - self.participant.vars['thirdtime'])/60

        self.player.compensate = round(comp)

        return {'htmla': htmla,
                'htmlb': htmlb,
                'result': result,
                'comp': self.player.compensate}


class Introduction_2(Page):

    def is_displayed(self):
        return self.player.treatment == 'Experimenter'

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return {'total': 30,
                'htmla': htmla,
                'htmlb': htmlb}

    timeout_seconds = 200

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_intro = 1


class Belieff(Page):
    form_model = models.Player
    form_fields = ['belief']

    def vars_for_template(self):
        return {'sum': 30}

    def belief_choices(self):
        if self.group.symbol_pair == 'uparrow':
            one = '0 chose ↗ and 30 chose ↖'
            two = '1 chose ↗ and 29 chose ↖'
            three = '2 chose ↗ and 28 chose ↖'
            four = '3 chose ↗ and 27 chose ↖'
            five = '4 chose ↗ and 26 chose ↖'
            six = '5 chose ↗ and 25 chose ↖'
            seven = '6 chose ↗ and 24 chose ↖'
            eight = '7 chose ↗ and 23 chose ↖'
            nine = '8 chose ↗ and 22 chose ↖'
            ten = '9 chose ↗ and 21 chose ↖'
            eleven = '10 chose ↗ and 20 chose ↖'
            twelve = '11 chose ↗ and 19 chose ↖'
            thirteen = '12 chose ↗ and 18 chose ↖'
            fourteen = '13 chose ↗ and 17 chose ↖'
            fifteen = '14 chose ↗ and 16 chose ↖'
            sixteen = '15 chose ↗ and 15 chose ↖'
            seventeen = '16 chose ↗ and 14 chose ↖'
            eighteen = '17 chose ↗ and 13 chose ↖'
            nineteen = '18 chose ↗ and 12 chose ↖'
            twenty = '19 chose ↗ and 11 chose ↖'
            twentyone = '20 chose ↗ and 10 chose ↖'
            twentytwo = '21 chose ↗ and 9 chose ↖'
            twentythree = '22 chose ↗ and 8 chose ↖'
            twentyfour = '23 chose ↗ and 7 chose ↖'
            twentyfive = '24 chose ↗ and 6 chose ↖'
            twentysix = '25 chose ↗ and 5 chose ↖'
            twentryseven = '26 chose ↗ and 4 chose ↖'
            twentyeight = '27 chose ↗ and 3 chose ↖'
            twentrynine = '28 chose ↗ and 2 chose ↖'
            thirty = '29 chose ↗ and 1 chose ↖'
            thirtyone = '30 chose ↗ and 0 chose ↖'
        elif self.group.symbol_pair == 'downarrow':
            one = '0 chose ↙ and 30 chose ↘'
            two = '1 chose ↙ and 29 chose ↘'
            three = '2 chose ↙ and 28 chose ↘'
            four = '3 chose ↙ and 27 chose ↘'
            five = '4 chose ↙ and 26 chose ↘'
            six = '5 chose ↙ and 25 chose ↘'
            seven = '6 chose ↙ and 24 chose ↘'
            eight = '7 chose ↙ and 23 chose ↘'
            nine = '8 chose ↙ and 22 chose ↘'
            ten = '9 chose ↙ and 21 chose ↘'
            eleven = '10 chose ↙ and 20 chose ↘'
            twelve = '11 chose ↙ and 19 chose ↘'
            thirteen = '12 chose ↙ and 18 chose ↘'
            fourteen = '13 chose ↙ and 17 chose ↘'
            fifteen = '14 chose ↙ and 16 chose ↘'
            sixteen = '15 chose ↙ and 15 chose ↘'
            seventeen = '16 chose ↙ and 14 chose ↘'
            eighteen = '17 chose ↙ and 13 chose ↘'
            nineteen = '18 chose ↙ and 12 chose ↘'
            twenty = '19 chose ↙ and 11 chose ↘'
            twentyone = '20 chose ↙ and 10 chose ↘'
            twentytwo = '21 chose ↙ and 9 chose ↘'
            twentythree = '22 chose ↙ and 8 chose ↘'
            twentyfour = '23 chose ↙ and 7 chose ↘'
            twentyfive = '24 chose ↙ and 6 chose ↘'
            twentysix = '25 chose ↙ and 5 chose ↘'
            twentryseven = '26 chose ↙ and 4 chose ↘'
            twentyeight = '27 chose ↙ and 3 chose ↘'
            twentrynine = '28 chose ↙ and 2 chose ↘'
            thirty = '29 chose ↙ and 1 chose ↘'
            thirtyone = '30 chose ↙ and 0 chose ↘'
        elif self.group.symbol_pair == 'heart':
            one = '0 chose ♡ and 30 chose ☺︎'
            two = '1 chose ♡ and 29 chose ☺︎'
            three = '2 chose ♡ and 28 chose ☺︎'
            four = '3 chose ♡ and 27 chose ☺︎'
            five = '4 chose ♡ and 26 chose ☺'
            six = '5 chose ♡ and 25 chose ☺'
            seven = '6 chose ♡ and 24 chose ☺'
            eight = '7 chose ♡ and 23 chose ☺'
            nine = '8 chose ♡ and 22 chose ☺'
            ten = '9 chose ♡ and 21 chose ☺'
            eleven = '10 chose ♡ and 20 chose ☺'
            twelve = '11 chose ♡ and 19 chose ☺'
            thirteen = '12 chose ♡ and 18 chose ☺'
            fourteen = '13 chose ♡ and 17 chose ☺'
            fifteen = '14 chose ♡ and 16 chose ☺'
            sixteen = '15 chose ♡ and 15 chose ☺'
            seventeen = '16 chose ♡ and 14 chose ☺'
            eighteen = '17 chose ♡ and 13 chose ☺'
            nineteen = '18 chose ♡ and 12 chose ☺'
            twenty = '19 chose ♡ and 11 chose ☺'
            twentyone = '20 chose ♡ and 10 chose ☺'
            twentytwo = '21 chose ♡ and 9 chose ☺'
            twentythree = '22 chose ♡ and 8 chose ☺'
            twentyfour = '23 chose ♡ and 7 chose ☺'
            twentyfive = '24 chose ♡ and 6 chose ☺'
            twentysix = '25 chose ♡ and 5 chose ☺'
            twentryseven = '26 chose ♡ and 4 chose ☺'
            twentyeight = '27 chose ♡ and 3 chose ☺'
            twentrynine = '28 chose ♡ and 2 chose ☺'
            thirty = '29 chose ♡ and 1 chose ☺'
            thirtyone = '30 chose ♡ and 0 chose ☺'
        elif self.group.symbol_pair == 'circle':
            one = '0 chose ◯ and 30 chose •'
            two = '1 chose ◯ and 29 chose •'
            three = '2 chose ◯ and 28 chose •'
            four = '3 chose ◯ and 27 chose •'
            five = '4 chose ◯ and 26 chose •'
            six = '5 chose ◯ and 25 chose •'
            seven = '6 chose ◯ and 24 chose •'
            eight = '7 chose ◯ and 23 chose •'
            nine = '8 chose ◯ and 22 chose •'
            ten = '9 chose ◯ and 21 chose •'
            eleven = '10 chose ◯ and 20 chose •'
            twelve = '11 chose ◯ and 19 chose •'
            thirteen = '12 chose ◯ and 18 chose •'
            fourteen = '13 chose ◯ and 17 chose •'
            fifteen = '14 chose ◯ and 16 chose •'
            sixteen = '15 chose ◯ and 15 chose •'
            seventeen = '16 chose ◯ and 14 chose •'
            eighteen = '17 chose ◯ and 13 chose •'
            nineteen = '18 chose ◯ and 12 chose •'
            twenty = '19 chose ◯ and 11 chose •'
            twentyone = '20 chose ◯ and 10 chose •'
            twentytwo = '21 chose ◯ and 9 chose •'
            twentythree = '22 chose ◯ and 8 chose •'
            twentyfour = '23 chose ◯ and 7 chose •'
            twentyfive = '24 chose ◯ and 6 chose •'
            twentysix = '25 chose ◯ and 5 chose •'
            twentryseven = '26 chose ◯ and 4 chose •'
            twentyeight = '27 chose ◯ and 3 chose •'
            twentrynine = '28 chose ◯ and 2 chose •'
            thirty = '29 chose ◯ and 1 chose •'
            thirtyone = '30 chose ◯ and 0 chose •'
        elif self.group.symbol_pair == 'downzhe':
            one = '0 chose ┓ and 30 chose ┏'
            two = '1 chose ┓ and 29 chose ┏'
            three = '2 chose ┓ and 28 chose ┏'
            four = '3 chose ┓ and 27 chose ┏'
            five = '4 chose ┓ and 26 chose ┏'
            six = '5 chose ┓ and 25 chose ┏'
            seven = '6 chose ┓ and 24 chose ┏'
            eight = '7 chose ┓ and 23 chose ┏'
            nine = '8 chose ┓ and 22 chose ┏'
            ten = '9 chose ┓ and 21 chose ┏'
            eleven = '10 chose ┓ and 20 chose ┏'
            twelve = '11 chose ┓ and 19 chose ┏'
            thirteen = '12 chose ┓ and 18 chose ┏'
            fourteen = '13 chose ┓ and 17 chose ┏'
            fifteen = '14 chose ┓ and 16 chose ┏'
            sixteen = '15 chose ┓ and 15 chose ┏'
            seventeen = '16 chose ┓ and 14 chose ┏'
            eighteen = '17 chose ┓ and 13 chose ┏'
            nineteen = '18 chose ┓ and 12 chose ┏'
            twenty = '19 chose ┓ and 11 chose ┏'
            twentyone = '20 chose ┓ and 10 chose ┏'
            twentytwo = '21 chose ┓ and 9 chose ┏'
            twentythree = '22 chose ┓ and 8 chose ┏'
            twentyfour = '23 chose ┓ and 7 chose ┏'
            twentyfive = '24 chose ┓ and 6 chose ┏'
            twentysix = '25 chose ┓ and 5 chose ┏'
            twentryseven = '26 chose ┓ and 4 chose ┏'
            twentyeight = '27 chose ┓ and 3 chose ┏'
            twentrynine = '28 chose ┓ and 2 chose ┏'
            thirty = '29 chose ┓ and 1 chose ┏'
            thirtyone = '30 chose ┓ and 0 chose ┏'
        elif self.group.symbol_pair == 'upzhe':
            one = '0 chose ┗ and 30 chose ┛︎'
            two = '1 chose ┗ and 29 chose ┛︎'
            three = '2 chose ┗ and 28 chose ┛︎'
            four = '3 chose ┗ and 27 chose ┛'
            five = '4 chose ┗ and 26 chose ┛'
            six = '5 chose ┗ and 25 chose ┛'
            seven = '6 chose ┗ and 24 chose ┛'
            eight = '7 chose ┗ and 23 chose ┛'
            nine = '8 chose ┗ and 22 chose ┛'
            ten = '9 chose ┗ and 21 chose ┛'
            eleven = '10 chose ┗ and 20 chose ┛'
            twelve = '11 chose ┗ and 19 chose ┛'
            thirteen = '12 chose ┗ and 18 chose ┛'
            fourteen = '13 chose ┗ and 17 chose ┛'
            fifteen = '14 chose ┗ and 16 chose ┛'
            sixteen = '15 chose ┗ and 15 chose ┛'
            seventeen = '16 chose ┗ and 14 chose ┛'
            eighteen = '17 chose ┗ and 13 chose ┛'
            nineteen = '18 chose ┗ and 12 chose ┛'
            twenty = '19 chose ┗ and 11 chose ┛'
            twentyone = '20 chose ┗ and 10 chose ┛'
            twentytwo = '21 chose ┗ and 9 chose ┛'
            twentythree = '22 chose ┗ and 8 chose ┛'
            twentyfour = '23 chose ┗ and 7 chose ┛'
            twentyfive = '24 chose ┗ and 6 chose ┛'
            twentysix = '25 chose ┗ and 5 chose ┛'
            twentryseven = '26 chose ┗ and 4 chose ┛'
            twentyeight = '27 chose ┗ and 3 chose ┛'
            twentrynine = '28 chose ┗ and 2 chose ┛'
            thirty = '29 chose ┗ and 1 chose ┛'
            thirtyone = '30 chose ┗ and 0 chose ┛'
        elif self.group.symbol_pair == 'square':
            one = '0 chose ■ and 30 chose □'
            two = '1 chose ■ and 29 chose □'
            three = '2 chose ■ and 28 chose □'
            four = '3 chose ■ and 27 chose □'
            five = '4 chose ■ and 26 chose □'
            six = '5 chose ■ and 25 chose □'
            seven = '6 chose ■ and 24 chose □'
            eight = '7 chose ■ and 23 chose □'
            nine = '8 chose ■ and 22 chose □'
            ten = '9 chose ■ and 21 chose □'
            eleven = '10 chose ■ and 20 chose □'
            twelve = '11 chose ■ and 19 chose □'
            thirteen = '12 chose ■ and 18 chose □'
            fourteen = '13 chose ■ and 17 chose □'
            fifteen = '14 chose ■ and 16 chose □'
            sixteen = '15 chose ■ and 15 chose □'
            seventeen = '16 chose ■ and 14 chose □'
            eighteen = '17 chose ■ and 13 chose □'
            nineteen = '18 chose ■ and 12 chose □'
            twenty = '19 chose ■ and 11 chose □'
            twentyone = '20 chose ■ and 10 chose □'
            twentytwo = '21 chose ■ and 9 chose □'
            twentythree = '22 chose ■ and 8 chose □'
            twentyfour = '23 chose ■ and 7 chose □'
            twentyfive = '24 chose ■ and 6 chose □'
            twentysix = '25 chose ■ and 5 chose □'
            twentryseven = '26 chose ■ and 4 chose □'
            twentyeight = '27 chose ■ and 3 chose □'
            twentrynine = '28 chose ■ and 2 chose □'
            thirty = '29 chose ■ and 1 chose □'
            thirtyone = '30 chose ■ and 0 chose □'
        elif self.group.symbol_pair == 'line':
            one = '0 chose — and 30 chose |'
            two = '1 chose — and 29 chose |'
            three = '2 chose — and 28 chose |'
            four = '3 chose — and 27 chose |'
            five = '4 chose — and 26 chose |'
            six = '5 chose — and 25 chose |'
            seven = '6 chose — and 24 chose |'
            eight = '7 chose — and 23 chose |'
            nine = '8 chose — and 22 chose |'
            ten = '9 chose — and 21 chose |'
            eleven = '10 chose — and 20 chose |'
            twelve = '11 chose — and 19 chose |'
            thirteen = '12 chose — and 18 chose |'
            fourteen = '13 chose — and 17 chose |'
            fifteen = '14 chose — and 16 chose |'
            sixteen = '15 chose — and 15 chose |'
            seventeen = '16 chose — and 14 chose |'
            eighteen = '17 chose — and 13 chose |'
            nineteen = '18 chose — and 12 chose |'
            twenty = '19 chose — and 11 chose |'
            twentyone = '20 chose — and 10 chose |'
            twentytwo = '21 chose — and 9 chose |'
            twentythree = '22 chose — and 8 chose |'
            twentyfour = '23 chose — and 7 chose |'
            twentyfive = '24 chose — and 6 chose |'
            twentysix = '25 chose — and 5 chose |'
            twentryseven = '26 chose — and 4 chose |'
            twentyeight = '27 chose — and 3 chose |'
            twentrynine = '28 chose — and 2 chose |'
            thirty = '29 chose — and 1 chose |'
            thirtyone = '30 chose — and 0 chose |'
        elif self.group.symbol_pair == 'arrow':
            one = '0 chose ↔ and 30 chose ↕'
            two = '1 chose ↔ and 29 chose ↕'
            three = '2 chose ↔ and 28 chose ↕'
            four = '3 chose ↔ and 27 chose ↕︎'
            five = '4 chose ↔ and 26 chose ↕'
            six = '5 chose ↔ and 25 chose ↕'
            seven = '6 chose ↔ and 24 chose ↕'
            eight = '7 chose ↔ and 23 chose ↕'
            nine = '8 chose ↔ and 22 chose ↕'
            ten = '9 chose ↔ and 21 chose ↕'
            eleven = '10 chose ↔ and 20 chose ↕'
            twelve = '11 chose ↔ and 19 chose ↕'
            thirteen = '12 chose ↔ and 18 chose ↕'
            fourteen = '13 chose ↔ and 17 chose ↕'
            fifteen = '14 chose ↔ and 16 chose ↕'
            sixteen = '15 chose ↔ and 15 chose ↕'
            seventeen = '16 chose ↔ and 14 chose ↕'
            eighteen = '17 chose ↔ and 13 chose ↕'
            nineteen = '18 chose ↔ and 12 chose ↕'
            twenty = '19 chose ↔ and 11 chose ↕'
            twentyone = '20 chose ↔ and 10 chose ↕'
            twentytwo = '21 chose ↔ and 9 chose ↕'
            twentythree = '22 chose ↔ and 8 chose ↕'
            twentyfour = '23 chose ↔ and 7 chose ↕'
            twentyfive = '24 chose ↔ and 6 chose ↕'
            twentysix = '25 chose ↔ and 5 chose ↕'
            twentryseven = '26 chose ↔ and 4 chose ↕'
            twentyeight = '27 chose ↔ and 3 chose ↕'
            twentrynine = '28 chose ↔ and 2 chose ↕'
            thirty = '29 chose ↔ and 1 chose ↕'
            thirtyone = '30 chose ↔ and 0 chose ↕'
        elif self.group.symbol_pair == 'circle2':
            one = '0 chose ◌ and 30 chose ●'
            two = '1 chose ◌ and 29 chose ●'
            three = '2 chose ◌ and 28 chose ●'
            four = '3 chose ◌ and 27 chose ●'
            five = '4 chose ◌ and 26 chose ●'
            six = '5 chose ◌ and 25 chose ●'
            seven = '6 chose ◌ and 24 chose ●'
            eight = '7 chose ◌ and 23 chose ●'
            nine = '8 chose ◌ and 22 chose ●'
            ten = '9 chose ◌ and 21 chose ●'
            eleven = '10 chose ◌ and 20 chose ●'
            twelve = '11 chose ◌ and 19 chose ●'
            thirteen = '12 chose ◌ and 18 chose ●'
            fourteen = '13 chose ◌ and 17 chose ●'
            fifteen = '14 chose ◌ and 16 chose ●'
            sixteen = '15 chose ◌ and 15 chose ●'
            seventeen = '16 chose ◌ and 14 chose ●'
            eighteen = '17 chose ◌ and 13 chose ●'
            nineteen = '18 chose ◌ and 12 chose ●'
            twenty = '19 chose ◌ and 11 chose ●'
            twentyone = '20 chose ◌ and 10 chose ●'
            twentytwo = '21 chose ◌ and 9 chose ●'
            twentythree = '22 chose ◌ and 8 chose ●'
            twentyfour = '23 chose ◌ and 7 chose ●'
            twentyfive = '24 chose ◌ and 6 chose ●'
            twentysix = '25 chose ◌ and 5 chose ●'
            twentryseven = '26 chose ◌ and 4 chose ●'
            twentyeight = '27 chose ◌ and 3 chose ●'
            twentrynine = '28 chose ◌ and 2 chose ●'
            thirty = '29 chose ◌ and 1 chose ●'
            thirtyone = '30 chose ◌ and 0 chose ●'
        elif self.group.symbol_pair == 'theta':
            one = '0 chose φ and 30 chose θ'
            two = '1 chose φ and 29 chose θ'
            three = '2 chose φ and 28 chose θ'
            four = '3 chose φ and 27 chose θ'
            five = '4 chose φ and 26 chose θ'
            six = '5 chose φ and 25 chose θ'
            seven = '6 chose φ and 24 chose θ'
            eight = '7 chose φ and 23 chose θ'
            nine = '8 chose φ and 22 chose θ'
            ten = '9 chose φ and 21 chose θ'
            eleven = '10 chose φ and 20 chose θ'
            twelve = '11 chose φ and 19 chose θ'
            thirteen = '12 chose φ and 18 chose θ'
            fourteen = '13 chose φ and 17 chose θ'
            fifteen = '14 chose φ and 16 chose θ'
            sixteen = '15 chose φ and 15 chose θ'
            seventeen = '16 chose φ and 14 chose θ'
            eighteen = '17 chose φ and 13 chose θ'
            nineteen = '18 chose φ and 12 chose θ'
            twenty = '19 chose φ and 11 chose θ'
            twentyone = '20 chose φ and 10 chose θ'
            twentytwo = '21 chose φ and 9 chose θ'
            twentythree = '22 chose φ and 8 chose θ'
            twentyfour = '23 chose φ and 7 chose θ'
            twentyfive = '24 chose φ and 6 chose θ'
            twentysix = '25 chose φ and 5 chose θ'
            twentryseven = '26 chose φ and 4 chose θ'
            twentyeight = '27 chose φ and 3 chose θ'
            twentrynine = '28 chose φ and 2 chose θ'
            thirty = '29 chose φ and 1 chose θ'
            thirtyone = '30 chose φ and 0 chose θ'
        elif self.group.symbol_pair == 'question':
            one = '0 chose ʔ and 30 chose ʕ︎'
            two = '1 chose ʔ and 29 chose ʕ︎'
            three = '2 chose ʔ and 28 chose ʕ'
            four = '3 chose ʔ and 27 chose ʕ'
            five = '4 chose ʔ and 26 chose ʕ'
            six = '5 chose ʔ and 25 chose ʕ'
            seven = '6 chose ʔ and 24 chose ʕ'
            eight = '7 chose ʔ and 23 chose ʕ'
            nine = '8 chose ʔ and 22 chose ʕ'
            ten = '9 chose ʔ and 21 chose ʕ'
            eleven = '10 chose ʔ and 20 chose ʕ'
            twelve = '11 chose ʔ and 19 chose ʕ'
            thirteen = '12 chose ʔ and 18 chose ʕ'
            fourteen = '13 chose ʔ and 17 chose ʕ'
            fifteen = '14 chose ʔ and 16 chose ʕ'
            sixteen = '15 chose ʔ and 15 chose ʕ'
            seventeen = '16 chose ʔ and 14 chose ʕ'
            eighteen = '17 chose ʔ and 13 chose ʕ'
            nineteen = '18 chose ʔ and 12 chose ʕ'
            twenty = '19 chose ʔ and 11 chose ʕ'
            twentyone = '20 chose ʔ and 10 chose ʕ'
            twentytwo = '21 chose ʔ and 9 chose ʕ'
            twentythree = '22 chose ʔ and 8 chose ʕ'
            twentyfour = '23 chose ʔ and 7 chose ʕ'
            twentyfive = '24 chose ʔ and 6 chose ʕ'
            twentysix = '25 chose ʔ and 5 chose ʕ'
            twentryseven = '26 chose ʔ and 4 chose ʕ'
            twentyeight = '27 chose ʔ and 3 chose ʕ'
            twentrynine = '28 chose ʔ and 2 chose ʕ'
            thirty = '29 chose ʔ and 1 chose ʕ'
            thirtyone = '30 chose ʔ and 0 chose ʕ'
        else:
            one = '0 chose ⑪ and 30 chose ⓫'
            two = '1 chose ⑪ and 29 chose ⓫'
            three = '2 chose ⑪ and 28 chose ⓫'
            four = '3 chose ⑪ and 27 chose ⓫'
            five = '4 chose ⑪ and 26 chose ⓫'
            six = '5 chose ⑪ and 25 chose ⓫'
            seven = '6 chose ⑪ and 24 chose ⓫'
            eight = '7 chose ⑪ and 23 chose ⓫'
            nine = '8 chose ⑪ and 22 chose ⓫'
            ten = '9 chose ⑪ and 21 chose ⓫'
            eleven = '10 chose ⑪ and 20 chose ⓫'
            twelve = '11 chose ⑪ and 19 chose ⓫'
            thirteen = '12 chose ⑪ and 18 chose ⓫'
            fourteen = '13 chose ⑪ and 17 chose ⓫'
            fifteen = '14 chose ⑪ and 16 chose ⓫'
            sixteen = '15 chose ⑪ and 15 chose ⓫'
            seventeen = '16 chose ⑪ and 14 chose ⓫'
            eighteen = '17 chose ⑪ and 13 chose ⓫'
            nineteen = '18 chose ⑪ and 12 chose ⓫'
            twenty = '19 chose ⑪ and 11 chose ⓫'
            twentyone = '20 chose ⑪ and 10 chose ⓫'
            twentytwo = '21 chose ⑪ and 9 chose ⓫'
            twentythree = '22 chose ⑪ and 8 chose ⓫'
            twentyfour = '23 chose ⑪ and 7 chose ⓫'
            twentyfive = '24 chose ⑪ and 6 chose ⓫'
            twentysix = '25 chose ⑪ and 5 chose ⓫'
            twentryseven = '26 chose ⑪ and 4 chose ⓫'
            twentyeight = '27 chose ⑪ and 3 chose ⓫'
            twentrynine = '28 chose ⑪ and 2 chose ⓫'
            thirty = '29 chose ⑪ and 1 chose ⓫'
            thirtyone = '30 chose ⑪ and 0 chose ⓫'

        return [[1, one],
                [2, two],
                [3, three],
                [4, four],
                [5, five],
                [6, six],
                [7, seven],
                [8, eight],
                [9, nine],
                [10, ten],
                [11, eleven],
                [12, twelve],
                [13, thirteen],
                [14, fourteen],
                [15, fifteen],
                [16, sixteen],
                [17, seventeen],
                [18, eighteen],
                [19, nineteen],
                [20, twenty],
                [21, twentyone],
                [22, twentytwo],
                [23, twentythree],
                [24, twentyfour],
                [25, twentyfive],
                [26, twentysix],
                [27, twentryseven],
                [28, twentyeight],
                [29, twentrynine],
                [30, thirty],
                [31, thirtyone]]

    def is_displayed(self):
        return self.player.treatment == 'Participant'

    timeout_seconds = 180
    timeout_submission = {'belief': 31}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_belief = 1


class Demographic(Page):
    form_model = models.Player
    form_fields = ['citizenship', 'language', 'age', 'gender', 'educ', 'time', 'religion', 'income']

    timeout_seconds = 200
    timeout_submission = {'citizenship': 'bots',
                          'language': 'bots',
                          'age': 11,
                          'gender': 'Other',
                          'educ': 1,
                          'time': 'Never',
                          'religion': 'bots',
                          'income': 'Less than $20000'}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_demo = 1
        self.participant.vars['thirdtime'] = time.time()



page_sequence = [
    FirstWait,
    Introduction,
    Introduction_2,
    Decide2,
    Decide_exp,
    Belieff,
    Demographic,
    ResultsWaitPage,
    Results,
    Results_2
]
