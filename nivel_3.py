from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from pygame.locals import *
from colisiones import detectar_colision_puertas, esferas_pos, esferas_activas, esferas_direcciones
import src.pinta as pt
import Acciones.escenarios as es
import Acciones.textos as tx
import time
from Acciones.sonidos import *

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
    global posx, posy, posz

    es.ultimo_fondo = None
    es.ultimo_suelo = None

    esferas_pos[:] = [[-30, 40, 0], [-15, 40, 0], [0, 40, 0], [15, 40, 0], [30, 40, 0]]
    esferas_activas[:] = [True] * 5
    esferas_direcciones[:] = [[0, -1, 0]] * 5

    posx, posy, posz = 0, 0, 0
    velocidad = 1.0
    teclas_activas = set()

    pygame.init()
    pygame.mixer.init()
    glutInit()
    sonidoOn("sonidos/nivel3.mp3")
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
    z_puerta = -10

    mensajes = [
        "Primera decisión importante...",
        "Evalúa bien tus opciones.",
        "Elige la puerta correcta.",
        "Tienes 10 segundos para decidir.",
        "¡Buena suerte!"
    ]
    duracion_mensaje = 3
    tiempo_total_mensajes = len(mensajes) * duracion_mensaje

    temporizador = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

    preguntas = [
        ("¿Cada cuánto debes cepillarte los dientes?", 
         ["Una vez al mes", "Dos veces al día", "Solo cuando están sucios"], 1),
        ("¿Qué es lo más importante para mantener las manos limpias?", 
         ["Enjuagarlas con agua", "Lavarlas con agua y jabón", "Secarlas al sol"], 1),
        ("¿Por qué es importante bañarse con regularidad?", 
         ["Para gastar agua", "Para sentirse más alto", "Para eliminar bacterias y olores"], 2),
        ("¿Cuál es un buen hábito antes de comer?", 
         ["Lavar las manos", "Correr", "Ver televisión"], 0),
        ("¿Qué debes hacer después de ir al baño?", 
         ["Lavarte las manos", "Dormir", "Jugar"], 0)
    ]

    duracion_pregunta = 15
    tiempo_inicio = time.time()
    tiempo_pregunta_inicio = None
    indice_pregunta = 0
    avanzar_pregunta = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sonidoOff()
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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        es.pinta_escenario("Imagenes/ciudad.jpg", "Imagenes/piso3.jpg")

        glPushMatrix()
        glTranslatef(posx, posy, posz)
        personaje_dibujar()
        glPopMatrix()

        for pos in posiciones_puertas:
            glPushMatrix()
            glTranslatef(pos, 0, z_puerta)
            glScalef(2.5, 2.5, 2.5)
            draw_puerta()
            glPopMatrix()

        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicio

        if tiempo_transcurrido <= tiempo_total_mensajes:
            indice_msg = int(tiempo_transcurrido // duracion_mensaje)
            mensaje = mensajes[indice_msg]
            tx.text(mensaje, -10, 37, 0, 30, 255, 255, 255, 0, 0, 0)
            tx.text("¡Bienvenido al laberinto de Decisiones!", -16, 46, 0, 30, 255, 255, 255, 0, 0, 0)
            tx.text("Presiona ESC para regresar", -8, 44, 0, 20, 255, 255, 255, 0, 0, 0)

        elif tiempo_transcurrido <= tiempo_total_mensajes + len(temporizador):
            tiempo_timer = tiempo_transcurrido - tiempo_total_mensajes
            indice_timer = int(tiempo_timer)
            if indice_timer < len(temporizador):
                tx.text(temporizador[indice_timer], -1, 35, 0, 45, 255, 255, 255, 0, 0, 0)
            else:
                tx.text("¡Tiempo!", -1, 35, 0, 45, 255, 255, 255, 0, 0, 0)
            tx.text("¡Bienvenido al laberinto de Decisiones!", -16, 46, 0, 30, 255, 255, 255, 0, 0, 0)
            tx.text("Presiona ESC para regresar", -8, 44, 0, 20, 255, 255, 255, 0, 0, 0)

        else:
            if tiempo_pregunta_inicio is None:
                tiempo_pregunta_inicio = tiempo_actual

            pregunta_actual = preguntas[indice_pregunta]
            texto_pregunta = pregunta_actual[0]
            respuestas = pregunta_actual[1]

            tx.text(texto_pregunta, -20, 25, 0, 30, 255, 255, 255, 0, 0, 0)
            tx.text("¡Bienvenido al laberinto de Decisiones!", -16, 46, 0, 30, 255, 255, 255, 0, 0, 0)
            tx.text("Presiona ESC para regresar", -8, 44, 0, 20, 255, 255, 255, 0, 0, 0)

            for i, pos in enumerate(posiciones_puertas):
                tx.text(respuestas[i], pos - len(respuestas[i]) * 0.5, 10, z_puerta, 22, 255, 255, 0, 0, 0, 0)

            if tiempo_actual - tiempo_pregunta_inicio > duracion_pregunta:
                avanzar_pregunta = True

            resultado = detectar_colision_puertas(posx, posz, posiciones_puertas, preguntas[indice_pregunta][2], z_puerta=z_puerta)
            if resultado == "correcta":
                print("¡Respuesta correcta! Pasando a la siguiente pregunta.")
                avanzar_pregunta = True
                posx, posy, posz = 0, 0, 20
            elif resultado == "incorrecta":
                print("Intenta otra puerta.")
                posx, posy, posz = 0, 0, 20

        if avanzar_pregunta:
            indice_pregunta += 1
            if indice_pregunta >= len(preguntas):
                print("¡Has completado todas las preguntas!")
                sonidoOff()
                return
            tiempo_pregunta_inicio = time.time()
            avanzar_pregunta = False

        pygame.display.flip()
        pygame.time.wait(10)

