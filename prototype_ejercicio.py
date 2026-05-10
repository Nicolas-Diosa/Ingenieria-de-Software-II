import copy

class Flota:
    def __init__(self, tipo_carga, capacidad_max, ):
        self.tipo_carga = tipo_carga
        self.capacidad_max = capacidad_max
        self.vehiculos = []

    def agregar_vehiculo(self, modelo):
        self.vehiculos.append(modelo)

    # El método clonar es el corazón del patrón Prototype
    def clonar(self):
        # deepcopy copia incluso las listas internas para que sean independientes
        return copy.deepcopy(self)

    def __str__(self):
        return (f"Flota de {self.tipo_carga} | "
                f"Capacidad: {self.capacidad_max}t | "
                f" Vehículos: {len(self.vehiculos)}")

def creacion_de_flotas():
    # 1. Creamos un prototipo base de flota pesada
    prototipo_pesado = Flota("General", 500)
    prototipo_pesado.agregar_vehiculo("Camión Kenworth T880")
    
    # Generamos la Flota de Alimentos
    # Alimentos necesita refrigeración
    flota_alimentos = prototipo_pesado.clonar()
    flota_alimentos.tipo_carga = "Alimentos Perecederos"
    
    # Generamos la Flota de Construcción
    flota_construccion = prototipo_pesado.clonar()
    flota_construccion.tipo_carga = "Materiales de Construcción"
    flota_construccion.capacidad_max = 1000  # Más capacidad
    
    #  Generamos la Flota de Animales 
    flota_animales = prototipo_pesado.clonar()
    flota_animales.tipo_carga = "Animales Vivos"
    flota_animales.agregar_vehiculo("Remolque Ganadero Especial")

    # Resultados
    print(flota_alimentos.vehiculos)
    print(flota_alimentos)
    print(flota_construccion)
    print(flota_animales)


def main():
    creacion_de_flotas()

if __name__ == "__main__":
    main()