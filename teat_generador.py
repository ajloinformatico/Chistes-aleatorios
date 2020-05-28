"""TEST Generador"""
from generador import *
from entrenador import *
import pytest

en = Entrendador()
ge = Generador()

def test_generador():
    """
    El generador es complementado por el constructor
    su finción en el programa es simplemente generar una cita aleatoria e imprimirla
    Esta cita se almacena en una lista junto con un contador solo para ella de 10
    cada vez que se llama a la clase se crea una nueva entrada en la lista con la cita
    generada automáticamente y el contador del resto de listas desciende
    """
    # primero cargaré las listas disponibles
    en.cargar_desde_csv()

    # Comprobamos que la lista del Generador está vacia
    assert ge.citas_no_disponibles == []

    # Al agregar una cita aleatoria se inserta el valor de dicha cita y un contador a 10
    ge.imprime_cita_aleatoria(en.citas)

    for l in ge.citas_no_disponibles:
        assert l[0] == 10
        assert type(l[1]) == str

    # si se genera una nueva cita el valor de la ingresada en primer lugar será de 9
    # y la nueva cita será distinta pues no podrá jhaber otra igual hasta que su valor sea
    # menor de 1 entonces se elimina de la lista

    ge.imprime_cita_aleatoria(en.citas)

    assert len(ge.citas_no_disponibles) == 2 # Tiene dos elementos ahota
    primer_valor = ge.citas_no_disponibles[0] # Primera entrada
    segundo_valor = ge.citas_no_disponibles[1] # Nueva entrada
    assert primer_valor[0] == 9 # disminuye en 1
    assert primer_valor[1] != segundo_valor[1] # la cita es diferente

    assert segundo_valor[0] == 10 # la nueva tiene valor de 10