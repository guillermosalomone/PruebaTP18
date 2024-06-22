import componentes.conexion_db as conexion1


def traer_todos():
    con = conexion1.conexion
    cursor = con.cursor(dictionary=True)
    consulta = 'SELECT * FROM usuarios;'
    
    cursor .execute(consulta)
    datos = cursor.fetchall()
    con.close()
    return datos
    
    
    