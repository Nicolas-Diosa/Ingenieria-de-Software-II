import capa_persistencia,capa_seguridad_API

def pantalla_home():
    user = capa_persistencia.obtener_usuario_local()

    print("           HOME")

    if user:
        print(f"Usuario: {user['usuario']}")
        print(f"Identificación: {user['identificacion']}")
        print(f"Nombre: {user['nombre']}")
    else:
        print("No hay datos de usuario logueado en la BD local.")
    print("\n1. Ver Tablas")
    print("\n2. Ver Localidades")
    print("\n3. Salir")


def pantalla_tablas():
    tablas = capa_persistencia.obtener_tablas_locales()
    print("         TABLAS (BD LOCAL)")
    if not tablas:
        print("No hay registros de tablas guardados.")
    else:
        for idx, tabla in enumerate(tablas, 1):
            print(f"{idx}. {tabla}")
    input("Enter para regresar HOME")

def pantalla_localidades():
    localidades = capa_seguridad_API.obtener_localidades_api()
    
    print("       LOCALIDADES ")
    if not localidades:
        print("No se encontraron registros de localidades.")
    else:
        for loc in localidades:
            # Extraer los campos solicitados de manera segura
            abrev = loc["AbreviacionCiudad"]
            nombre_comp = loc["NombreCompleto"]
            print(f"Abreviación: {abrev} - Nombre Completo: {nombre_comp}")
            
    input("Enter para regresar HOME")




if __name__ == "__main__":
    capa_persistencia.inicializar_bd()
    capa_seguridad_API.verificar_version()

    autenticacion_exitosa = capa_seguridad_API.autenticar_y_sincronizar()
    
    if autenticacion_exitosa:
        while True:

            pantalla_home()
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                pantalla_tablas()
            elif opcion == "2":
                pantalla_localidades()
            elif opcion == "3":
                break
            else:
                print("\nOpción inválida.")
    else:
        print("\nAutenticación fallida.")