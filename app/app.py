from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__) #Esto es que se trae lo más básico de la app que estamos creando pero viniendo de Flask

app.config


@app.route("/") #Esto es para indicar que es la ruta raíz
def index():               #Por esa razón acá va lo que se va a escribir en html
    #return "<h1>siuu</h1>"    #Esta función es para crear una vista en el navegador

    datos = ["Azul", "Rojo", "Amarillo", "Naranjaaaaaaaaaaaa", "Verde", "Gris"]

    paquete = {
        "titulo": "Probando...",
        "Nombre": "Isaac",
        "colores": datos,
        "lista_colores": len(datos)
    }
            #El argumento data me permite enviar cosas al html siempre y cuando lo reciba en el html como {{ data }}, se pasa el argumento, no la variable
    return render_template("index.html", data=paquete) #Retorno el render template pra más html, se le pone el name del archivo deseado dentro de "templates", para más información ver "anotaciones.txt"


@app.route('/contacto/<nombre>/<int:edad>') #esta url personalizada debe de llever al que está entre <> con el mismo nombre al argumento que le estoy pasando a la función
def contacto(nombre, edad): #la idea es que cuando en el url ponga "...5000/contacto/david", eso se pase hasta la plantilla y se convierta en contenido de la pág
    info = {
        "titulo": "Contacto",
        "nombre": nombre,
        "edad": edad #hay que ir agregando esto a la plantilla
    }

    return render_template("contacto.html", data=info)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get("param1"))

    arg = request.args.get("param1")

    return render_template("contacto.html", data=arg) #esto es similar a lo de arriba, ver anotaciones para ver lo del param, pero puedo recuperar lo de la url y usarlo, por ejemplo para escribir en la pag
                                                
def not_found(error):
    #return render_template("404.html"), 404 #codigo de error va afuera
    return redirect(url_for("index")) #Nos permite acceder a una página que sí existe si intentan buscar una que no existe

if __name__ == "__main__": #Condicional para ver si cumple con lo más básico, que es la importación de la raíz
    app.add_url_rule("/contacto/query_string", view_func=query_string) #Ojo que el def de arriba no tiene @app, se pone acá, se le pone el url que lo va a albergar y otro argumento que se llama view_func y es la función que asocia el app y la def de arriba
    app.register_error_handler(404, not_found) #nuevamente se le pasa el # de error y la funcion
    app.run(debug=True, port=5000) #El debug me permite que se actualice automáticamente cuando refresco la pág, es necesario correr nuevamente el script

    