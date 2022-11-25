from flask import Flask, render_template

app = Flask(__name__) #Esto es que se trae lo más básico de la app que estamos creando pero viniendo de Flask

@app.route("/") #Esto es para indicar que es la ruta raíz
def index():               #Por esa razón acá va lo que se va a escribir en html
    #return "<h1>siuu</h1>"    #Esta función es para crear una vista en el navegador

    datos = {
       "Titulo":  "index",
       "Nombre": "Nicole"
    }

    return render_template("index.html", data=datos) #Retorno el render template pra más html, se le pone el name del archivo deseado dentro de "templates", para más información ver "anotaciones.txt"


if __name__ == "__main__": #Condicional para ver si cumple con lo más básico, que es la importación de la raíz
    app.run(debug=True, port=5000) #El debug me permite que se actualice automáticamente cuando refresco la pág, es necesario correr nuevamente el script

    