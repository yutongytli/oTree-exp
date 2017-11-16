from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Welcome(Page):
    def before_next_page(self):
        self.participant.vars['pic'] = random.choice(['asc', 'dec'])
        # random.shuffle(Constants.last_three)
        questions = random.sample(Constants.questions, 8)

        self.participant.vars['q_1'] = questions[0][1]
        self.participant.vars['q_2'] = questions[1][1]
        self.participant.vars['q_3'] = questions[2][1]
        self.participant.vars['q_4'] = questions[3][1]
        self.participant.vars['q_5'] = questions[4][1]
        self.participant.vars['q_6'] = questions[5][1]
        self.participant.vars['q_7'] = questions[6][1]
        self.participant.vars['q_8'] = questions[7][1]
        self.participant.vars['q_9'] = Constants.last_three[0][1]
        self.participant.vars['q_10'] = Constants.last_three[1][1]
        self.participant.vars['q_11'] = Constants.last_three[2][1]

        self.player.question_1 = questions[0][0]
        self.player.question_2 = questions[1][0]
        self.player.question_3 = questions[2][0]
        self.player.question_4 = questions[3][0]
        self.player.question_5 = questions[4][0]
        self.player.question_6 = questions[5][0]
        self.player.question_7 = questions[6][0]
        self.player.question_8 = questions[7][0]
        self.player.question_9 = Constants.last_three[0][0]
        self.player.question_10 = Constants.last_three[1][0]
        self.player.question_11 = Constants.last_three[2][0]

        self.participant.vars['party'] = 'none'



class Partisan1(Page):
    form_model = models.Player
    form_fields = ['partisan_1']

    def vars_for_template(self):
        pair = [[1, 'An Independent'],
                [2, 'A Republican'],
                [3, 'A Democrat']]
        random.shuffle(pair)
        content = [pair[0][1], pair[1][1], pair[2][1]]
        value = [pair[0][0], pair[1][0], pair[2][0]]
        mylist = zip(value, content)

        return {'mylist': mylist}

    def is_displayed(self):
        return self.player.treatment == 'prime'


class Partisan2(Page):
    form_model = models.Player
    form_fields = ['partisan_2']

    def vars_for_template(self):
        pair = [[1, 'Closer to Republican Party'],
                [2, 'Closer to Democratic Party'],
                [3, 'Neither']]
        random.shuffle(pair)
        content = [pair[0][1], pair[1][1], pair[2][1]]
        value = [pair[0][0], pair[1][0], pair[2][0]]
        mylist = zip(value, content)

        return {'mylist': mylist}

    def is_displayed(self):
        return self.player.treatment == 'prime'

    def before_next_page(self):
        if self.player.partisan_1 == 2:
            self.participant.vars['party'] = 'rep'
        elif self.player.partisan_1 == 3:
            self.participant.vars['party'] = 'dem'
        else:
            if self.player.partisan_2 == 1:
                self.participant.vars['party'] = 'rep'
            elif self.player.partisan_2 == 2:
                self.participant.vars['party'] = 'dem'
            else:
                self.participant.vars['party'] = 'ind'


class Internet(Page):
    form_model = models.Player
    form_fields = ['internet_1']

    def vars_for_template(self):
        content = ['I use my smartphone', 'I use my computer', 'I use a friend or a family member\'s smartphone',
                   'I use a friend or a family member\'s computer', 'I do not have access to the internet']
        value = [1, 2, 3, 4, 5]
        mylist = zip(value, content)

        return {'mylist': mylist}

    def is_displayed(self):
        return self.participant.vars['party'] != 'ind' and self.player.treatment == 'prime'


class Internet2(Page):
    form_model = models.Player
    form_fields = ['internet_2']

    def vars_for_template(self):
        list1 = [[1, 'I do not have access to the internet'], [2, 'I use my smartphone']]
        list2 = [[2, 'I use my smartphone'], [1, 'I do not have access to the internet']]
        mylist = random.choice([list1, list2])
        return {'value1': mylist[0][0],
                'value2': mylist[1][0],
                'content1': mylist[0][1],
                'content2': mylist[1][1]}

    def is_displayed(self):
        return self.player.internet_1 != 5 and self.participant.vars['party'] != 'ind' and self.player.treatment == 'prime'


