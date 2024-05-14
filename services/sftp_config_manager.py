import json

class SFTPConfigManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sftp_config = self.read_sftp_config()

    def read_sftp_config(self):
        with open(self.file_path, 'r') as file:
            sftp_data = json.load(file)
        return sftp_data

    def save_sftp_config(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.sftp_config, file, indent=4)

    def add_sftp_connection(self, sftp_host, sftp_port, sftp_user, sftp_password):
        new_connection = {
            "sftp_host": sftp_host,
            "sftp_port": sftp_port,
            "sftp_user": sftp_user,
            "sftp_password": sftp_password
        }
        self.sftp_config.append(new_connection)
        self.save_sftp_config()

    def remove_sftp_connection(self, index):
        del self.sftp_config[index]
        self.save_sftp_config()

# Ejemplo de uso:
# Creamos una instancia de la clase SFTPConfigManager
sftp_manager = SFTPConfigManager("c:/proyecto/config/sftp.json")

# Agregamos una nueva conexión SFTP
sftp_manager.add_sftp_connection("nuevo_host", 22, "nuevo_usuario", "nueva_contraseña")

# Eliminamos la segunda conexión SFTP (índice 1)
sftp_manager.remove_sftp_connection(1)