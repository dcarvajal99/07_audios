import sys

sys.path.append('C:/07_Audios')

from menus.campaigns_menu import menu as campaigns_menu
from services.get_audios_by_date import get_audios_by_date
from services.rut_list import rut_list



def menu():

    while True:
        print("1. Cargar registros de archivo excel")
        print("2. Cargar registros manualmente")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registros, fechas = rut_list()
            campaigns_menu(registros, fechas)
        elif opcion == "2":
            #hacer inputs consultando la campaña y los ruts
            campaña = input("Ingrese nombre de la campaña para buscar audios:")
            registros = input("Ingrese los ruts separados por coma:")
            registros = registros.split(',')
            fechas = input("Ingrese las fechas separadas por coma:")
            fechas = fechas.split(',')
            get_audios_by_date(campaña, registros, fechas)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


