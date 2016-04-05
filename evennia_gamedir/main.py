import datetime

from flask import Flask, render_template
from flask_restful import Api

from evennia_gamedir import resources, models

app = Flask(__name__)
api = Api(app)


@app.route('/')
def game_list():
    cutoff_time = datetime.datetime.now() - datetime.timedelta(hours=24)
    games = models.GameListing.query()
    # Getting around a weird Google Cloud Datastore limitation crappily
    # until I can figure out a better way.
    filtered_games = [g for g in games if g.checkin_time > cutoff_time]
    # Saves us from having to create an index, which is apparently slightly
    # more expensive (monetarily).
    sorted_games = sorted(filtered_games, key=lambda x: (
        x.connected_player_count * -1, x.game_name))
    return render_template('index.html', games=sorted_games)

api.add_resource(resources.game.GameCheckIn, '/api/v1/game/check_in')


if __name__ == '__main__':
    app.run()
