from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
from django.http import HttpResponse, HttpResponseRedirect


class Introduction(Page):
    form_model = models.Player
    form_fields = ['prolific_id', 'consent']

    def is_displayed(self):
        return self.round_number == 1


class MyPage(Page):
    form_model = models.Player
    form_fields = ['answer']

    def answer_choices(self):
        ans = self.player.current_answers()
        return [
            ans['choice1'],
            ans['choice2'],
            ans['choice3'],
            ans['choice4']
        ]

    def before_next_page(self):
        self.participant.vars['ans_%s' % self.round_number] = self.player.answer
        if self.round_number == Constants.num_rounds:
            # self.player.get_scores()
            if self.player.condition == 'Scramble':
                unscram = []
                scram = []
                for i, j in zip(self.participant.vars['order_list'], self.participant.vars['pic_final_list']):
                    if i != j:
                        scram.append(i)
                    else:
                        unscram.append(i)

                listc10 = random.sample(scram, 5) + random.sample(unscram, 5)
                self.participant.vars['listc10'] = random.sample(listc10, 10)
            else:
                self.participant.vars['listc10'] = random.sample(list(range(self.round_number)), 10)

    def vars_for_template(self):
        ans = self.player.current_answers()
        choice1 = ans['choice1']
        choice2 = ans['choice2']
        choice3 = ans['choice3']
        choice4 = ans['choice4']
        title1 = ans['title1']
        title2 = ans['title2']
        title3 = ans['title3']
        title4 = ans['title4']
        if self.player.condition == 'Scramble':
            self.player.question_num = self.participant.vars['pic_final_list'][self.round_number - 1] + 1
        else:
            self.player.question_num = self.round_number
        image = "REMT/eye%s.png" % self.player.question_num
        return {
            'choice1': choice1,
            'choice2': choice2,
            'choice3': choice3,
            'choice4': choice4,
            'image': image,
            'title1': title1,
            'title2': title2,
            'title3': title3,
            'title4': title4
        }


class C0(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C1(Page):
    form_model = models.Player
    form_fields = ['C1']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][0]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic1 = pic + 1
            image = "REMT/eye%s.png" % (pic+1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][0] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][0] + 1)
            self.player.pic1 = self.participant.vars['listc10'][0] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C2(Page):
    form_model = models.Player
    form_fields = ['C2']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][1]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic2 = pic + 1
            image = "REMT/eye%s.png" % (pic+1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][1] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][1] + 1)
            self.player.pic2 = self.participant.vars['listc10'][1] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C3(Page):
    form_model = models.Player
    form_fields = ['C3']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][2]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic3 = pic + 1
            image = "REMT/eye%s.png" % (pic+1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][2] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][2] + 1)
            self.player.pic3 = self.participant.vars['listc10'][2] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C4(Page):
    form_model = models.Player
    form_fields = ['C4']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][3]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic4 = pic + 1
            image = "REMT/eye%s.png" % (pic+1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][3] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][3] + 1)
            self.player.pic4 = self.participant.vars['listc10'][3] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C5(Page):
    form_model = models.Player
    form_fields = ['C5']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][4]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic5 = pic + 1
            image = "REMT/eye%s.png" % (pic+1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][4] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][4] + 1)
            self.player.pic5 = self.participant.vars['listc10'][4] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C6(Page):
    form_model = models.Player
    form_fields = ['C6']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][5]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic6 = pic + 1
            image = "REMT/eye%s.png" % (pic+1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][5] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][5] + 1)
            self.player.pic6 = self.participant.vars['listc10'][5] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C7(Page):
    form_model = models.Player
    form_fields = ['C7']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][6]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic7 = pic + 1
            image = "REMT/eye%s.png" % (pic+1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][6] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][6] + 1)
            self.player.pic7 = self.participant.vars['listc10'][6] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C8(Page):
    form_model = models.Player
    form_fields = ['C8']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][7]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic8 = pic + 1
            image = "REMT/eye%s.png" % (pic+1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][7] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][7] + 1)
            self.player.pic8 = self.participant.vars['listc10'][7] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C9(Page):
    form_model = models.Player
    form_fields = ['C9']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][8]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic9 = pic + 1
            image = "REMT/eye%s.png" % (pic+1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][8] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][8] + 1)
            self.player.pic9 = self.participant.vars['listc10'][8] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class C10(Page):
    form_model = models.Player
    form_fields = ['C10']

    def vars_for_template(self):
        if self.player.condition == 'Scramble':
            num = self.participant.vars['listc10'][9]
            indx = self.participant.vars['order_list'].index(num)
            pic = self.participant.vars['pic_final_list'][indx]
            ans = self.participant.vars['ans_%s' % (indx + 1)]
            self.player.pic10 = pic + 1
            image = "REMT/eye%s.png" % (pic + 1)
        else:
            ans = self.participant.vars['ans_%s' % (self.participant.vars['listc10'][9] + 1)]
            image = "REMT/eye%s.png" % (self.participant.vars['listc10'][9] + 1)
            self.player.pic10 = self.participant.vars['listc10'][9] + 1
        return {'image': image,
                'ans': ans}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class Completion(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Introduction,
    MyPage,
    C0,
    C1,
    C2,
    C3,
    C4,
    C5,
    C6,
    C7,
    C8,
    C9,
    C10,
    Completion,
    Results
]
