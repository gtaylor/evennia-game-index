"""
This is pretty stripped down, but serves as the entrypoint during local
development and in production on App Engine.
"""
from evennia_gamedir import app
from evennia_gamedir.config import populate_flask_config


def run_app(*args, **kwargs):
    populate_flask_config(app)
    return app(*args, **kwargs)

if __name__ == '__main__':
    run_app()
