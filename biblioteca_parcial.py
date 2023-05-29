import json
import re
from tabulate import tabulate

def leer_archivo(nombre_archivo: str):
    """
    Lee un archivo JSON y devuelve una lista de héroes.
    Recibe el nombre del archivo JSON a leer.
    Retorna una lista de diccionarios que representan los héroes.
    """
    lista = []
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        data = json.load(archivo)
        lista = data["jugadores"]
    
    return lista

lista_dream_team = leer_archivo(r"C:\Users\Torre\Documents\Parcial_Programacion_I\pp_lab1_Torres_Almada_Marcelo\dt.json")

def guardar_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, mode='w+') as archivo:
            archivo.write(contenido)
            mensaje = f'Se creó el archivo: {nombre_archivo}'
            return mensaje
    except Exception as e:
        mensaje = f'Error al crear el archivo: {nombre_archivo}. {str(e)}'
        return mensaje

def mostrar_lista_clave(lista:list, clave:str):
    mensaje=""
    for jugador in lista:
        mensaje += "{0} - {1}\n".format(jugador["nombre"], jugador[clave])
    
    return mensaje.rstrip()


def mostrar_jugador_estadistica(lista:list):
    indices= "Estos son los indices junto a los jugadores que representan:"
    for indice in range(len(lista)):
        indices +="\n{0}.{1}".format(str(indice),lista[indice]["nombre"])
    print(indices)
    indice = input("Ingrese el indice del jugador buscado. ")
    patron = r'^([0-9]|1[01])$'
    while not re.match(patron,indice):
        print("\n"+indices)
        indice = input("Ingreso incorrecto. Por favor ingrese el indice del jugador buscado. ")        
    indice = int(indice)
    mensaje = "Nombre: {0}".format(lista[indice]["nombre"])
    for clave, valor in lista[indice]["estadisticas"].items():
        mensaje += "\n{0}: {1}".format(clave.capitalize(), valor)
    print(mensaje)

    return indice

#Punto 3

def guardar_csv_jugador_punto_dos(lista:list ,indice:int):
    contenido ="Nombre"
    mensaje="\n"+lista[indice]["nombre"]+""
    for clave, valor in lista[indice]["estadisticas"].items(): 
        contenido += ",{0}".format(clave.capitalize())
        mensaje += ",{0}".format(valor)
    nombre_archivo = (lista[indice]["nombre"]).lower().replace(" ", "_")+"_estadisticas.csv"
    contenido +=mensaje
    
    return guardar_archivo(nombre_archivo, contenido)


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
            elif lista_ordenada[indice_A][clave][0] == lista_ordenada[indice_A+1][clave][0]:
                if  lista_ordenada[indice_A][clave][1] > lista_ordenada[indice_A+1][clave][1]:
                    lista_ordenada[indice_A],lista_ordenada[indice_A+1] = lista_ordenada[indice_A+1],lista_ordenada[indice_A]
                    flag_swap = True
                elif lista_ordenada[indice_A][clave][1] == lista_ordenada[indice_A+1][clave][1]:
                    if lista_ordenada[indice_A][clave][2] > lista_ordenada[indice_A+1][clave][2]:
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
    
    return contenido


'''
Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es
miembro del Salón de la Fama del Baloncesto.
'''
def es_miembro_salon_de_la_fama(lista:list):
    logros = mostrar_jugador_logros(lista)
    if "Baloncesto Universitario" in logros:
        mensaje = "Es miembro del Salón de la Fama del Baloncesto Universitario"
    elif "Miembro del Salon de la Fama del Baloncesto" in logros:
        mensaje = "Es miembro del Salón de la Fama del Baloncesto"
    else:
        mensaje = "No pertecece al Salón de la Fama."

    return mensaje


'''
7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
'''

def calcular_y_mostrar_maximo_estadistica_clave(lista:list, clave:str):
    max_clave = lista[0]["estadisticas"][clave]
    lista_maximos=[lista[0]["nombre"]]
    for jugador in lista[1:]:
        clave_valor = jugador["estadisticas"][clave]
        if(clave_valor > max_clave ):
            max_clave = clave_valor
            lista_maximos.clear()
            lista_maximos.append(jugador["nombre"])
        elif (clave_valor == max_clave ):
            max_clave = clave_valor
            lista_maximos.append(" y "+ jugador["nombre"])
    
    mensaje="La estadistica de mayor {0} pertenece a ".format(clave.replace("_", " "))
    if len(lista_maximos) ==1:
        mensaje += lista_maximos[0]
    else:
        for maximo in lista_maximos:
            mensaje += "{0}".format(maximo)
    mensaje+= " con un valor de {0}.".format(str(max_clave))
    
    return mensaje
    
