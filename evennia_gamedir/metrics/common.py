import datetime

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

from evennia_gamedir import app

__GCP_PROJECT_ID = app.config['GCP_PROJECT_ID']


def get_metrics_client():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('monitoring', 'v3', credentials=credentials)


def format_rfc3339(datetime_instance=None):
    """
    Formats a datetime per RFC 3339.

    :param datetime_instance: Datetime instance to format, defaults to utcnow
    """
    return datetime_instance.isoformat("T") + "Z"


def get_now_rfc3339():
    # Return now
    return format_rfc3339(datetime.datetime.utcnow())


def _get_standard_label_descriptors():
    return [
        {
            "key": "environment",
            "valueType": "STRING",
            "description": "One of 'production' or 'devel'"
        },
    ]


def _get_metric_vars(name):
    md_type = "custom.googleapis.com/{}".format(name)
    md_name = "projects/{}/metricDescriptors/{}".format(
        __GCP_PROJECT_ID, md_type)
    project_resource = "projects/{0}".format(__GCP_PROJECT_ID)
    return md_name, md_type, project_resource


def create_gauge_metric(gauge_name, display_name, description,
                        extra_labels=None):
    """
    :param str gauge_name:
    :param str display_name:
    :param str description:
    :param list extra_labels:
    """
    # We have a standard set of labels that we apply to all metrics.
    labels = _get_standard_label_descriptors()
    if extra_labels:
        labels += extra_labels

    md_name, md_type, project_resource = _get_metric_vars(gauge_name)
    metrics_descriptor = {
        "name": md_name,
        "type": md_type,
        "labels": labels,
        "metricKind": 'GAUGE',
        "valueType": "INT64",
        "unit": "items",
        "displayName": display_name,
        "description": description,
    }

    client = get_metrics_client()
    return client.projects().metricDescriptors().create(
        name=project_resource, body=metrics_descriptor).execute()


def _get_standard_label_values():
    return {
        "environment": 'prod' if app.config['IS_PRODUCTION'] else 'dev'
    }


def write_gauge_metric(gauge_name, value, extra_labels=None):
    # We have a standard set of labels that we apply to all metrics.
    labels = _get_standard_label_values()
    if extra_labels:
        labels.update(extra_labels)

    # Specify a new data point for the time series.
    now = get_now_rfc3339()
    md_name, md_type, project_resource = _get_metric_vars(gauge_name)
    timeseries_data = {
        "metric": {
            "type": md_type,
            "labels": labels,
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
                    "int64Value": value,
                }
            }
        ]
    }

    client = get_metrics_client()
    request = client.projects().timeSeries().create(
        name=project_resource, body={"timeSeries": [timeseries_data]})
    request.execute()
