from evennia_gamedir import app
from evennia_gamedir.api_resources.gamelisting.checkin import GameListingCheckIn
from flask_restful import Api

api = Api(app)

api.add_resource(GameListingCheckIn, '/api/v1/game/check_in')
