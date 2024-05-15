import sys
sys.path.append('C:/07_Audios')
from managers.sftp_manager import SFTPManager
import re



sftp_manager = SFTPManager("c:/07_AUDIOS/data/sftp.json")

def sftp_config():
    while True:
        print("1. Mostar conexiones SFTP")
        print("2. Agregar conexión SFTP")
        print("3. Eliminar conexión SFTP")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            sftp_manager.display_sftp_connections()
        elif opcion == "2":
            while True:
                host = input("Ingrese el host:")
                if not re.match(r'^(\d{1,3}\.){3}\d{1,3}$', host) and not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', host):
                    print("Error: El host debe ser una dirección IP o un dominio válido.")
                else:
                    break
            while True:
                port = input("Ingrese el puerto:")
                if not port.isdigit():
                    print("Error: El puerto debe ser un número.")
                else:
                    break
            while True:
                user = input("Ingrese el usuario:")
                if not user:
                    print("Error: El usuario es obligatorio.")
                else:
                    break
            while True:
                password = input("Ingrese la contraseña:")
                if not password:
                    print("Error: La contraseña es obligatoria.")
                else:
                    break
            sftp_manager.add_sftp_connection(host, port, user, password)
        elif opcion == "3":
            sftp_manager.display_sftp_connections()
            try:
                index = int(input("Ingrese el número de la conexión que desea eliminar:")) - 1
                sftp_manager.remove_sftp_connection(index)
            except ValueError:
                print("Error: Ingrese un número válido.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# # Ejemplo de uso:
# # Creamos una instancia de la clase SFTPConfigManager
# sftp_manager = SFTPConfigManager("c:/proyecto/config/sftp.json")

# # Agregamos una nueva conexión SFTP
# sftp_manager.add_sftp_connection("nuevo_host", 22, "nuevo_usuario", "nueva_contraseña")

# # Eliminamos la segunda conexión SFTP (índice 1)
# sftp_manager.remove_sftp_connection(1)