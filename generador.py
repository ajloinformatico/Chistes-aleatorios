from entrenador import *
import random


class Generador:
    """
    Deberá generar una cita aleatoria que no podrá ser una repetición de las últimas 10 citas generadas. Debe indicar también la referencia a la fuente.
    Ejemplo:
    """

    def __init__(self):
        """
        Su constructor está compuesto de dos listas
        una que almacena citas_disponibles y la segundo que almacena durante 10 turnos las citas que
        ya no son disponibles
        """
        self.citas_no_disponibles = []
                    
    def genera_cita_aleatoria(self, citas_disponibles):
        """
        Genera la cita aleatoria
        :param citas_disponibles {list}: listado de citas
        :return {dic}: devuelve la cita aleatoria
        """
        while True:
            autor = citas_disponibles[random.randint(0, len(citas_disponibles) -1)] # posición aleatoria en la lista de cistas del
            # autor seleccionado a partir un numero aleatorio entre 0 y la longitud de la lista de citas
            cita = autor[random.randint(0, len(autor) -1)]
            if self.comp_esta_disponible(cita):
                return cita # posición aleatoria en la lista del autor seleccionado a partir
                # un numero aleatorio entre 0 y la longitud de la lista de ese autor

    def imprime_cita_aleatoria(self, citas_disponibles):
        """
        Imprime la frase antes de ello comprueba que esta no esté en la lista de frases no disponibles
        entonces resta uno a los contadores de todas las frases y imprime la frase aleatoria
        :param citas_disponibles{list}: listado de citas en disccionarios agrupadas en listas por autor
        :return {str}: Imprime la cita aleatoria
        """
        self.trunos() # Resta uno a los turnos
        cita = self.genera_cita_aleatoria(citas_disponibles)
        for c, v in cita.items():
            self.citas_no_disponibles.append([10,v]) # Agrega la cita a citas no disponibles con un contador
             # resta uno en los turnos
            return  c + " : " + v

    def comp_esta_disponible(self, cita):
        """
        Comprueba si la cita aleatoria está disponible
        :param cita {dic}: cita generada aleatoriamente
        :return {bool}: True está disponible, False no está disponible
        """
        print(cita)
        for c, v in cita.items():
            for l in self.citas_no_disponibles:
                if v in l[1]:
                    return False
            return True

    def trunos(self):
        for i in self.citas_no_disponibles:
            i[0] -= 1
            if i[0] <= 0:
                self.citas_no_disponibles.remove(i)

if __name__ == "__main__":
    ### Test en el main
    t = Entrendador()
    t.cargar_desde_csv()
    ge1 = Generador()

    while True:
        i = input("\n>>>")
        if i == "ge1":
            print(ge1.imprime_cita_aleatoria(t.citas)) # Imprime una cita aleatoria
            print(ge1.citas_no_disponibles)
        if i == "salir":
            break