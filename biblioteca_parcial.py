import json
import re
from tabulate import tabulate

def leer_archivo(nombre_archivo: str) -> list:
    """
    Lee un archivo JSON y devuelve una lista de jugadores.

    Args:
        nombre_archivo (str): El nombre o la ruta del archivo JSON a leer.

    Returns:
        lista (list): Una lista de diccionarios que representan a los jugadores.

    """
    lista = []
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        data = json.load(archivo)
        lista = data["jugadores"]
    
    return lista

lista_dream_team = leer_archivo(r"C:\Users\Torre\Documents\Parcial_Programacion_I\pp_lab1_Torres_Almada_Marcelo\dt.json")

def guardar_archivo(nombre_archivo, contenido) -> str:
    """
    Guarda el contenido en un archivo especificado.

    Args:
        nombre_archivo (str): El nombre o la ruta del archivo a guardar.
        contenido (str): El contenido a escribir en el archivo.

    Returns:
        mensaje (str): Un mensaje que indica si se creó exitosamente el archivo 
        o si ocurrió un error.

    """
    try:
        with open(nombre_archivo, mode='w+') as archivo:
            archivo.write(contenido)
            mensaje = f'\nSe creó el archivo: {nombre_archivo}'
            return mensaje
    except Exception as e:
        mensaje = f'\nError al crear el archivo: {nombre_archivo}. {str(e)}'
        return mensaje

def mostrar_lista_jugador_y_clave(lista:list, clave:str) -> str:
    """
    Muestra jugador junto a la respectiva clave asociada al diccionario jugador.

    Args:
        lista (list): La lista de diccionarios que representa a cada jugador
        del Dream Team.
        clave (str): La clave del diccionario a imprimir .

    Returns:
        mensaje (str): Un mensaje formateado con el nombre del jugador y la 
        clave correspondiente.

    """
    mensaje="\nNombre del jugador junto a su posición:"
    for jugador in lista:
        mensaje += "\n{0} - {1}".format(jugador["nombre"], jugador[clave])
    
    return mensaje


def mostrar_jugador_estadistica(lista:list) -> int:
    """
    Muestra las estadisticas que pertenecen al jugador ingresado a traves de su indice.

    Args:
        lista (list): La lista de diccionarios que representa a cada jugador del 
        Dream Team.

    Returns:
        indice (int): Un numero entero que representa al indice del jugador elegido.

    """
    indices= "\nEstos son los indices junto a los jugadores que representan:"
    for indice in range(len(lista)):
        indices +="\n{0}.{1}".format(str(indice),lista[indice]["nombre"])
    print(indices)
    indice = input("Ingrese el indice del jugador buscado. ")
    patron = r'^([0-9]|1[01])$'
    while not re.match(patron,indice):
        print("\n"+indices)
        indice = input("Ingreso incorrecto. Por favor ingrese el indice del jugador buscado. ")        
    indice = int(indice)
    mensaje = "\nNombre: {0}".format(lista[indice]["nombre"])
    for clave, valor in lista[indice]["estadisticas"].items():
        mensaje += "\n{0}: {1}".format(clave.capitalize(), valor)
    print(mensaje)

    return indice

def guardar_csv_jugador_punto_dos(lista:list ,indice:int) -> str:
    '''
    Guarda las estadísticas de un jugador en formato CSV.
    La función toma la lista de jugadores, selecciona el jugador en el índice especificado y
    guarda sus estadísticas
    en un archivo CSV. El nombre del archivo se genera a partir del nombre del jugador.

    Args:
        lista (list): La lista de jugadores.
        indice (int): El índice del jugador cuyas estadísticas se guardarán.

    Returns:
        str: Un mensaje que indica si se creó exitosamente el archivo CSV o si ocurrió un 
        error.
    '''
    contenido ="Nombre"
    mensaje="\n"+lista[indice]["nombre"]+""
    for clave, valor in lista[indice]["estadisticas"].items(): 
        contenido += ",{0}".format(clave.capitalize())
        mensaje += ",{0}".format(valor)
    nombre_archivo = (lista[indice]["nombre"]).lower().replace(" ", "_")+"_estadisticas.csv"
    contenido +=mensaje
    
    return guardar_archivo(nombre_archivo, contenido)

