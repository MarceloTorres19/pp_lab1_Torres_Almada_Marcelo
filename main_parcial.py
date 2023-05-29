import biblioteca_parcial

def parcial_app(lista:list):
    if lista ==[]:
        print("La lista se encuentra vacia.")
        exit()
    flag_punto_dos =0
    while True:
        biblioteca_parcial.imprimir_menu()
        opcion = biblioteca_parcial.validar_respuesta()
        match (opcion):
            case 1:
                mensaje = biblioteca_parcial.mostrar_lista_jugador_y_clave(lista, "posicion")
            case 2:
                indice = biblioteca_parcial.mostrar_jugador_estadistica(lista)
                flag_punto_dos = 1
                mensaje = "Puede acceder al punto 3"
            case 3:
                if flag_punto_dos == 1:
                    mensaje = biblioteca_parcial.guardar_csv_jugador_punto_dos(lista,indice)
                else:
                    mensaje ="Primero debe utilizar la funcion 2."
            case 4:
                mensaje = biblioteca_parcial.mostrar_jugador_logros(lista)
            case 5:
                mensaje = biblioteca_parcial.calcular_y_mostrar_promedio_puntos_orden_alfa_asc(lista)
            case 6:
                mensaje = biblioteca_parcial.es_miembro_salon_de_la_fama(lista)
            case 7:
                mensaje = biblioteca_parcial.calcular_y_mostrar_maximo_estadistica_clave(lista, "rebotes_totales")
            case 8:
                mensaje = biblioteca_parcial.calcular_y_mostrar_maximo_estadistica_clave(lista, "porcentaje_tiros_de_campo")
            case 9:
                mensaje = biblioteca_parcial.calcular_y_mostrar_maximo_estadistica_clave(lista, "asistencias_totales")
            case 10:
                mensaje = biblioteca_parcial.jugador_con_valor_mayor_al_ingresado(lista, "promedio_puntos_por_partido")
            case 11:
                mensaje = biblioteca_parcial.jugador_con_valor_mayor_al_ingresado(lista, "promedio_rebotes_por_partido")
            case 12:
                mensaje = biblioteca_parcial.jugador_con_valor_mayor_al_ingresado(lista, "promedio_asistencias_por_partido")
            case 13:
                mensaje = biblioteca_parcial.calcular_y_mostrar_maximo_estadistica_clave(lista, "robos_totales")
            case 14:
                mensaje = biblioteca_parcial.calcular_y_mostrar_maximo_estadistica_clave(lista, "bloqueos_totales")
            case 15:
                mensaje = biblioteca_parcial.jugador_con_valor_mayor_al_ingresado(lista, "porcentaje_tiros_libres")
            case 16:
                mensaje = biblioteca_parcial.calcular_promedio_excluyendo_al_minimo(lista, "promedio_puntos_por_partido")
            case 17:
                mensaje = biblioteca_parcial.calcular_y_mostrar_jugador_mas_logros(lista)
            case 18:
                mensaje = biblioteca_parcial.jugador_con_valor_mayor_al_ingresado(lista, "porcentaje_tiros_triples")
            case 19:
                mensaje = biblioteca_parcial.calcular_y_mostrar_maximo_estadistica_clave(lista, "temporadas")
            case 20:
                mensaje = biblioteca_parcial.mostrar_jugadores_mayor_al_dato_ingresado_ordenado_por_posicion(lista)
            case 23:
                mensaje = biblioteca_parcial.crear_y_guardar_ranking(lista)
            case 0:     
                break
        print(mensaje)

        input("\nPulse enter para continuar\n")
    
def main():
    lista_dream_team = biblioteca_parcial.leer_archivo("dt.json")
    parcial_app(lista_dream_team)

main()
