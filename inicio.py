from mnu import mostrar_menu
from seleccion_personaje import seleccion_de_personaje
from seleccion_nivel import seleccion_de_nivel
from main import iniciar_juego
from lobby import iniciar_lobby
from Acciones.sonidos import *
import pygame

if __name__ == "__main__":
    sonidoOn("sonidos/SoteMenu.mp3")

    while True:
        accion = mostrar_menu("Imagenes/SoteImage.png")
        bandera=True
        if accion == "jugar":
            while True:
                # Seleccionar personaje
                personaje = seleccion_de_personaje()
                if iniciar_lobby(personaje)==True:
                    nivel_elegido = seleccion_de_nivel()
                    print("Personaje seleccionado:", personaje)
                    print("Nivel elegido:", nivel_elegido)
                    iniciar_juego(personaje, nivel_elegido)

                break  # Salir del bucle interno y regresar al menú principal
 
        elif accion == "salir":
            pygame.quit()  # Terminar pygame correctamente al salir
            break  # Salir del ciclo principal