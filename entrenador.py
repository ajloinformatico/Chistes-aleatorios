"""
Permitirá cargar citas a través de teclado o importarlas desde un formato CSV con dos columnas
(el separador puede ser uno de los siguientes caracteres [ ; , | TAB ]
Permitirá también eliminar citas por su contenido o por su referencia.
"""
import os
import sys


class Entrendador:
    """
    Permitirá cargar citas a través de teclado o importarlas desde un formato CSV con dos columnas
    (el separador puede ser uno de los siguientes caracteres [ ; , | TAB ]
    Permitirá también eliminar citas por su contenido o por su referencia.
    """

    def __init__(self):
        """Constructor almacena en listas de diccionario"""
        self.citas = []

    def cargar_desde_csv(self):
        """
        Carga los datos del CSV en self.citas
        :return {list}: devuelve una lista de diccionarios cada lista corresponde a un autor utilizando el método
        de la clase introduce citas
        """
        with open('chistes.csv', 'r', encoding="UTF-8") as manf:
            for linea in manf.readlines()[1:]:
                self.introduce_citas((linea.split(";")[1].rstrip().upper(), linea.split(";")[0].lower()))

    def introduce_citas(self, param: tuple):
        """
        Recibbe una tupla con autor y cita si el autor existe inserta el dic en su lista
        si no inserta una nueva lista para el nuevo autor y el diccionario en esta lista
        :param param {tuple}: tupla del autor y la cita
        :return {void}: modifica la lista de citas
        """
        # Si el autor existe
        if self.comprueba_si_existe_el_autor(param[0]):
            for lista in self.citas:
                if param[0] in lista[0].keys():
                    lista.append({param[0]: param[1]})
        else:
            self.citas.append([{param[0]: param[1]}])



    def comprueba_si_existe_la_cita(self, param: str):
        """
        Comprueba si existe el autor
        :param param {str}: str of the cita busca su valor en algún diccionario
        :returns {bool}: True si existe, False si no existe
        """
        for lista in self.citas:
            for dic in lista:
                if param.lower() in dic.values():
                    return True
        return False

    def comprueba_si_existe_el_autor(self, param: str):
        """
        Comprueba si existe el autor
        :param {str}: str of the autor busca su clave en algún diccionario
        :returns {bool}: True si existe, False si no existe
        """
        for lista in self.citas:
            if param.upper() in lista[0].keys():
                return True
        return False

    def __str__(self):
        """
        to string de la clase entrenador
        :return {str} result: el resultado de recorrer con un bucle la lista de citas
        """
        result = ""
        for lista in self.citas:
            for dic in lista:
                for c, v in dic.items():
                    result += f"{c} : {v} \n"
        return result

    def comp_no_es_un_numero(self, param: str):
        """
        Comprueba si el parametro de entrada no es un numero
        :param param {str}: parametro de entrada
        :return {bool}: True si no es un número, False si es un número
        """
        try:
            int(param)
            return False
        except ValueError:
            return True

    def muestra_autores(self):
        """
        Muestra todos los autors
        :return {str}: string de autores
        """
        resultado = ""
        for lista in self.citas:
            for dic in lista:
                for c, v in dic.items():
                    if c not in resultado:
                        resultado += "* " + c + "\n"
        return resultado

    def muestra_citas_ap_autor(self, autor):
        resultado = "citas de " + autor.upper() + "\n"
        con = 0
        for lista in self.citas:
            for dic in lista:
                for c, v in dic.items():
                    if c == autor.upper():
                        con += 1
                        resultado += str(con) + " " + v + "\n"
        return resultado

    def elimina_cita(self, param: tuple):
        # elimina a partir de la cita
        resultado = self.muestra_citas_ap_autor(param[1])
        resultado = resultado.split("\n")
        if not self.comp_no_es_un_numero(param[0]):
            for linea in resultado:
                if str(param[0]) in linea:
                    for listas in self.citas:
                        for dic in listas:
                            for c, v in dic.items():
                                if linea[2:] in v:
                                    del dic[c]
                                    return "Se ha eliminado la cita " + param[1] + " : " + linea[2:]
            return "índice para eliminar fuera de rango"
        else:
            return "No has introducido un numero"

    def elimina_todas_citas_ap_a(self,autor):
        """
        Elimina todas las listas a partir de un autor
        :param autor {str} : parametro de busqueda en las listas de self.citas
        :return {void}: modifica la self.citas
        """
        for lista in self.citas:
            for dic in lista:
                for c, v in dic.items():
                    if c == autor:
                        self.citas.remove(lista)
                        return True

    def comp_listas_vacias(self):
        """
        # TODO Comprueba en el método de eliminar que no haya ninguna lista vacia
        """
        for lista in self.citas:
            if  lista == [{}] or lista == []:
                self.citas.remove(lista)
            for dic in lista:
                if dic == {}:
                    lista.remove(dic)



if __name__ == "__main__":
    ### Tests en el main
    e = Entrendador()
    e.cargar_desde_csv()  # Devuelve una lista de diccionarios cada lista corresponde a un autor diferente
    e.comprueba_si_existe_el_autor("etapa")  # Comprueba si el autor exoste en el diccionario, debe de ser una clave

    # Comprueba que la cita existe
    e.comprueba_si_existe_la_cita(
        '¿Por qué se suicidó el libro de matemáticas?. Porque tenía muchos problemas por resolver')

    # Función es un numero
    e.comp_no_es_un_numero("3")
    e.comp_no_es_un_numero("JUAN")

    e.elimina_todas_citas_ap_a("VERNE")
    e.comp_listas_vacias()
    print(e.citas)