class Pic1(Page):
    form_model = models.Player
    form_fields = ['pic1']

    def is_displayed(self):
        return self.participant.vars['pic'] == 'asc' and self.participant.vars['party'] != 'ind' and self.player.treatment == 'prime'


class Pic2(Page):
    form_model = models.Player
    form_fields = ['pic2_like', 'pic2_dislike']

    def vars_for_template(self):
        if self.player.partisan_1 == 2:
            party_self = 'Republican'
            party_other = 'Democratic'
        else:
            party_self = 'Democratic'
            party_other = 'Republican'

        return {'party_self': party_self,
                'party_other': party_other}

    def is_displayed(self):
        return self.participant.vars['party'] != 'ind' and self.participant.vars['pic'] == 'asc' and self.player.treatment == 'prime'


class Pic11(Page):
    form_model = models.Player
    form_fields = ['pic1']

    def is_displayed(self):
        return self.participant.vars['pic'] == 'dec' and self.participant.vars['party'] != 'ind' and self.player.treatment == 'prime'


class Pic22(Page):
    form_model = models.Player
    form_fields = ['pic2_like', 'pic2_dislike']

    def vars_for_template(self):
        if self.player.partisan_1 == 2:
            party_self = 'Republican'
            party_other = 'Democratic'
        else:
            party_self = 'Democratic'
            party_other = 'Republican'

        return {'party_self': party_self,
                'party_other': party_other}

    def is_displayed(self):
        return self.participant.vars['party'] != 'ind' and self.participant.vars['pic'] == 'dec' and self.player.treatment == 'prime'


class Internet3(Page):
    form_model = models.Player
    form_fields = ['internet_3']

    def vars_for_template(self):
        content = ['I use my smartphone', 'I use my computer',
                   'I use a friend or a family member\'s smartphone',
                   'I use a friend or a family member\'s computer', 'I do not have access to the internet']
        value = [1, 2, 3, 4, 5]
        mylist = zip(value, content)

        return {'mylist': mylist}

    def is_displayed(self):
        return self.participant.vars['party'] != 'ind' and self.player.treatment == 'prime'


class Internet4(Page):
    form_model = models.Player
    form_fields = ['internet_4']

    def vars_for_template(self):
        list1 = [[1, 'I do not have access to the internet'], [2, 'I use my smartphone']]
        list2 = [[2, 'I use my smartphone'], [1, 'I do not have access to the internet']]
        mylist = random.choice([list1, list2])
        return {'value1': mylist[0][0],
                'value2': mylist[1][0],
                'content1': mylist[0][1],
                'content2': mylist[1][1]}

    def is_displayed(self):
        return self.player.internet_3 != 5 and self.participant.vars['party'] != 'ind' and self.player.treatment == 'prime'


class Q1(Page):
    form_model = models.Player
    form_fields = ['answer_1']

    def vars_for_template(self):
        q_1 = self.participant.vars['q_1']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']

        mylist1 = zip(value1, content1)

        return {'mylist1': mylist1,
                'q_1': q_1}


class Q2(Page):
    form_model = models.Player
    form_fields = ['answer_2']

    def vars_for_template(self):
        q_2 = self.participant.vars['q_2']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']

        mylist1 = zip(value1, content1)

        return {'mylist1': mylist1,
                'q_2': q_2}


class Q3(Page):
    form_model = models.Player
    form_fields = ['answer_3']

    def vars_for_template(self):
        q_3 = self.participant.vars['q_3']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']

        mylist1 = zip(value1, content1)

        return {'mylist1': mylist1,
                'q_3': q_3}


class Q4(Page):
    form_model = models.Player
    form_fields = ['answer_4']

    def vars_for_template(self):
        q_4 = self.participant.vars['q_4']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']

        mylist1 = zip(value1, content1)

        return {'mylist1': mylist1,
                'q_4': q_4}


