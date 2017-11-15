from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import os
import requests

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'covering'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    audio_group = models.CharField()

    attractive_1 = models.CharField()
    attractive_2 = models.CharField()
    attractive_3 = models.CharField()
    attractive_4 = models.CharField()
    attractive_5 = models.CharField()
    attractive_6 = models.CharField()
    attractive_7 = models.CharField()
    attractive_8 = models.CharField()
    attractive_9 = models.CharField()
    attractive_10 = models.CharField()
    attractive_11 = models.CharField()
    attractive_12 = models.CharField()
    attractive_13 = models.CharField()
    attractive_14 = models.CharField()
    attractive_15 = models.CharField()
    attractive_16 = models.CharField()
    attractive_17 = models.CharField()
    attractive_18 = models.CharField()
    attractive_19 = models.CharField()
    attractive_20 = models.CharField()
    attractive_21 = models.CharField()
    attractive_22 = models.CharField()
    attractive_23 = models.CharField()
    attractive_24 = models.CharField()
    attractive_25 = models.CharField()
    attractive_26 = models.CharField()
    attractive_27 = models.CharField()
    attractive_28 = models.CharField()
    attractive_29 = models.CharField()
    attractive_30 = models.CharField()
    attractive_31 = models.CharField()
    attractive_32 = models.CharField()
    attractive_33 = models.CharField()
    attractive_34 = models.CharField()
    attractive_35 = models.CharField()
    attractive_36 = models.CharField()
    attractive_37 = models.CharField()
    attractive_38 = models.CharField()
    attractive_39 = models.CharField()
    attractive_40 = models.CharField()
    attractive_41 = models.CharField()
    attractive_42 = models.CharField()
    attractive_43 = models.CharField()
    attractive_44 = models.CharField()
    attractive_45 = models.CharField()
    attractive_46 = models.CharField()
    attractive_47 = models.CharField()
    attractive_48 = models.CharField()
    attractive_49 = models.CharField()
    attractive_50 = models.CharField()
    attractive_51 = models.CharField()
    attractive_52 = models.CharField()
    attractive_53 = models.CharField()
    attractive_54 = models.CharField()
    attractive_55 = models.CharField()
    attractive_56 = models.CharField()
    attractive_57 = models.CharField()
    attractive_58 = models.CharField()
    attractive_59 = models.CharField()
    attractive_60 = models.CharField()
    attractive_61 = models.CharField()
    attractive_62 = models.CharField()
    attractive_63 = models.CharField()
    attractive_64 = models.CharField()
    attractive_65 = models.CharField()
    attractive_66 = models.CharField()

    masculine_1 = models.CharField()
    masculine_2 = models.CharField()
    masculine_3 = models.CharField()
    masculine_4 = models.CharField()
    masculine_5 = models.CharField()
    masculine_6 = models.CharField()
    masculine_7 = models.CharField()
    masculine_8 = models.CharField()
    masculine_9 = models.CharField()
    masculine_10 = models.CharField()
    masculine_11 = models.CharField()
    masculine_12 = models.CharField()
    masculine_13 = models.CharField()
    masculine_14 = models.CharField()
    masculine_15 = models.CharField()
    masculine_16 = models.CharField()
    masculine_17 = models.CharField()
    masculine_18 = models.CharField()
    masculine_19 = models.CharField()
    masculine_20 = models.CharField()
    masculine_21 = models.CharField()
    masculine_22 = models.CharField()
    masculine_23 = models.CharField()
    masculine_24 = models.CharField()
    masculine_25 = models.CharField()
    masculine_26 = models.CharField()
    masculine_27 = models.CharField()
    masculine_28 = models.CharField()
    masculine_29 = models.CharField()
    masculine_30 = models.CharField()
    masculine_31 = models.CharField()
    masculine_32 = models.CharField()
    masculine_33 = models.CharField()
    masculine_34 = models.CharField()
    masculine_35 = models.CharField()
    masculine_36 = models.CharField()
    masculine_37 = models.CharField()
    masculine_38 = models.CharField()
    masculine_39 = models.CharField()
    masculine_40 = models.CharField()
    masculine_41 = models.CharField()
    masculine_42 = models.CharField()
    masculine_43 = models.CharField()
    masculine_44 = models.CharField()
    masculine_45 = models.CharField()
    masculine_46 = models.CharField()
    masculine_47 = models.CharField()
    masculine_48 = models.CharField()
    masculine_49 = models.CharField()
    masculine_50 = models.CharField()
    masculine_51 = models.CharField()
    masculine_52 = models.CharField()
    masculine_53 = models.CharField()
    masculine_54 = models.CharField()
    masculine_55 = models.CharField()
    masculine_56 = models.CharField()
    masculine_57 = models.CharField()
    masculine_58 = models.CharField()
    masculine_59 = models.CharField()
    masculine_60 = models.CharField()
    masculine_61 = models.CharField()
    masculine_62 = models.CharField()
    masculine_63 = models.CharField()
    masculine_64 = models.CharField()
    masculine_65 = models.CharField()
    masculine_66 = models.CharField()

    intelligent_1 = models.CharField()
    intelligent_2 = models.CharField()
    intelligent_3 = models.CharField()
    intelligent_4 = models.CharField()
    intelligent_5 = models.CharField()
    intelligent_6 = models.CharField()
    intelligent_7 = models.CharField()
    intelligent_8 = models.CharField()
    intelligent_9 = models.CharField()
    intelligent_10 = models.CharField()
    intelligent_11 = models.CharField()
    intelligent_12 = models.CharField()
    intelligent_13 = models.CharField()
    intelligent_14 = models.CharField()
    intelligent_15 = models.CharField()
    intelligent_16 = models.CharField()
    intelligent_17 = models.CharField()
    intelligent_18 = models.CharField()
    intelligent_19 = models.CharField()
    intelligent_20 = models.CharField()
    intelligent_21 = models.CharField()
    intelligent_22 = models.CharField()
    intelligent_23 = models.CharField()
    intelligent_24 = models.CharField()
    intelligent_25 = models.CharField()
    intelligent_26 = models.CharField()
    intelligent_27 = models.CharField()
    intelligent_28 = models.CharField()
    intelligent_29 = models.CharField()
    intelligent_30 = models.CharField()
    intelligent_31 = models.CharField()
    intelligent_32 = models.CharField()
    intelligent_33 = models.CharField()
    intelligent_34 = models.CharField()
    intelligent_35 = models.CharField()
    intelligent_36 = models.CharField()
    intelligent_37 = models.CharField()
    intelligent_38 = models.CharField()
    intelligent_39 = models.CharField()
    intelligent_40 = models.CharField()
    intelligent_41 = models.CharField()
    intelligent_42 = models.CharField()
    intelligent_43 = models.CharField()
    intelligent_44 = models.CharField()
    intelligent_45 = models.CharField()
    intelligent_46 = models.CharField()
    intelligent_47 = models.CharField()
    intelligent_48 = models.CharField()
    intelligent_49 = models.CharField()
    intelligent_50 = models.CharField()
    intelligent_51 = models.CharField()
    intelligent_52 = models.CharField()
    intelligent_53 = models.CharField()
    intelligent_54 = models.CharField()
    intelligent_55 = models.CharField()
    intelligent_56 = models.CharField()
    intelligent_57 = models.CharField()
    intelligent_58 = models.CharField()
    intelligent_59 = models.CharField()
    intelligent_60 = models.CharField()
    intelligent_61 = models.CharField()
    intelligent_62 = models.CharField()
    intelligent_63 = models.CharField()
    intelligent_64 = models.CharField()
    intelligent_65 = models.CharField()
    intelligent_66 = models.CharField()

    aggressive_1 = models.CharField()
    aggressive_2 = models.CharField()
    aggressive_3 = models.CharField()
    aggressive_4 = models.CharField()
    aggressive_5 = models.CharField()
    aggressive_6 = models.CharField()
    aggressive_7 = models.CharField()
    aggressive_8 = models.CharField()
    aggressive_9 = models.CharField()
    aggressive_10 = models.CharField()
    aggressive_11 = models.CharField()
    aggressive_12 = models.CharField()
    aggressive_13 = models.CharField()
    aggressive_14 = models.CharField()
    aggressive_15 = models.CharField()
    aggressive_16 = models.CharField()
    aggressive_17 = models.CharField()
    aggressive_18 = models.CharField()
    aggressive_19 = models.CharField()
    aggressive_20 = models.CharField()
    aggressive_21 = models.CharField()
    aggressive_22 = models.CharField()
    aggressive_23 = models.CharField()
    aggressive_24 = models.CharField()
    aggressive_25 = models.CharField()
    aggressive_26 = models.CharField()
    aggressive_27 = models.CharField()
    aggressive_28 = models.CharField()
    aggressive_29 = models.CharField()
    aggressive_30 = models.CharField()
    aggressive_31 = models.CharField()
    aggressive_32 = models.CharField()
    aggressive_33 = models.CharField()
    aggressive_34 = models.CharField()
    aggressive_35 = models.CharField()
    aggressive_36 = models.CharField()
    aggressive_37 = models.CharField()
    aggressive_38 = models.CharField()
    aggressive_39 = models.CharField()
    aggressive_40 = models.CharField()
    aggressive_41 = models.CharField()
    aggressive_42 = models.CharField()
    aggressive_43 = models.CharField()
    aggressive_44 = models.CharField()
    aggressive_45 = models.CharField()
    aggressive_46 = models.CharField()
    aggressive_47 = models.CharField()
    aggressive_48 = models.CharField()
    aggressive_49 = models.CharField()
    aggressive_50 = models.CharField()
    aggressive_51 = models.CharField()
    aggressive_52 = models.CharField()
    aggressive_53 = models.CharField()
    aggressive_54 = models.CharField()
    aggressive_55 = models.CharField()
    aggressive_56 = models.CharField()
    aggressive_57 = models.CharField()
    aggressive_58 = models.CharField()
    aggressive_59 = models.CharField()
    aggressive_60 = models.CharField()
    aggressive_61 = models.CharField()
    aggressive_62 = models.CharField()
    aggressive_63 = models.CharField()
    aggressive_64 = models.CharField()
    aggressive_65 = models.CharField()
    aggressive_66 = models.CharField()

    trustworthy_1 = models.CharField()
    trustworthy_2 = models.CharField()
    trustworthy_3 = models.CharField()
    trustworthy_4 = models.CharField()
    trustworthy_5 = models.CharField()
    trustworthy_6 = models.CharField()
    trustworthy_7 = models.CharField()
    trustworthy_8 = models.CharField()
    trustworthy_9 = models.CharField()
    trustworthy_10 = models.CharField()
    trustworthy_11 = models.CharField()
    trustworthy_12 = models.CharField()
    trustworthy_13 = models.CharField()
    trustworthy_14 = models.CharField()
    trustworthy_15 = models.CharField()
    trustworthy_16 = models.CharField()
    trustworthy_17 = models.CharField()
    trustworthy_18 = models.CharField()
    trustworthy_19 = models.CharField()
    trustworthy_20 = models.CharField()
    trustworthy_21 = models.CharField()
    trustworthy_22 = models.CharField()
    trustworthy_23 = models.CharField()
    trustworthy_24 = models.CharField()
    trustworthy_25 = models.CharField()
    trustworthy_26 = models.CharField()
    trustworthy_27 = models.CharField()
    trustworthy_28 = models.CharField()
    trustworthy_29 = models.CharField()
    trustworthy_30 = models.CharField()
    trustworthy_31 = models.CharField()
    trustworthy_32 = models.CharField()
    trustworthy_33 = models.CharField()
    trustworthy_34 = models.CharField()
    trustworthy_35 = models.CharField()
    trustworthy_36 = models.CharField()
    trustworthy_37 = models.CharField()
    trustworthy_38 = models.CharField()
    trustworthy_39 = models.CharField()
    trustworthy_40 = models.CharField()
    trustworthy_41 = models.CharField()
    trustworthy_42 = models.CharField()
    trustworthy_43 = models.CharField()
    trustworthy_44 = models.CharField()
    trustworthy_45 = models.CharField()
    trustworthy_46 = models.CharField()
    trustworthy_47 = models.CharField()
    trustworthy_48 = models.CharField()
    trustworthy_49 = models.CharField()
    trustworthy_50 = models.CharField()
    trustworthy_51 = models.CharField()
    trustworthy_52 = models.CharField()
    trustworthy_53 = models.CharField()
    trustworthy_54 = models.CharField()
    trustworthy_55 = models.CharField()
    trustworthy_56 = models.CharField()
    trustworthy_57 = models.CharField()
    trustworthy_58 = models.CharField()
    trustworthy_59 = models.CharField()
    trustworthy_60 = models.CharField()
    trustworthy_61 = models.CharField()
    trustworthy_62 = models.CharField()
    trustworthy_63 = models.CharField()
    trustworthy_64 = models.CharField()
    trustworthy_65 = models.CharField()
    trustworthy_66 = models.CharField()

    confident_1 = models.CharField()
    confident_2 = models.CharField()
    confident_3 = models.CharField()
    confident_4 = models.CharField()
    confident_5 = models.CharField()
    confident_6 = models.CharField()
    confident_7 = models.CharField()
    confident_8 = models.CharField()
    confident_9 = models.CharField()
    confident_10 = models.CharField()
    confident_11 = models.CharField()
    confident_12 = models.CharField()
    confident_13 = models.CharField()
    confident_14 = models.CharField()
    confident_15 = models.CharField()
    confident_16 = models.CharField()
    confident_17 = models.CharField()
    confident_18 = models.CharField()
    confident_19 = models.CharField()
    confident_20 = models.CharField()
    confident_21 = models.CharField()
    confident_22 = models.CharField()
    confident_23 = models.CharField()
    confident_24 = models.CharField()
    confident_25 = models.CharField()
    confident_26 = models.CharField()
    confident_27 = models.CharField()
    confident_28 = models.CharField()
    confident_29 = models.CharField()
    confident_30 = models.CharField()
    confident_31 = models.CharField()
    confident_32 = models.CharField()
    confident_33 = models.CharField()
    confident_34 = models.CharField()
    confident_35 = models.CharField()
    confident_36 = models.CharField()
    confident_37 = models.CharField()
    confident_38 = models.CharField()
    confident_39 = models.CharField()
    confident_40 = models.CharField()
    confident_41 = models.CharField()
    confident_42 = models.CharField()
    confident_43 = models.CharField()
    confident_44 = models.CharField()
    confident_45 = models.CharField()
    confident_46 = models.CharField()
    confident_47 = models.CharField()
    confident_48 = models.CharField()
    confident_49 = models.CharField()
    confident_50 = models.CharField()
    confident_51 = models.CharField()
    confident_52 = models.CharField()
    confident_53 = models.CharField()
    confident_54 = models.CharField()
    confident_55 = models.CharField()
    confident_56 = models.CharField()
    confident_57 = models.CharField()
    confident_58 = models.CharField()
    confident_59 = models.CharField()
    confident_60 = models.CharField()
    confident_61 = models.CharField()
    confident_62 = models.CharField()
    confident_63 = models.CharField()
    confident_64 = models.CharField()
    confident_65 = models.CharField()
    confident_66 = models.CharField()

    win_1 = models.CharField()
    win_2 = models.CharField()
    win_3 = models.CharField()
    win_4 = models.CharField()
    win_5 = models.CharField()
    win_6 = models.CharField()
    win_7 = models.CharField()
    win_8 = models.CharField()
    win_9 = models.CharField()
    win_10 = models.CharField()
    win_11 = models.CharField()
    win_12 = models.CharField()
    win_13 = models.CharField()
    win_14 = models.CharField()
    win_15 = models.CharField()
    win_16 = models.CharField()
    win_17 = models.CharField()
    win_18 = models.CharField()
    win_19 = models.CharField()
    win_20 = models.CharField()
    win_21 = models.CharField()
    win_22 = models.CharField()
    win_23 = models.CharField()
    win_24 = models.CharField()
    win_25 = models.CharField()
    win_26 = models.CharField()
    win_27 = models.CharField()
    win_28 = models.CharField()
    win_29 = models.CharField()
    win_30 = models.CharField()
    win_31 = models.CharField()
    win_32 = models.CharField()
    win_33 = models.CharField()
    win_34 = models.CharField()
    win_35 = models.CharField()
    win_36 = models.CharField()
    win_37 = models.CharField()
    win_38 = models.CharField()
    win_39 = models.CharField()
    win_40 = models.CharField()
    win_41 = models.CharField()
    win_42 = models.CharField()
    win_43 = models.CharField()
    win_44 = models.CharField()
    win_45 = models.CharField()
    win_46 = models.CharField()
    win_47 = models.CharField()
    win_48 = models.CharField()
    win_49 = models.CharField()
    win_50 = models.CharField()
    win_51 = models.CharField()
    win_52 = models.CharField()
    win_53 = models.CharField()
    win_54 = models.CharField()
    win_55 = models.CharField()
    win_56 = models.CharField()
    win_57 = models.CharField()
    win_58 = models.CharField()
    win_59 = models.CharField()
    win_60 = models.CharField()
    win_61 = models.CharField()
    win_62 = models.CharField()
    win_63 = models.CharField()
    win_64 = models.CharField()
    win_65 = models.CharField()
    win_66 = models.CharField()

    quality_1 = models.CharField()
    quality_2 = models.CharField()
    quality_3 = models.CharField()
    quality_4 = models.CharField()
    quality_5 = models.CharField()
    quality_6 = models.CharField()
    quality_7 = models.CharField()
    quality_8 = models.CharField()
    quality_9 = models.CharField()
    quality_10 = models.CharField()
    quality_11 = models.CharField()
    quality_12 = models.CharField()
    quality_13 = models.CharField()
    quality_14 = models.CharField()
    quality_15 = models.CharField()
    quality_16 = models.CharField()
    quality_17 = models.CharField()
    quality_18 = models.CharField()
    quality_19 = models.CharField()
    quality_20 = models.CharField()
    quality_21 = models.CharField()
    quality_22 = models.CharField()
    quality_23 = models.CharField()
    quality_24 = models.CharField()
    quality_25 = models.CharField()
    quality_26 = models.CharField()
    quality_27 = models.CharField()
    quality_28 = models.CharField()
    quality_29 = models.CharField()
    quality_30 = models.CharField()
    quality_31 = models.CharField()
    quality_32 = models.CharField()
    quality_33 = models.CharField()
    quality_34 = models.CharField()
    quality_35 = models.CharField()
    quality_36 = models.CharField()
    quality_37 = models.CharField()
    quality_38 = models.CharField()
    quality_39 = models.CharField()
    quality_40 = models.CharField()
    quality_41 = models.CharField()
    quality_42 = models.CharField()
    quality_43 = models.CharField()
    quality_44 = models.CharField()
    quality_45 = models.CharField()
    quality_46 = models.CharField()
    quality_47 = models.CharField()
    quality_48 = models.CharField()
    quality_49 = models.CharField()
    quality_50 = models.CharField()
    quality_51 = models.CharField()
    quality_52 = models.CharField()
    quality_53 = models.CharField()
    quality_54 = models.CharField()
    quality_55 = models.CharField()
    quality_56 = models.CharField()
    quality_57 = models.CharField()
    quality_58 = models.CharField()
    quality_59 = models.CharField()
    quality_60 = models.CharField()
    quality_61 = models.CharField()
    quality_62 = models.CharField()
    quality_63 = models.CharField()
    quality_64 = models.CharField()
    quality_65 = models.CharField()
    quality_66 = models.CharField()

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
        choices=['Female', 'Male', 'Other'],
        doc="""Please choose one of the choices""",
    )

    race = models.CharField(
        choices=['Female', 'Male', 'Other'],
        doc="""Please choose one of the choices""",
    )

    income = models.IntegerField(
        choices=[0, 1],
        doc="""Please choose one of the choices""",
    )

    audio_for_player_1 = models.CharField()
    audio_for_player_2 = models.CharField()
    audio_for_player_3 = models.CharField()
    audio_for_player_4 = models.CharField()
    audio_for_player_5 = models.CharField()
    audio_for_player_6 = models.CharField()
    audio_for_player_7 = models.CharField()
    audio_for_player_8 = models.CharField()
    audio_for_player_9 = models.CharField()
    audio_for_player_10 = models.CharField()
    audio_for_player_11 = models.CharField()
    audio_for_player_12 = models.CharField()
    audio_for_player_13 = models.CharField()
    audio_for_player_14 = models.CharField()
    audio_for_player_15 = models.CharField()
    audio_for_player_16 = models.CharField()
    audio_for_player_17 = models.CharField()
    audio_for_player_18 = models.CharField()
    audio_for_player_19 = models.CharField()
    audio_for_player_20 = models.CharField()
    audio_for_player_21 = models.CharField()
    audio_for_player_22 = models.CharField()
    audio_for_player_23 = models.CharField()
    audio_for_player_24 = models.CharField()
    audio_for_player_25 = models.CharField()
    audio_for_player_26 = models.CharField()
    audio_for_player_27 = models.CharField()
    audio_for_player_28 = models.CharField()
    audio_for_player_29 = models.CharField()
    audio_for_player_30 = models.CharField()
    audio_for_player_31 = models.CharField()
    audio_for_player_32 = models.CharField()
    audio_for_player_33 = models.CharField()
    audio_for_player_34 = models.CharField()
    audio_for_player_35 = models.CharField()
    audio_for_player_36 = models.CharField()
    audio_for_player_37 = models.CharField()
    audio_for_player_38 = models.CharField()
    audio_for_player_39 = models.CharField()
    audio_for_player_40 = models.CharField()
    audio_for_player_41 = models.CharField()
    audio_for_player_42 = models.CharField()
    audio_for_player_43 = models.CharField()
    audio_for_player_44 = models.CharField()
    audio_for_player_45 = models.CharField()
    audio_for_player_46 = models.CharField()
    audio_for_player_47 = models.CharField()
    audio_for_player_48 = models.CharField()
    audio_for_player_49 = models.CharField()
    audio_for_player_50 = models.CharField()
    audio_for_player_51 = models.CharField()
    audio_for_player_52 = models.CharField()
    audio_for_player_53 = models.CharField()
    audio_for_player_54 = models.CharField()
    audio_for_player_55 = models.CharField()
    audio_for_player_56 = models.CharField()
    audio_for_player_57 = models.CharField()
    audio_for_player_58 = models.CharField()
    audio_for_player_59 = models.CharField()
    audio_for_player_60 = models.CharField()
    audio_for_player_61 = models.CharField()
    audio_for_player_62 = models.CharField()
    audio_for_player_63 = models.CharField()
    audio_for_player_64 = models.CharField()
    audio_for_player_65 = models.CharField()
    audio_for_player_66 = models.CharField()

    left_1 = models.CharField()
    left_2 = models.CharField()
    left_3 = models.CharField()
    left_4 = models.CharField()
    left_5 = models.CharField()
    left_6 = models.CharField()

    right_1 = models.CharField()
    right_2 = models.CharField()
    right_3 = models.CharField()
    right_4 = models.CharField()
    right_5 = models.CharField()
    right_6 = models.CharField()

    name_1 = models.CharField()
    name_2 = models.CharField()
    name_3 = models.CharField()
    name_4 = models.CharField()
    name_5 = models.CharField()
    name_6 = models.CharField()

    value_1 = models.CharField()
    value_2 = models.CharField()
    value_3 = models.CharField()
    value_4 = models.CharField()
    value_5 = models.CharField()
    value_6 = models.CharField()

    name_list_left_7 = models.CharField()
    name_list_right_7 = models.CharField()
    name_7 = models.CharField()
    value_7 = models.CharField()
    name_list_left_8 = models.CharField()
    name_list_right_8 = models.CharField()
    name_8 = models.CharField()
    value_8 = models.CharField()

    def get_audio_group(self):
        self.audio_group = random.choice(['female', 'male'])


    def get_audios(self):
        # if self.audio_group == 'male':
        #     path = "/Users/Nicole/Documents/oTree/covering_test/static/covering_test/male"  # insert the path to your directory
        # else:
        #     path = "/Users/Nicole/Documents/oTree/covering_test/static/covering_test/female"

        if self.audio_group == 'male':
            path = '/Users/Nicole/Documents/oTree/covering_test/static/covering_test/female'
        else:
            path = '/Users/Nicole/Documents/oTree/covering_test/static/covering_test/female'

        collection = os.listdir(path)
        selected = set()  # the set don't allow repetition

        while len(selected) <= 66:
            selected.add(random.choice(collection))

        temp_1 = list(selected)
        temp = []

        for i in range(len(temp_1)):
            if self.group == 'male':
                temp.append('male/'+temp_1[i])
            else:
                temp.append('female/' + temp_1[i])
        #
        # temp = list(selected)

        self.audio_for_player_1 = temp[0]
        self.audio_for_player_2 = temp[1]
        self.audio_for_player_3 = temp[2]
        self.audio_for_player_4 = temp[3]
        self.audio_for_player_5 = temp[4]
        self.audio_for_player_6 = temp[5]
        self.audio_for_player_7 = temp[6]
        self.audio_for_player_8 = temp[7]
        self.audio_for_player_9 = temp[8]
        self.audio_for_player_10 = temp[9]
        self.audio_for_player_11 = temp[10]
        self.audio_for_player_12 = temp[11]
        self.audio_for_player_13 = temp[12]
        self.audio_for_player_14 = temp[13]
        self.audio_for_player_15 = temp[14]
        self.audio_for_player_16 = temp[15]
        self.audio_for_player_17 = temp[16]
        self.audio_for_player_18 = temp[17]
        self.audio_for_player_19 = temp[18]
        self.audio_for_player_20 = temp[19]
        self.audio_for_player_21 = temp[20]
        self.audio_for_player_22 = temp[21]
        self.audio_for_player_23 = temp[22]
        self.audio_for_player_24 = temp[23]
        self.audio_for_player_25 = temp[24]
        self.audio_for_player_26 = temp[25]
        self.audio_for_player_27 = temp[26]
        self.audio_for_player_28 = temp[27]
        self.audio_for_player_29 = temp[28]
        self.audio_for_player_30 = temp[29]
        self.audio_for_player_31 = temp[30]
        self.audio_for_player_32 = temp[31]
        self.audio_for_player_33 = temp[32]
        self.audio_for_player_34 = temp[33]
        self.audio_for_player_35 = temp[34]
        self.audio_for_player_36 = temp[35]
        self.audio_for_player_37 = temp[36]
        self.audio_for_player_38 = temp[37]
        self.audio_for_player_39 = temp[38]
        self.audio_for_player_40 = temp[39]
        self.audio_for_player_41 = temp[40]
        self.audio_for_player_42 = temp[41]
        self.audio_for_player_43 = temp[42]
        self.audio_for_player_44 = temp[43]
        self.audio_for_player_45 = temp[44]
        self.audio_for_player_46 = temp[45]
        self.audio_for_player_47 = temp[46]
        self.audio_for_player_48 = temp[47]
        self.audio_for_player_49 = temp[48]
        self.audio_for_player_50 = temp[49]
        self.audio_for_player_51 = temp[50]
        self.audio_for_player_52 = temp[51]
        self.audio_for_player_53 = temp[52]
        self.audio_for_player_54 = temp[53]
        self.audio_for_player_55 = temp[54]
        self.audio_for_player_56 = temp[55]
        self.audio_for_player_57 = temp[56]
        self.audio_for_player_58 = temp[57]
        self.audio_for_player_59 = temp[58]
        self.audio_for_player_60 = temp[59]
        self.audio_for_player_61 = temp[60]
        self.audio_for_player_62 = temp[61]
        self.audio_for_player_63 = temp[62]
        self.audio_for_player_64 = temp[63]
        self.audio_for_player_65 = temp[64]
        self.audio_for_player_66 = temp[65]



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

        self.left_1 = name_list_left[0]
        self.left_2 = name_list_left[1]
        self.left_3 = name_list_left[2]
        self.left_4 = name_list_left[3]
        self.left_5 = name_list_left[4]
        self.left_6 = name_list_left[5]

        self.right_1 = name_list_right[0]
        self.right_2 = name_list_right[1]
        self.right_3 = name_list_right[2]
        self.right_4 = name_list_right[3]
        self.right_5 = name_list_right[4]
        self.right_6 = name_list_right[5]

        self.name_1 = name_list[0]
        self.name_2 = name_list[1]
        self.name_3 = name_list[2]
        self.name_4 = name_list[3]
        self.name_5 = name_list[4]
        self.name_6 = name_list[5]

        self.value_1 = value[0]
        self.value_2 = value[1]
        self.value_3 = value[2]
        self.value_4 = value[3]
        self.value_5 = value[4]
        self.value_6 = value[5]

        self.name_list_left_7 = name_list_left[6]
        self.name_list_right_7 = name_list_right[6]
        self.name_7 = name_list[6]
        self.value_7 = value[6]
        self.name_list_left_8 = name_list_left[7]
        self.name_list_right_8 = name_list_right[7]
        self.name_8 = name_list[7]
        self.value_8 = value[7]
