from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage1(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_1']

    def before_next_page(self):
        self.participant.vars['opinion_1'] = 'Indifferent'
        self.participant.vars['preference_1'] = 999



class MyPage2(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_2']

    def before_next_page(self):
        self.participant.vars['opinion_2'] = 'Indifferent'
        self.participant.vars['preference_2'] = 999


class MyPage3(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_3']

    def before_next_page(self):
        self.participant.vars['opinion_3'] = 'Indifferent'
        self.participant.vars['preference_3'] = 999


class MyPage4(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_4']

    def before_next_page(self):
        self.participant.vars['opinion_4'] = 'Indifferent'
        self.participant.vars['preference_4'] = 999


class MyPage5(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_5']

    def before_next_page(self):
        self.participant.vars['opinion_5'] = 'Indifferent'
        self.participant.vars['preference_5'] = 999

class MyPage6(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_6']

    def before_next_page(self):
        self.participant.vars['opinion_6'] = 'Indifferent'
        self.participant.vars['preference_6'] = 999

class MyPage7(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_7']

    def before_next_page(self):
        self.participant.vars['opinion_7'] = 'Indifferent'
        self.participant.vars['preference_7'] = 999

class MyPage8(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_8']

    def before_next_page(self):
        self.participant.vars['opinion_8'] = 'Indifferent'
        self.participant.vars['preference_8'] = 999

class MyPage9(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_9']

    def before_next_page(self):
        self.participant.vars['opinion_9'] = 'Indifferent'
        self.participant.vars['preference_9'] = 999

class MyPage10(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_10']

    def before_next_page(self):
        self.participant.vars['opinion_10'] = 'Indifferent'
        self.participant.vars['preference_10'] = 999


class Likert(Page):
    form_model = models.Player
    form_fields = ['likert_1']

    def is_displayed(self):
        return self.player.submitted_answer_1 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_1'] = 'Agree'
        self.participant.vars['preference_1'] = self.player.likert_1

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likertt(Page):
    form_model = models.Player
    form_fields = ['likert_1']

    def is_displayed(self):
        return self.player.submitted_answer_1 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_1'] = 'Disagree'
        self.participant.vars['preference_1'] = self.player.likert_1


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert

class Likert2(Page):
    form_model = models.Player
    form_fields = ['likert_2']

    def is_displayed(self):
        return self.player.submitted_answer_2 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_2'] = 'Agree'
        self.participant.vars['preference_2'] = self.player.likert_2

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }



class Likertt2(Page):
    form_model = models.Player
    form_fields = ['likert_2']

    def is_displayed(self):
        return self.player.submitted_answer_2 == 'Oppose'

    def before_next_page(self):
        self.participant.vars['opinion_2'] = 'Disagree'
        self.participant.vars['preference_2'] = self.player.likert_2


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

class Likert3(Page):
    form_model = models.Player
    form_fields = ['likert_3']

    def is_displayed(self):
        return self.player.submitted_answer_3 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_3'] = 'Agree'
        self.participant.vars['preference_3'] = self.player.likert_3

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }



class Likertt3(Page):
    form_model = models.Player
    form_fields = ['likert_3']

    def is_displayed(self):
        return self.player.submitted_answer_3 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_3'] = 'Disagree'
        self.participant.vars['preference_3'] = self.player.likert_3


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

class Likert4(Page):
    form_model = models.Player
    form_fields = ['likert_4']

    def is_displayed(self):
        return self.player.submitted_answer_4 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_4'] = 'Agree'
        self.participant.vars['preference_4'] = self.player.likert_4

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likertt4(Page):
    form_model = models.Player
    form_fields = ['likert_4']

    def is_displayed(self):
        return self.player.submitted_answer_4 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_4'] = 'Disagree'
        self.participant.vars['preference_4'] = self.player.likert_4


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Likert5(Page):
    form_model = models.Player
    form_fields = ['likert_5']

    def is_displayed(self):
        return self.player.submitted_answer_5 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_5'] = 'Agree'
        self.participant.vars['preference_5'] = self.player.likert_5

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likertt5(Page):
    form_model = models.Player
    form_fields = ['likert_5']

    def is_displayed(self):
        return self.player.submitted_answer_5 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_5'] = 'Disagree'
        self.participant.vars['preference_5'] = self.player.likert_5


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Likert6(Page):
    form_model = models.Player
    form_fields = ['likert_6']

    def is_displayed(self):
        return self.player.submitted_answer_6 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_6'] = 'Agree'
        self.participant.vars['preference_6'] = self.player.likert_6

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likertt6(Page):
    form_model = models.Player
    form_fields = ['likert_6']

    def is_displayed(self):
        return self.player.submitted_answer_6 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_6'] = 'Disagree'
        self.participant.vars['preference_6'] = self.player.likert_6


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Likert7(Page):
    form_model = models.Player
    form_fields = ['likert_7']

    def is_displayed(self):
        return self.player.submitted_answer_7 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_7'] = 'Agree'
        self.participant.vars['preference_7'] = self.player.likert_7

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likertt7(Page):
    form_model = models.Player
    form_fields = ['likert_7']

    def is_displayed(self):
        return self.player.submitted_answer_7 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_7'] = 'Disagree'
        self.participant.vars['preference_7'] = self.player.likert_7


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Likert8(Page):
    form_model = models.Player
    form_fields = ['likert_8']

    def is_displayed(self):
        return self.player.submitted_answer_8 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_8'] = 'Agree'
        self.participant.vars['preference_8'] = self.player.likert_8

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likertt8(Page):
    form_model = models.Player
    form_fields = ['likert_8']

    def is_displayed(self):
        return self.player.submitted_answer_8 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_8'] = 'Disagree'
        self.participant.vars['preference_8'] = self.player.likert_8


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Likert9(Page):
    form_model = models.Player
    form_fields = ['likert_9']

    def is_displayed(self):
        return self.player.submitted_answer_9 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_9'] = 'Agree'
        self.participant.vars['preference_9'] = self.player.likert_9

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likertt9(Page):
    form_model = models.Player
    form_fields = ['likert_9']

    def is_displayed(self):
        return self.player.submitted_answer_9 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_9'] = 'Disagree'
        self.participant.vars['preference_9'] = self.player.likert_9


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Likert10(Page):
    form_model = models.Player
    form_fields = ['likert_10']

    def is_displayed(self):
        return self.player.submitted_answer_10 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_10'] = 'Agree'
        self.participant.vars['preference_10'] = self.player.likert_10

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likertt10(Page):
    form_model = models.Player
    form_fields = ['likert_10']

    def is_displayed(self):
        return self.player.submitted_answer_10 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_10'] = 'Disagree'
        self.participant.vars['preference_10'] = self.player.likert_10


    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Important(Page):
    form_model = models.Player
    form_fields = ['important_1']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important',
                 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important',
                 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Important2(Page):
    form_model = models.Player
    form_fields = ['important_2']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Important3(Page):
    form_model = models.Player
    form_fields = ['important_3']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }



class Important4(Page):
    form_model = models.Player
    form_fields = ['important_4']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Important5(Page):
    form_model = models.Player
    form_fields = ['important_5']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Important6(Page):
    form_model = models.Player
    form_fields = ['important_6']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Important7(Page):
    form_model = models.Player
    form_fields = ['important_7']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Important8(Page):
    form_model = models.Player
    form_fields = ['important_8']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }


class Important9(Page):
    form_model = models.Player
    form_fields = ['important_9']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }



class Important10(Page):
    form_model = models.Player
    form_fields = ['important_10']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    def before_next_page(self):
        preference_list = []
        preference_3 = []
        preference_2 = []
        preference_1 = []
        for i in range(1, 11):
            preference_list.append(self.participant.vars['preference_%s' % i])
        for i, item in enumerate(preference_list):
            if item == 3:
                preference_3.append(i+1)
            elif item == 2:
                preference_2.append(i+1)
            elif item == 1:
                preference_1.append(i+1)
            else:
                pass

        if len(preference_1) != 0:
            self.participant.vars['issue'] = random.choice(preference_1)  # number of issue
            self.participant.vars['important'] = 'a great deal'
        else:
            if len(preference_2) != 0:
                self.participant.vars['issue'] = random.choice(preference_2)
                self.participant.vars['important'] = 'a moderate amount'
            else:
                if len(preference_3) != 0:
                    self.participant.vars['issue'] = random.choice(preference_3)
                    self.participant.vars['important'] = 'a little'
                else:
                    self.participant.vars['issue'] = 999



class Care1(Page):
    form_model = models.Player
    form_fields = ['care1f']

    def care1f_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        random.shuffle(list_question)
        return list_question



class Care1_2(Page):
    form_model = models.Player
    form_fields = ['care1o']

    def care1o_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o]
        list_temp = [list_question[int(self.player.care1f) - 1]]

        # list_new = list(set(list_question)-set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)
        return list_new


class Care2(Page):
    form_model = models.Player
    form_fields = ['care2f']

    def care2f_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1]]

        # list_new = list(set(list_question)-set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new



class Care2_2(Page):
    form_model = models.Player
    form_fields = ['care2o']

    def care2o_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1],
                     list_question[int(self.player.care2f) - 1]]

        # list_new = list(set(list_question)-set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new