class Q5(Page):
    form_model = models.Player
    form_fields = ['answer_5']

    def vars_for_template(self):
        q_5 = self.participant.vars['q_5']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']

        mylist1 = zip(value1, content1)

        return {'mylist1': mylist1,
                'q_5': q_5}


class Q6(Page):
    form_model = models.Player
    form_fields = ['answer_6']

    def vars_for_template(self):
        q_6 = self.participant.vars['q_6']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']

        mylist1 = zip(value1, content1)

        return {'mylist1': mylist1,
                'q_6': q_6}


class Q7(Page):
    form_model = models.Player
    form_fields = ['answer_7']

    def vars_for_template(self):
        q_7 = self.participant.vars['q_7']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']

        mylist1 = zip(value1, content1)

        return {'mylist1': mylist1,
                'q_7': q_7}


class Q8(Page):
    form_model = models.Player
    form_fields = ['answer_8']

    def vars_for_template(self):
        q_8 = self.participant.vars['q_8']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']

        mylist1 = zip(value1, content1)

        return {'mylist1': mylist1,
                'q_8': q_8}


class Q9(Page):
    form_model = models.Player
    form_fields = ['answer_9', 'importance_9']

    def vars_for_template(self):
        q_9 = self.participant.vars['q_9']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']
        order2 = random.choice(['asc', 'dec'])
        if order2 == 'asc':
            value2 = [1, 2, 3, 4, 5]
            content2 = ['Not Important at all', 'Not too Important', 'Somewhat Important', 'Very Important',
                        'Extremely Important']
        else:
            value2 = [5, 4, 3, 2, 1]
            content2 = ['Extremely Important', 'Very Important', 'Somewhat Important', 'Not too Important',
                        'Not Important at all']

        mylist1 = zip(value1, content1)
        mylist2 = zip(value2, content2)

        return {'mylist1': mylist1,
                'mylist2': mylist2,
                'q_9': q_9}


class Q10(Page):
    form_model = models.Player
    form_fields = ['answer_10', 'importance_10']

    def vars_for_template(self):
        q_10 = self.participant.vars['q_10']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']
        order2 = random.choice(['asc', 'dec'])
        if order2 == 'asc':
            value2 = [1, 2, 3, 4, 5]
            content2 = ['Not Important at all', 'Not too Important', 'Somewhat Important', 'Very Important',
                        'Extremely Important']
        else:
            value2 = [5, 4, 3, 2, 1]
            content2 = ['Extremely Important', 'Very Important', 'Somewhat Important', 'Not too Important',
                        'Not Important at all']

        mylist1 = zip(value1, content1)
        mylist2 = zip(value2, content2)

        return {'mylist1': mylist1,
                'mylist2': mylist2,
                'q_10': q_10}


class Q11(Page):
    form_model = models.Player
    form_fields = ['answer_11', 'importance_11']

    def vars_for_template(self):
        q_11 = self.participant.vars['q_11']

        order1 = random.choice(['asc', 'dec'])
        if order1 == 'asc':
            value1 = [1, 2, 3, 4, 5, 6, 7]
            content1 = ['Oppose a Great Deal', 'Oppose Moderately', 'Oppose a Little', 'Neither Favor nor Oppose',
                        'Favor a Little', 'Favor Moderately', 'Favor a Great Deal']
        else:
            value1 = [7, 6, 5, 4, 3, 2, 1]
            content1 = ['Favor a Great Deal', 'Favor Moderately', 'Favor a Little', 'Neither Favor nor Oppose',
                        'Oppose a Little', 'Oppose Moderately', 'Oppose a Great Deal']
        order2 = random.choice(['asc', 'dec'])
        if order2 == 'asc':
            value2 = [1, 2, 3, 4, 5]
            content2 = ['Not Important at all', 'Not too Important', 'Somewhat Important', 'Very Important',
                        'Extremely Important']
        else:
            value2 = [5, 4, 3, 2, 1]
            content2 = ['Extremely Important', 'Very Important', 'Somewhat Important', 'Not too Important',
                        'Not Important at all']

        mylist1 = zip(value1, content1)
        mylist2 = zip(value2, content2)

        return {'mylist1': mylist1,
                'mylist2': mylist2,
                'q_11': q_11}


