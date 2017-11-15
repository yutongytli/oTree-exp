from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import os


class MyPage(Page):
    def before_next_page(self):
        self.player.get_audio_group()
        # self.player.get_audios()
        self.player.get_question()



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass

class pagetest(Page):
    form_model = models.Player
    form_fields = ['attractive_1', 'masculine_1', 'intelligent_1', 'aggressive_1', 'trustworthy_1', 'confident_1',
                   'win_1', 'quality_1']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_1)

        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                            self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                            self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3), list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}


class p1(Page):
    form_model = models.Player
    form_fields = ['attractive_1', 'masculine_1', 'intelligent_1', 'aggressive_1', 'trustworthy_1', 'confident_1',
                   'win_1', 'quality_1']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_1)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p2(Page):
    form_model = models.Player
    form_fields = ['attractive_2', 'masculine_2', 'intelligent_2', 'aggressive_2', 'trustworthy_2', 'confident_2',
                   'win_2', 'quality_2']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_2)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p3(Page):
    form_model = models.Player
    form_fields = ['attractive_3', 'masculine_3', 'intelligent_3', 'aggressive_3', 'trustworthy_3', 'confident_3', 'win_3',
                   'quality_3']


    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_3)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p4(Page):
    form_model = models.Player
    form_fields = ['attractive_4', 'masculine_4', 'intelligent_4', 'aggressive_4', 'trustworthy_4', 'confident_4', 'win_4',
                   'quality_4']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_4)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p5(Page):
    form_model = models.Player
    form_fields = ['attractive_5', 'masculine_5', 'intelligent_5', 'aggressive_5', 'trustworthy_5', 'confident_5', 'win_5',
                   'quality_5']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_5)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p6(Page):
    form_model = models.Player
    form_fields = ['attractive_6', 'masculine_6', 'intelligent_6', 'aggressive_6', 'trustworthy_6', 'confident_6', 'win_6',
                   'quality_6']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_6)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p7(Page):
    form_model = models.Player
    form_fields = ['attractive_7', 'masculine_7', 'intelligent_7', 'aggressive_7', 'trustworthy_7', 'confident_7', 'win_7',
                   'quality_7']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_7)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p8(Page):
    form_model = models.Player
    form_fields = ['attractive_8', 'masculine_8', 'intelligent_8', 'aggressive_8', 'trustworthy_8', 'confident_8', 'win_8',
                   'quality_8']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_8)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}


class p9(Page):
    form_model = models.Player
    form_fields = ['attractive_9', 'masculine_9', 'intelligent_9', 'aggressive_9', 'trustworthy_9', 'confident_9',
                   'win_9', 'quality_9']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_9)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}


class p10(Page):
    form_model = models.Player
    form_fields = ['attractive_10', 'masculine_10', 'intelligent_10', 'aggressive_10', 'trustworthy_10', 'confident_10', 'win_10',
                   'quality_10']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_10)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}


