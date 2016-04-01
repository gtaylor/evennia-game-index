from flask_restful import Resource, reqparse


post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'game_name', dest='game_name', location='form', required=True,
    help='The game\'s name',
)
post_parser.add_argument(
    'game_status', dest='game_status', location='form', required=True,
    choices=['pre-alpha', 'alpha', 'beta', 'launched'],
    help='The game\'s development status',
)
post_parser.add_argument(
    'game_website', dest='game_website', location='form', required=False,
    help='The game\'s website',
)
post_parser.add_argument(
    'telnet_hostname', dest='server_hostname',
    location='form', required=True,
    help='The hostname where users can telnet into the game',
)
post_parser.add_argument(
    'telnet_port', dest='telnet_port', type=int, location='form', required=True,
    help='The port where users can telnet into the game',
)
post_parser.add_argument(
    'connected_player_count', dest='connected_player_count', type=int,
    location='form', required=False,
    help='Total number of connected players',
)
post_parser.add_argument(
    'total_player_count', dest='total_player_count', type=int,
    location='form', required=False,
    help='Total number of players',
)


class GameCheckIn(Resource):

    def post(self):
        args = post_parser.parse_args()
        print "ARGS", args
        return {'hello': 'world'}
