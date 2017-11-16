from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Yutong LI'

doc = """
The classical REMT
"""


class Constants(BaseConstants):
    name_in_url = 'Eye_Exam'
    players_per_group = None
    num_rounds = 1

    conditions = ['Empathy', 'Control', 'Guile']


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    def get_scores(self):

        def compute(player):
            answer = [player.option_1, player.option_2, player.option_3, player.option_4, player.option_5,
                      player.option_6, player.option_7, player.option_8, player.option_9, player.option_10,
                      player.option_11, player.option_12, player.option_13, player.option_14, player.option_15,
                      player.option_16, player.option_17, player.option_18, player.option_19, player.option_20,
                      player.option_21, player.option_22, player.option_23, player.option_24, player.option_25,
                      player.option_26, player.option_27, player.option_28, player.option_29, player.option_30,
                      player.option_31, player.option_32, player.option_33, player.option_34, player.option_35,
                      player.option_36]

            correction = ['Playful', 'Upset', 'Desire', 'Insisting', 'Worried', 'Fantasizing', 'Uneasy', 'Despondent',
                          'Preoccupied', 'Cautious', 'Regretful', 'Skeptical', 'Anticipating', 'Accusing',
                          'Contemplative', 'Thoughtful', 'Doubtful', 'Decisive', 'Tentative', 'Friendly', 'Fantasizing',
                          'Preoccupied', 'Defiant', 'Pensive', 'Interested', 'Hostile', 'Cautious', 'Interested',
                          'Reflective', 'Flirtatious', 'Confident', 'Serious', 'Concerned', 'Distrustful', 'Nervous',
                          'Suspicious']
            filtered = filter(lambda x: x[0] == x[1], zip(answer, correction))

            player.score = len(list(filtered))

            return player.score

        for p in self.get_players():
            p.score = compute(p)



