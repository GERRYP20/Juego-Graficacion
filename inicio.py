from mnu import mostrar_menu
from seleccion_personaje import seleccion_de_personaje
from main import iniciar_juego 
from Acciones.sonidos import *

if __name__ == "__main__":
    sonidoOn("sonidos/SoteMenu.mp3") 
    while True:
        accion = mostrar_menu("Imagenes/SoteImage.png")
        if accion == "jugar":
            personaje = seleccion_de_personaje()
            iniciar_juego(personaje)
        elif accion == "salir":
            break
