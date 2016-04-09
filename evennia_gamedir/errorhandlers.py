from flask import jsonify

from evennia_gamedir import app
from evennia_gamedir.exceptions import NotFoundError


@app.errorhandler(NotFoundError)
def handle_notfound(error):
    if error.json_encode:
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
    else:
        # TODO: 404 template here?
        return error.message, error.status_code