def validar_jugador_ingresado(lista:list) -> str:
    '''
    Valida si un jugador ingresado se encuentra en una lista de jugadores.
    La función recorre la lista de jugadores y solicita al usuario ingresar el nombre de 
    un jugador. Luego, busca el nombre del jugador ingresado en la lista de jugadores. 
    Si se encuentra una coincidencia, se devuelve el nombre del jugador encontrado.

    Args:
        lista (list): La lista de jugadores.

    Returns:
        nombre (str): El nombre del jugador encontrado.

    '''
    jugadores = str([(diccionario["nombre"]).lower()  for diccionario in lista])
    jugador_buscado = input("Ingrese el nombre del jugador.")
    while not (re.search(jugador_buscado.lower(), jugadores)):
        jugador_buscado = input("Error. Ingrese el nombre del jugador.")
    for jugador in lista:
        if re.search(jugador_buscado.lower(), (jugador["nombre"]).lower()):
            nombre = jugador["nombre"]
    print("Jugador encontrado: " +nombre)
    return nombre

def mostrar_jugador_logros(lista:list) -> str:
    '''
    Muestra los logros de un jugador específico en una lista de jugadores.
    La función solicita al usuario ingresar el nombre de un jugador y valida si se 
    encuenntra en la lista. De ser asi, se muestra el nombre del jugador junto con sus logros.

    Args:
        lista (list): La lista de jugadores.

    Returns:
        mensaje (str): Un mensaje que muestra el nombre del jugador y sus logros.
    '''
    jugador_buscado = validar_jugador_ingresado(lista)
    for indice in range(len(lista)):
        if jugador_buscado == lista[indice]["nombre"]:
            jugador_encontrado = indice

    mensaje = "{0} - {1}".format(lista[jugador_encontrado]["nombre"], 
                                 lista[jugador_encontrado]["logros"])
    return mensaje

def ordenar_alfabeticamente_por_clave_ascendente(lista:list, clave:str) -> list:
    '''
    Ordena una lista de diccionarios alfabéticamente ascendente según el valor de una clave específica.

    La función toma una lista de diccionarios y ordena los elementos alfabéticamente ascendente (a-z)
    según el valor de la clave especificada. La ordenación se realiza utilizando el algoritmo de ordenamiento
    de burbuja modificado.

    Args:
        lista (list): La lista de diccionarios a ordenar.
        clave (str): La clave por la cual se ordenara alfabeticamente.

    Returns:
        lista_ordenada (list): Una nueva lista con los diccionarios ordenados alfabéticamente.

    '''
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


def calcular_y_mostrar_promedio_puntos_orden_alfa_asc(lista:list) -> str:
    '''
    Calcula y muestra el promedio de puntos por partido de cada jugador ordenado alfabeticamente (a-z),
    ademas del promedio total del equipo.

    La función calcula el promedio de puntos por partido de cada jugador en la lista de jugadores (ya 
    ordenada por nombre) y muestra el nombre de cada jugador junto con su promedio de puntos por partido y
    el promedio total del equipo.

    Args:
        lista (list): La lista de jugadores.

    Returns:
        contenido (str): Un mensaje con los nombres y promedios de puntos por partido de los jugadores,
                         seguido del promedio del equipo.

    '''
    lista_ordenada = ordenar_alfabeticamente_por_clave_ascendente(lista,"nombre")
    suma = 0
    contenido="\nPromedio de puntos por partido de cada jugador. "
    for jugador in lista_ordenada:
        suma += jugador["estadisticas"]["promedio_puntos_por_partido"]
        mensaje = "\n{0}: {1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"])
        contenido += mensaje
    
    promedio = suma/ len(lista_ordenada)
    contenido += "\n\nPromedio del equipo: "+str(promedio)
    
    return contenido


