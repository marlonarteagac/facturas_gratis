from flask import Flask  # Importamos flask
from flask import render_template  # importamos render_template (plantillas )
from funciones import conexion_db


app = Flask(__name__)  # Inicializamos app flask


@app.route('/')  # declaramos la ruta raiz de la aplicacion
def home():  # funcion que retorna la ruta del html

    return render_template("index.html")


@app.route('/sorteo1',methods=['POST', 'GET'])  # declaramos la ruta para la pagina estratos1-3.html
def sorteo1():  # funcion que retorna la ruta del html
    # se renderiza la ruta del html con render_template
    mi_db = "DB/db_sorteo"
    mi_consulta_sql = """
            SELECT 
                contrato, 
                nombre,
                barrio,
                estrato
                
            FROM Estratos1_3
            
            ORDER BY RANDOM()
            LIMIT 1;

    """
    datos = conexion_db.Conexion(mi_db, mi_consulta_sql) 
    
        
    # Preparar la consulta para insertar los datos en la tabla Ganadores
    insertar_ganador = """
    INSERT INTO Ganadores (contrato, nombre, barrio, estrato)
    VALUES (?, ?, ?, ?);
    """
        # Conectarse a la base de datos y ejecutar la inserción
    conexion_db.Conexion(mi_db, insertar_ganador, datos[0])  # Asumiendo que datos[0] tiene el contrato, datos[1] tiene el nombre, etc.
    return render_template("estratos1-3.html", datos=datos)


# Ruta a la pagina del sorteo para estratos 4 al 6
@app.route('/sorteo2')  # declaramos la ruta para la pagina estratos4-3.html
def sorteo2():  # funcion que retorna la ruta del html
    # se renderiza la ruta del html con render_template
    mi_db = "DB/db_sorteo"
    mi_consulta_sql = """
    SELECT 
    contrato, 
    nombre,
    barrio,
    estrato
    FROM Estratos4_6
    WHERE contrato = (SELECT contrato FROM Estratos4_6 ORDER BY RANDOM() LIMIT 1);  
    """
    datos = conexion_db.Conexion(mi_db, mi_consulta_sql)
    return render_template("estratos4-6.html", datos=datos)


# Ruta a la pagina del sorteo para estratos 4 al 6


@app.route('/ganadores')  # declaramos la ruta para la pagina "ganadores.html
def Ganadores():  # funcion que retorna la ruta del html
    # se renderiza la ruta del html con render_template


     # se renderiza la ruta del html con render_template
    mi_db = "DB/db_sorteo"
    mi_consulta_sql = """
            SELECT * from Ganadores
    """
    datos = conexion_db.Conexion(mi_db, mi_consulta_sql) 
    
    return render_template("ganadores.html", datos=datos)







if __name__ == '__main__':
    app.run(debug=True)
