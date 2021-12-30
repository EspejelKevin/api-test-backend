from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from src.security import authenticate, identity
from src.resources.settlement import Settlement, SettlementByName
from src.resources.municipality import Municipality
from src.resources.state import State
from src.resources.city import City
from src.resources.postaladmin import PostalAdmin
from src.resources.user import UserRegister

app = Flask(__name__)
api = Api(app)
app.secret_key = 'development'

jwt = JWT(app, authenticate, identity)

api.add_resource(Settlement, "/settlements/<int:cp>", "/settlement")
api.add_resource(SettlementByName, "/settlement/<string:name>")
api.add_resource(Municipality, "/municipality/<string:name>", "/municipality")
api.add_resource(State, "/state/<string:name>", "/state")
api.add_resource(City, "/city/<string:name>", "/city")
api.add_resource(PostalAdmin, "/postaladmin")
api.add_resource(UserRegister, '/register')