class Care3(Page):
    form_model = models.Player
    form_fields = ['care3f']

    def care3f_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o, self.player.care2f, self.player.care2o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1],
                     list_question[int(self.player.care2f) - 1], list_question[int(self.player.care2o) - 1]]

        # list_new = list(set(list_question) - set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new


class Care3_2(Page):
    form_model = models.Player
    form_fields = ['care3o']

    def care3o_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o, self.player.care2f, self.player.care2o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1],
                     list_question[int(self.player.care2f) - 1], list_question[int(self.player.care2o) - 1],
                     list_question[int(self.player.care3f) - 1]]

        # list_new = list(set(list_question) - set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new

    def before_next_page(self):
        self.participant.vars['lot1'] = self.player.care1f
        self.participant.vars['lot2'] = self.player.care2f
        self.participant.vars['lot3'] = self.player.care3f
        self.participant.vars['little1'] = self.player.care1o
        self.participant.vars['little2'] = self.player.care2o
        self.participant.vars['little3'] = self.player.care3o


page_sequence = [
        MyPage1,
    Likert,
    Likertt,
    Important,
    MyPage2,
    Likert2,
    Likertt2,
    Important2,
    MyPage3,
    Likert3,
    Likertt3,
    Important3,
    MyPage4,
    Likert4,
    Likertt4,
    Important4,
    MyPage5,
    Likert5,
    Likertt5,
    Important5,
    MyPage6,
    Likert6,
    Likertt6,
    Important6,
    MyPage7,
    Likert7,
    Likertt7,
    Important7,
    MyPage8,
    Likert8,
    Likertt8,
    Important8,
    MyPage9,
    Likert9,
    Likertt9,
    Important9,
    MyPage10,
    Likert10,
    Likertt10,
    Important10,
    Care1,
    Care1_2,
    Care2,
    Care2_2,
    Care3,
    Care3_2
]
