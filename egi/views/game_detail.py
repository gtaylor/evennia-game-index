from slugify import slugify
from flask import render_template

from egi import models, app
from egi.exceptions import NotFoundError


@app.route('/game/<game_slug>', endpoint='game-detail')
def game_detail(game_slug):
    """
    Detail view for a game.
    """

    slug = slugify(game_slug)
    game = models.GameListing.get_by_id(slug)
    if not game:
        raise NotFoundError("No such game with that ID.")

    return render_template('game_detail.html', game=game)
