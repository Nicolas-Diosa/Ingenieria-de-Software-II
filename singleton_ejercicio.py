class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Conductor(metaclass=SingletonMeta):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class mula:
    def __init__(self, conductor):
        self.conductor =conductor

def main():

    conductor_en_turno1 = Conductor(1, "Miguel")
    conductor_en_turno2 = Conductor(2, "Alberto")

    mula_en_servicio = mula(Conductor(1,"Esteban"))

    print(mula_en_servicio.conductor.nombre)

if __name__ == "__main__":
    main()