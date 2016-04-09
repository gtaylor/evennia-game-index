from evennia_gamedir import models, app
from evennia_gamedir.metrics.metric_defines import EvenniaTotalConnectedPlayers, \
    EvenniaTotalRegisteredPlayers


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

    EvenniaTotalConnectedPlayers.write_gauge(connected_player_count)
    EvenniaTotalRegisteredPlayers.write_gauge(total_player_count)

    return "OK"
