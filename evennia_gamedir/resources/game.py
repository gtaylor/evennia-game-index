from flask_restful import Resource, reqparse

from evennia_gamedir import models


post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'game_name', dest='game_name', location='form', required=True,
)
post_parser.add_argument(
    'game_status', dest='game_status', location='form', required=True,
    choices=['pre-alpha', 'alpha', 'beta', 'launched'],
)
post_parser.add_argument(
    'game_website', dest='game_website', location='form', required=False,
)
post_parser.add_argument(
    'listing_contact', dest='listing_contact', location='form', required=True,
)
post_parser.add_argument(
    'evennia_version', dest='evennia_version', location='form', required=True,
)
post_parser.add_argument(
    'telnet_hostname', dest='telnet_hostname',
    location='form', required=True,
)
post_parser.add_argument(
    'telnet_port', dest='telnet_port', type=int, location='form', required=True,
)
post_parser.add_argument(
    'connected_player_count', dest='connected_player_count', type=int,
    location='form', required=False,
)
post_parser.add_argument(
    'total_player_count', dest='total_player_count', type=int,
    location='form', required=False,
)


class GameCheckIn(Resource):

    def post(self):
        args = post_parser.parse_args()
        # If it exists, we'll end up with the existing list. If not,
        # it gets created.
        gl = models.GameListing.get_or_insert(args.game_name, **args)
        # Regardless of what we do, time to update it.
        for key, val in args.items():
            setattr(gl, key, val)
        # Bombs away!
        gl.put()
        return 'OK', 200
