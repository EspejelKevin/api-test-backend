from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from src.db import *

class Municipality(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "clave",
        type=int,
        required=True,
        help="this field cannot be left blank!"
    )
    parser.add_argument(
        "name",
        required=True,
        help="the name of the municipality"
    )
    parser.add_argument(
        "state",
        required=True,
        help="name of the state to which the municipality belongs"
    )

    @jwt_required()
    def get(self, name):
        municipality = getMunicipalitiesByName(name)
        if municipality:
            return municipality
        return {"message": "Municipality not found"}, 404

    @jwt_required()
    def post(self):
        data = Municipality.parser.parse_args()
        idmunici = data["clave"]
        name = data["name"]
        state = data["state"]

        municipality = getMunicipalitiesByName(name)
        if municipality:
            return {"message": "An municipality with name {} already exists.".format(name)}, 400

        try:
            respond = insertMunicipality(idmunici, name, state)
            if respond:
                return {"New municipality": {"No. Munici": idmunici, "Municipality": name, "State belongs": respond}}, 201
            return {"message": "An error occurred inserting the municipality."}, 500
        except:
            return {"message": "An error occurred inserting the municipality."}, 500