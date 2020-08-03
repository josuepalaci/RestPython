from flask import Flask, jsonify, request
from products import products
app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({'mesaje':'pong'})


@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({'productos':products,'mensaje':'lista de productos'})

@app.route('/products/<string:produc_name>')
def getProduct(produc_name):
    producto = [product for product in products if product['name'] == produc_name]
    if(len(producto)>0):
        return jsonify({'producto':producto[0]})
    else: return 'No encontrado'


@app.route('/products', methods=['POST'])
def addProduct():
    newProduct = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(newProduct)
    print(request.json)
    return jsonify({"mensaje":"agregado satisfactoriamente", "products": products})

@app.route('/products/<string:produc_name>', methods=['PUT']) 
def editProduct(produc_name):
    producto = [product for product in products if product['name']==produc_name]
    if (len(producto)>0):
        producto[0]['name'] = request.json['name']
        producto[0]['price'] = request.json['price']
        producto[0]['quantity'] = request.json['quantity']
        return jsonify({
            "mensaje":"actualizado...",
            "procuto":producto[0]
        })
    else : return jsonify({"mensaje":"producto no encontrado"})

@app.route('/products/<string:produc_name>', methods=['DELETE']) 
def deleteProduct(produc_name):
    producto = [product for product in products if product['name']==produc_name]
    if (len(producto)>0):
        products.remove(producto[0])
        return jsonify({"mensaje":"eliminado","productos":products})
    else: return jsonify({"mensaje":"prodcuto no encontrado"})

if __name__=='__main__':
    app.run(debug=True,port=4000)

