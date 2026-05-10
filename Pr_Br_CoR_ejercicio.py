import copy
from abc import ABC, abstractmethod

# PATRÓN BRIDGE: INTERFAZ Y LOGÍSTICAS
class Logistica(ABC):
    @abstractmethod
    def calcular_costo(self, peso): pass
    @abstractmethod
    def obtener_medio(self): pass

class LogisticaCarretera(Logistica):
    def calcular_costo(self, peso): return peso * 1.5
    def obtener_medio(self): return "Camiones (Carretera)"

class LogisticaFerroviaria(Logistica):
    def calcular_costo(self, peso): return peso * 0.8
    def obtener_medio(self): return "Trenes (Vía Férrea)"

class LogisticaMaritima(Logistica): # Nueva Logística añadida
    def calcular_costo(self, peso): return (peso * 0.4) + 500
    def obtener_medio(self): return "Buque Carguero (Marítimo)"

# PATRÓN PROTOTYPE: CLASE FLOTA 
class Flota:
    def __init__(self, tipo_carga, capacidad_max, logistica: Logistica):
        self.tipo_carga = tipo_carga
        self.capacidad_max = capacidad_max
        self.logistica = logistica
        self.vehiculos = []

    def agregar_vehiculo(self, modelo):
        self.vehiculos.append(modelo)

    def clonar(self, nueva_logistica=None):
        nuevo = copy.deepcopy(self)
        if nueva_logistica:
            nuevo.logistica = nueva_logistica
            nuevo.vehiculos = [] 
        return nuevo

    def __str__(self):
        vehiculos_str = ", ".join(self.vehiculos) if self.vehiculos else "Sin vehículos"
        return (f"[{self.tipo_carga} | {self.capacidad_max}t | {self.logistica.obtener_medio()}]")

#  PATRÓN CHAIN OF RESPONSIBILITY: MANEJADORES 
class ManejadorTransporte(ABC):
    def __init__(self):
        self.siguiente = None

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente
        return siguiente

    @abstractmethod
    def validar_envio(self, flota):
        if self.siguiente:
            return self.siguiente.validar_envio(flota)
        return f" RECHAZADO: No hay transporte para {flota.capacidad_max}t."

class ManejadorCarretera(ManejadorTransporte):
    def validar_envio(self, flota):
        if flota.capacidad_max <= 100:
            return f"DESPACHADO por Carretera: {flota}"
        return super().validar_envio(flota)

class ManejadorFerroviario(ManejadorTransporte):
    def validar_envio(self, flota):
        if flota.capacidad_max <= 1000:
            return f" DESPACHADO por Ferrocarril: {flota}"
        return super().validar_envio(flota)

class ManejadorMaritimo(ManejadorTransporte):
    def validar_envio(self, flota):
        if flota.capacidad_max <= 10000:
            return f" DESPACHADO por Mar: {flota}"
        return super().validar_envio(flota)

# --- 4. LÓGICA PRINCIPAL ---
def main():
    # Inicialización de medios (Bridge)
    vial = LogisticaCarretera()
    ferroviaria = LogisticaFerroviaria()
    maritima = LogisticaMaritima()

    # Configuración de la Cadena (Responsabilidad)
    cadena_logistica = ManejadorCarretera()
    cadena_logistica.set_siguiente(ManejadorFerroviario()).set_siguiente(ManejadorMaritimo())

    # Creación de flotas (Prototype)
    prototipo = Flota("Carga General", 0, vial)

    # Flota Alimentos (Pequeña)
    f_alimentos = prototipo.clonar()
    f_alimentos.tipo_carga = "Alimentos"
    f_alimentos.capacidad_max = 80
    f_alimentos.agregar_vehiculo("Camión Refrigerado")

    # Flota Construcción (Mediana)
    f_construccion = prototipo.clonar(nueva_logistica=ferroviaria)
    f_construccion.tipo_carga = "Materiales de Construcción"
    f_construccion.capacidad_max = 800
    f_construccion.agregar_vehiculo("Vagón de Carga")

    # Flota Animales (Grande - decidimos mandarla por mar)
    f_animales = prototipo.clonar(nueva_logistica=maritima)
    f_animales.tipo_carga = "Animales Vivos"
    f_animales.capacidad_max = 5000
    f_animales.agregar_vehiculo("Buque Ganadero")

    # Una carga excesiva
    f_exceso = prototipo.clonar()
    f_exceso.tipo_carga = "Carga Ilegal"
    f_exceso.capacidad_max = 99999

    # Procesamiento por la cadena
    print("--- PROCESANDO ENVÍOS POR CAPACIDAD ---")
    for f in [f_alimentos, f_construccion, f_animales, f_exceso]:
        print(cadena_logistica.validar_envio(f))

if __name__ == "__main__":
    main()