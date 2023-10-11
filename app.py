from flask import Flask, render_template
# traer todo flask
app = Flask(__name__)
# rutas
@app.route('/')
def index():
    return render_template('index.html')

# bloque de prueba
if __name__ == "__main__":
    app.run(debug = True)