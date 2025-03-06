from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, DevOps con Docker y Kubernetes! esto es nuevo espero este todo bien configurado, asi solo tendre que pusherar las paginas para poder realizar los despliegues (habian errores pero esta ves espero este todo correcto)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)