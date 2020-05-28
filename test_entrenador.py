"""TEST Entrenador"""
import pytest
from entrenador import *

entrenador = Entrendador()


def test_constructor_entrenador():
    """
    Comprueba el constructor debe iniciarse con una lista vacía en la cual se almacenraán listas
    de diccionarios una por cada autor
    """
    # Creo la instancia de Entrenador
    e = Entrendador()

    # Compruebo que su atributo citas es igual a una lista vacia
    assert type(e.citas) == list and e.citas == []


def test_carga_citas_desde_csv():
    """
    Apoyandose en el método de la clase introduce_citas() inserta en el constructor las citas del csv
    este se compone de dos columnas cita y autor. El sistema comprueba si el autor existe. En caso de que exista
    insertará las citas en su lista en el caso de que no se creará una nueva lista para insertar sus citas
    """
    entrenador.cargar_desde_csv()  # Carga las citas del csv
    # Autores y citas
    assert entrenador.citas == [[{'VERNE': '¿sabes cómo se llaman los habitantes de barcelona? hombre. pues '
                                           'todos no.'},
                                 {'VERNE': '¿qué le dice la foca a su madre? i love you mother foca'},
                                 {'VERNE': 'doctor, tengo todo el cuerpo cubierto de pelo. ¿qué padezco?, '
                                           'padece uzté un ozito.'}],
                                [{'LLARRY': 'gol. ¿de quién? di maría. maría, pero quién ha marcado el gol.'}],
                                [{'ETAPA': '¿cuál es el colmo de un futbolista?. que le hagan la pelota'},
                                 {'ETAPA': '¿por qué se suicidó el libro de matemáticas?. porque tenía muchos '
                                           'problemas por resolver'},
                                 {'ETAPA': 'buenos días, ¿tienen libros sobre el cansancio? sí, pero ahora '
                                           'mismo están todos agotados'}],
                                [{'SECTOVIRAL': 'hombre, juan, cómo has cambiado. yo no soy juan. más a mi '
                                                'favor'},
                                 {'SECTOVIRAL': 'ha dicho el doctor que lo mejor para curarme el dolor de '
                                                'garganta es un striptease. un strepsils. joder, paqui, le '
                                                'quitas la ilusión a cualquiera…'},
                                {'SECTOVIRAL': 'un placer venir a su mutua. es mutuo. un placer venir a su '
                                               'mutuo'}]]


def test_introduce_citas():
    """
    El sistema comprueba si el autor existe. En caso de que exista
    insertará las citas en su lista en el caso de que no se creará una nueva lista para insertar sus citas
    """
    # Ingreso la cita en el verne
    cita_pertenece_a_autor = "¿Qué le dice una iguana a su hermana gemela?. Somos iguanitas"
    # Inserto la cita en el autor VERNE
    entrenador.introduce_citas(("VERNE", "¿Qué le dice una iguana a su hermana gemela?. Somos iguanitas"))

    # Comprueba si la cita está dentro del autor
    assert cita_pertenece_a_autor in entrenador.muestra_citas_ap_autor("verne")

    # Comprueba todas las citas
    assert entrenador.citas == [[{'VERNE': '¿sabes cómo se llaman los habitantes de barcelona? hombre. pues '
                                           'todos no.'},
                                 {'VERNE': '¿qué le dice la foca a su madre? i love you mother foca'},
                                 {'VERNE': 'doctor, tengo todo el cuerpo cubierto de pelo. ¿qué padezco?, '
                                           'padece uzté un ozito.'},
                                 {'VERNE': '¿Qué le dice una iguana a su hermana gemela?. Somos iguanitas'}],
                                [{'LLARRY': 'gol. ¿de quién? di maría. maría, pero quién ha marcado el gol.'}],
                                [{'ETAPA': '¿cuál es el colmo de un futbolista?. que le hagan la pelota'},
                                 {'ETAPA': '¿por qué se suicidó el libro de matemáticas?. porque tenía muchos '
                                           'problemas por resolver'},
                                 {'ETAPA': 'buenos días, ¿tienen libros sobre el cansancio? sí, pero ahora '
                                           'mismo están todos agotados'}],
                                [{'SECTOVIRAL': 'hombre, juan, cómo has cambiado. yo no soy juan. más a mi '
                                                'favor'},
                                 {'SECTOVIRAL': 'ha dicho el doctor que lo mejor para curarme el dolor de '
                                                'garganta es un striptease. un strepsils. joder, paqui, le '
                                                'quitas la ilusión a cualquiera…'},
                                {'SECTOVIRAL': 'un placer venir a su mutua. es mutuo. un placer venir a su '
                                               'mutuo'}]]
    # La cita se inserto correctamente

    # Inserto autor y cita nueva
    cita_sin_autor = "¿dónde cuelga superman su supercapa?. somos iguanitas"

    # Introduzco la cita en un nuevo autor
    entrenador.introduce_citas(("ELENA", cita_sin_autor))

    # Comprobamos que la cita se ha introducido en el autor nuevo
    assert cita_sin_autor in entrenador.muestra_citas_ap_autor("elena")

    # La cita está en una nueva lista solo para elena
    assert entrenador.citas == [[{'VERNE': '¿sabes cómo se llaman los habitantes de barcelona? hombre. pues '
                                           'todos no.'},
                                 {'VERNE': '¿qué le dice la foca a su madre? i love you mother foca'},
                                 {'VERNE': 'doctor, tengo todo el cuerpo cubierto de pelo. ¿qué padezco?, '
                                           'padece uzté un ozito.'},
                                 {'VERNE': '¿Qué le dice una iguana a su hermana gemela?. Somos iguanitas'}],
                                [{'LLARRY': 'gol. ¿de quién? di maría. maría, pero quién ha marcado el gol.'}],
                                [{'ETAPA': '¿cuál es el colmo de un futbolista?. que le hagan la pelota'},
                                 {'ETAPA': '¿por qué se suicidó el libro de matemáticas?. porque tenía muchos '
                                           'problemas por resolver'},
                                 {'ETAPA': 'buenos días, ¿tienen libros sobre el cansancio? sí, pero ahora '
                                           'mismo están todos agotados'}],
                                [{'SECTOVIRAL': 'hombre, juan, cómo has cambiado. yo no soy juan. más a mi '
                                                'favor'},
                                 {'SECTOVIRAL': 'ha dicho el doctor que lo mejor para curarme el dolor de '
                                                'garganta es un striptease. un strepsils. joder, paqui, le '
                                                'quitas la ilusión a cualquiera…'},
                                {'SECTOVIRAL': 'un placer venir a su mutua. es mutuo. un placer venir a su '
                                               'mutuo'}],
                                [{'ELENA': '¿dónde cuelga superman su supercapa?. somos iguanitas'}]]


