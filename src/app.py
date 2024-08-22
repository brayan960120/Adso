from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def Inicio():
    return render_template('Inicio.html')

@app.route('/pagar')
def pagar():
    return render_template('pagado.html')

@app.route('/seguir')
def seguir():
    return render_template('Inicio.html')

@app.route('/usuarios')
def usuarios():
    return render_template('Usuario.html')

@app.route('/registrarse')
def registarse():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('Crear_producto.html')

@app.route('/Iniciar')
def Iniciar():
    return render_template('login.html')

@app.route('/comprar')
def comprar():
    return render_template('Factura_producto.html')


@app.route('/empezar')
def empezar():
    return render_template('Inicio.html')

@app.route('/Iniciar_sesion')
def Iniciar_sesion():
    return render_template('login.html')

@app.route('/Inscribirse')
def Inscribirse():
    return render_template('Usuario.html')

@app.route('/crear')
def crear():
    return render_template('Inicio.html')

@app.route('/comprar_dos')
def comprar2():
    return render_template('Factura.html')

@app.route('/Inicio_dos')
def Inicio2():
    return render_template('Inicio.html')

@app.route('/Inhabilitar')
def Inhabilitar():
    return render_template('Inhabilitar_producto.html')

@app.route('/Inhabilitado')
def Inhabilitado():
    return render_template('Inicio.html')

@app.route('/Productos')
def Productos():
    return render_template('Inicio.html')

@app.route('/contacto')
def Contacto():
    return render_template('Contacto.html')

@app.route('/Editar')
def Editar():
    return render_template('Editar_productos.html')

@app.route('/Primero')
def Primero():
    return render_template('Inicio.html')














