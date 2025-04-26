from mnu import mostrar_menu
from inter import seleccion_de_personaje
from main import iniciar_juego  # Asegúrate de importar esto

if __name__ == "__main__":
    while True:
        accion = mostrar_menu("Imagenes/Menu.jpg")

        if accion == "jugar":
            personaje = seleccion_de_personaje()
            iniciar_juego(personaje)
        elif accion == "salir":
            break  # Sale del ciclo principal y termina el programa
