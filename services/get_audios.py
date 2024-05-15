import os
import re
import sys
import paramiko
import datetime

sys.path.append('C:/07_Audios')

from services.mkdir import mkdir
from connections.conn_sftp import Sftp as Sftp
from menus.sftp import sftp_menu
from helpers.helpers import Helpers

# Datos del servidor SFTP
sftplist = [
    {
        "sftp_host" : "200.111.131.198",
        "sftp_port" : 49000,
        "sftp_user" : "zs_bases",
        "sftp_password" : "7!RqdV8Ka8"
    },
    {
        "sftp_host" : "200.111.131.198",
        "sftp_port" : 49000,
        "sftp_user" : "zs_bases",
        "sftp_password" : "7!RqdV8Ka8"
    },
]



def get_audios_by_date(campaña, registros,fechas):
    
    #hacer un case para campaña y bridar 3 rutas diferentes
    base_dir = Helpers.dir_campaing(campaña)

    # crear una funcion que me busque los archivos en la carpeta records mi lista de ruts y me devuelva los archivos encontrados
    def buscar_grabaciones(ruts, fechas, directorio):
        grabaciones_encontradas = []
        for rut in ruts:
            for fecha in fechas:
                # Formateamos la fecha correctamente para buscarla en la ruta
                fecha_formateada = fecha.replace('-', os.sep)
                # Construimos la ruta base con la fecha
                ruta_fecha_base = os.path.join(directorio, fecha_formateada)
                if os.path.exists(ruta_fecha_base):
                    # Buscamos archivos dentro de la carpeta correspondiente a la fecha
                    for archivo_fecha in os.listdir(ruta_fecha_base):
                        if rut in archivo_fecha:
                            grabaciones_encontradas.append(os.path.join(ruta_fecha_base, archivo_fecha))
                            # print(f"Se encontró una coincidencia de rut ({rut}) en la fecha {fecha}: {os.path.join(ruta_fecha_base, archivo_fecha)}")
        return grabaciones_encontradas

    # Directorio donde buscar las grabaciones
    directorio_raiz = base_dir  # Usa el directorio según la campaña
    print("directorio_raiz: ",directorio_raiz)
    #fechas = [fecha.replace('-', '/') for fecha in fechas]
    grabaciones_encontradas = buscar_grabaciones(registros, fechas, directorio_raiz)

    if grabaciones_encontradas:
        print("Se encontraron las siguientes grabaciones:")
        for grabacion in grabaciones_encontradas:
            print(grabacion)
    else:
        print("No se encontraron grabaciones para los ruts proporcionados en las fechas especificadas.")
        exit()
    

    try:
        sftp_host, sftp_port, sftp_user, sftp_password = sftp_menu().values()
        print("aaaaaaaaaaaaaaaa",sftp_host, sftp_port, sftp_user, sftp_password)
        sftp = Sftp(sftp_host, sftp_port, sftp_user, sftp_password)
        # Crear una conexión SSH
        sftp.connect()
        print("Conexión SFTP establecida con éxito.")
    except Exception as e:
        print(f"Error al abrir la conexión SFTP: {e}")
        sftp.close()
        exit()

    # Directorio remoto en el servidor SFTP
    remote_records_dir = "/Upload/08_Audios/Audios_Auditoria_Abril_24/"+campaña
    
    #verificar si existe la carpeta records en el servidor
    mkdir(remote_records_dir)
    
    
    # Subir archivos faltantes
    for local_file in grabaciones_encontradas:
        remote_filename = os.path.basename(local_file)  # Obtener solo el nombre del archivo
        remote_path = f"{remote_records_dir}/{remote_filename}"  # Concatenar la carpeta remota con el nombre del archivo
        try:
            sftp.put(local_file, remote_path)
            print(f"Archivo '{remote_filename}' subido a la carpeta 'records' en el servidor.")
        except Exception as e:
            print(f"Error al subir el archivo '{remote_filename}': {e}")
    
    #obtner el mes anterior en formato de mm
    mes = datetime.datetime.now().strftime('%m')
    #obtener el dia actual en formato de dd
    dia = datetime.datetime.now().strftime('%d')

    # Directorio remoto en el servidor SFTP
    remote_records_dir = "/Upload/08_Audios/Audios_Auditoria_Abril_24/"+campaña+"/"+dia
    mkdir(remote_records_dir)

    num_archivos_subidos = 0  # Variable para contar la cantidad de archivos subidos
    for local_file in grabaciones_encontradas:
        remote_filename = os.path.basename(local_file)  # Obtener solo el nombre del archivo
        remote_path = f"{remote_records_dir}/{remote_filename}"  # Concatenar la carpeta remota con el nombre del archivo
        try:
            sftp.put(local_file, remote_path)
            print(f"Archivo '{remote_filename}' subido a la carpeta 'records' en el servidor.")
            num_archivos_subidos += 1  # Incrementar el contador de archivos subidos
        except Exception as e:
            print(f"Error al subir el archivo '{remote_filename}': {e}")

    # Imprimir el resumen
    print(f"Se subieron {num_archivos_subidos} archivos al SFTP.")

    # Cerrar la conexión SFTP y SSH
    sftp.close()