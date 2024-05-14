import os
import re
import sys
import paramiko
import datetime

from services.mkdir import mkdir
import os

# Datos del servidor SFTP
sftp_host = "200.111.131.198"
sftp_port = 49000
sftp_user = "zs_bases"
sftp_password = "7!RqdV8Ka8"

def dir_campaing(campaña):
    if campaña == 'defaults':
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

def get_audios_by_date(campaña, registros,fechas):
    
    #hacer un case para campaña y bridar 3 rutas diferentes
    base_dir = dir_campaing(campaña)

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
        # Crear una conexión SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(sftp_host, sftp_port, sftp_user, sftp_password)
        sftp = ssh.open_sftp()
        print("Conexión SFTP establecida con éxito.")
    except Exception as e:
        print(f"Error al abrir la conexión SFTP: {e}")
        ssh.close()
        exit()

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
    ssh.close()