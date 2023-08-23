"""
 * Developed by Felipe A. Mesa N, Olga P. Fuentes, Johann F. Osma.
 * Universidad de los Andes. Reaserch Group CMUA. B10MICROSYSTEMS.
 *
 * These project is based on a template
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
import traceback
from tabulate import tabulate
from matplotlib import pyplot as plt
import numpy
import pyfiglet as dt

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def print_menu_esp():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Mostrar información de los archivos")
    print("3- Añadir información a los archivos")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")
    
def print_menu_eng():
    print("Welcome")
    print("1- Load data from files")
    print("2- Show file data")
    print("3- Add data to files")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Exit")



def load_data(control):
    """
    Carga los datos
    """
    controller.load_data(control)
    pass

def print_show_data(control, language):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    if language == 2:
        msg = "Imprimiendo información de los archivos...\n"
    else: 
        msg = "Printing all files..."
    #llamar función que imprime los archivos
    pass


def print_add_data(control, language):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    #METER ESTA FUNCIÓN ENTERA EN UN WHILE PARA UNA MEJOR EXPERIENCIA DE USUARIO
    if language == 2:
        msg_1 = """
        ARCHIVOS DISPONIBLES:
        (1)-> reagents.csv (REACTIVOS)
        (2)-> equipment.csv (EQUIPOS DE LABORATORIO)
        (3)-> energy_sources.csv (FUENTES DE ENERGÍA)
        (4)-> water_consumption.csv (CONSUMO Y TIPOS DE AGUA)
        """
        msg_2 = "Seleccione el archivo al que quiere añadir información:\n>"
        msg_3 = "IMPORTANTE: Para que la información que registró sea utilizada, debe volver a cargar la información al programa."
        #IMPRIMIR ESTO DE AQUÍ ARRIBA EN COLOR 
    else: 
        msg_1 = """
        AVAILABLE FILES:
        (1)-> reagents.csv (REAGENTS)
        (2)-> equipment.csv (LAB EQUIPMENT)
        (3)-> energy_sources.csv (ENERGY SOURCES)
        (4)-> water_consumption.csv (WATER CONSUMPTION AND TYPES)
        """
        msg_2 = "Select the file you want to add data to:\n>"
    print(msg_1)
    file = int(input(msg_2))
    if file == 1:
        pass #llamar función de inputs para añadir datos a reagents.csv (USAR WHILES PARA METER DATOS)
    elif file == 2:
        pass #llamar función de inputs para añadir datos a equipment.csv (USAR WHILES PARA METER DATOS)
    elif file == 3:
        pass #llamar función de inputs para añadir datos a energy_sources.csv (USAR WHILES PARA METER DATOS)
    elif file == 4:
        pass #llamar función de inputs para añadir datos a water_consumption.csv (USAR WHILES PARA METER DATOS)
    else:
        if language == 2:
            print("Opción errónea, vuelva a elegir.\n")
        else:
            print("Option not available, choose or type again.\n")
    pass


def print_req_3(control, language):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    if language == 2:
        msg = ""
    else: 
        msg = ""
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control, language):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    if language == 2:
        msg = ""
    else: 
        msg = ""
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control, language):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    if language == 2:
        msg = ""
    else: 
        msg = ""
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control, language):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    if language == 2:
        msg = ""
    else: 
        msg = ""
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control, language):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    if language == 2:
        msg = ""
    else: 
        msg = ""
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control, language):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    if language == 2:
        msg = ""
    else: 
        msg = ""
    # TODO: Imprimir el resultado del requerimiento 8
    pass

#mensajes de terminal 
#text = pyfiglet.figlet_format("B1O\nMICRO\nSYSTEMS", "computer",justify="center")
#correr esto en la terminal y coger ese texto para printearlo


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    print("SELECT LANGUAGE/SELECCIONE EL IDIOMA")
    language = int(input("TYPE 1 FOR ENGLISH, PRESIONE 2 PARA ESPAÑOL\n>"))
    
    #ciclo del menu
    while working:
        if language == 2:
            print_menu_esp()
            inputs = input('Seleccione una opción para continuar\n>')
        else:
            print_menu_eng()
            inputs = input('Select an option to continue\n>')
        try:
            if int(inputs) == 1:
                if language == 2:
                    print("Cargando información de los archivos ...\n")
                else: 
                    print("Loading data from files ...\n")
                data = load_data(control)
            elif int(inputs) == 2:
                print_show_data(control, language)

            elif int(inputs) == 3:
                print_add_data(control, language)

            elif int(inputs) == 4:
                print_req_3(control, language)

            elif int(inputs) == 5:
                print_req_4(control, language)

            elif int(inputs) == 6:
                print_req_5(control, language)

            elif int(inputs) == 7:
                print_req_6(control, language)

            elif int(inputs) == 8:
                print_req_7(control, language)

            elif int(inputs) == 9:
                print_req_8(control, language)

            elif int(inputs) == 0:
                working = False
                if language == 2:
                    print("\nGracias por utilizar el programa.")
                else:
                    print("\nThan you for using this software.")
                
            else:
                if language == 2:
                    print("Opción errónea, vuelva a elegir.\n")
                else:
                    print("Option not available, choose or type again.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)