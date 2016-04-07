import datetime

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def get_metrics_client():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('monitoring', 'v3', credentials=credentials)


def format_rfc3339(datetime_instance=None):
    """Formats a datetime per RFC 3339.
    :param datetime_instance: Datetime instanec to format, defaults to utcnow
    """
    return datetime_instance.isoformat("T") + "Z"


def get_now_rfc3339():
    # Return now
    return format_rfc3339(datetime.datetime.utcnow())
