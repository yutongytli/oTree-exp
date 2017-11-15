from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Yutong Li'

doc = """
This is the first experiment originated from
<a href="http://users.nber.org/~dlchen/papers/Testing_Axiomatizations_of_Ambiguity_Aversion.pdf" target="_blank">
    Daniel L. Chen and Martin Schonger (2016)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'ambiguity_exp1'
    players_per_group = 2
    num_rounds = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    decision = models.CharField(
        choices=['Lottery A', 'Lottery B'],
        doc="""Either Lottery A or Lottery B""",
        widget=widgets.RadioSelect()
    )
