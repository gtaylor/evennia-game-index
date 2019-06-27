"""
Checkin resource that allows games to send us their deets.
"""
from slugify import slugify
from flask_restful import Resource, reqparse, abort

from egi import models
from egi.api_resources.validators import markdown_str, \
    game_short_description

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
    'short_description', dest='short_description', location='form',
    required=True, type=game_short_description,
)
post_parser.add_argument(
    'long_description', dest='long_description', location='form', required=False,
    type=markdown_str,
)


post_parser.add_argument(
    'telnet_hostname', dest='telnet_hostname',
    location='form', required=False,
)
post_parser.add_argument(
    'telnet_port', dest='telnet_port', location='form',
    required=False,
)
post_parser.add_argument(
    'web_client_url', dest='web_client_url',
    location='form', required=False,
)

post_parser.add_argument(
    'connected_account_count', dest='connected_account_count', type=int,
    location='form', required=False,
)
post_parser.add_argument(
    'total_account_count', dest='total_account_count', type=int,
    location='form', required=False,
)

post_parser.add_argument(
    'connected_player_count', dest='connected_player_count', type=int,
    location='form', required=False,
)
post_parser.add_argument(
    'total_player_count', dest='total_player_count', type=int,
    location='form', required=False,
)

post_parser.add_argument(
    'evennia_version', dest='evennia_version', location='form', required=True,
)
post_parser.add_argument(
    'python_version', dest='python_version', location='form', required=False,
)
post_parser.add_argument(
    'django_version', dest='django_version', location='form', required=False,
)
post_parser.add_argument(
    'server_platform', dest='server_platform', location='form', required=False,
)


# noinspection PyMethodMayBeStatic
class GameListingCheckIn(Resource):
    """
    The Evennia Game Index client hits this resource periodically to
    check in and let us know that its game is still alive. It sends along
    full details on the game each time it does.
    """

    def post(self):
        args = post_parser.parse_args()

        if args.telnet_port:
            # we want to allow the port being the empty string so only validate
            # if it's actually set to something.
            try:
                int(args.telnet_port)
            except ValueError:
                abort(400, message="The given Telnet port is not a valid number")

        # handle Evennia 0.6 and prior EGI keys
        if not args.connected_account_count \
           and args.connected_player_count:
            args.connected_account_count = args.connected_player_count
        if not args.total_account_count \
           and args.total_player_count:
            args.total_account_count = args.total_player_count

        # some older game versions send None here
        args.connected_account_count = args.connected_account_count or 0
        args.total_account_count = args.total_account_count or 0

        # Flask-restful's reqparser is acting a little odd.
        # It reports True to hasattr, but throws an exception
        # if we try del args.connected_player_count without it
        # having been provided.
        if hasattr(args, 'connected_player_count'):
            del args['connected_player_count']
        if hasattr(args, 'total_player_count'):
            del args['total_player_count']

        # If it exists, we'll end up with the existing list. If not,
        # it gets created.
        slug = slugify(args.game_name)
        # noinspection PyArgumentList
        gl = models.GameListing.get_or_insert(slug, **args)
        # Regardless of what we do, time to update it.
        for key, val in args.items():
            setattr(gl, key, val)
        # Bombs away!
        gl.put()
        return 'OK', 200