def test_comprueba_si_existe_la_cita():
    """
    Comprueba si existe la cita si existe devuelve True y si es False
    """
    # compruebo si existe la nota de Elena '¿Dónde cuelga Superman su supercapa?. Somos iguanitas'
    cita_elena = '¿dónde cuelga superman su supercapa?. somos iguanitas'
    assert entrenador.comprueba_si_existe_la_cita(cita_elena) == True

    # Elimino las citas y las cargo de nuevo al comprobar si existe devuelve False
    entrenador.citas = []
    entrenador.cargar_desde_csv()
    assert entrenador.comprueba_si_existe_la_cita(cita_elena) == False


def test_comprueba_si_existe_el_autor():
    """
    Comprueba si existe el autor, si existe devuelve True si no devuelve False
    """
    entrenador.citas = []
    assert entrenador.comprueba_si_existe_el_autor("VERNE") == False
    entrenador.cargar_desde_csv()
    assert entrenador.comprueba_si_existe_el_autor("VERNE") == True


def test_no_es_un_numero():
    """
    Comprueba que no se ha introducido un numero, si no es numero devuelve True, si es un numero devuelve False
    """
    assert entrenador.comp_no_es_un_numero("3") == False
    assert entrenador.comp_no_es_un_numero("VERNE") == True


def test_muestra_autores():
    """
    Comrpueba si se muestran los autores, deben mostrarse los autores del CSV
    """
    assert entrenador.muestra_autores() == '* VERNE\n* LLARRY\n* ETAPA\n* SECTOVIRAL\n'

def test_muestra_citas_ap_autor():
    """
    Comprueba si se muestran las citas del autor, mostraé las citas de llaray y de un nuevo
    """
    assert entrenador.muestra_citas_ap_autor("VERNE") == 'citas de VERNE\n'+ '1 ¿sabes cómo se llaman los habitantes de ' \
            'barcelona? hombre. pues todos no.\n'+ '2 ¿qué le dice la foca a su madre? i love you mother foca\n'+ \
           '3 doctor, tengo todo el cuerpo cubierto de pelo. ¿qué padezco?, padece uzté '+ 'un ozito.\n'


    entrenador.introduce_citas(("MICHEL","las cosas de las cosas son para las cosas"))

    assert entrenador.muestra_citas_ap_autor("MICHEL") == 'citas de MICHEL\n1 las cosas de las cosas son para las cosas\n'

def test_elimina_cita():
    """
    Comprueba si se elimina la cita. Esta se hace a partir de un indice, El indice de la posicion
    en la lista
    """
    # Comprobamos si existe la cita insertada en Michel
    assert entrenador.comprueba_si_existe_la_cita("las cosas de las cosas son para las cosas") == True
    # Elimina la cita
    entrenador.elimina_cita(("1", "MICHEL"))
    # La cita ya no existe
    assert entrenador.comprueba_si_existe_la_cita("las cosas de las cosas son para las cosas") == False

def test_elimina_todas_citas_ap_a_Y_comp_listas_vacias():
    """
    Comprueba si al introducir un autor se eliminan todas las citas, lo haré a partir de la función comprueba
    autor y mostrando self.citas en la que no debe de estar la lista vacia
    """
    # Comprobamos si existe el autor
    assert entrenador.comprueba_si_existe_el_autor("VERNE") == True
    # Elimina el autor
    assert entrenador.elimina_todas_citas_ap_a("VERNE")
    # El autor no existe
    assert entrenador.comprueba_si_existe_el_autor("VERNE") == False
    entrenador.comp_listas_vacias() # Elimina las listas vacías
    # Muestro citas para comprobar que el autor y sus cii¡tas no existen y que la lista que se usba para ese autor
    # tampoco existe
    assert entrenador.citas == [[{'LLARRY': 'gol. ¿de quién? di maría. maría, pero quién ha marcado el gol.'}],
    [{'ETAPA': '¿cuál es el colmo de un futbolista?. que le hagan la pelota'},
    {'ETAPA': '¿por qué se suicidó el libro de matemáticas?. porque tenía muchos '
            'problemas por resolver'},
    {'ETAPA': 'buenos días, ¿tienen libros sobre el cansancio? sí, pero ahora '
            'mismo están todos agotados'}],
    [{'SECTOVIRAL': 'hombre, juan, cómo has cambiado. yo no soy juan. más a mi '
                 'favor'},
    {'SECTOVIRAL': 'ha dicho el doctor que lo mejor para curarme el dolor de '
                 'garganta es un striptease. un strepsils. joder, paqui, le '
                 'quitas la ilusión a cualquiera…'},
    {'SECTOVIRAL': 'un placer venir a su mutua. es mutuo. un placer venir a su '
                'mutuo'}]]


