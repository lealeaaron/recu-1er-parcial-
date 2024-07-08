from random import randint
import csv
import json
import os
######################################################## PUNTO 1 ###########################################################


def get_path_actual(nombre_archivo):
    direccion_actual = os.path.dirname(__file__)
    return os.path.join(direccion_actual, nombre_archivo)

def obtener_lista_peliculas(nombre_archivo):
    with open(get_path_actual(nombre_archivo), "r", encoding = "utf-8") as archivo:
        lista = []
        archivo.readline().strip("\n").split(",")
        
        for linea in archivo.readlines():
            peli = {}
            linea = linea.strip("\n").split(",")

            id, titulo, genero, rating = linea
            peli["id"] = int(id)
            peli["titulo"] = titulo
            peli["genero"] = genero
            peli["rating"] = float(rating)
            lista.append(peli)

        return lista
    

######################################################## PUNTO 2 ###########################################################


def mostrar_peliculas(lista_peliculas: list)-> None:
    tam = len(lista_peliculas)
    print("                ***Listado de Peliculas***")
    print()
    print("|ID|         |Titulo|                   |Genero|     |Rating|")
    print("-------------------------------------------------------------")
    for i in range(tam):
        mostrar_items(lista_peliculas[i])
    print()


def mostrar_items(una_peli: list):
    print(f"{una_peli['id']:<3}    {una_peli['titulo']:<30}  {una_peli['genero']:<14}  {una_peli['rating']:.2f}")



######################################################## PUNTO 3 ###########################################################
def asignar_rating(lista):
    from random import randint
    for peli in lista:
        peli["rating"] = randint(1, 10)

def mapear_peliculas(mapear, lista)-> list:
    lista_a_devolver = []
    for peli in lista:
        lista_a_devolver.append(mapear(peli))
    return lista_a_devolver #devuelve una peli mapeada

def mostrar_datos(lista, dato):
    print(f"Titulo                               {dato.capitalize()}")
    for el in lista:
        print(f"{el['titulo']:<30}       {el[dato]}")
        

######################################################## PUNTO 4 ###########################################################
def asignar_genero(lista):
    from random import randint
    for el in lista:
        aux = randint(1, 4)
        match aux:
            case 1:
                el["genero"] = "drama"
            case 2:
                el["genero"] = "comedia"
            case 3:
                el["genero"] = "accion"
            case 4:
                el["genero"] = "terror"

######################################################## PUNTO 5 ###########################################################
def filtrar_peliculas(genero_especifico, lista: list)-> list:
    lista_filtrada = []
    for pelicula in lista:  # Cambio el nombre de la variable del bucle
        if pelicula["genero"] == genero_especifico:
            lista_filtrada.append(pelicula)  # Agregar la película completa
    return lista_filtrada

def crear_archivo_generos(lista, nombre_archivo):
    if not nombre_archivo.endswith('.csv'):
        nombre_archivo += '.csv'

    # Crear el archivo CSV
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        
        # Escribir los datos de la lista en el archivo CSV
        for elemento in lista:
            escritor.writerow([elemento])

    print(f"Archivo {nombre_archivo} creado exitosamente.\n")





######################################################## PUNTO 6 ###########################################################

def ordenar_por_genero_y_rating(peliculas: list):
    peliculas.sort(key=lambda x: (x["genero"], -x["rating"]))




######################################################## PUNTO 7 ###########################################################
def mejor_rating(lista, dato):
    rating_maximo = 0
    pelicula = None
    rating = True
    for i in lista:
        if rating or i[dato] > rating_maximo:
            rating_maximo = i[dato]
            pelicula = i
            rating = False
    return pelicula

def mostrar_dato_rating(listado, dato):
    print(f"Pelicula con mejor rating")
    print(f"Titulo: {listado['titulo']} | {dato}: {listado[dato]}")


######################################################## PUNTO 8 ###########################################################

def crear_archivo_rating(mayor_rating, nombre):
    with open(get_path_actual(nombre),"w",encoding = "utf8") as archivo:
        json.dump(mayor_rating,archivo)