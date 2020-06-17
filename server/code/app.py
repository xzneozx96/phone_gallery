from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.user import *
from resources.item import Items, Item, CreateItem

app = Flask(__name__)
app.secret_key = 'bkai@417'
CORS(app)
api = Api(app)

jwt = JWTManager(app)

api.add_resource(UserRegister, "/admin/register") 
api.add_resource(UserLogin, "/admin/login")  
api.add_resource(CreateItem, "/admin/create")  
api.add_resource(Items, "/phones")  
api.add_resource(Item, "/phone/<string:name>")  

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
