import os
from os import environ

import dj_database_url

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CHANNEL_ROUTING = 'participant_generated_urn_2.routing.channel_routing'

# ROOT_URLCONF = 'redirect.urls'

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
# if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
#     DEBUG = False
# else:
#     DEBUG = True

# OTREE_PRODUCTION = "1"

DEBUG = False

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# don't share this with anybody.
SECRET_KEY = '3i$avo!uk%txf%)y+$l29jy&b74=wuu@k%=m0$@(t3(*!k-ckx'

DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = [
    'otree',
    'otree_mturk_utils',
]

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
oTree games
"""

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    # to use qualification requirements, you need to uncomment the 'qualification' import
    # at the top of this file.
    'qualification_requirements': [],
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.000,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [
    # {
    #     'name': 'Eye_Exam',
    #     'display_name': 'Read Eyes in Mind Test',
    #     'num_demo_participants': 5,
    #     'app_sequence': ['Eye_Exam'],
    # },
    # {
    #     'name': 'REMT',
    #     'display_name': 'Read Eyes in Mind Test (with scrambled pic)',
    #     'num_demo_participants': 5,
    #     'app_sequence': ['REMT'],
    # },
    # {
    #     'name': 'Empathy',
    #     'display_name': 'Empathy Game w/o Timer',
    #     'num_demo_participants': 10,
    #     'app_sequence': ['Empathy_Beget_Guile'],
    # },
    # {
    #     'name': 'participant_generated_urn_1',
    #     'display_name': 'Participant Generate Urn Game w/o Timer',
    #     'num_demo_participants': 8,
    #     'app_sequence': ['participant_generated_urn_1'],
    # },
    # {
    #     'name': 'participant_generate_urn_2',
    #     'display_name': 'Participant Generate Urn Game w/ Timer',
    #     'num_demo_participants': 10,
    #     'app_sequence': ['participant_generated_urn_2'],
    # },
    # {
    #     'name': 'erase_old',
    #     'display_name': 'Who Cares - Mouse Eraser',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['erase_old'],
    # },
    # {
    #     'name': 'erase',
    #     'display_name': 'Who Cares - Mouse Spotlight',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['erase'],
    # },
    # {
    #     'name': 'pilot1',
    #     'display_name': 'Who Cares - Pilot 1',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['pilot2_1'],
    # },
    # {
    #     'name': 'pilot2',
    #     'display_name': 'Who Cares - Pilot 2',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['pilot2_2'],
    # },
    # {
    #     'name': 'envelope',
    #     'display_name': 'Testing Axiomatizations of Ambiguity Aversion',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['test_axiom'],
    # },
    # {
    #     'name': 'trolley',
    #     'display_name': 'Moral Trolley Problem',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['trolley'],
    # },
    # {
    #     'name': 'oral_argument',
    #     'display_name': 'Oral Argument',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['oral_argument'],
    # },
    # {
    #     'name': 'petition',
    #     'display_name': 'Who Cares - Petition',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['petition'],
    # },
    # {
    #     'name': 'donation',
    #     'display_name': 'Who Cares - Donations',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['donation'],
    # },
    # {
    #     'name': 'mouse_tracking',
    #     'display_name': 'Mouse Tracking',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['mouse_tracking'],
    # },
    # {
    #     'name': 'all_likert',
    #     'display_name': 'Who Cares - Likert Questions',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['all_likert'],
    # },
    # {
    #     'name': 'testall',
    #     'display_name': 'Iframe',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['testall'],
    # },
    # {
    #     'name': 'prisoner',
    #     'display_name': 'prisoner',
    #     'num_demo_participants': 10,
    #     'app_sequence': ['prisoner'],
    # },
    {
        'name': 'experiment',
        'display_name': 'experiment',
        'num_demo_participants': 10,
        'app_sequence': ['prisoner', 'mysurvey'],
    },

]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
