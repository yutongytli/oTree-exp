from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import Submission

class PlayerBot(Bot):

    def play_round(self):

        if self.player.treatment == 'Experimenter':
            yield Submission(views.Introduction_2, {'foo': 99}, timeout_happened=True)
            yield Submission(views.Decide_exp, {'foo': 99}, timeout_happened=True)
            yield Submission(views.Demographic, {'foo': 99}, timeout_happened=True)
            yield (views.Results_2)

        else:
            yield Submission(views.Introduction, {'foo': 99}, timeout_happened=True)
            yield Submission(views.Decide2, {'foo': 99}, timeout_happened=True)
            yield Submission(views.Belieff, {'foo': 99}, timeout_happened=True)
            yield Submission(views.Demographic, {'foo': 99}, timeout_happened=True)
            yield (views.Results)