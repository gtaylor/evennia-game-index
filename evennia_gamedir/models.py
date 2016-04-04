from google.appengine.ext import ndb


class GameListing(ndb.Model):
    game_name = ndb.StringProperty(required=True)
    game_status = ndb.StringProperty(required=True)
    game_website = ndb.StringProperty()
    listing_contact = ndb.StringProperty(required=True)
    evennia_version = ndb.StringProperty(required=True)
    telnet_hostname = ndb.StringProperty(required=True)
    telnet_port = ndb.IntegerProperty(required=True)
    connected_player_count = ndb.IntegerProperty()
    total_player_count = ndb.IntegerProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)
    checkin_time = ndb.DateTimeProperty(auto_now=True)
