from flask import Flask
from flask_restful import Api

import resources

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

api.add_resource(resources.game.GameCheckIn, '/api/v1/game/check_in')


if __name__ == '__main__':
    app.run()
