from funciones import *


numero = None
lista_peliculas = []

while True:
    respuesta = input("Menu\n"
                    "1- Cargar archivo .CSV\n"
                    "2- Imprimir lista\n"
                    "3- Asignar rating\n"
                    "4- Asignar genero\n"
                    "5- Filtrar genero\n"
                    "6- Ordenar peliculas\n"
                    "7- Mejor Rating\n"
                    "8- Guardar peliculas\n"
                    "9- Salir\n"
                    "Ingrese una opcion:")
    
    if respuesta == "1":
        nombre = input("\ningrese nombre del archivo:")
        lista_peliculas = obtener_lista_peliculas(nombre)
    if respuesta == "2":
        mostrar_peliculas(lista_peliculas)
    if respuesta == "3":
        asignar_rating(lista_peliculas)
        mostrar_datos(lista_peliculas, "rating")
    if respuesta == "4":
        asignar_genero(lista_peliculas)
        mostrar_datos(lista_peliculas, "genero")
    if respuesta == "5":
        nombre_especificado = input("\ningrese el genero a separar:")
        lista_especificada = filtrar_peliculas(nombre_especificado, lista_peliculas)
        mostrar_datos(lista_especificada,"genero")
        crear_archivo_generos(lista_especificada,nombre_especificado)
    if respuesta == "6":
        ordenar_por_genero_y_rating(lista_peliculas)
        mostrar_peliculas(lista_peliculas)
    if respuesta == "7":
        lista_mejor_rating= mejor_rating(lista_peliculas, "rating")
        mostrar_dato_rating(lista_mejor_rating,"rating")
    if respuesta == "8":
        crear_archivo_rating(lista_mejor_rating,"la mejor peli")
    


        ######## punto 9 ########
    continuar = input("\ndesea continuar?: ")
    if continuar == "no":
        break
        