class Employ(Page):
    form_model = models.Player
    form_fields = ['employ']


class Trump(Page):
    form_model = models.Player
    form_fields = ['trump']


class Partisan3(Page):
    form_model = models.Player
    form_fields = ['partisan_3']

    def vars_for_template(self):
        if self.participant.vars['party'] == 'rep':
            party_self = 'a Republican'
        elif self.participant.vars['party'] == 'dem':
            party_self = 'a Democrat'
        else:
            party_self = 'an Independent'

        order = random.choice(['dec', 'asc'])
        if order == 'dec':
            value = [4, 3, 2, 1]
            content = ['Not at all', 'Very little', 'Somewhat', 'A great deal']
        else:
            value = [1, 2, 3, 4]
            content = ['A great deal', 'Somewhat', 'Very little', 'Not at all']

        mylist = zip(value, content)

        return {'mylist': mylist,
                'party_self': party_self}


class Partisan4(Page):
    form_model = models.Player
    form_fields = ['partisan_4']

    def vars_for_template(self):
        if self.participant.vars['party'] == 'rep':
            party_self = 'Republican'
        elif self.participant.vars['party'] == 'dem':
            party_self = 'Democrat'
        else:
            party_self = 'Independent'

        order = random.choice(['dec', 'asc'])
        if order == 'dec':
            value = [4, 3, 2, 1]
            content = ['Not well at all', 'Not very well', 'Very well', 'Extremely well']
        else:
            value = [1, 2, 3, 4]
            content = ['Extremely well', 'Very well', 'Not very well', 'Not well at all']

        mylist = zip(value, content)

        return {'mylist': mylist,
                'party_self': party_self}


class Partisan5(Page):
    form_model = models.Player
    form_fields = ['partisan_5']

    def vars_for_template(self):
        if self.participant.vars['party'] == 'rep':
            party_self = 'a Republican'
        elif self.participant.vars['party'] == 'dem':
            party_self = 'a Democrat'
        else:
            party_self = 'an Independent'

        order = random.choice(['dec', 'asc'])
        if order == 'dec':
            value = [4, 3, 2, 1]
            content = ['Not important at all', 'Not very important', 'Very important', 'Extremely important']
        else:
            value = [1, 2, 3, 4]
            content = ['Extremely important', 'Very important', 'Not very important', 'Not important at all']

        mylist = zip(value, content)

        return {'mylist': mylist,
                'party_self': party_self}


class Partisan6(Page):
    form_model = models.Player
    form_fields = ['partisan_6']

    def vars_for_template(self):
        if self.participant.vars['party'] == 'rep':
            party_self = 'Republicans'
        elif self.participant.vars['party'] == 'dem':
            party_self = 'Democrats'
        else:
            party_self = 'Independents'
        order = random.choice(['dec', 'asc'])
        if order == 'dec':
            value = [5, 4, 3, 2, 1]
            content = ['Never', 'Rarely', 'Some of the time', 'Most of the time', 'All of the time']
        else:
            value = [1, 2, 3, 4, 5]
            content = ['All of the time', 'Most of the time', 'Some of the time', 'Rarely', 'Never']

        mylist = zip(value, content)

        return {'mylist': mylist,
                'party_self': party_self,}


class QV(Page):
    def is_displayed(self):
        return self.participant.vars['party'] == 'ind' or self.player.treatment == 'deprime'


class Results(Page):
    def vars_for_template(self):
        url = self.player.participant._start_url()
        id = url.split('/', 3)
        code = id[2]

        return {'code': code}


page_sequence = [
    Welcome,
    Partisan1,
    Partisan2,
    Internet,
    Internet2,
    Pic1,
    Pic22,
    Internet3,
    Internet4,
    Pic2,
    Pic11,
    Q1,
    Q2,
    Q3,
    Q4,
    Q5,
    Q6,
    Q7,
    Q8,
    Q9,
    Q10,
    Q11,
    Employ,
    Trump,
    Partisan3,
    Partisan4,
    Partisan5,
    Partisan6,
    QV,
    Results
]