def es_miembro_salon_de_la_fama(lista:list) -> str:
    '''
    Verifica si un jugador es miembro del Salón de la Fama del baloncesto (Universitario o no).

    La función toma una lista de jugadores y verifica los logros de cada jugador para determinar
    si es miembro del Salón de la Fama del baloncesto. Los logros se obtienen utilizando la función
    mostrar_jugador_logros.

    Args:
        lista (list): La lista de jugadores.

    Returns:
        mensaje (str): Un mensaje que indica si el jugador es miembro del Salón de la Fama o no.
    '''
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

def calcular_y_mostrar_maximo_estadistica_clave(lista:list, clave:str) -> str:
    '''
    Calcula y muestra el jugador con el máximo valor de una estadística.

    La función recorre la lista de jugadores y busca aquel jugador que tenga el máximo valor
    para la estadística especificada por la clave. Luego, muestra el nombre del jugador y el valor
    máximo de la estadística.

    Args:
        lista (list): La lista de jugadores.
        clave (str): La clave de la estadística a considerar.

    Returns:
        mensaje (str): Un mensaje que indica el jugador o jugadores con el máximo valor de la estadística.
    '''
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
    
    mensaje="\nLa estadistica de mayor {0} pertenece a ".format(clave.replace("_", " "))
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

def jugador_con_valor_mayor_al_ingresado(lista:list, clave:str) -> str:
    '''
    Busca los jugadores cuya estadística especificada supere un valor ingresado.

    La función solicita al usuario que ingrese un valor y luego verifica cada jugador de la lista
    para determinar si su estadística asociada a la clave supera dicho valor. Si se encuentran jugadores
    que cumplan esta condición, se muestra el nombre del jugador y el valor de la estadística.

    Args:
        lista (list): La lista de jugadores.
        clave (str): La clave de la estadística a considerar.

    Returns:
        mensaje (str): Un mensaje que indica los jugadores que superan el valor ingresado para la 
                       estadística o si no hay jugadores que lo superen.
    '''
    valor_ingresado = input("Ingrese un valor. ")
    valor_ingresado = float(valor_ingresado)
    flag_primer_ingreso = 0
    mensaje = ("\nEn cuanto a {0} los siguientes jugadores superan el valor" 
               " ingresado :").format(clave.replace("_", " "))

    for jugador in lista:
        if jugador["estadisticas"][clave] > valor_ingresado:
            mensaje += "\n{0} con un valor de {1}.".format(jugador["nombre"], 
                                                              jugador["estadisticas"][clave])
            flag_primer_ingreso = 1
        
    if flag_primer_ingreso ==0:
        mensaje = "\nNo hay ningun jugador que supere ese {0}.".format(clave.replace("_", " "))
    
    return mensaje
   
'''
16) Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al
jugador con la menor cantidad de puntos por partido.
'''
def calcular_y_mostrar_minimo_estadistica_clave(lista:list, clave:str) -> tuple:
    '''
    Calcula el valor mínimo de una estadística específica y lo muestra.

    La función recorre la lista de jugadores y compara el valor de la estadística
    asociada a la clave especificada. Encuentra el valor mínimo y lo devuelve como
    un número de tipo float.

    Args:
        lista (list): La lista de jugadores.
        clave (str): La clave de la estadística a considerar.

    Returns:
        contador,clave_valor (tuple): Una tupla de valores donde el primer valor 
        representa la cantidad de minimos encontrados y el segundo el valor unitario
        del minimo encontrado.
    '''
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
    return contador,clave_valor


