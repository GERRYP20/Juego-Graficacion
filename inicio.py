from mnu import mostrar_menu
from seleccion_personaje import seleccion_de_personaje
from seleccion_nivel import seleccion_de_nivel
from main import iniciar_juego
from Acciones.sonidos import *

if __name__ == "__main__":
    sonidoOn("sonidos/SoteMenu.mp3")
    while True:
        accion = mostrar_menu("Imagenes/SoteImage.png")
        if accion == "jugar":
            while True:
                # Seleccionar personaje
                personaje = seleccion_de_personaje()
                if iniciar_juego(personaje, "lobby")==True:
                    # Seleccionar nivel
                    nivel_elegido = seleccion_de_nivel()


                # Confirmar selección y comenzar el juego
                print("Personaje seleccionado:", personaje)
                print("Nivel elegido:", nivel_elegido)
                iniciar_juego(personaje, nivel_elegido)
                break  # Salir del bucle interno y regresar al menú principal
        elif accion == "salir":
            break