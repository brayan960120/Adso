from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('Crear_producto.html')

@app.route('/Inicio')
def index():
    return render_template('Inicio.html')





