from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Welcome(Page):

    def before_next_page(self):
        random.shuffle(Constants.first_two)
        random.shuffle(Constants.questions)
        self.participant.vars['q_1'] = Constants.first_two[0][1]
        self.participant.vars['q_2'] = Constants.first_two[1][1]
        self.participant.vars['q_3'] = Constants.questions[0][1]
        self.participant.vars['q_4'] = Constants.questions[1][1]
        self.participant.vars['q_5'] = Constants.questions[2][1]
        self.participant.vars['q_6'] = Constants.questions[3][1]
        self.player.question_1 = Constants.first_two[0][0]
        self.player.question_2 = Constants.first_two[1][0]
        self.player.question_3 = Constants.questions[0][0]
        self.player.question_4 = Constants.questions[1][0]
        self.player.question_5 = Constants.questions[2][0]
        self.player.question_6 = Constants.questions[3][0]


class Internet(Page):
    form_model = models.Player
    form_fields = ['internet_1']

    def vars_for_template(self):
        content = ['I use my smartphone', 'I use my computer', 'I use a friend or a family member\'s smartphone',
                   'I use a friend or a family member\'s computer', 'I do not have access to the internet']
        value = [1, 2, 3, 4, 5]
        mylist = zip(value, content)

        return {'mylist': mylist}


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
        return self.player.internet_1 != 5


class Q1(Page):
    form_model = models.Player
    form_fields = ['answer_1', 'importance_1']

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
                'q_1': q_1}


class Q2(Page):
    form_model = models.Player
    form_fields = ['answer_2', 'importance_2']

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
                'q_2': q_2}


class Q3(Page):
    form_model = models.Player
    form_fields = ['answer_3', 'importance_3']

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
                'q_3': q_3}


class Q4(Page):
    form_model = models.Player
    form_fields = ['answer_4', 'importance_4']

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
                'q_4': q_4}


class Q5(Page):
    form_model = models.Player
    form_fields = ['answer_5', 'importance_5']

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
                'q_5': q_5}


class Q6(Page):
    form_model = models.Player
    form_fields = ['answer_6', 'importance_6']

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
                'q_6': q_6}


class Frequency(Page):
    form_model = models.Player
    form_fields = ['freq']


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


class QV(Page):
    pass


class Result(Page):
    def vars_for_template(self):
        url = self.player.participant._start_url()
        id = url.split('/', 3)
        code = id[2]

        return {'code': code}

page_sequence = [
    Welcome,
    Q1,
    Q2,
    Internet,
    Internet2,
    Q3,
    Q4,
    Q5,
    Q6,
    Frequency,
    Partisan1,
    Partisan2,
    QV,
    Result
]
