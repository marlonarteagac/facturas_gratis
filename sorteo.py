from flask import Flask, request  # Importamos flask
from flask import render_template  # importamos render_template (plantillas )
from funciones import conexion_db


app = Flask(__name__)  # Inicializamos app flask


@app.route('/')  # declaramos la ruta raiz de la aplicacion
def home():  # funcion que retorna la ruta del html

    return render_template("index.html")


@app.route('/formulario')  # declaramos la ruta raiz de la aplicacion
def formulario():  # funcion que retorna la ruta del html

    return render_template("formulario.html")


# declaramos la ruta para la pagina estratos1-3.html
@app.route('/sorteo1', methods=['POST', 'GET'])
def sorteo1():  # funcion que retorna la ruta del html
    # se renderiza la ruta del html con render_template
    if request.method == 'POST':

        mi_db = "facturas_gratis\DB\db_sorteo"
        mi_consulta_sql = """
                SELECT
                    contrato,
                    nombre,
                    barrio,
                    estrato

                FROM Estratos1_3

                ORDER BY RANDOM()
                LIMIT 1; """
        datos = conexion_db.Conexion(mi_db, mi_consulta_sql)
        contrato, nombre, barrio, estrato = datos[0]
        mensaje = f"Felicitaciones al señor {nombre}"

        # Preparar la consulta para insertar los datos en la tabla Ganadores
        insertar_ganador = """
        INSERT INTO Ganadores (contrato, nombre, barrio, estrato)
        VALUES (?, ?, ?, ?);
        """
        # Conectarse a la base de datos y ejecutar la inserción
        # Asumiendo que datos[0] tiene el contrato, datos[1] tiene el nombre, etc.
        conexion_db.Conexion(mi_db, insertar_ganador, datos[0])
        return render_template("estratos1-3.html",
                               nombre=nombre,
                               contrato=contrato,
                               estrato=estrato,
                               barrio=barrio,
                               mensaje=mensaje)
    else:
        return render_template("formulario.html")

# Ruta a la pagina del sorteo para estratos 4 al 6


# declaramos la ruta para la pagina estratos4-3.html
@app.route('/sorteo2', methods=['POST', 'GET'])
def sorteo2():  # funcion que retorna la ruta del html
    # se renderiza la ruta del html con render_template
    if request.method == 'POST':
        mi_db = "facturas_gratis\DB\db_sorteo"
        mi_consulta_sql = """
                SELECT
                    contrato,
                    nombre,
                    barrio,
                    estrato

                FROM Estratos4_6

                ORDER BY RANDOM()
                LIMIT 1; """
        datos = conexion_db.Conexion(mi_db, mi_consulta_sql)

        # Preparar la consulta para insertar los datos en la tabla Ganadores
        insertar_ganador = """
        INSERT INTO Ganadores (contrato, nombre, barrio, estrato)
        VALUES (?, ?, ?, ?);
        """
        # Conectarse a la base de datos y ejecutar la inserción
        # Asumiendo que datos[0] tiene el contrato, datos[1] tiene el nombre, etc.
        conexion_db.Conexion(mi_db, insertar_ganador, datos[0])
        return render_template("estratos4-6.html", datos=datos)

    else:
        return render_template("formulario.html")


@app.route('/ganadores')  # declaramos la ruta para la pagina "ganadores.html
def Ganadores():  # funcion que retorna la ruta del html
    # se renderiza la ruta del html con render_template

    # se renderiza la ruta del html con render_template
    mi_db = "facturas_gratis\DB\db_sorteo"
    mi_consulta_sql = """
            SELECT * from Ganadores
    """
    datos = conexion_db.Conexion(mi_db, mi_consulta_sql)

    return render_template("ganadores.html", datos=datos)


# declaramos la ruta para la pagina "ganadores.html
@app.route('/limpiar_ganadores',methods= ['POST'])
def limpiar_ganadores():  # funcion que retorna la ruta del html
    mi_db = "facturas_gratis\DB\db_sorteo"
    mi_consulta_sql = """
           delete from ganadores"""
    datos = conexion_db.Conexion(mi_db, mi_consulta_sql)

    return render_template("ganadores.html")

if __name__ == '__main__':
    app.run(debug=True)
