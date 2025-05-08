from OpenGL.GL import *
from OpenGL.GLU import *
import math



# Variables globales (asegúrate de inicializarlas en el archivo principal)
pelota_pos = [-100, 2, 0]
pelota_direccion = [1, 0, 0]
pelota_velocidad = 2 # Aumenté la velocidad
pelota2_pos = [0, 100, 0]
pelota2_direccion = [0, -1, 0]
radio_personaje = 1
radio_pelota = 1.5
radio_pelota2 = 1.5
pelota_activa = True    
pelota2_activa = True


def mover_pelota():
    global pelota_pos, pelota_activa
    if pelota_activa:
        pelota_pos[0] += pelota_direccion[0] * pelota_velocidad
        pelota_pos[1] += pelota_direccion[1] * pelota_velocidad
        pelota_pos[2] += pelota_direccion[2] * pelota_velocidad
    
        # Si colisiona, cambia la dirección
        if detectar_colision():
            print("¡Colisión detectada!")  # Para que confirmes que sí detecta
            pelota_direccion[0] *= -1  # Rebote en X
            pelota_direccion[2] *= -1  # Rebote en Z (opcional)

            # Si la pelota se aleja mucho, desactívala
        if abs(pelota_pos[0]) > 100 or abs(pelota_pos[2]) > 100:
            pelota_activa = False
            print("Pelota1 desactivada")


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
    global pelota2_pos, pelota2_activa
    if pelota2_activa:
        pelota2_pos[0] += pelota2_direccion[0] * pelota_velocidad
        pelota2_pos[1] += pelota2_direccion[1] * pelota_velocidad
        pelota2_pos[2] += pelota2_direccion[2] * pelota_velocidad
        if detectar_colision2():
            print("¡Colisión con pelota 2!")
            pelota2_direccion[1] *= -1  # Rebote hacia arriba

        # Si cae muy abajo, se desactiva
        if pelota2_pos[1] > 100:
            pelota2_activa = False
            print("Pelota 2 desactivada")

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