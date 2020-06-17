from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["phone_market"]
collection_admins = db["admin"]

class UserModule:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        _user = collection_admins.find({"username": username})[0]
        if _user:
            user = cls(_user["id"], _user["username"], _user["password"])
        else:
            user = None

        return user

    @classmethod
    def find_by_id(cls, _id):
        _user = collection_admins.find({"id": _id})[0]
        if _user:
            user = cls(_user["id"], _user["username"], _user["password"])
        else:
            user = None

        return user