'''
10) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
más puntos por partido que ese valor.
11) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
más rebotes por partido que ese valor.
12) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
más asistencias por partido que ese valor.
'''

def jugador_con_valor_mayor_al_ingresado(lista:list, clave:str):
    valor_ingresado = input("Ingrese un valor. ")
    valor_ingresado = float(valor_ingresado)
    flag_primer_ingreso = 0
    mensaje = ("En cuanto a {0} los siguientes jugadores superan el valor" 
               " ingresado :").format(clave.replace("_", " "))

    for jugador in lista:
        if jugador["estadisticas"][clave] > valor_ingresado:
            mensaje += "\n{0} con un valor de {1}.".format(jugador["nombre"], 
                                                              jugador["estadisticas"][clave])
            flag_primer_ingreso = 1
        
    if flag_primer_ingreso ==0:
        mensaje = "No hay ningun jugador que supere ese {0}.".format(clave.replace("_", " "))
    
    return mensaje
   
'''
16) Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al
jugador con la menor cantidad de puntos por partido.
'''
def calcular_y_mostrar_minimo_estadistica_clave(lista:list, clave:str):
    min_clave = lista[0]["estadisticas"][clave]
    contador = 0
    for jugador in lista[1:]:
        clave_valor = jugador["estadisticas"][clave]
        if(clave_valor < min_clave ):
            min_clave = clave_valor
            contador=1
        elif (clave_valor == min_clave ):
            min_clave = clave_valor
            contador += 1
    return contador*clave_valor


def calcular_promedio_excluyendo_al_minimo(lista:list, clave:str):
    suma = -calcular_y_mostrar_minimo_estadistica_clave(lista_dream_team, clave)
    for jugador in lista:
        suma += jugador["estadisticas"][clave]
    promedio = suma/ (len(lista)-1)
    contenido = "Promedio del equipo: "+str(promedio)

    return contenido



'''
17) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
'''
def calcular_y_mostrar_jugador_mas_logros(lista:list):
    lista_logros=[]
    lista_logros_jugador=[]
    for jugador in lista:
        contador=0
        lista_logros_jugador.append(jugador["nombre"])
        for logro in jugador["logros"]:
            match= re.search(r'^\d+', logro)
            if match:
                contador += int(match.group(0))
            else:
                contador += 1
        lista_logros.append(contador)
    
    max_clave = lista_logros[0]
    lista_maximos=[lista_logros_jugador[0]]
    for indice in range(1, len(lista_logros)):
        clave_valor = lista_logros[indice]
        if(clave_valor > max_clave ):
            max_clave = clave_valor
            lista_maximos.clear()
            lista_maximos.append(lista_logros_jugador[indice])
        elif (clave_valor == max_clave ):
            max_clave = clave_valor
            lista_maximos.append(" | "+ lista_logros_jugador[indice])
    
    if len(lista_maximos) ==1:
        mensaje="El jugador con mayor cantidad de logros es "
        mensaje += lista_maximos[0]
    else:
        mensaje="Los jugadores con mayor cantidad de logros son "
        for maximo in lista_maximos:
            mensaje += "{0}".format(maximo)
    mensaje+= " con un valor de {0} logros.".format(str(max_clave))
    
    return mensaje

 
'''
20) Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por
posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a
ese valor.
'''
def jugador_con_valor_mayor_al_ingresado2(lista:list, clave:str):
    valor_ingresado = input("Ingrese un valor. ")
    valor_ingresado = float(valor_ingresado)
    flag_primer_ingreso = 0
    mensaje = ("En cuanto a {0}, los siguientes jugadores superan el valor" 
               " ingresado :").format(clave.replace("_", " "))

    for jugador in lista:
        if jugador["estadisticas"][clave] > valor_ingresado:
            mensaje += "\n{0} ({2}) con un valor de {1}.".format(jugador["nombre"], 
                                                              jugador["estadisticas"][clave],
                                                              jugador["posicion"])
            flag_primer_ingreso = 1
        
    if flag_primer_ingreso ==0:
        mensaje = "No hay ningun jugador que supere ese {0}.".format(clave.replace("_", " "))
    
    return mensaje

