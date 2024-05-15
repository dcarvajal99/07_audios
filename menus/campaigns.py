from services.get_audios import get_audios_by_date

def menu(registros, fechas):
    while True:
                print("1. Multicampaña")
                print("2. Asistencias")
                print("3. Contact Center")
                print("4. Cancelaciones")
                print("5. Retencion")
                print("6. Otra campaña")
                print("7. Salir")
                campaña = input("Selecciona una campaña:")
                if campaña == "1":
                    get_audios_by_date('Siniestros', registros, fechas)
                    break
                elif campaña == "2":
                    get_audios_by_date('Asistencias', registros, fechas)
                    break
                elif campaña == "3":
                    get_audios_by_date('Contact_Center', registros, fechas)
                    break
                elif campaña == "4":
                    get_audios_by_date('Cancelaciones', registros, fechas)
                    break
                elif campaña == "5":
                    get_audios_by_date('Retencion', registros, fechas)
                    break
                elif campaña == "6":
                    campaña = input("Ingrese nombre de la campaña para buscar audios:")
                    get_audios_by_date(campaña, registros, fechas)
                    break
                elif campaña == "7":
                    break
                else:
                    print("Opción inválida. Por favor, selecciona una opción válida.")