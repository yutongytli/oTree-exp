from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ["gender","age","is_student","level","income"]

    def before_next_page(self): #any code is gona be executed before you go to next page
        self.participant.vars["is_student"]=self.player.is_student #we safe this on the participant :)

class Results(Page):
    pass

page_sequence = [
    MyPage,
    Results
]
