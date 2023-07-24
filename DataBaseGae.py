import sqlite3 as sql

#es importante estar en la carpeta donde quieres crear la base de datos
#Para Axions GAE si solo hay un tipo de grafico no hace falta la base de datos
def createDB(): #CREA LA BASE DE DATOS (SOLO HACER SI ES NECESARIA CAMBIAR MUCHOS ELEMENTOS)
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae.db")#modificarlo para que si ya existe haga un pass
    conn.commit()
    conn.close()


def createtable(): #ESTO SE USA A LA VEZ QUE CREAMOS UNA BASE DE DATOS
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae.db")#modificarlo para que si ya existe haga un pass
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Axions (
        name text , 
        type text ,
        large_panorama integer,
        panorama integer,
        helioscopes integer,
        haloscopes integer,
        lswexps integer,
        projection integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(name, type, path, LP,P,Helios,Halos,LSW ,projection): #PARA AÑADIR UNA SOLA COLUMNA (IDEAL PARA AÑADIR UN EXPERIMENTO NUEVO)
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Axions  VALUES ('{name}', '{type}','{path}','{LP}','{P}','{Helios}','{Halos}',{LSW},{projection})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()    

def readRows(): #SE USA PARA LEER TODAS LAS COLUMNAS
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM Axions"
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close() 
    print(data)

def insertRows(axionexps): #ESTA ES PARECIDA A LA DE UNA SOLA COLUMNA PERO AÑADIENDO MAS PARA ELLO HAY QUE DEFINIR UNA LISTA DE LISTAS CON LOS EXPERIMENTOS COMO ESTA HECHO MAS ADELANTE
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Axions  VALUES (?,?,?,?,?,?,?,?,?)"
    cursor.executemany(instruction,axionexps)
    conn.commit()
    conn.close()

def readOrdered(field): #SE USA PARA LEER LA LISTA Y QUE DEVUELVA UN LISTA ORDENADA SEGUN UN CRITERIO
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae.db")
    cursor = conn.cursor()
    #Se lee ordenado alfabeticamente, y de menor a mayor , para la inversa escribir DESC despues de {field}
    instruction = f"SELECT * FROM Axions ORDER BY {field}"
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close() 
    print(data)
#HAY QUE CREER VARIAS FUNCIONES MAS DE SEARCH

def search(field, token): #SE USA PARA BUSCAR EN LA BASE DE DATOS SEGUN UN CRITERIO Y DEVUELVE UNA LISTA DE LISTAS CONFORME A LAS CONDICIONES
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM Axions WHERE {field} = {token} "
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close()

    return data

def search_names(field, token):
    names = []
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM Axions WHERE {field} = {token} "
    cursor.execute(instruction)
    data = cursor.fetchall()
    for row in data:
        names.append(row[0])
    conn.commit()
    conn.close()
    return names

#HAY QUE MODIFICAR PARA QUE SEA MAS GENEREAL
def update(field,value): #SE USA PARA MODIFICAR UN ELEMENTO 
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae.db")
    cursor = conn.cursor()
    instruction = f"UPDATE Axions SET '{field}' == {value} "
    cursor.execute(instruction)

    conn.commit()
    conn.close() 

def deleteRow(): #PARA ELIMINAR UNA FILA
    conn = sql.connect("/home/tfg_2022_1/git/axion-limits/AxionsGae..db")
    cursor = conn.cursor()
    instruction = f"DELETE FROM Axions WHERE name = 'qcdband' "
    cursor.execute(instruction)

    conn.commit()
    conn.close() 
