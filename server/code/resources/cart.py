from pymongo import MongoClient
from flask_restful import Resource, request
from flask import make_response
from bson import json_util
import json

from models.cart import CartModule

client = MongoClient("mongodb://localhost:27017/")
db = client["phone_market"]
collection_cart = db["cart"]


class Cart(Resource):
    def get(self):
        item_list = []
        item_collection = list(collection_cart.find())
        for item in item_collection:
            item_list.append(item)
        return make_response(json_util.dumps(item_list, ensure_ascii=False).encode('utf8'))

    def post(self):
        data = request.get_json()
        print(data)
        item_name = data["name"]
        item = CartModule.find_by_name(item_name)
        # if CartModule.create_item(item["name"], item["category"], item["imageURl"], item["price"], quantity):
        #     return 201
        # else:
        #     return {"msg": "Fail to add this item to cart"}, 400
        print(item)
    def delete(self):
        item_name = request.get_json()["name"]
        quantity = request.get_json()["quantity"]

        if quantity == 1:
          CartModule.delete_one_item(item_name)
          return {"msg": "Deleted succesfully"}, 200
        else:
          CartModule.delete_many_items(item_name)
          return {"msg": "Fail to delete item from cart"}, 400
