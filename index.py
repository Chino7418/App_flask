from flask import Flask, render_template

app = Flask(__name__)

# @app.route sirve para el ruteo de las paginas /o secciones


@app.route('/')
def principal():
   # render_template
    return render_template('index.html')


@app.route('/lenguajes')
def mostrar_lenguajes():
    mis_lenguajes = ("C#", "Python", "JS", "Visual Basic",
                     "HTML", "CSS", "JSON", "NodeJS", "PHP", "SQL")
    return render_template('lenguajes.html', lenguajes=mis_lenguajes)


@app.route('/contacto')
def contacto():
    mis_provincias = provincias_argentinas = (
        "Buenos Aires",
        "Catamarca",
        "Chaco",
        "Chubut",
        "Córdoba",
        "Corrientes",
        "Entre Ríos",
        "Formosa",
        "Jujuy",
        "La Pampa",
        "La Rioja",
        "Mendoza",
        "Misiones",
        "Neuquén",
        "Río Negro",
        "Salta",
        "San Juan",
        "San Luis",
        "Santa Cruz",
        "Santa Fe",
        "Santiago del Estero",
        "Tierra del Fuego",
        "Tucumán"
    )
    return render_template('contacto.html',provincias=mis_provincias)


if __name__ == '__main__':
    # app.run(debug=True) es para que el servidor se reinicie cuando haya algun cambio de esta manera no tengo que estar deteniendo y/o iniciando el servidor
    # port= defino el puerto

    app.run(debug=True, port=5017)
