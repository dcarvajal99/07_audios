from managers.sftp_manager import SFTPManager

list_sfpt = SFTPManager().read_sftp_config()

def sftp_menu():
    print(list_sfpt)
    while True:
        # mostrar las opciones de conexiones a sftp
        for i, sftp in enumerate(list_sfpt):
            print(f"{i+1}. {sftp['sftp_host']}:{sftp['sftp_port']} - {sftp['sftp_user']}")
        opcion = input("Selecciona una opción: ")
        if opcion.isdigit() and int(opcion) <= len(list_sfpt):
            # print(f"Conectando a {list_sfpt[int(opcion)-1]['sftp_host']}:{list_sfpt[int(opcion)-1]['sftp_port']} - {list_sfpt[int(opcion)-1]['sftp_user']}")
            #print (list_sfpt[int(opcion)-1])
            return list_sfpt[int(opcion)-1]
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
    return None