import requests,capa_persistencia

# Configuración de URLs base
URL_BASE = "https://apitesting.interrapidisimo.co/"
URL_SECCION_API = "apicontrollerpruebas/api/"
URL_VERSION = f"{URL_BASE}{URL_SECCION_API}ParametrosFramework/ConsultarParametrosFramework/VPStoreAppControl"
URL_LOGIN = f"{URL_BASE}/FtEntregaElectronica/MultiCanales/ApiSeguridadPruebas/api/Seguridad/AuthenticaUsuarioApp"
URL_TABLAS = f"{URL_BASE}{URL_SECCION_API}SincronizadorDatos/ObtenerEsquema/true"
URL_LOCALIDADES = f"{URL_BASE}{URL_SECCION_API}ParametrosFramework/ObtenerLocalidadesRecogidas"
VERSION_LOCAL = 1


def verificar_version():
    url = URL_VERSION
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            version_api = int(data)
            
            if VERSION_LOCAL < version_api:
                print(f"\nLa versión local ({VERSION_LOCAL}) es INFERIOR a la versión del servidor ({version_api}).")
            elif VERSION_LOCAL > version_api:
                print(f"\nLa versión local ({VERSION_LOCAL}) es SUPERIOR a la versión del servidor ({version_api}).")
        else:
            print(f"No se pudo verificar la versión. Status Code: {response.status_code}")
        return version_api
    except requests.RequestException as e:
        print(f"Error de red al verificar versión: {e}")
        return []

def autenticar_y_sincronizar():
    #Login y consumo de endpoint de tablas
    url_login = URL_LOGIN
    
    headers = {
        "Usuario": "pam.meredy21",
        "Identificacion": "987204545",
        "Accept": "text/json",
        "IdUsuario": "pam.meredy21",
        "IdCentroServicio": "1295",
        "NombreCentroServicio": "PTO/BOGOTA/CUND/COL/OF PRINCIPAL - CRA 30 # 7-45",
        "IdAplicativoOrigen": "9",
        "Content-Type": "application/json"
    }
    
    body = {
        "Mac":"",
        "NomAplicacion":"Controller APP",
        "Password":"SW50ZXIyMDIx\n",
        "Path":"",
        "Usuario":"cGFtLm1lcmVkeTIx\n"
    }
    
    try:
        # Petición de Login
        response = requests.post(url_login, json=body, headers=headers)
        
        if response.status_code != 200:
            print(f"\nError de autenticación. Código HTTP: {response.status_code}")
            return False
            
        data_user = response.json()
        # Extraer campos requeridos
        usuario = data_user["Usuario"]
        identificacion = data_user["Identificacion"]
        nombre = data_user["Nombre"]
        
        capa_persistencia.guardar_usuario(usuario, identificacion, nombre)
        
        url_esquema = URL_TABLAS
        res_esquema = requests.get(url_esquema)
        
        if res_esquema.status_code == 200:
            capa_persistencia.guardar_tablas_esquema(res_esquema.json())
        else:
            print(f"No se pudo obtener el esquema de tablas. HTTP {res_esquema.status_code}")
            
        return True

    except requests.RequestException as e:
        print(f"\nError crítico de consumo API: {e}")
        return False

def obtener_localidades_api():
    url = URL_LOCALIDADES
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            print(f"Error al traer localidades. HTTP {res.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Error al obtener localidades: {e}")
        return []
