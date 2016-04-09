from flask import render_template

from evennia_gamedir import models, app


@app.route('/')
def game_list():
    """
    The root game listing view.
    """
    games = models.GameListing.get_all_fresh_games_list()
    return render_template('game_list.html', games=games)
