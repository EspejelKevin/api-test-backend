from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from src.db import *

class City(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "idcity",
        type=int,
        required=True,
        help="id city"
    )
    parser.add_argument(
        "name",
        required=True,
        help="name the city"
    )

    @jwt_required()
    def get(self, name):
        city = getCity(name)
        if city:
            return city
        return {"message": "City not found"}, 404

    @jwt_required()
    def post(self):
        data = City.parser.parse_args()
        idcity = data["idcity"]
        name = data["name"]
        

        city = getCity(name)
        if city:
            return {"message": "An city with name {} already exists.".format(name)}, 400

        try:
            respond = insertCity(idcity, name)
            if respond:
                return {"New city":{"Id city": idcity, "Name city": name}}, 201
            return {"message": "An error occurred inserting the city."}, 500
        except:
            return {"message": "An error occurred inserting the city."}, 500