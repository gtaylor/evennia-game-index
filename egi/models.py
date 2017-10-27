import datetime

from google.appengine.ext import ndb


class GameListing(ndb.Model):
    # Game listing stuff
    game_name = ndb.StringProperty(required=True)
    game_status = ndb.StringProperty(required=True)
    game_website = ndb.StringProperty()
    listing_contact = ndb.StringProperty(required=True)
    short_description = ndb.StringProperty()
    long_description = ndb.TextProperty()

    # How to play
    telnet_hostname = ndb.StringProperty()
    telnet_port = ndb.IntegerProperty()
    web_client_url = ndb.StringProperty()

    # Game stats
    connected_account_count = ndb.IntegerProperty()
    total_account_count = ndb.IntegerProperty()

    # System info
    evennia_version = ndb.StringProperty(required=True)
    python_version = ndb.StringProperty()
    django_version = ndb.StringProperty()
    server_platform = ndb.StringProperty()

    created_time = ndb.DateTimeProperty(auto_now_add=True)
    checkin_time = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_all_fresh_games_list(cls):
        games = cls.query()
        # Getting around a weird Google Cloud Datastore limitation crappily
        # until I can figure out a better way.
        filtered_games = [g for g in games if g.is_fresh()]
        # Saves us from having to create an index, which is apparently slightly
        # more expensive (monetarily).
        return sorted(filtered_games, key=lambda game: (
            (game.connected_account_count or 0) * -1, game.game_name))

    def is_fresh(self):
        cutoff_time = datetime.datetime.now() - datetime.timedelta(hours=2)
        return self.checkin_time > cutoff_time
