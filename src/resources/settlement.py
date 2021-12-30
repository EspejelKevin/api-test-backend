from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from src.db import *

class Settlement(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name",
        required=True,
        help="the name of settlement"
    )
    parser.add_argument(
        "codepostal",
        type=int,
        required=True,
        help="code postal of the settlement"
    )
    parser.add_argument(
        "zone",
        required=True,
        help="Urban/Rural"
    )
    parser.add_argument(
        "id_asenta_muni",
        required=True,
        type=int,
        help="id settlement municipality"
    )
    parser.add_argument(
        "type_sett",
        required=True,
        help="type settlement"
    )
    parser.add_argument(
        "munici",
        required=True,
        help="name of the municipality"
    )
    parser.add_argument(
        "city",
        required=True,
        help="name of the city"
    )
    parser.add_argument(
        "id_office",
        required=True,
        type=int,
        help="id postal administration settlement"
    )

    @jwt_required()
    def get(self, cp):
        settlements = getSettlementsByCp(cp)
        if settlements:
            return settlements
        return {"message": "Settlements not found"}, 404

    @jwt_required()
    def post(self):
        data = Settlement.parser.parse_args()
        name = data["name"]
        codepostal = data["codepostal"]
        zone = data["zone"]
        id_asenta_muni = data["id_asenta_muni"]
        typesett = data["type_sett"]        
        munici = data["munici"] 
        city = data["city"] 
        idoffice = data["id_office"] 

        settlement = getSettlementsByName(name)
        if settlement:
            return {"message": "An settlement with name {} already exists.".format(name)}, 400

        try:
            respond = insertSettlement(name, codepostal, zone, id_asenta_muni, typesett, munici, city, idoffice)
            if respond:
                return {"message": "Successfully saved settlement"}, 201
            return {"message": "An error occurred inserting the settlement."}, 500
        except:
            return {"message": "An error occurred inserting the settlement."}, 500

class SettlementByName(Resource):

    @jwt_required()
    def get(self, name):
        settlement = getSettlementsByName(name)
        if settlement:
            return settlement
        return {"message": "Settlement not found"}, 404