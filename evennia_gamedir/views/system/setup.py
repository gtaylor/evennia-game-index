from evennia_gamedir import app
from evennia_gamedir.metrics.common import BaseMetric


def _setup_metrics():
    """
    Makes sure all of the metrics are defined.
    """
    metric_types = BaseMetric.__subclasses__()
    for metric_type in metric_types:
        for metric in metric_type.__subclasses__():
            metric.create_metric()


@app.route('/_system/setup/all')
def setup_all_the_things():
    """
    This call does all setup work needed to configure the App Engine
    environment for normal operation.
    """

    _setup_metrics()
    return "OK"
