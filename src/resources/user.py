from flask_restful import Resource, reqparse
from src.db import *
from src.models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        username = data["username"]
        password = data["password"]

        if UserModel.find_by_username(username):
            return {"message": "User with that username already exists."}, 400

        insertUser(username, password)

        return {"message": "User created successfully."}, 201