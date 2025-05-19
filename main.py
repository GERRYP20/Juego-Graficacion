import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
import tkinter.messagebox as messagebox
import Acciones.textos as tx
import colisiones as col

# Estas variables deben declararse en el archivo principal
pelota_pos = [-200, 2, 0]
pelota_direccion = [1, 0, 0]
pelota2_pos = [0, 100, 0]
pelota2_direccion = [0, -1, 0]
pelota_activa = False  # Inicialmente, la pelota no está activa
pelota2_activa = False  # Inicialmente, la pelota no está activa

def iniciar_juego(personaje, nivel):
    print(f"Iniciando juego con el personaje: {personaje} en el nivel: {nivel}")

    if nivel == "memorama":
        print("Configurando nivel: Memorama")
        from nivel_1 import iniciar_memorama
        iniciar_memorama(personaje)
        return
    elif nivel == "tormenta":
        print("Configurando nivel: Memorama_real")
        from nivel_2 import iniciar_ruinas
        iniciar_ruinas(personaje)
        return
    elif nivel == "laberinto":
        print("Configurando nivel: Laberinto")
        from nivel_3 import iniciar_puertas
        iniciar_puertas(personaje)
        return
