from OpenGL.GL import *
from OpenGL.GLU import *
import math


# Variables globales (asegúrate de inicializarlas en el archivo principal)
pelota_pos = [-20, 2, 0]
pelota_direccion = [1, 0, 0]
pelota2_pos = [0, 50, 0]
pelota2_direccion = [0, -1, 0]
radio_personaje = 1
radio_pelota = 1
radio_pelota2 = 1

def mover_pelota():
    global pelota_pos
    pelota_pos[0] += pelota_direccion[0]
    pelota_pos[1] += pelota_direccion[1]
    pelota_pos[2] += pelota_direccion[2]
    if pelota_pos[0] > 50:  # Limite derecho
        pelota_pos[0] = -20  # Reinicia la posición

def dibujar_pelota():
    glPushMatrix()
    glTranslatef(pelota_pos[0], pelota_pos[1], pelota_pos[2])
    glColor3f(1.0, 0.0, 0.0)  # Color rojo
    quad = gluNewQuadric()
    gluSphere(quad, 1, 32, 32)  # Radio de 1, detalle 32x32
    glPopMatrix()

def detectar_colision():
        distancia = math.sqrt(
            (pelota_pos[0] - 0)**2 +
            (pelota_pos[1] - 0)**2 +
            (pelota_pos[2] - 0)**2
    )
        print("Distancia a personaje:", distancia)
        return distancia < (radio_pelota + radio_personaje)

def mover_pelota2():
    global pelota2_pos
    pelota2_pos[0] += pelota2_direccion[0]
    pelota2_pos[1] += pelota2_direccion[1]
    pelota2_pos[2] += pelota2_direccion[2]
    if pelota2_pos[1] < 0:  # Límite inferior
        pelota2_pos[1] = 50  # Reinicia la posición

def dibujar_pelota2():
    glPushMatrix()
    glTranslatef(pelota2_pos[0], pelota2_pos[1], pelota2_pos[2])
    glColor3f(0.0, 1.0, 0.0)  # Color verde
    quad = gluNewQuadric()
    gluSphere(quad, 1, 32, 32)
    glPopMatrix()

def detectar_colision2():
        distancia = math.sqrt(
            (pelota2_pos[0] - 0)**2 +
            (pelota2_pos[1] - 0)**2 +
            (pelota2_pos[2] - 0)**2
        )
        return distancia < (radio_pelota2 + 10)