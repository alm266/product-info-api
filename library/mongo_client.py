from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__)
client = MongoClient(config.get('mongodb_uri'))
db = client['mydatabase']

@app.route('/products')
def get_products():
    products = []
    for product in db.products.find():
        products.append({
            '_id': product['_id'],
            'name': product['name'],
            'brand': product['brand'],
            'price': product['price'],
            'url': product['url'],
            'images': product['images'],
        })
    return jsonify(products)

if __name__ == '__main__':
    app.run()
