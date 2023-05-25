import json
import re

def leer_archivo(nombre_archivo: str):
    """
    Lee un archivo JSON y devuelve una lista de héroes.
    Recibe el nombre del archivo JSON a leer.
    Retorna una lista de diccionarios que representan los héroes.
    """
    lista = []
    with open(nombre_archivo) as archivo:
        data = json.load(archivo)
        lista = data["jugadores"]
    
    return lista

lista_dream_team = leer_archivo(r"C:\Users\Torre\Documents\Programacion\Clase_11_Parcial\dt.json")

def mostrar_lista_clave(lista:list, clave:str):
    contenido =""
    for jugador in lista:
        mensaje = "{0} - {1}".format(jugador["nombre"], jugador[clave])
        contenido += mensaje+"\n"
    print(contenido)

def mostrar_jugador_estadistica(lista:list):
    indice = input("Ingrese el indice. ")
    indice = int(indice)
    for clave, valor in lista[indice]["estadisticas"].items():
        print(f"{(clave.capitalize())}: {valor}")


def mostrar_jugador_logros(lista:list):

    
    jugadores = str([(diccionario["nombre"]).lower()  for diccionario in lista])
    jugador = input("Ingrese el nombre del jugador.")
    while not (re.search(jugador.lower(), jugadores)):
        jugador = input("Error. Ingrese el nombre del jugador.")

    for indice in range(len(lista)):
        if re.search(jugador.lower(), (lista[indice]["nombre"]).lower()):
            jugador_encontrado = indice
            print(jugador_encontrado)

    
    mensaje = "{0} - {1}".format(lista[jugador_encontrado]["nombre"], 
                                 lista[jugador_encontrado]["logros"])
    
    print(mensaje)

mostrar_jugador_logros(lista_dream_team)

# jugadores = [diccionario["nombre"]  for diccionario in lista_dream_team]
# print(jugadores)