class Player(BasePlayer):
    # Used to transcribe a paragraph
    text = models.TextField()

    # 36 eye expressions
    feeling1_response = models.CharField(
        choices=['Playful', 'Comforting', 'Irritated', 'Bored'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling2_response = models.CharField(
        choices=['Terrified', 'Upset', 'Arrogant', 'Annoyed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling3_response = models.CharField(
        choices=['Joking', 'Flustered', 'Desire', 'Convinced'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling4_response = models.CharField(
        choices=['Joking', 'Insisting', 'Amused', 'Relaxed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling5_response = models.CharField(
        choices=['Irritated', 'Sarcastic', 'Worried', 'Friendly'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling6_response = models.CharField(
        choices=['Aghast', 'Fantasizing', 'Impatient', 'Alarmed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling7_response = models.CharField(
        choices=['Apologetic', 'Friendly', 'Uneasy', 'Dispirited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling8_response = models.CharField(
        choices=['Despondent', 'Relieved', 'Shy', 'Excited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling9_response = models.CharField(
        choices=['Annoyed', 'Hostile', 'Horrified', 'Preoccupied'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling10_response = models.CharField(
        choices=['Cautious', 'Insisting', 'Bored', 'Aghast'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling11_response = models.CharField(
        choices=['Terrified', 'Amused', 'Regretful', 'Flirtatious'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling12_response = models.CharField(
        choices=['Indifferent', 'Embarrassed', 'Skeptical', 'Dispirited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling13_response = models.CharField(
        choices=['Decisive', 'Anticipating', 'Threatening', 'Shy'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling14_response = models.CharField(
        choices=['Irritated', 'Disappointed', 'Depressed', 'Accusing'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling15_response = models.CharField(
        choices=['Contemplative', 'Flustered', 'Encouraging', 'Amused'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling16_response = models.CharField(
        choices=['Irritated', 'Thoughtful', 'Encouraging', 'Sympathetic'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling17_response = models.CharField(
        choices=['Doubtful', 'Affectionate', 'Playful', 'Aghast'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling18_response = models.CharField(
        choices=['Decisive', 'Amused', 'Aghast', 'Bored'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling19_response = models.CharField(
        choices=['Arrogant', 'Grateful', 'Sarcastic', 'Tentative'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling20_response = models.CharField(
        choices=['Dominant', 'Friendly', 'Guilty', 'Horrified'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling21_response = models.CharField(
        choices=['Embarrassed', 'Fantasizing', 'Confused', 'Panicked'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling22_response = models.CharField(
        choices=['Preoccupied', 'Grateful', 'Insisting', 'Imploring'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling23_response = models.CharField(
        choices=['Contented', 'Apologetic', 'Defiant', 'Curious'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling24_response = models.CharField(
        choices=['Pensive', 'Irritated', 'Excited', 'Hostile'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling25_response = models.CharField(
        choices=['Panicked', 'Incredulous', 'Despondent', 'Interested'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling26_response = models.CharField(
        choices=['Alarmed', 'Shy', 'Hostile', 'Anxious'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling27_response = models.CharField(
        choices=['Joking', 'Cautious', 'Arrogant', 'Reassuring'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling28_response = models.CharField(
        choices=['Interested', 'Joking', 'Affectionate', 'Contented'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling29_response = models.CharField(
        choices=['Impatient', 'Aghast', 'Irritated', 'Reflective'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling30_response = models.CharField(
        choices=['Grateful', 'Flirtatious', 'Hostile', 'Disappointed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling31_response = models.CharField(
        choices=['Ashamed', 'Confident', 'Joking', 'Dispirited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling32_response = models.CharField(
        choices=['Serious', 'Ashamed', 'Bewildered', 'Alarmed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling33_response = models.CharField(
        choices=['Embarrassed', 'Guilty', 'Fantasizing', 'Concerned'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling34_response = models.CharField(
        choices=['Aghast', 'Baffled', 'Distrustful', 'Terrified'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling35_response = models.CharField(
        choices=['Puzzled', 'Nervous', 'Insisting', 'Contemplative'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling36_response = models.CharField(
        choices=['Ashamed', 'Nervous', 'Suspicious', 'Indecisive'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    # Priming paragraph
    priming = models.CharField()

    # Computing eye scores
    score = models.IntegerField()

    def get_scores(self):
        answer = [self.feeling1_response, self.feeling2_response, self.feeling3_response,
                  self.feeling4_response, self.feeling5_response,
                  self.feeling6_response, self.feeling7_response, self.feeling8_response,
                  self.feeling9_response, self.feeling10_response,
                  self.feeling11_response, self.feeling12_response, self.feeling13_response,
                  self.feeling14_response, self.feeling15_response,
                  self.feeling16_response, self.feeling17_response, self.feeling18_response,
                  self.feeling19_response, self.feeling20_response,
                  self.feeling21_response, self.feeling22_response, self.feeling23_response,
                  self.feeling24_response, self.feeling25_response,
                  self.feeling26_response, self.feeling27_response, self.feeling28_response,
                  self.feeling29_response, self.feeling30_response,
                  self.feeling31_response, self.feeling32_response, self.feeling33_response,
                  self.feeling34_response, self.feeling35_response,
                  self.feeling36_response]

        correction = ['Playful', 'Upset', 'Desire', 'Insisting', 'Worried', 'Fantasizing', 'Uneasy', 'Despondent',
                      'Preoccupied', 'Cautious', 'Regretful', 'Skeptical', 'Anticipating', 'Accusing',
                      'Contemplative', 'Thoughtful', 'Doubtful', 'Decisive', 'Tentative', 'Friendly', 'Fantasizing',
                      'Preoccupied', 'Defiant', 'Pensive', 'Interested', 'Hostile', 'Cautious', 'Interested',
                      'Reflective', 'Flirtatious', 'Confident', 'Serious', 'Concerned', 'Distrustful', 'Nervous',
                      'Suspicious']
        filtered = filter(lambda x: x[0] == x[1], zip(answer, correction))

        self.score = len(list(filtered))




