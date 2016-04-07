from evennia_gamedir import GCP_PROJECT_ID
from evennia_gamedir.metrics.common import get_metrics_client, get_now_rfc3339


def create_total_evennia_registered_players_metric():
    client = get_metrics_client()

    # This is our specific metric name
    custom_metric_type = "custom.googleapis.com/evennia/total-registered-players"
    project_resource = "projects/{0}".format(GCP_PROJECT_ID)

    metrics_descriptor = {
        "name": "projects/{}/metricDescriptors/{}".format(
            GCP_PROJECT_ID, custom_metric_type),
        "type": custom_metric_type,
        "labels": [],
        "metricKind": 'GAUGE',
        "valueType": "INT64",
        "unit": "items",
        "description": "Total number of registered Evennia players.",
        "displayName": "Total Registered Players"
    }

    return client.projects().metricDescriptors().create(
        name=project_resource, body=metrics_descriptor).execute()


def write_total_evennia_registered_players_metric(player_count):
    client = get_metrics_client()
    project_resource = "projects/{0}".format(GCP_PROJECT_ID)
    custom_metric_type = "custom.googleapis.com/evennia/total-registered-players"

    # Specify a new data point for the time series.
    now = get_now_rfc3339()
    timeseries_data = {
        "metric": {
            "type": custom_metric_type,
            "labels": {}
        },
        "resource": {
            "type": 'global',
        },
        "metricKind": 'GAUGE',
        "valueType": "INT64",
        "points": [
            {
                "interval": {
                    "startTime": now,
                    "endTime": now
                },
                "value": {
                    "int64Value": player_count,
                }
            }
        ]
    }

    request = client.projects().timeSeries().create(
        name=project_resource, body={"timeSeries": [timeseries_data]})
    request.execute()