class p11(Page):
    form_model = models.Player
    form_fields = ['attractive_11', 'masculine_11', 'intelligent_11', 'aggressive_11', 'trustworthy_11', 'confident_11', 'win_11',
                   'quality_11']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_11)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p12(Page):
    form_model = models.Player
    form_fields = ['attractive_12', 'masculine_12', 'intelligent_12', 'aggressive_12', 'trustworthy_12', 'confident_12', 'win_12',
                   'quality_12']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_12)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p13(Page):
    form_model = models.Player
    form_fields = ['attractive_13', 'masculine_13', 'intelligent_13', 'aggressive_13', 'trustworthy_13', 'confident_13', 'win_13',
                   'quality_13']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_13)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p14(Page):
    form_model = models.Player
    form_fields = ['attractive_14', 'masculine_14', 'intelligent_14', 'aggressive_14', 'trustworthy_14', 'confident_14', 'win_14',
                   'quality_14']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_14)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p15(Page):
    form_model = models.Player
    form_fields = ['attractive_15', 'masculine_15', 'intelligent_15', 'aggressive_15', 'trustworthy_15', 'confident_15', 'win_15',
                   'quality_15']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_15)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p16(Page):
    form_model = models.Player
    form_fields = ['attractive_16', 'masculine_16', 'intelligent_16', 'aggressive_16', 'trustworthy_16', 'confident_16', 'win_16',
                   'quality_16']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_16)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p17(Page):
    form_model = models.Player
    form_fields = ['attractive_17', 'masculine_17', 'intelligent_17', 'aggressive_17', 'trustworthy_17', 'confident_17', 'win_17',
                   'quality_17']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_17)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p18(Page):
    form_model = models.Player
    form_fields = ['attractive_18', 'masculine_18', 'intelligent_18', 'aggressive_18', 'trustworthy_18', 'confident_18', 'win_18',
                   'quality_18']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_18)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p19(Page):
    form_model = models.Player
    form_fields = ['attractive_19', 'masculine_19', 'intelligent_19', 'aggressive_19', 'trustworthy_19', 'confident_19', 'win_19',
                   'quality_19']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_19)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p20(Page):
    form_model = models.Player
    form_fields = ['attractive_20', 'masculine_20', 'intelligent_20', 'aggressive_20', 'trustworthy_20', 'confident_20', 'win_20',
                   'quality_20']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_20)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p21(Page):
    form_model = models.Player
    form_fields = ['attractive_21', 'masculine_21', 'intelligent_21', 'aggressive_21', 'trustworthy_21', 'confident_21', 'win_21',
                   'quality_21']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_21)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p22(Page):
    form_model = models.Player
    form_fields = ['attractive_22', 'masculine_22', 'intelligent_22', 'aggressive_22', 'trustworthy_22', 'confident_22', 'win_22',
                   'quality_22']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_22)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p23(Page):
    form_model = models.Player
    form_fields = ['attractive_23', 'masculine_23', 'intelligent_23', 'aggressive_23', 'trustworthy_23', 'confident_23', 'win_23',
                   'quality_23']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_23)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p24(Page):
    form_model = models.Player
    form_fields = ['attractive_24', 'masculine_24', 'intelligent_24', 'aggressive_24', 'trustworthy_24', 'confident_24', 'win_24',
                   'quality_24']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_24)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p25(Page):
    form_model = models.Player
    form_fields = ['attractive_25', 'masculine_25', 'intelligent_25', 'aggressive_25', 'trustworthy_25', 'confident_25', 'win_25',
                   'quality_25']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_25)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p26(Page):
    form_model = models.Player
    form_fields = ['attractive_26', 'masculine_26', 'intelligent_26', 'aggressive_26', 'trustworthy_26', 'confident_26', 'win_26',
                   'quality_26']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_26)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p27(Page):
    form_model = models.Player
    form_fields = ['attractive_27', 'masculine_27', 'intelligent_27', 'aggressive_27', 'trustworthy_27', 'confident_27', 'win_27',
                   'quality_27']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_27)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p28(Page):
    form_model = models.Player
    form_fields = ['attractive_28', 'masculine_28', 'intelligent_28', 'aggressive_28', 'trustworthy_28', 'confident_28', 'win_28',
                   'quality_28']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_28)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p29(Page):
    form_model = models.Player
    form_fields = ['attractive_29', 'masculine_29', 'intelligent_29', 'aggressive_29', 'trustworthy_29', 'confident_29', 'win_29',
                   'quality_29']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_29)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p30(Page):
    form_model = models.Player
    form_fields = ['attractive_30', 'masculine_30', 'intelligent_30', 'aggressive_30', 'trustworthy_30', 'confident_30', 'win_30',
                   'quality_30']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_30)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p31(Page):
    form_model = models.Player
    form_fields = ['attractive_31', 'masculine_31', 'intelligent_31', 'aggressive_31', 'trustworthy_31', 'confident_31', 'win_31',
                   'quality_31']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_31)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p32(Page):
    form_model = models.Player
    form_fields = ['attractive_32', 'masculine_32', 'intelligent_32', 'aggressive_32', 'trustworthy_32', 'confident_32', 'win_32',
                   'quality_32']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_32)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p33(Page):
    form_model = models.Player
    form_fields = ['attractive_33', 'masculine_33', 'intelligent_33', 'aggressive_33', 'trustworthy_33', 'confident_33', 'win_33',
                   'quality_33']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_33)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p34(Page):
    form_model = models.Player
    form_fields = ['attractive_34', 'masculine_34', 'intelligent_34', 'aggressive_34', 'trustworthy_34', 'confident_34', 'win_34',
                   'quality_34']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_34)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p35(Page):
    form_model = models.Player
    form_fields = ['attractive_35', 'masculine_35', 'intelligent_35', 'aggressive_35', 'trustworthy_35', 'confident_35', 'win_35',
                   'quality_35']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_35)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p36(Page):
    form_model = models.Player
    form_fields = ['attractive_36', 'masculine_36', 'intelligent_36', 'aggressive_36', 'trustworthy_36', 'confident_36', 'win_36',
                   'quality_36']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_36)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p37(Page):
    form_model = models.Player
    form_fields = ['attractive_37', 'masculine_37', 'intelligent_37', 'aggressive_37', 'trustworthy_37', 'confident_37', 'win_37',
                   'quality_37']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_37)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p38(Page):
    form_model = models.Player
    form_fields = ['attractive_38', 'masculine_38', 'intelligent_38', 'aggressive_38', 'trustworthy_38', 'confident_38', 'win_38',
                   'quality_38']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_38)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p39(Page):
    form_model = models.Player
    form_fields = ['attractive_39', 'masculine_39', 'intelligent_39', 'aggressive_39', 'trustworthy_39', 'confident_39', 'win_39',
                   'quality_39']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_39)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p40(Page):
    form_model = models.Player
    form_fields = ['attractive_40', 'masculine_40', 'intelligent_40', 'aggressive_40', 'trustworthy_40', 'confident_40', 'win_40',
                   'quality_40']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_40)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p41(Page):
    form_model = models.Player
    form_fields = ['attractive_41', 'masculine_41', 'intelligent_41', 'aggressive_41', 'trustworthy_41', 'confident_41', 'win_41',
                   'quality_41']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_41)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p42(Page):
    form_model = models.Player
    form_fields = ['attractive_42', 'masculine_42', 'intelligent_42', 'aggressive_42', 'trustworthy_42', 'confident_42', 'win_42',
                   'quality_42']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_42)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p43(Page):
    form_model = models.Player
    form_fields = ['attractive_43', 'masculine_43', 'intelligent_43', 'aggressive_43', 'trustworthy_43', 'confident_43', 'win_43',
                   'quality_43']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_43)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p44(Page):
    form_model = models.Player
    form_fields = ['attractive_44', 'masculine_44', 'intelligent_44', 'aggressive_44', 'trustworthy_44', 'confident_44', 'win_44',
                   'quality_44']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_44)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p45(Page):
    form_model = models.Player
    form_fields = ['attractive_45', 'masculine_45', 'intelligent_45', 'aggressive_45', 'trustworthy_45', 'confident_45', 'win_45',
                   'quality_45']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_45)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p46(Page):
    form_model = models.Player
    form_fields = ['attractive_46', 'masculine_46', 'intelligent_46', 'aggressive_46', 'trustworthy_46', 'confident_46', 'win_46',
                   'quality_46']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_46)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p47(Page):
    form_model = models.Player
    form_fields = ['attractive_47', 'masculine_47', 'intelligent_47', 'aggressive_47', 'trustworthy_47', 'confident_47', 'win_47',
                   'quality_47']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_47)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p48(Page):
    form_model = models.Player
    form_fields = ['attractive_48', 'masculine_48', 'intelligent_48', 'aggressive_48', 'trustworthy_48', 'confident_48', 'win_48',
                   'quality_48']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_48)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p49(Page):
    form_model = models.Player
    form_fields = ['attractive_49', 'masculine_49', 'intelligent_49', 'aggressive_49', 'trustworthy_49', 'confident_49', 'win_49',
                   'quality_49']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_49)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p50(Page):
    form_model = models.Player
    form_fields = ['attractive_50', 'masculine_50', 'intelligent_50', 'aggressive_50', 'trustworthy_50', 'confident_50', 'win_50',
                   'quality_50']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_50)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p51(Page):
    form_model = models.Player
    form_fields = ['attractive_51', 'masculine_51', 'intelligent_51', 'aggressive_51', 'trustworthy_51', 'confident_51', 'win_51',
                   'quality_51']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_51)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p52(Page):
    form_model = models.Player
    form_fields = ['attractive_52', 'masculine_52', 'intelligent_52', 'aggressive_52', 'trustworthy_52', 'confident_52', 'win_52',
                   'quality_52']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_52)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p53(Page):
    form_model = models.Player
    form_fields = ['attractive_53', 'masculine_53', 'intelligent_53', 'aggressive_53', 'trustworthy_53', 'confident_53', 'win_53',
                   'quality_53']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_53)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p54(Page):
    form_model = models.Player
    form_fields = ['attractive_54', 'masculine_54', 'intelligent_54', 'aggressive_54', 'trustworthy_54', 'confident_54', 'win_54',
                   'quality_54']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_54)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p55(Page):
    form_model = models.Player
    form_fields = ['attractive_55', 'masculine_55', 'intelligent_55', 'aggressive_55', 'trustworthy_55', 'confident_55', 'win_55',
                   'quality_55']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_55)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p56(Page):
    form_model = models.Player
    form_fields = ['attractive_56', 'masculine_56', 'intelligent_56', 'aggressive_56', 'trustworthy_56', 'confident_56', 'win_56',
                   'quality_56']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_56)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p57(Page):
    form_model = models.Player
    form_fields = ['attractive_57', 'masculine_57', 'intelligent_57', 'aggressive_57', 'trustworthy_57', 'confident_57', 'win_57',
                   'quality_57']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_57)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p58(Page):
    form_model = models.Player
    form_fields = ['attractive_58', 'masculine_58', 'intelligent_58', 'aggressive_58', 'trustworthy_58', 'confident_58', 'win_58',
                   'quality_58']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_58)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p59(Page):
    form_model = models.Player
    form_fields = ['attractive_59', 'masculine_59', 'intelligent_59', 'aggressive_59', 'trustworthy_59', 'confident_59', 'win_59',
                   'quality_59']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_59)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p60(Page):
    form_model = models.Player
    form_fields = ['attractive_60', 'masculine_60', 'intelligent_60', 'aggressive_60', 'trustworthy_60', 'confident_60', 'win_60',
                   'quality_60']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_60)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p61(Page):
    form_model = models.Player
    form_fields = ['attractive_61', 'masculine_61', 'intelligent_61', 'aggressive_61', 'trustworthy_61', 'confident_61', 'win_61',
                   'quality_61']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_61)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}


