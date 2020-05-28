import sys
from entrenador import *
from generador import *

if __name__ == "__main__":
    print("""
*****************************************************************
                    GENERADOR DE CHISTES
*****************************************************************
    """)
    comandos = ("""
-----------------------------------------------------------------
                        COMANDOS
                        
    * Introducir Cita   'Carga una cita en la aplicación'
    * Cargar Citas      'Carga las citas almacenadas en el CSV'
    * Eliminar Cita     'Elimina una o varias citas por maarametro'
    * Mostrar Citas     'Muestra las citas'
    * Generar Cita      'Genera las citas'
    * Comandos          'Muestra la lista de comandos'
    * Salir             'Cierra el programa'
-----------------------------------------------------------------
    """)
    print(comandos)
    trainer = Entrendador()
    generator = Generador()
    while True:
        print("""
-----------------------------------------------------------------
                    INTODUCE UN COMANDO
-----------------------------------------------------------------
        """)
        eleccion = input(">>> ").lower().replace(" ", "")
        if eleccion.lower() == "salir":
            print("Hasta Luego amigo")
            sys.exit()

        elif eleccion == "introducircita":
            n_cita = input("Introduce autor y cita separado por coma\n>>> ").split(",")
            if len(n_cita) == 2 and trainer.comp_no_es_un_numero(n_cita[0]) \
                    and trainer.comp_no_es_un_numero(n_cita[1]):
                if not trainer.comprueba_si_existe_la_cita(n_cita[1]):
                    trainer.introduce_citas((n_cita[0].upper(), n_cita[1].lower()))
                    print(f"Se ha agregado la cita\n{n_cita[0].upper()} : {n_cita[1].lower()}")
                else:
                    print("La cita ya existe existe")
            else:
                print("La entrada no es válida")

        elif eleccion == "cargarcitas" or eleccion == "cargarcita":
            trainer.cargar_desde_csv()  # Carga el csv
            print("Se han cargado las citas del CSV")

        elif eleccion == "eliminarcita" or eleccion == "eliminarcitas":
            if trainer.citas != []:
                print("Indique el autor al que pertenece la cita\nTODAS o SALIR\n", trainer.muestra_autores(), )
                e = input(">>> ")
                if e.lower() != "salir":
                    if e.lower() != "todas":
                        if trainer.comprueba_si_existe_el_autor(e):
                            print(trainer.muestra_citas_ap_autor(e))
                            c = input("Introduce el numero de la cita a eliminar o TODAS\n>>> ")
                            if c.lower() != "todas":
                                print(trainer.elimina_cita((c, e.upper())))
                                trainer.comp_listas_vacias() # Elimina las listas vacías
                            else:
                                trainer.elimina_todas_citas_ap_a(e.upper())
                                trainer.comp_listas_vacias()  # Elimina las listas vacías
                                print("Se han eliminado todas las citas de " + e.upper())
                        else:
                            print("El autor no existe")
                    else:
                        trainer.citas = []
                        print("Se han eliminado todas las citas del sistema")
                else:
                    pass
            else:
                print("No hay ninguna cita en el sistema")

        elif eleccion == "mostrarcitas":
            if trainer.citas != []:
                print("Indique el autor al que pertenece la cita\nTODAS o SALIR\n", trainer.muestra_autores(),)
                e = input(">>> ")
                if e.lower() != "salir":
                    if e.lower() == "todas":
                        print(trainer)
                    else:
                        print(trainer.muestra_citas_ap_autor(e.upper()))
                else:
                    pass
            else:
                print("No hay ninguna cita en el sistema")

        elif eleccion == "comandos" or eleccion == "comando":
            print(comandos)


        elif eleccion == "generar" or eleccion == "generarcita" or eleccion == "genera" or eleccion=="genera":
            if trainer.citas != []:
                print(generator.imprime_cita_aleatoria(trainer.citas))
            else:
                print("No hay ninguna cita en el sistema")


        else:
            print("El comando no existe")
