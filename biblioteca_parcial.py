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

lista_dream_team = leer_archivo(r"C:\Users\Torre\Documents\Parcial_Programacion_I\pp_lab1_Torres_Almada_Marcelo\dt.json")

def mostrar_lista_clave(lista:list, clave:str):
    contenido =""
    for jugador in lista:
        mensaje = "{0} - {1}".format(jugador["nombre"], jugador[clave])
        contenido += mensaje+"\n"
    print(contenido.rstrip())

#mostrar_lista_clave(lista_dream_team, "posicion")

def mostrar_jugador_estadistica(lista:list):
    indice = input("Ingrese el indice. ")
    indice = int(indice)
    contenido = "Nombre: {0}\n".format(lista[indice]["nombre"])
    for clave, valor in lista[indice]["estadisticas"].items():
        mensaje = "{0}: {1}".format(clave.capitalize(), valor)
        contenido += mensaje +"\n"
    print(contenido.rstrip())

#mostrar_jugador_estadistica(lista_dream_team)
def validar_jugador_ingresado(lista:list):
    jugadores = str([(diccionario["nombre"]).lower()  for diccionario in lista])
    jugador_buscado = input("Ingrese el nombre del jugador.")
    while not (re.search(jugador_buscado.lower(), jugadores)):
        jugador_buscado = input("Error. Ingrese el nombre del jugador.")
    for jugador in lista:
        if re.search(jugador_buscado.lower(), (jugador["nombre"]).lower()):
            nombre = jugador["nombre"]
    return nombre

def mostrar_jugador_logros(lista:list):
    jugador_buscado = validar_jugador_ingresado(lista)
    for indice in range(len(lista)):
        if jugador_buscado == lista[indice]["nombre"]:
            jugador_encontrado = indice

    mensaje = "{0} - {1}".format(lista[jugador_encontrado]["nombre"], 
                                 lista[jugador_encontrado]["logros"])
    return mensaje

# mostrar_jugador_logros(lista_dream_team)

'''
Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
Team, ordenado por nombre de manera ascendente
'''
def ordenar_alfabeticamente_por_clave_ascendente(lista:list, clave:str):
    lista_ordenada = lista[:]
    rango_a = len(lista_ordenada)
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if  lista_ordenada[indice_A][clave][0] > lista_ordenada[indice_A+1][clave][0]:
                lista_ordenada[indice_A],lista_ordenada[indice_A+1] = lista_ordenada[indice_A+1],lista_ordenada[indice_A]
                flag_swap = True

    return lista_ordenada

def calcular_y_mostrar_promedio_puntos_orden_alfa_asc(lista:list):
    lista_ordenada = ordenar_alfabeticamente_por_clave_ascendente(lista,"nombre")
    suma = 0
    contenido=""
    for jugador in lista_ordenada:
        suma += jugador["estadisticas"]["promedio_puntos_por_partido"]
        mensaje = "{0}: {1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"])
        contenido += mensaje+ "\n"
    
    promedio = suma/ len(lista_ordenada)
    contenido += "Promedio del equipo: "+str(promedio)
    print(contenido)

#calcular_y_mostrar_promedio_puntos_orden_alfa_asc(lista_dream_team)

'''
Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es
miembro del Salón de la Fama del Baloncesto.
'''
def es_miembro_salon_de_la_fama(lista:list):
    logros = mostrar_jugador_logros(lista)
    if "Baloncesto Universitario" in logros:
        print("Baloncesto Universitario")
    elif "Miembro del Salón de la Fama del Baloncesto" in logros:
        print("fama comun")
    else:
        print("nada")

#es_miembro_salon_de_la_fama(lista_dream_team)

'''
7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
'''

def calcular_y_mostrar_maximo_estadistica_clave(lista:list, clave:str):
    max_clave = lista[0]["estadisticas"][clave]
    lista_maximos=[]
    for jugador in lista[1:]:
        clave_valor = jugador["estadisticas"][clave]
        if(clave_valor > max_clave ):
            max_clave = clave_valor
            lista_maximos.clear()
            lista_maximos.append(jugador["nombre"])
        elif (clave_valor == max_clave ):
            max_clave = clave_valor
            lista_maximos.append(" y "+ jugador["nombre"])
    
    mensaje="La estadistica de mayor {0} pertenece a ".format(clave)
    if len(lista_maximos) ==1:
        mensaje += lista_maximos[0]
    else:
        for maximo in lista_maximos:
            mensaje += "{0}".format(maximo)
    mensaje+= " con un valor de {0}.".format(str(max_clave))
    print(mensaje)
    
    # print(maximo) 
    # print(lista[indice_max]["nombre"]+str(lista[indice_max]["estadisticas"][clave]))       
    # return lista[indice_max]


