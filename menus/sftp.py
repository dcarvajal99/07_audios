
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

def sftp_menu(list_sfpt):
    while True:
        # mostrar las opciones de conexiones a sftp
        for i, sftp in enumerate(list_sfpt):
            print(f"{i+1}. {sftp['sftp_host']}:{sftp['sftp_port']} - {sftp['sftp_user']}")
        print(f"{len(list_sfpt)+1}. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == str(len(list_sfpt)+1):
            break
        elif opcion.isdigit() and int(opcion) <= len(list_sfpt):
            # print(f"Conectando a {list_sfpt[int(opcion)-1]['sftp_host']}:{list_sfpt[int(opcion)-1]['sftp_port']} - {list_sfpt[int(opcion)-1]['sftp_user']}")
            #print (list_sfpt[int(opcion)-1])
            return list_sfpt[int(opcion)-1]
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
    return None
