import datetime

from flask import Flask
from flask_restful import Api

from evennia_gamedir import resources, models

app = Flask(__name__)
api = Api(app)


@app.route('/')
def game_list():
    # TODO: Index on checkin_time?
    # TODO: Sort by player count?
    cutoff_td = datetime.timedelta(hours=24)
    games = models.GameListing.query().filter(
        models.GameListing.checkin_time > datetime.datetime.now() - cutoff_td)
    buf = '<html><head><title>Evennia Game Directory</title></head><body>'
    for game in games:
        buf += '%s<br>' % game.game_name
    buf += '</body></html>'
    return buf

api.add_resource(resources.game.GameCheckIn, '/api/v1/game/check_in')


if __name__ == '__main__':
    app.run()
