from flask import Flask, jsonify, request
from products import products


app = Flask(__name__)

#jsonify retorna un json pasandole un objeto por parametro
#methods=['GET'] se puede obviar, porque get esta por defecto
@app.route("/products", methods=['GET'])
def get_products():
    return jsonify(products)

@app.route("/products/<string:name>", methods=["GET"])
def get_product_by_name(name):    
    product = [x for x in products if x["name"]==name]
    if (len(product)==0):
        product = {"message":"Product not found"}
    return jsonify(product)


@app.route("/products", methods=["POST"])
def add_product():
    product = request.json
    new_product = {
        "name": product["name"],
        "price": product["price"],
        "quantity": product["quantity"]
    }
    products.append(new_product)    
    return jsonify({"message":"Product added succesfully!", "products": products})


@app.route("/products/<string:name>",methods=["PUT"])
def update_product(name):
    product = [product for product in products if product["name"]==name]       
    if(len(product)>0):
        product=product[0]
        product["name"] = request.json["name"]
        product["price"] = request.json["price"]
        product["quantity"] = request.json["quantity"]    
    else:
        product = "PRODUCT NOT FOUND!"
    return jsonify({"product":product})


@app.route("/products/<string:product_name>", methods=["DELETE"])
def delete_product(product_name):
    product = [product for product in products if product["name"]==product_name]
    if (len(product) > 0):
        products.remove(product[0])
        return jsonify({"new products":products})
    else:
        return jsonify({"message":"PRODUCT NOT FOUND"})






if __name__ == '__main__':
    app.run(debug=True, port=4000)