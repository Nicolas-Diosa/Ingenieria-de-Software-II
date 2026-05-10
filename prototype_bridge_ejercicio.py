import copy
from abc import ABC, abstractmethod

# --- 1. INTERFAZ LOGÍSTICA (Parte del Bridge) ---
class Logistica(ABC):
    @abstractmethod
    def calcular_costo(self, peso):
        pass

    @abstractmethod
    def obtener_medio(self):
        pass

# --- 2. IMPLEMENTACIONES CONCRETAS DEL BRIDGE ---
class LogisticaCarretera(Logistica):
    def calcular_costo(self, peso): return peso * 1.5
    def obtener_medio(self): return "Camiones (Carretera)"

class LogisticaFerroviaria(Logistica):
    def calcular_costo(self, peso): return peso * 0.8
    def obtener_medio(self): return "Trenes (Vía Férrea)"


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
            nuevo.vehiculos = [] # Limpiamos los camiones si cambiamos a Tren/Barco
        return nuevo

    def __str__(self):
        vehiculos_str = ", ".join(self.vehiculos) if self.vehiculos else "Sin vehículos asignados"
        return (f"Flota de {self.tipo_carga} | "
                f"Transporte: {self.logistica.obtener_medio()} | "
                f"Vehículos: [{vehiculos_str}]")

def creacion_de_flotas():
    vial = LogisticaCarretera()
    ferroviaria = LogisticaFerroviaria()

    # Prototipo base (Vacío de vehículos para que sea genérico)
    prototipo_base = Flota("Carga General", 0, vial)

    # Flota de Alimentos (Mantiene la logística vial del prototipo)
    flota_alimentos = prototipo_base.clonar()
    flota_alimentos.tipo_carga = "Alimentos"
    flota_alimentos.agregar_vehiculo("Camión Refrigerado")

    # Flota de Construcción (Cambiamos el puente y se limpia la lista de vehículos)
    flota_construccion = prototipo_base.clonar(nueva_logistica=ferroviaria)
    flota_construccion.tipo_carga = "Materiales de construcción"
    flota_construccion.capacidad_max = 2000
    flota_construccion.agregar_vehiculo("Vagón de Carga Pesada")
    

    print(flota_alimentos)
    print(flota_construccion)

def main():
    creacion_de_flotas()

if __name__ == "__main__":
    main()