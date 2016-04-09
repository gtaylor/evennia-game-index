from evennia_gamedir import app
from evennia_gamedir.metrics.common import create_gauge_metric
from evennia_gamedir.metrics.metric_defines import METRIC_DEFINES


def _setup_metrics():
    for metric_name, values in METRIC_DEFINES.items():
        create_gauge_metric(
            gauge_name=metric_name,
            display_name=values['display_name'],
            description=values['description'],
        )


@app.route('/_system/setup/all')
def setup_all_the_things():
    """
    This call does all setup work needed to configure the App Engine
    environment for normal operation.
    """

    _setup_metrics()
    return "OK"
