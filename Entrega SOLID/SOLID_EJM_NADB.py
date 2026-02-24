class fabrica_carros:
    def __init__(self,colores,chasis,carroceria):
        self.ensamblador_carroceria1 = ensamblador_carroceria()
        self.pintor_carroceria1 = pintor_carroceria(colores)
        self.ensamblador_final1 = ensamblador_final(chasis,carroceria)


class ensamblador:
    def ensamblar(piezas):
        pass

class ensamblador_carroceria(ensamblador):
    def __init__(self):
        pass
    def ensamblar(piezas_carroceria):
        pass

class pintor_carroceria:
    def __init__(self,colores):
        self.colores = colores

    def pintar_carroceria(self,carroceria, color):
        try:
            self.colores.index(color)
        except ValueError:
            print("Color "+color+" no disponible")

class ensamblador_final:
    def __init__(self,chasis,carroceria):
        self.piezas=chasis+carroceria
        print(self.piezas)
    def ensamblar(self):
        print(self.piezas)

def main():
    colores = ["amarillo","verde","azul"]
    fabrica1 = fabrica_carros(colores,"ev8","ec9")
    fabrica1.ensamblador_final1.ensamblar()



main()