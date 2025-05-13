from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from pygame.locals import *
from colisiones import mover_esferas, dibujar_esferas, esferas_pos, esferas_activas, esferas_direcciones
import src.pinta as pt
import Acciones.escenarios as es
import Acciones.textos as tx
import time

# Posición inicial del personaje
posx = 0
posy = 0
posz = 0

def draw_puerta():
    glColor3f(0.6, 0.3, 0.0)  # Color madera
    glBegin(GL_QUADS)
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 4, 1)
    glVertex3f(-1, 4, 1)
    glEnd()

    glColor3f(0.3, 0.15, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-1, 4, 1)
    glVertex3f(1, 4, 1)
    glVertex3f(1, 4, 0.8)
    glVertex3f(-1, 4, 0.8)
    glEnd()

def iniciar_puertas(personaje):
    es.ultimo_fondo = None
    es.ultimo_suelo = None

    esferas_pos[:] = [[-30, 40, 0], [-15, 40, 0], [0, 40, 0], [15, 40, 0], [30, 40, 0]]
    esferas_activas[:] = [True] * 5
    esferas_direcciones[:] = [[0, -1, 0]] * 5

    global posx, posy, posz
    velocidad = 1.0
    teclas_activas = set()
    inicio_tiempo = time.time()

    pygame.init()
    pygame.mixer.init()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 50, -10, 1))

    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)
    glTranslatef(0, -20, -70)

    if personaje == "mapache":
        personaje_dibujar = pt.pintaMapache
    elif personaje == "huesos":
        personaje_dibujar = pt.pintaHuesos
    elif personaje == "mike":
        personaje_dibujar = pt.pintarsincambiosMike
    else:
        personaje_dibujar = pt.pintaMapache

    posiciones_puertas = [-20, 0, 20]
    nombres_puertas = ["RESPUESTA 1", "RESPUESTA 2", "RESPUESTA 3"]
    z_puerta = -10  # Alejar puertas

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                teclas_activas.add(event.key)
            if event.type == KEYUP:
                teclas_activas.discard(event.key)

        if K_w in teclas_activas:
            posz -= velocidad
        if K_s in teclas_activas:
            posz += velocidad
        if K_a in teclas_activas:
            posx -= velocidad
        if K_d in teclas_activas:
            posx += velocidad

        if time.time() - inicio_tiempo > 10:
            mover_esferas(posx, posy, posz)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        es.pinta_escenario("Imagenes/fondo7.jpg", "Imagenes/suelo7.jpg")

        glPushMatrix()
        glTranslatef(posx, posy, posz)
        personaje_dibujar()
        glPopMatrix()

        # Dibujar puertas
        for i, pos in enumerate(posiciones_puertas):
            glPushMatrix()
            glTranslatef(pos, 0, z_puerta)
            glScalef(2.5, 2.5, 2.5)
            draw_puerta()
            glPopMatrix()

            # Texto sobre la puerta (centrado y elevado)
            tx.text(
                nombres_puertas[i],
                pos - 4,        # x
                10,             # y
                z_puerta,       # z
                28,             # tamaño
                255, 255, 0,    # color
                0, 0, 0         # fondo
            )

        tx.text("¡Bienvenido al laberinto de Decisiones!", -12, 46, 0, 30, 255, 255, 255, 0, 0, 0)
        tx.text("Presiona ESC para regresar", -8, 44, 0, 20, 255, 255, 255, 0, 0, 0)

        pygame.display.flip()
        pygame.time.wait(10)
