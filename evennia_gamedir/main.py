"""
This is pretty stripped down, but serves as the entrypoint during local
development and in production on App Engine.
"""
from evennia_gamedir import app


if __name__ == '__main__':
    app.run()
