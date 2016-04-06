import datetime

from evennia_gamedir import models
from evennia_gamedir.main import app
from flask import render_template


@app.route('/')
def game_list():
    """
    The root game listing view.
    """
    cutoff_time = datetime.datetime.now() - datetime.timedelta(hours=24)
    games = models.GameListing.query()
    # Getting around a weird Google Cloud Datastore limitation crappily
    # until I can figure out a better way.
    filtered_games = [g for g in games if g.checkin_time > cutoff_time]
    # Saves us from having to create an index, which is apparently slightly
    # more expensive (monetarily).
    sorted_games = sorted(filtered_games, key=lambda x: (
        x.connected_player_count * -1, x.game_name))
    return render_template('game_list.html', games=sorted_games)
