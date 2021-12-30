from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from src.db import *

class PostalAdmin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "idpostal",
        type=int,
        required=True,
        help="this field cannot be left blank!"
    )

    @jwt_required()
    def post(self):
        data = PostalAdmin.parser.parse_args()
        idpostal = data["idpostal"]

        postaladmin = getPostalAdmin(data["idpostal"])

        if postaladmin:
            return {"message": "An settlement with name {} already exists.".format(data["idpostal"])}, 400

        try:
            respond = insertPostalAdmin(idpostal)
            if respond:
                return {"New postal admin": {"Id postal admin": idpostal, "Office": idpostal}}, 201
            return {"message": "An error occurred inserting the postal admin."}, 500
        except:
            return {"message": "An error occurred inserting the postal admin."}, 500