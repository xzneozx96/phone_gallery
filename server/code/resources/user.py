from pymongo import MongoClient
from flask_restful import Resource, request
from flask_jwt_extended import create_access_token, create_refresh_token
import bcrypt

from models.user import UserModule

client = MongoClient("mongodb://localhost:27017/")
db = client["phone_market"]
collection_admins = db["admin"]


def verify_pw(username, password):
    if not UserModule.find_by_username(username):
        return False
    else:
        hased_pw = collection_admins.find(
            {"username": username})[0]["password"]

    return True if bcrypt.checkpw(password.encode("utf-8"), hased_pw) else False


class UserRegister(Resource):
    def post(self):
        postedData = request.get_json()
        _id = postedData["id"]
        username = postedData["username"]
        password = postedData["password"]
        alias = postedData["alias"]

        if UserModule.find_by_username(username):
            return {"msg": "Existed user "}, 400

        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        collection_admins.insert_one(
            {"username": username, "password": hashed_pw, "alias": alias, "id": _id, }
        )

        return {"msg": "Creating new admin successfully"}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"]

        user = UserModule.find_by_username(username)

        if not UserModule.find_by_username(username):
            return {"msg": "Can not found this username"}, 400
        check_password = verify_pw(username, password)

        if check_password:
            access_token = create_access_token(identity=user.id, fresh=True)
            refesh_token = create_refresh_token(identity=username)
            return {
                'access_token': access_token,
                'refesh_token': refesh_token
            }, 200
        return {"msg": "Invalid Credentials"}, 401
 