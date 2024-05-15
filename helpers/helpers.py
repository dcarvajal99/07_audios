import pandas as pd
import re
import os
import sys

class Helpers: 
    
    def df_definer(xls):
        df = pd.read_excel(xls)
        # Guardar una lista con los rut de la columna rut de cada dataframe
        rut = df['RUT'].tolist()
        # Necesito cambiar el formato de rut a 'rut'
        rut = [str(r) for r in rut]
        # Consultar si mi columna Fec_Gest existe en el dataframe
        fec_col = ''
        fec_cols = ['FECHA DE GESTION','fec_gest', 'Fec_Gest', 'FECHA_GESTION', 'Fecha_Gestion', 'fecha_gestion', 'Fecha de Gestion', 'fecha de gestion']
        for col in fec_cols:
            if col in df.columns:
                fec_col = col
                break
        if fec_col == '':
            print('No se encontró la columna de fecha de gestión')
            sys.exit()

        # Convertir en string la columna Fec_Gest
        df[fec_col] = df[fec_col].astype(str)
        
        # Formatear fechas y llenar vacíos
        formatted_dates = []
        for fecha in df[fec_col]:
            if re.match(r'\d{4}-\d{2}-\d{2}', fecha):  # Si ya está en formato aaaa-mm-dd
                formatted_dates.append(fecha.split()[0])  # Solo tomar la parte de la fecha si hay una marca de tiempo
            elif re.match(r'\d{2}-\d{2}-\d{4}', fecha):  # Si está en formato dd-mm-aaaa
                formatted_dates.append("-".join(fecha.split("-")[::-1]))
            else:
                formatted_dates.append("2000-01-01")  # Si está vacía o no es un formato reconocido, se llena con 2000-01-01

        return rut, formatted_dates
    
    def dir_campaing(campaña):
        if campaña == 'default':
            base_dir = r'C:\07_Audios\ASESORIA_DE_DENUNCIAS_ZURICH'
        elif campaña == 'Siniestros' or campaña == 'RECHAZO_DE_SINIESTRO':
            base_dir = r'D:\hermes_p\Files\16461677473437B4\RECORDS\MULTICAMPANA'
        elif campaña == 'Asistencias':
            base_dir = r'D:\hermes_p\Files\16461677473437B4\RECORDS\ASISTENCIAS'
        elif campaña == 'Contact_Center':
            base_dir = r'D:\hermes_p\Files\16461677473437B4\RECORDS\ENCUESTA_CONTACT_CENTER'
        elif campaña == 'Cancelaciones':
            base_dir = r'D:\hermes_p\Files\16461677473437B4\RECORDS\26467605164415B4'
        elif campaña == 'Retencion':
            base_dir = r'D:\hermes_p\Files\16461677473437B4\RECORDS\RETENCION'
        else:
            print('Campaña no encontrada')
            sys.exit()
        return base_dir


# Ejemplo de uso:
# rut, fechas = Helpers.df_definer('tu_archivo.xlsx')
# print(fechas)