def calcular_promedio_excluyendo_al_minimo(lista:list, clave:str) -> str:
    '''
    Calcula el promedio de una estadística específica excluyendo al jugador o jugadores 
    con el valor mínimo.

    La función utiliza la función 'calcular_y_mostrar_minimo_estadistica_clave' para obtener 
    la cantidad de jugadores con valor de estadistica minimos y el valor mínimo de la estadística 
    especificada. Luego, excluye a esos jugadores del cálculo del promedio.

    Args:
        lista (list): La lista de jugadores.
        clave (str): La clave de la estadística a considerar.

    Returns:
        mensaje (str): El mensaje que muestra el promedio del equipo excluyendo al jugador o 
                       jugadores con el valor mínimo de la estadística.
    '''
    valores_minimos = calcular_y_mostrar_minimo_estadistica_clave(lista_dream_team, clave)
    cantidad_minimos, valor_minimo = valores_minimos
    suma = -cantidad_minimos * valor_minimo
    for jugador in lista:
        suma += jugador["estadisticas"][clave]
    promedio = suma/ (len(lista)-cantidad_minimos)
    mensaje = ("\nPromedio del equipo quitando al jugador o jugadores con la menor"
               " cantidad de {0} ({1}): {2}").format(clave.replace("_", " "),
                                                    str(cantidad_minimos * valor_minimo),
                                                    str(promedio))

    return mensaje

'''
17) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
'''
def calcular_y_mostrar_jugador_mas_logros(lista:list) -> str:
    '''
    Calcula y muestra el jugador con la mayor cantidad de logros.

    La función recorre la lista de jugadores y cuenta la cantidad de logros para cada uno. 
    Luego, determina el jugador con la mayor cantidad de logros y muestra un mensaje indicando 
    dicho jugador y la cantidad de logros.

    Args:
        lista (list): La lista de jugadores.

    Returns:
        mensaje (str): El mensaje que indica el jugador o jugadores con la mayor 
        cantidad de logros y la cantidad de logros.
    """
    '''
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
        mensaje= "\nEl jugador con mayor cantidad de logros es "+ lista_maximos[0]
    else:
        mensaje="\nLos jugadores con mayor cantidad de logros son "
        for maximo in lista_maximos:
            mensaje += "{0}".format(maximo)
    mensaje+= " con un valor de {0} logros.".format(str(max_clave))
    
    return mensaje

 
'''
20) Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por
posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a
ese valor.
'''
def jugador_con_valor_mayor_al_ingresado_y_posicion(lista:list, clave:str) -> str:
    '''
    Busca los jugadores cuyo valor de una estadística supere un valor ingresado, 
    muestra su nombre y posición.

    La función solicita al usuario que ingrese un valor y compara ese valor con la
    estadística especificada para cada jugador de la lista. Si el valor de la estadística 
    es mayor que el valor ingresado, se muestra el nombre del jugador, su valor de 
    estadística y su posición. Al final se genera un mensaje que indica los jugadores que
    superan el valor ingresado junto con su posición.

    Args:
        lista (list): La lista de jugadores.
        clave (str): La clave de la estadística a considerar.

    Returns:
        mensaje (str): El mensaje que indica los jugadores que superan el valor ingresado,
                       su respectivo valor y posición.
    '''
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

def mostrar_jugadores_mayor_al_dato_ingresado_ordenado_por_posicion(lista) -> str:
    '''
    Muestra los jugadores cuyo porcentaje de tiros de campo supere un valor ingresado, 
    ordenados por posición.

    La función ordena la lista de jugadores alfabeticamente por posición y luego utiliza la función 
    "jugador_con_valor_mayor_al_ingresado_y_posicion" para encontrar los jugadores que superan un 
    valor específico de porcentaje de tiros de campo. Finalmente, retorna el mensaje formateado.

    Args:
        lista (list): La lista de jugadores.

    Returns:
        mensaje (str): El mensaje que indica los jugadores que superan el valor ingresado de porcentaje 
                       de tiros de campo, junto a su respectivo valor y ordenados por posición.
    '''
    lista_ordenada = ordenar_alfabeticamente_por_clave_ascendente(lista,"posicion")
    
    return jugador_con_valor_mayor_al_ingresado_y_posicion(lista_ordenada, "porcentaje_tiros_de_campo")


