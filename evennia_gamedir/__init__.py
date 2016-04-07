from flask import Flask


GCP_PROJECT_ID = 'evennia-game-directory'
app = Flask(__name__)


# This makes me queasy just looking at it, but it's considered the way to go
# for large Flask apps.
# http://flask.pocoo.org/docs/0.10/patterns/packages/#simple-packages
from evennia_gamedir import views  # noqa
from evennia_gamedir import api_resources  # noqa
from evennia_gamedir import errorhandlers  # noqa