def mostrar_jugadores_mayor_al_dato_ingresado_ordenado_por_posicion(lista):
    lista_ordenada = ordenar_alfabeticamente_por_clave_ascendente(lista,"posicion")
    
    return jugador_con_valor_mayor_al_ingresado2(lista_ordenada, "porcentaje_tiros_de_campo")


'''
Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking 
● Puntos ● Rebotes ● Asistencias ● Robos
'''

def ordenar_y_listar_por_clave(lista_original:list, clave:str)->list:
    lista_de = []
    lista_iz = []

    if(len(lista_original)<=1):
        return lista_original
    else:
        pivot = lista_original[0]["estadisticas"][clave]
        for jugador in lista_original[1:]:
            if(jugador["estadisticas"][clave] < pivot):
                lista_de.append(jugador)
            else:
                lista_iz.append(jugador)
    
    lista_iz = ordenar_y_listar_por_clave(lista_iz, clave)
    lista_iz.append(lista_original[0]) 
    lista_de = ordenar_y_listar_por_clave(lista_de, clave)
    lista_iz.extend(lista_de) 
    return lista_iz

def crear_lista_de_nombres(lista:list):
    lista_nombres=[]
    lista_puntos=[]
    for jugador in lista:
        lista_nombres.append(jugador["nombre"])
        lista_puntos.append(jugador["estadisticas"]["puntos_totales"])
    
    return lista_nombres

def crear_y_guardar_ranking(lista:list):
    lista_nombres_ordenada_alfa = crear_lista_de_nombres(ordenar_alfabeticamente_por_clave_ascendente(lista, "nombre"))
    lista_puntos_totales= crear_lista_de_nombres(ordenar_y_listar_por_clave(lista, "puntos_totales"))
    lista_rebotes_totales= crear_lista_de_nombres(ordenar_y_listar_por_clave(lista, "rebotes_totales"))
    lista_asistencias_totales= crear_lista_de_nombres(ordenar_y_listar_por_clave(lista, "asistencias_totales"))
    lista_robos_totales= crear_lista_de_nombres(ordenar_y_listar_por_clave(lista, "robos_totales"))
    contenido = "Jugador|Puntos|Rebotes|Asistencias|Robos"
  
    for indice in range(len(lista_nombres_ordenada_alfa)):
        contenido += "\n{0}|{1}|{2}|{3}|{4}".format(lista_nombres_ordenada_alfa[indice],
                                                                             1+lista_puntos_totales.index(lista_nombres_ordenada_alfa[indice]),
                                                                             1+lista_rebotes_totales.index(lista_nombres_ordenada_alfa[indice]),
                                                                             1+lista_asistencias_totales.index(lista_nombres_ordenada_alfa[indice]),
                                                                             1+lista_robos_totales.index(lista_nombres_ordenada_alfa[indice]))
    filas = [fila.split('|') for fila in contenido.split('\n')]
    tabla = tabulate(filas, headers="firstrow", tablefmt="pipe")
    print(tabla)

    return guardar_archivo("ranking_dream_team.csv", contenido.replace("|", ","))


def imprimir_menu():
    menu = '''Menú de opciones:
    1.  Mostrar a los miembros del Dream Team junto a su posición.
    2.  Mostrar estadisticas del jugador seleccionado, ingresando su indice.
    3.  Exportar a un archivo CSV las estadisticas obtenidas en el punto 2.
    4.  Ingresar el nombre de un jugador y mostrar sus logros.
    5.  Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.
    6.  Ingresar el nombre de un jugador y mostrar si pertenece al Salón de la Fama.
    7.  Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
    8.  Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
    9.  Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
    10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.
    11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.
    12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.
    13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.
    14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
    15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
    16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
    17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.
    18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.
    19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.
    20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.
    23. Mostrar el ranking por cantidad de puntos, rebotes, asistencias y robos.
    0. Salir.'''
    print(menu)
    

def validar_respuesta():
    patron = r'^([0-9]|1[0-9]|20|23)$'
    respuesta = input("Ingrese la opción deseada: ")
    while not re.match(patron, respuesta):
        respuesta= input("Respuesta inválida. Por favor, ingrese una opción del menú: ")

    return int(respuesta)
    
