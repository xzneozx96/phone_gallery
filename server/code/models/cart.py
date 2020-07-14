from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["phone_market"]
collection_cart = db["cart"]


class CartModule:

    @classmethod
    def create_item(cls, name, category, imageURL, price, quantity):
        collection_cart.insert_one({
            "name": name,
            "category": category,
            "price": price,
            "find_price": int(price) + 200000,
            "quantity": quantity
        })

    @classmethod
    def delete_one_item(cls, name):
        collection_cart.deleteOne({"name":name})[0]

    @classmethod
    def delete_many_items(cls, name):
        collection_cart.deleteMany({"name":name})

    @classmethod
    def find_by_name(cls, name):
        _item = collection_cart.find({"name": name})[0]
        if _item:
            item = _item
        else:
            item = None

        return item
