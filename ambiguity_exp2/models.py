from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Yutong Li'

doc = """
This is the second experiment originated from
<a href="http://users.nber.org/~dlchen/papers/Testing_Axiomatizations_of_Ambiguity_Aversion.pdf" target="_blank">
    Daniel L. Chen and Martin Schonger (2016)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'ambiguity_exp2'
    players_per_group = 5
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.g = random.choice(['First Group', 'Second Group'])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.CharField(
        choices=['Alternative A', 'Alternative B'],
        doc="""Either Alternative A or Alternative B""",
        widget=widgets.RadioSelect()
    )
    g = models.CharField()
