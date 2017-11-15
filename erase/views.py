from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ['option']

    # def is_displayed(self):
    #     return self.participant.vars['group'] == '1LM' or self.participant.vars['group'] == '1QM' or \
    #            self.participant.vars['group'] == '1QNM' or self.participant.vars['group'] == '2LM' or \
    #             self.participant.vars['group'] == '2QM' or self.participant.vars['group'] == '2QNM' or \
    #             self.participant.vars['group'] == '3LM' or self.participant.vars['group'] == '3QM' or \
    #             self.participant.vars['group'] == '3QNM'


class Results(Page):
    form_model = models.Player
    form_fields = ['mouse_x', 'mouse_y', 'percentage']

    def vars_for_template(self):
        question = ['Reduce the difference in income', 'Limit imports', 'Send troops to fight ISIS',
                    'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                    'Change access to citizenship for children of illegal immigrants',
                    'Build a wall on the US-Mexico border',
                    'Paid leave for parents of new children', 'Increase number of black students at universities',
                    'Pay women and men the same amount for the same work']
        issue = question[self.player.option - 1]
        return {'issue': issue}

    def before_next_page(self):
        if self.player.mouse_x == '' or self.player.mouse_y == '':
            mouse_x_temp = -1
            mouse_y_temp = -1
            mouse_x = [mouse_x_temp]
            mouse_y = [mouse_y_temp]
        else:
            mouse_x_temp = self.player.mouse_x.split(",")
            mouse_y_temp = self.player.mouse_y.split(",")
            mouse_x = list(map(int, map(float, mouse_x_temp)))
            mouse_y = list(map(int, map(float, mouse_y_temp)))

        radius = 30
        width = 690
        height = 600
        area = []

        for i in range(len(mouse_x)):
            if 0 <= mouse_x[i] <= 690 and 0 <= mouse_y[i] <= 600:
                if i == 0:
                    area.append((radius * 2)*(radius * 2))
                else:
                    if abs(mouse_x[i]-mouse_x[i-1]) <= radius and abs(mouse_y[i]-mouse_y[i-1]) <= radius:
                        area.append(2*(abs(mouse_x[i]-mouse_x[i-1]))*radius + 2*(abs(mouse_y[i]-mouse_y[i-1]))*radius - \
                            abs(mouse_y[i]-mouse_y[i-1])*abs(mouse_x[i]-mouse_x[i-1]))
                    else:
                        area.append((radius * 2)*(radius * 2))
            else:
                pass

        if sum(area) <= width*height:
            self.player.percentage = sum(area) / (width*height)
        else:
            self.player.percentage = 1

    def is_displayed(self):
        return self.player.option == 1 or self.player.option == 2 or self.player.option == 3 or self.player.option == 4 or \
               self.player.option == 5 or self.player.option == 6 or self.player.option == 7 or self.player.option == 8 or \
               self.player.option == 9 or self.player.option == 10
        # and (self.participant.vars['group'] == '1LM' or self.participant.vars['group'] == '1QM' or \
               # self.participant.vars['group'] == '1QNM' or self.participant.vars['group'] == '2LM' or \
               #  self.participant.vars['group'] == '2QM' or self.participant.vars['group'] == '2QNM' or \
               #  self.participant.vars['group'] == '3LM' or self.participant.vars['group'] == '3QM' or \
               #  self.participant.vars['group'] == '3QNM')



class Lamp(Page):
    form_model = models.Player
    form_fields = ['mouse_x', 'mouse_y', 'percentage']

    def vars_for_template(self):
        question = ['Reduce the difference in income', 'Limit imports', 'Send troops to fight ISIS',
                    'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                    'Change access to citizenship for children of illegal immigrants',
                    'Build a wall on the US-Mexico border',
                    'Paid leave for parents of new children', 'Increase number of black students at universities',
                    'Pay women and men the same amount for the same work']
        issue = question[self.player.option - 1]
        return {'issue': issue}

    def before_next_page(self):
        if self.player.mouse_x == '' or self.player.mouse_y == '':
            mouse_x_temp = -1
            mouse_y_temp = -1
            mouse_x = [mouse_x_temp]
            mouse_y = [mouse_y_temp]
        else:
            mouse_x_temp = self.player.mouse_x.split(",")
            mouse_y_temp = self.player.mouse_y.split(",")
            mouse_x = list(map(int, map(float, mouse_x_temp)))
            mouse_y = list(map(int, map(float, mouse_y_temp)))

        radius = 30
        width = 690
        height = 600
        area = []

        for i in range(len(mouse_x)):
            if 0 <= mouse_x[i] <= 690 and 0 <= mouse_y[i] <= 600:
                if i == 0:
                    area.append((radius * 2)*(radius * 2))
                else:
                    if abs(mouse_x[i]-mouse_x[i-1]) <= radius and abs(mouse_y[i]-mouse_y[i-1]) <= radius:
                        area.append(2*(abs(mouse_x[i]-mouse_x[i-1]))*radius + 2*(abs(mouse_y[i]-mouse_y[i-1]))*radius - \
                            abs(mouse_y[i]-mouse_y[i-1])*abs(mouse_x[i]-mouse_x[i-1]))
                    else:
                        area.append((radius * 2)*(radius * 2))
            else:
                pass

        if sum(area) <= width*height:
            self.player.percentage = sum(area) / (width*height)
        else:
            self.player.percentage = 1

    def is_displayed(self):
        return self.player.option == 1 or self.player.option == 2 or self.player.option == 3 or self.player.option == 4 or \
               self.player.option == 5 or self.player.option == 6 or self.player.option == 7 or self.player.option == 8 or \
               self.player.option == 9 or self.player.option == 10


class Test2(Page):
    form_model = models.Player
    form_fields = ['mouse_x', 'mouse_y', 'mouse_t']

    def vars_for_template(self):
        question = ['Reduce the difference in income', 'Limit imports', 'Send troops to fight ISIS',
                    'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                    'Change access to citizenship for children of illegal immigrants',
                    'Build a wall on the US-Mexico border',
                    'Paid leave for parents of new children', 'Increase number of black students at universities',
                    'Pay women and men the same amount for the same work']
        issue = question[self.player.option - 1]
        return {'issue': issue}

    def before_next_page(self):
        mouse_t_temp = self.player.mouse_t.split(",")
        mouse_t = list(map(float, mouse_t_temp))
        self.player.time = sum(mouse_t)



    def is_displayed(self):
        return self.player.option == 1 or self.player.option == 2 or self.player.option == 3 or self.player.option == 4 or \
               self.player.option == 5 or self.player.option == 6 or self.player.option == 7 or self.player.option == 8 or \
               self.player.option == 9 or self.player.option == 10

page_sequence = [
    MyPage,
    # ResultsWaitPage,
    # Results
    # Lamp
    Test2
]
