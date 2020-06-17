from pymongo import MongoClient
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
from bson import json_util

import json

client = MongoClient("mongodb://localhost:27017/")
db = client["phone_market"]
collection_phones = db["phones"]
collection_trash_items = db["trash"]


class Items(Resource):
    def get(self):
        docs_list = []
        for doc in collection_phones.find():
            docs_list.append(doc)
        return json.dumps(docs_list, indent=4, default=json_util.default), 200


class Item(Resource):
    def get(self, name):
        name = "https://tiki.vn/" + name + ".html"
        docs_list = []
        if collection_phones.find({"linkproduct": name}):
            data = collection_phones.find({"linkproduct": name})[0]
            return json.dumps(data, indent=4, default=json_util.default), 200
        else:
            return {"msg": "this phone is not found"}, 400

    def delete(self, name):
        name = "https://tiki.vn/" + name + ".html"
        docs_list = []
        data = collection_phones.find({"linkproduct": name})[0]
        if data:
            if collection_trash_items.find({"linkproduct": name}):
                pass
            else:
                collection_trash_items.insert_one(data)
            collection_phones.delete_one(data)
            # for doc in collection_trash_items.find({"linkproduct": name}):
            #     docs_list.append(doc)
            # return json.dumps(docs_list, indent=4, default=json_util.default), 200
            return {"msg": "Delete succesfully"}, 200
        else:
            return {"msg": "Can not found this phone"}, 400

    def post(self, name):  # restore the deleted item
        name = "https://tiki.vn/" + name + ".html"
        docs_list = []
        data = collection_trash_items.find({"linkproduct": name})[0]
        if data:
            if collection_phones.find({"linkproduct": name}):
                pass
            else:
                collection_phones.insert_many(data)
            collection_trash_items.delete_many({"linkproduct": name})

            for doc in collection_phones.find({"linkproduct": name}):
                docs_list.append(doc)
            return json.dumps(docs_list, indent=4, default=json_util.default), 200
        else:
            return {"msg": "Can not found this phone"}, 400

    def put(self, name):
        name = "https://tiki.vn/" + name + ".html"
        docs_list = []
        data = collection_phones.find({"linkproduct": name})[0]
        if data:
            requestedData = request.get_json()
            collection_phones.update_one(
                {"linkproduct": name},
                {
                    "$set": {
                        "name": requestedData["name"],
                        "category": requestedData["category"],
                        "imageURL": requestedData["imageURL"],
                        "price": requestedData["price"],
                        "description": requestedData["description"],
                    }
                },
            )
            updatedData = collection_phones.find({"linkproduct": name})[0]

            return json.dumps(updatedData, indent=4, default=json_util.default), 200
        else:
            return {"msg": "Error while updating "}, 400


class CreateItem(Resource):
    def post(self):
        data = request.get_json()

        collection_phones.insert_one(
            {
                "name": data["name"],
                "linkproduct": data["linkproduct"],
                "category": data["category"],
                "imageURL": data["imageURL"],
                "price": data["price"],
                "description": data["description"],
            }
        )

        return {"msg": "Create new item successfully"}, 200
