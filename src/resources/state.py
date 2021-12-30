from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from src.db import *

class State(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "clave",
        type=int,
        required=True,
        help="number of the state"
    )
    parser.add_argument(
        "name",
        required=True,
        help="name of state"
    )

    @jwt_required()
    def get(self, name):
        state = getStateByName(name)
        if state:
            return state
        return {"message": "State not found"}, 404

    @jwt_required()
    def post(self):
        data = State.parser.parse_args()
        no_state = data["clave"]
        name = data["name"]

        state = getStateByName(name)
        if state:
            return {"message": "An state with name {} already exists.".format(name)}, 400

        try:
            respond = insertState(no_state, name)
            if respond:
                return {"New state": {"No. State": no_state, "State": name}}, 201
            return {"message": "An error occurred inserting the state."}, 500
        except:
            return {"message": "An error occurred inserting the state."}, 500
