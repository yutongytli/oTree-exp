from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def before_next_page(self):
        self.player.get_audio_group()
        self.player.get_question()

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = models.Player
    form_fields = ['attractive', 'masculine', 'intelligent', 'aggressive', 'trustworthy', 'confident',
                   'win', 'quality']

    def vars_for_template(self):
        selected = 'oral_argument/{}'.format(self.participant.vars['clip_%s' % self.round_number])
        self.player.audio_for_player = selected

        name_list_left = [self.participant.vars['left1'], self.participant.vars['left2'], self.participant.vars['left3'], self.participant.vars['left4'],
                          self.participant.vars['left5'], self.participant.vars['left6']]
        name_list_right = [self.participant.vars['right1'], self.participant.vars['right2'], self.participant.vars['right3'], self.participant.vars['right4'],
                           self.participant.vars['right5'], self.participant.vars['right6']]
        name = [self.participant.vars['name1'], self.participant.vars['name2'], self.participant.vars['name3'], self.participant.vars['name4'], self.participant.vars['name5'],
                self.participant.vars['name6']]
        value = [list(self.participant.vars['value1']), list(self.participant.vars['value2']), list(self.participant.vars['value3']), list(self.participant.vars['value4']),
                 list(self.participant.vars['value5']), list(self.participant.vars['value6'])]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.participant.vars['name_list_left_7'],
                'adj_list_right_2': self.participant.vars['name_list_right_7'],
                'name_2': self.participant.vars['name_7'],
                'value_2': self.participant.vars['value_7'],
                'adj_list_left_3': self.participant.vars['name_list_left_8'],
                'adj_list_right_3': self.participant.vars['name_list_right_8'],
                'name_3': self.participant.vars['name_8'],
                'value_3': self.participant.vars['value_8']}


class Demographic(Page):
    form_model = models.Player
    form_fields = ['birth', 'gender', 'state', 'education', 'race', 'income']

    def is_displayed(self):
        return self.round_number == 5


class Results(Page):
    def is_displayed(self):
        return self.round_number == 5

class FirstPage(Page):
    def is_displayed(self):
        return self.round_number == 1

page_sequence = [
    FirstPage,
    MyPage,
    Main,
    Demographic,
    Results
]
