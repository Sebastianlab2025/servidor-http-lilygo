from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def recibir_datos():
    data = request.get_data(as_text=True)
    print(f"📥 Recibido: {data}")
    return "OK", 200

if __name__ == "__main__":
    app.run()