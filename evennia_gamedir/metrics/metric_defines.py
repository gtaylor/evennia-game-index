"""
We may need to break this up into multiple modules eventually, but toss any
metrics that we need to track in here.
"""
from evennia_gamedir.metrics.common import GaugeMetric


class EvenniaTotalConnectedPlayers(GaugeMetric):
    metric_name = "evennia/total-connected-players"
    display_name = "Total Connected Players"
    description = "Total number of connected Evennia players."
    metric_value_type = 'INT64'


class EvenniaTotalRegisteredPlayers(GaugeMetric):
    metric_name = "evennia/total-registered-players"
    display_name = "Total Registered Players"
    description = "Total number of registered Evennia players."
    metric_value_type = 'INT64'
