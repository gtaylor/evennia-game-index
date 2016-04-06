from flask_restful import Api

from evennia_gamedir import app
from evennia_gamedir.api import resources
from evennia_gamedir.api.resources.gamelisting import GameListingCheckIn

api = Api(app)

api.add_resource(GameListingCheckIn, '/api/v1/game/check_in')