class p62(Page):
    form_model = models.Player
    form_fields = ['attractive_62', 'masculine_62', 'intelligent_62', 'aggressive_62', 'trustworthy_62', 'confident_62', 'win_62',
                   'quality_62']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_62)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p63(Page):
    form_model = models.Player
    form_fields = ['attractive_63', 'masculine_63', 'intelligent_63', 'aggressive_63', 'trustworthy_63', 'confident_63', 'win_63',
                   'quality_63']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_63)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p64(Page):
    form_model = models.Player
    form_fields = ['attractive_64', 'masculine_64', 'intelligent_64', 'aggressive_64', 'trustworthy_64', 'confident_64', 'win_64',
                   'quality_64']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_64)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p65(Page):
    form_model = models.Player
    form_fields = ['attractive_65', 'masculine_65', 'intelligent_65', 'aggressive_65', 'trustworthy_65', 'confident_65', 'win_65',
                   'quality_65']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_65)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class p66(Page):
    form_model = models.Player
    form_fields = ['attractive_66', 'masculine_66', 'intelligent_66', 'aggressive_66', 'trustworthy_66', 'confident_66', 'win_66',
                   'quality_66']

    def vars_for_template(self):
        selected = 'covering_test/{}'.format(self.player.audio_for_player_66)
        name_list_left = [self.player.left_1, self.player.left_2, self.player.left_3, self.player.left_4,
                          self.player.left_5, self.player.left_6]
        name_list_right = [self.player.right_1, self.player.right_2, self.player.right_3, self.player.right_4,
                           self.player.right_5, self.player.right_6]
        name = [self.player.name_1, self.player.name_2, self.player.name_3, self.player.name_4, self.player.name_5,
                self.player.name_6]
        value = [list(self.player.value_1), list(self.player.value_2), list(self.player.value_3),
                 list(self.player.value_4),
                 list(self.player.value_5), list(self.player.value_6)]
        mylist = zip(name_list_left, name_list_right, name, value)

        return {'audio': selected,
                'list': mylist,
                'adj_list_left_2': self.player.name_list_left_7,
                'adj_list_right_2': self.player.name_list_right_7,
                'name_2': self.player.name_7,
                'value_2': self.player.value_7,
                'adj_list_left_3': self.player.name_list_left_8,
                'adj_list_right_3': self.player.name_list_right_8,
                'name_3': self.player.name_8,
                'value_3': self.player.value_8}

class Demographic(Page):
    form_model = models.Player
    form_fields = ['birth', 'gender', 'state', 'education', 'race', 'income']

page_sequence = [
    MyPage,
    # pagetest,
    p1,
    p2,
    p3,
    p4,
    p5,
    p6,
    p7,
    p8,
    p9,
    p10,
    p11,
    p12,
    # p13,
    # p14,
    # p15,
    # p16,
    # p17,
    # p18,
    # p19,
    # p20,
    # p21,
    # p22,
    # p23,
    # p24,
    # p25,
    # p26,
    # p27,
    # p28,
    # p29,
    # p30,
    # p31,
    # p32,
    # p33,
    # p34,
    # p35,
    # p36,
    # p37,
    # p38,
    # p39,
    # p40,
    # p41,
    # p42,
    # p43,
    # p44,
    # p45,
    # p46,
    # p47,
    # p48,
    # p49,
    # p50,
    # p51,
    # p52,
    # p53,
    # p54,
    # p55,
    # p56,
    # p57,
    # p58,
    # p59,
    # p60,
    # p61,
    # p62,
    # p63,
    # p64,
    # p65,
    # p66,
    Demographic,
    # ResultsWaitPage,
    Results
]
