from flask import Flask, request

app = Flask(__name__)

@app.route('/datos', methods=['POST'])
def recibir_datos():
    data = request.data.decode('utf-8')
    print(f"📥 Datos recibidos: {data}")
    return 'OK', 200

@app.route('/', methods=['GET'])
def home():
    return 'Servidor activo y esperando datos por POST en /datos', 200
