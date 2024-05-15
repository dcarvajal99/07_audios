import pandas as pd
import re
import os
import sys

from helpers.helpers import Helpers as hp


def rut_list():
    try:
        #ruta de directorio es: C:/07_audios/
        archivo = 'C:/07_audios/data/'
        # concatenar con la ruta del directorio cualquier archivo excel dentro de la carpeta
        name = input("Ingrese el nombre del archivo: ")
        archivo = os.path.join(archivo, name+'.xlsx')
        print(archivo)
        xls = pd.ExcelFile(archivo)
        #crear los dataframes
        #consultar si el archivo tiene una o mas de una hoja 
        if len(xls.sheet_names) == 1:
            rut, fecha = hp.df_definer(xls)
            print(rut, fecha)           
            return rut, fecha
        elif len(xls.sheet_names) == 4:  
            df1 = pd.read_excel(xls, 'Base Siniestros')
            df2 = pd.read_excel(xls, 'TNPS Asistencias')
            df3 = pd.read_excel(xls, 'TNPS Contact Center')
            df4 = pd.read_excel(xls, 'TNPS CANCELACIONES')
            #guardar una lista con los rut de la columna rut de cada dataframe
            rut1 = df1['RUT'].tolist()
            fecha1 = df1['Fec_Gest'].tolist()
            rut2 = df2['RUT'].tolist()
            fecha2 = df2['FECHA_GESTION'].tolist()
            rut3 = df3['RUT_CLIENTE'].tolist()
            fecha3 = df3['FECHA_GESTION'].tolist()
            rut4 = df4['RUT'].tolist()
            fecha4 = df4['FECHA_GESTION'].tolist()
            return rut1, fecha1, rut2, fecha2, rut3, fecha3, rut4, fecha4
        else:
            print("El archivo no tiene 1 o 4 hojas")
    except FileNotFoundError:
        print("No se encontraron archivos en la carpeta")
        sys.exit()
