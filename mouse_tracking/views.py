from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

from otree.api import safe_json

class TrackMouse(Page):
    form_model = models.Player
    form_fields = ['mouse_x', 'mouse_y', 'mouse_t']

class Results(Page):
    def vars_for_template(self):
        mouse_x = self.player.mouse_x.split(",")
        mouse_y = self.player.mouse_y.split(",")

        mouse_x = list(map(int, mouse_x))
        mouse_y = list(map(int, mouse_y))

        mouse_y = [max(mouse_y) - x for x in mouse_y]

        data = []

        for i, j in zip(mouse_x, mouse_y):
            data.append([i, j])

        series = [{'name': 'Coordinate', 'data': data}]

        return {
            'series': safe_json(series)
        }

page_sequence = [
    TrackMouse,
    Results
]
