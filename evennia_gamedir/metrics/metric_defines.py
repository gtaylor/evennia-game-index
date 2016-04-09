"""
We may need to break this up into multiple modules eventually, but toss any
metrics that we need to track in here.
"""
from evennia_gamedir.metrics.common import GaugeMetric


class EvenniaPlayerConnected(GaugeMetric):
    metric_name = "evennia.players.connected"
    display_name = "Total Connected Players"
    description = "Total number of connected Evennia players."
    metric_value_type = 'INT64'


class EvenniaPlayersAll(GaugeMetric):
    metric_name = "evennia.players.all"
    display_name = "Total Registered Players"
    description = "Total number of registered Evennia players."
    metric_value_type = 'INT64'


class EDGGameListingsAll(GaugeMetric):
    metric_name = "egd.game-listings.all"
    display_name = "Total Game Listings"
    description = "Total count of all game listings, fresh or stale."
    metric_value_type = 'INT64'


class EDGGameListingsFresh(GaugeMetric):
    metric_name = "egd.game-listings.fresh"
    display_name = "Fresh Game Listings"
    description = "Count of all game listings that have been seen recently."
    metric_value_type = 'INT64'


class GamePlayersAll(GaugeMetric):
    metric_name = "game.players.all"
    display_name = "Per-Game Registered Players"
    description = "Total number of registered players on specific games."
    metric_value_type = 'INT64'

    extra_labels = [
        {
            "key": "game_key_name",
            "valueType": "STRING",
            "description": "The game's Datastore key name."
        },
    ]


class GamePlayersConnected(GaugeMetric):
    metric_name = "game.players.connected"
    display_name = "Per-Game Connected Players"
    description = "Total number of connected players on specific games."
    metric_value_type = 'INT64'

    extra_labels = [
        {
            "key": "game_key_name",
            "valueType": "STRING",
            "description": "The game's Datastore key name."
        },
    ]