'''
Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking 
● Puntos ● Rebotes ● Asistencias ● Robos
'''

def ordenar_y_listar_por_clave(lista_original:list, clave:str)->list:
    '''
    Ordena una lista de jugadores por una clave específica y devuelve la lista ordenada.

    La función utiliza el algoritmo de ordenamiento rápido (quicksort) para ordenar la lista
    de jugadores en base al valor de la clave especificada. Retorna la lista ordenada.

    Args:
        lista_original (list): La lista original de jugadores.
        clave (str): La clave por la cual se va a realizar el ordenamiento.

    Returns:
        lista_ordenada (list): La lista ordenada de jugadores.
    '''
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
    '''
    Crea una lista de nombres de jugadores a partir de una lista de jugadores.

    La función recorre la lista de jugadores y extrae el nombre de cada jugador,
    agregándolo a una lista de nombres. Retorna la lista de nombres resultante.

    Args:
        lista (list): La lista de jugadores.

    Returns:
        lista_nombres (list): La lista de nombres de jugadores.
    '''
    lista_nombres=[]
    lista_puntos=[]
    for jugador in lista:
        lista_nombres.append(jugador["nombre"])
        lista_puntos.append(jugador["estadisticas"]["puntos_totales"])
    
    return lista_nombres

def crear_y_guardar_ranking(lista:list):
    '''
    Crea un ranking de jugadores y lo guarda en un archivo CSV.

    La función genera listas ordenadas por clave utilizando "ordenar_y_listar_por_clave"
    y alfabeticamente utilizando "ordenar_alfabeticamente_por_clave_ascendente". De dichas 
    listas se extraen unicamente los nombres de los jugadores ya ordenados, luego a través 
    de la funcion index() se obtiene que lugar ocupa el nombre de jugador en cada lista
    (indice) y se le suma 1 para que en el ranking aparezca de 1-12 y no de 0-11.
    Se le da formato de tabla al mensaje utilizando el método tabulate y se imprime en 
    consola y por ultimo se guarda en un archivo CSV.

    Args:
        lista (list): La lista de jugadores.

    Returns:
        mensaje (str): Un mensaje que indica si se creó exitosamente el archivo 
                       o si ocurrió un error.
    '''
    lista_puntos_totales= crear_lista_de_nombres(ordenar_y_listar_por_clave(lista, "puntos_totales"))
    lista_rebotes_totales= crear_lista_de_nombres(ordenar_y_listar_por_clave(lista, "rebotes_totales"))
    lista_asistencias_totales= crear_lista_de_nombres(ordenar_y_listar_por_clave(lista, "asistencias_totales"))
    lista_robos_totales= crear_lista_de_nombres(ordenar_y_listar_por_clave(lista, "robos_totales"))
    lista_nombres_ordenada_alfa = crear_lista_de_nombres(ordenar_alfabeticamente_por_clave_ascendente(lista, "nombre"))
    print(" ")
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
    

def validar_respuesta() -> int:
    '''
    Valida una respuesta numérica ingresada por el usuario.

    La función solicita al usuario que ingrese una opción del menú y valida que la 
    respuesta sea un número entre 0-20 y 23. Si la respuesta no cumple con el patrón 
    establecido, se solicita nuevamente al usuario que ingrese una opción válida.

    Returns:
        int(respuesta) (int): La respuesta válida ingresada por el usuario casteada
                              a entero.
    '''
    patron = r'^([0-9]|1[0-9]|20|23)$'
    respuesta = input("Ingrese la opción deseada: ")
    while not re.match(patron, respuesta):
        respuesta= input("Respuesta inválida. Por favor, ingrese una opción del menú: ")

    return int(respuesta)
    
