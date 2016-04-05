from google.appengine.ext import ndb


class GameListing(ndb.Model):
    # Game listing stuff
    game_name = ndb.StringProperty(required=True)
    game_status = ndb.StringProperty(required=True)
    game_website = ndb.StringProperty()
    listing_contact = ndb.StringProperty(required=True)

    # How to play
    telnet_hostname = ndb.StringProperty()
    telnet_port = ndb.IntegerProperty()
    web_client_url = ndb.StringProperty()

    # Game stats
    connected_player_count = ndb.IntegerProperty()
    total_player_count = ndb.IntegerProperty()

    # System info
    evennia_version = ndb.StringProperty(required=True)
    python_version = ndb.StringProperty()
    django_version = ndb.StringProperty()
    server_platform = ndb.StringProperty()

    created_time = ndb.DateTimeProperty(auto_now_add=True)
    checkin_time = ndb.DateTimeProperty(auto_now=True)
