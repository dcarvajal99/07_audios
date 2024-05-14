import paramiko
import datetime

# from connections.conn_sftp import sftplist

# # Datos del servidor SFTP
sftp_host = "200.111.131.198"
sftp_port = 49000
sftp_user = "zs_bases"
sftp_password = "7!RqdV8Ka8"


def mkdir_recursive(sftp, path):
    """
    Crea una carpeta de manera recursiva en el servidor SFTP.
    """
    dirs = path.split("/")
    current_path = ""
    for dir_name in dirs:
        current_path = current_path + "/" + dir_name
        try:
            sftp.listdir(current_path)
        except IOError:
            sftp.mkdir(current_path)
        except Exception as e:
            print(f"Error al crear la carpeta {current_path}: {e}")

def mkdir(directorio):
    # Consultar en el sftp si existe el directorio
    try:
        # Crear una conexión SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(sftp_host, port=sftp_port, username=sftp_user, password=sftp_password)
        sftp = ssh.open_sftp()
        
        # Crear directorio de manera recursiva
        mkdir_recursive(sftp, directorio)
        
        print(f"Directorio {directorio} y sus padres creados con éxito.")
        
        sftp.close()
        ssh.close()
    except paramiko.ssh_exception.AuthenticationException:
        print("Error de autenticación. Por favor, revisa las credenciales.")
    except paramiko.ssh_exception.SSHException:
        print("Error al intentar conectarse al servidor SFTP.")
    except Exception as e:
        print(f"Error inesperado: {e}")
