from OpenGL.GL import *
from OpenGL.GLU import *
import math
from OpenGL.GLUT import *


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

# Variables globales para las esferas
esferas_pos = [
    [-30, 40, 0],  # Esfera 1
    [-15, 40, 0],   # Esfera 2
    [0, 40, 0],   # Esfera 3
    [15, 40, 0],    # Esfera 4
    [30, 40, 0],      # Esfera 5 (centro)
]
esfera_velocidad = 0.8  # Velocidad de caída de las esferas
esferas_activas = [True, True, True, True, True]  # Estado de las esferas (activas o no)
radio_esfera = 4  # Radio de las esferas
radio_cabeza_personaje = 2.0  # Radio de la cabeza del personaje

# Variables globales para las direcciones de las esferas
esferas_direcciones = [
    [0, -1, 0],  # Dirección inicial de la esfera 1 (hacia abajo)
    [0, -1, 0],  # Dirección inicial de la esfera 2
    [0, -1, 0],  # Dirección inicial de la esfera 3
    [0, -1, 0],  # Dirección inicial de la esfera 4
    [0, -1, 0],  # Dirección inicial de la esfera 5
]

# Función para mover las esferas
def mover_esferas(posx, posy, posz, indice):
    global esferas_pos, esferas_activas, esferas_direcciones

    for i in range(len(esferas_pos)):
        if esferas_activas[i]:
            esferas_pos[i][0] += esferas_direcciones[i][0] * esfera_velocidad
            esferas_pos[i][1] += esferas_direcciones[i][1] * esfera_velocidad
            esferas_pos[i][2] += esferas_direcciones[i][2] * esfera_velocidad

            if detectar_colision_esfera(esferas_pos[i], posx, posy, posz):
                if i == indice:
                    print(f"✅ ¡Respuesta correcta! Colisión con la esfera {i + 1}")
                    resultado = "correcta"
                else:
                    print(f"❌ Respuesta incorrecta. Colisión con la esfera {i + 1}")
                    resultado = "incorrecta"

                esferas_direcciones[i][0] *= -1
                esferas_direcciones[i][1] *= -1
                esferas_direcciones[i][2] *= -1

                return resultado

    return None

# Función para dibujar las esferas
def dibujar_esferas():
    global esferas_pos, esferas_activas
    for i in range(len(esferas_pos)):
        if esferas_activas[i]:
            glPushMatrix()
            glTranslatef(esferas_pos[i][0], esferas_pos[i][1], esferas_pos[i][2])
            glColor3f(0.5, 0.0, 0.5)  # Color morado
            quad = gluNewQuadric()
            gluSphere(quad, radio_esfera, 32, 32)  # Dibujar una esfera
            glPopMatrix()

# Función para detectar colisiones con las esferas
def detectar_colision_esfera(esfera_pos, posx, posy, posz):
    # Detectar colisión con la cabeza del personaje
    distancia = math.sqrt(
        (esfera_pos[0] - posx) ** 2 +
        (esfera_pos[1] - (posy + radio_cabeza_personaje)) ** 2 +  # Ajustar para la cabeza
        (esfera_pos[2] - posz) ** 2
    )
    return distancia < (radio_esfera + radio_cabeza_personaje)  # Colisión con la cabeza

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


def detectar_colision_puertas(posx, posz, posiciones_puertas, respuesta_correcta, z_puerta=-10):
    ancho_puerta = 2.5  # mitad del ancho de la puerta escalada
    profundidad_colision = 1.0  # rango de colisión en Z

    for i, px in enumerate(posiciones_puertas):
        # Checar si posx está dentro del ancho de la puerta
        if (px - ancho_puerta) <= posx <= (px + ancho_puerta):
            # Checar si posz está dentro del rango de profundidad para colisionar
            if (z_puerta - profundidad_colision) <= posz <= (z_puerta + profundidad_colision):
                if i == respuesta_correcta:
                    return "correcta"
                else:
                    return "incorrecta"
    return None

