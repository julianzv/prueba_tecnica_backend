from flask import Flask, jsonify

app = Flask(__name__)

productos = [
    {'id': 1, 'nombre': 'Producto 1', 'precio': 10.99},
    {'id': 2, 'nombre': 'Producto 2', 'precio': 20.99},
    {'id': 3, 'nombre': 'Producto 3', 'precio': 5.99},
]

@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

@app.route('/productos', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nombre = data['nombre']
    precio = data['precio']
    # Lógica para crear el producto en la base de datos o lista de productos
    # ...
    producto = {'nombre': nombre, 'precio': precio}
    productos.append(producto)
    return jsonify(message='Producto creado correctamente')

@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.get_json()
    nombre = data['nombre']
    precio = data['precio']
    for producto in productos:
        if producto['id'] == id:
            producto['nombre'] = nombre
            producto['precio'] = precio
            return jsonify(message='Producto actualizado correctamente')
    return jsonify(message='Producto no encontrado'), 404

@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    for producto in productos:
        if producto['id'] == id:
            productos.remove(producto)
            return jsonify(message='Producto eliminado correctamente')
    return jsonify(message='Producto no encontrado'), 404

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(message='¡Hola, mundo!')

usuarios = {
    1: {'id': 1, 'nombre': 'Usuario 1', 'edad': 25},
    2: {'id': 2, 'nombre': 'Usuario 2', 'edad': 30},
    3: {'id': 3, 'nombre': 'Usuario 3', 'edad': 35},
}

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data['nombre']
    edad = data['edad']
    # Lógica para crear el usuario en la base de datos
    # ...
    return jsonify(message='Usuario creado correctamente')


@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    if id in usuarios:
        return jsonify(usuarios[id])
    else:
        return jsonify(message='Usuario no encontrado'), 404


if __name__ == '__main__':
    app.run()
