from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
import random

author = 'Yutong LI'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'oral_argument'
    players_per_group = None
    num_rounds = 5

    with open('oral_argument/female_name.csv') as f:
        clips = list(csv.DictReader(f))


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            selected_clips = random.sample(Constants.clips, 5)
            for i in range(len(selected_clips)):
                p.participant.vars['clip_%s' % (i+1)] = selected_clips[i]['clip_name']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    audio_group = models.CharField()
    audio_for_player = models.CharField()

    attractive = models.CharField()
    masculine = models.CharField()
    intelligent = models.CharField()
    aggressive = models.CharField()
    trustworthy = models.CharField()
    confident = models.CharField()
    win = models.CharField()
    quality = models.CharField()

    birth = models.IntegerField(
        max=2017,
        min=1900,
        doc="""Please choose one of the choices""",
    )

    gender = models.CharField(
        choices=['Female', 'Male', 'Other'],
        doc="""Please choose one of the choices""",
    )

    state = models.CharField(
        choices=[
            ("AL", 'Alabama'),
            ("AK", 'Alaska'),
            ("AZ", 'Arizona'),
            ("AR", 'Arkansas'),
            ("CA", 'California'),
            ("CO", 'Colorado'),
            ("CT", 'Connecticut'),
            ("DE", 'Delaware'),
            ("DC", 'District Of Columbia'),
            ("FL", 'Florida'),
            ("GA", 'Georgia'),
            ("HI", 'Hawaii'),
            ("ID", 'Idaho'),
            ("IL", 'Illinois'),
            ("IN", 'Indiana'),
            ("IA", 'Iowa'),
            ("KS", 'Kansas'),
            ("KY", 'Kentucky'),
            ("LA", 'Louisiana'),
            ("ME", 'Maine'),
            ("MD", 'Maryland'),
            ("MA", 'Massachusetts'),
            ("MI", 'Michigan'),
            ("MN", 'Minnesota'),
            ("MS", 'Mississippi'),
            ("MO", 'Missouri'),
            ("MT", 'Montana'),
            ("NE", 'Nebraska'),
            ("NV", 'Nevada'),
            ("NH", 'New Hampshire'),
            ("NJ", 'New Jersey'),
            ("NM", 'New Mexico'),
            ("NY", 'New York'),
            ("NC", 'North Carolina'),
            ("ND", 'North Dakota'),
            ("OH", 'Ohio'),
            ("OK", 'Oklahoma'),
            ("OR", 'Oregon'),
            ("PA", 'Pennsylvania'),
            ("RI", 'Rhode Island'),
            ("SC", 'South Carolina'),
            ("SD", 'South Dakota'),
            ("TN", 'Tennessee'),
            ("TX", 'Texas'),
            ("UT", 'Utah'),
            ("VT", 'Vermont'),
            ("VA", 'Virginia'),
            ("WA", 'Washington'),
            ("WV", 'West Virginia'),
            ("WI", 'Wisconsin'),
            ("WY", 'Wyoming'),
            ("AS", 'American Samoa'),
            ("GU", 'Guam'),
            ("MP", 'Northern Mariana Islands'),
            ("PR", 'Puerto Rico'),
            ("UM", 'United States Minor Outlying Islands'),
            ("VI", 'Virgin Islands')],
        doc="""Please choose one of the choices""",
    )

    education = models.CharField(
        choices=['Doctoral degree', 'Professional degree', 'Master\'s degree', 'Bachelor\'s degree', 'Associate\'s degree',
                 'college', 'Graduated high school', 'Some high school', 'No high school-level education'],
        doc="""Please choose one of the choices""",
    )

    race = models.CharField(
        choices=['African American', 'American Indian or Native American', 'Asian', 'Hispanic or Latino/Latina',
                 'Native Hawaiian or Pacific Islander', 'White'],
        doc="""Please choose one of the choices""",
    )

    income = models.CharField(
        choices=['Less than $20000', 'Between $20000 to $40000', 'Between $40001 to $60000', 'Between $60001 to $80000',
                 'More than $80000'],
        doc="""Please choose one of the choices""",
    )

    # male or female voice clips for one player
    def get_audio_group(self):
        self.audio_group = random.choice(['female', 'male'])

    def get_question(self):
        if self.audio_group == 'male':
            name_list_1 = [['Very Unattractive', 'Very Attractive'], ['Not At All Masculine', 'Very Masculine'],
                           ['Not Intelligent', 'Intelligent'], ['Very Unaggressive', 'Very Aggressive'],
                           ['Not Trustworthy', 'Trustworthy'], ['Very Timid', 'Very Confident'],
                           ['Will Definitely Loss', 'Will Definitely Win'], ['Very Bad', 'Very Good']]
        else:
            name_list_1 = [['Very Unattractive', 'Very Attractive'], ['Not At All Feminine', 'Very Feminine'],
                           ['Not Intelligent', 'Intelligent'], ['Very Unaggressive', 'Very Aggressive'],
                           ['Not Trustworthy', 'Trustworthy'], ['Very Timid', 'Very Confident'],
                           ['Will Definitely Loss', 'Will Definitely Win'], ['Very Bad', 'Very Good']]

        temp = []
        name_list_2 = []
        direction = []

        for i in range(len(name_list_1)):
            random.shuffle(name_list_1[i])
            temp.append(name_list_1[i])
            if len(temp[i][0]) > len(temp[i][1]) and temp[i][0] != 'Very Confident' and temp[i][0] != 'Very Good':
                direction.append('ascending')
            elif temp[i][0] == 'Very Timid' or temp[i][0] == 'Very Bad':
                direction.append('ascending')
            else:
                direction.append('descending')

            name_list_2.append([i, temp[i][0], temp[i][1]])

        name_list_3 = name_list_2[0:6]

        random.shuffle(name_list_3)
        name_list_3.extend(name_list_2[6:8])

        for i in range(len(direction)):
            for j in range(len(name_list_3)):
                if name_list_3[j][0] == i:
                    name_list_3[j].append(direction[i])
                else:
                    pass

        name = {0: 'attractive', 1: 'masculine', 2: 'intelligent', 3: 'aggressive', 4: 'trustworthy', 5: 'confident',
                6: 'win', 7: 'quality'}

        for i in range(len(name_list_3)):
            if name_list_3[i][0] in name:
                name_list_3[i][0] = name[name_list_3[i][0]]

        value_1 = '1234567'
        value_2 = '7654321'
        name_list_left = []
        name_list_right = []
        name_list = []
        value = []

        for i in range(len(name_list_3)):
            if name_list_3[i][3] == 'ascending':
                value.append(value_1)
            else:
                value.append(value_2)
            name_list_left.append(name_list_3[i][1])
            name_list_right.append(name_list_3[i][2])
            name_list.append(name_list_3[i][0])

        self.participant.vars['left1'] = name_list_left[0]
        self.participant.vars['left2'] = name_list_left[1]
        self.participant.vars['left3'] = name_list_left[2]
        self.participant.vars['left4'] = name_list_left[3]
        self.participant.vars['left5'] = name_list_left[4]
        self.participant.vars['left6'] = name_list_left[5]

        self.participant.vars['right1'] = name_list_right[0]
        self.participant.vars['right2'] = name_list_right[1]
        self.participant.vars['right3'] = name_list_right[2]
        self.participant.vars['right4'] = name_list_right[3]
        self.participant.vars['right5'] = name_list_right[4]
        self.participant.vars['right6'] = name_list_right[5]

        self.participant.vars['name1'] = name_list[0]
        self.participant.vars['name2'] = name_list[1]
        self.participant.vars['name3'] = name_list[2]
        self.participant.vars['name4'] = name_list[3]
        self.participant.vars['name5'] = name_list[4]
        self.participant.vars['name6'] = name_list[5]

        self.participant.vars['value1'] = value[0]
        self.participant.vars['value2'] = value[1]
        self.participant.vars['value3'] = value[2]
        self.participant.vars['value4'] = value[3]
        self.participant.vars['value5'] = value[4]
        self.participant.vars['value6'] = value[5]

        self.participant.vars['name_list_left_7'] = name_list_left[6]
        self.participant.vars['name_list_right_7'] = name_list_right[6]
        self.participant.vars['name_7'] = name_list[6]
        self.participant.vars['value_7'] = value[6]
        self.participant.vars['name_list_left_8'] = name_list_left[7]
        self.participant.vars['name_list_right_8'] = name_list_right[7]
        self.participant.vars['name_8'] = name_list[7]
        self.participant.vars['value_8'] = value[7]
