from evennia_gamedir import models
from evennia_gamedir.main import app
from evennia_gamedir.metrics.total_evennia_connected_players import \
    create_total_evennia_connected_players_metric, write_total_evennia_connected_players_metric
from evennia_gamedir.metrics.total_evennia_registered_players import \
    create_total_evennia_registered_players_metric, \
    write_total_evennia_registered_players_metric


@app.route('/_cron/metrics/frequent-all-game-iter-metrics')
def report_evennia_total_connected_players():
    """
    This is a rudimentary endpoint that App Engine cron hits to trigger
    the sending of metrics that require iterating through the entire list
    of fresh games.
    """
    games = models.GameListing.get_all_fresh_games_list()

    connected_player_count = 0
    total_player_count = 0
    for game in games:
        if game.connected_player_count:
            connected_player_count += game.connected_player_count
        if game.total_player_count:
            total_player_count += game.total_player_count

    create_total_evennia_connected_players_metric()
    create_total_evennia_registered_players_metric()
    write_total_evennia_connected_players_metric(connected_player_count)
    write_total_evennia_registered_players_metric(total_player_count)

    return "OK"
