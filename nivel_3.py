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
posx, posy, posz = 0, 0, 0

def draw_puerta():
    glColor3f(0.6, 0.3, 0.0)
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

def resetear_opengl():
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glDisable(GL_COLOR_MATERIAL)
    glDisable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    pygame.display.quit()
    pygame.quit()

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
    sonidoOn("Sonidos/nivel3.mp3")
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

    personaje_dibujar = {
        "mapache": pt.pintaMapache,
        "huesos": pt.pintaHuesos,
        "mike": pt.pintarsincambiosMike
    }.get(personaje, pt.pintaMapache)

    posiciones_puertas = [-20, 0, 20]
    z_puerta = -18

    mensajes = [
        "Primera decisión importante...",
        "Evalúa bien tus opciones.",
        "Atraviesa la puerta correcta.",
        "Tienes 7 segundos para decidir.",
        "¡Buena suerte!"
    ]
    duracion_mensaje = 3
    tiempo_total_mensajes = len(mensajes) * duracion_mensaje

    temporizador = ["5", "4", "3", "2", "1"]

    preguntas = [
        ("¿Cada cuánto debes cepillarte los dientes?", ["Una vez al mes", "Dos veces al día", "Solo cuando están sucios"], 1),
        ("¿Qué es lo más importante para mantener las manos limpias?", ["Enjuagarlas con agua", "Lavarlas con agua y jabón", "Secarlas al sol"], 1),
        ("¿Por qué es importante bañarse con regularidad?", ["Para gastar agua", "Para ser más alto", "Para eliminar bacterias y olores"], 2),
        ("¿Cuál es un buen hábito antes de comer?", ["Lavar las manos", "Correr", "Ver televisión"], 0),
        ("¿Qué debes hacer después de ir al baño?", ["Lavarte las manos", "Dormir", "Jugar"], 0)
    ]

    duracion_pregunta = 7
    tiempo_inicio = time.time()
    tiempo_pregunta_inicio = None
    indice_pregunta = 0
    avanzar_pregunta = False
    respuestas_correctas = 0
    respuestas_incorrectas = 0
    mostrar_resultados = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                resetear_opengl()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    resetear_opengl()
                    return None
                if mostrar_resultados and event.key == K_RETURN:
                    resetear_opengl()
                    return iniciar_puertas(personaje)
                teclas_activas.add(event.key)
            if event.type == KEYUP:
                teclas_activas.discard(event.key)

        if not mostrar_resultados:
            if K_w in teclas_activas: posz -= velocidad
            if K_s in teclas_activas: posz += velocidad
            if K_a in teclas_activas: posx -= velocidad
            if K_d in teclas_activas: posx += velocidad

        posx = max(-36, min(36, posx))

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        es.pinta_escenario("Imagenes/ciudad.jpg", "Imagenes/piso3.jpg")

        glPushMatrix()
        glTranslatef(posx, posy, posz)
        personaje_dibujar()
        glPopMatrix()

        for pos in posiciones_puertas:
            glPushMatrix()
            glTranslatef(pos, 0, z_puerta)
            glScalef(4, 4, 2.5)
            draw_puerta()
            glPopMatrix()

        if mostrar_resultados:
            tx.text("¡Juego Terminado!", -10, 35, 0, 40, 255, 255, 255, 0, 0, 0)
            tx.text(f"Correctas: {respuestas_correctas}", -10, 30, 0, 30, 0, 255, 0, 0, 0, 0)
            tx.text(f"Incorrectas: {respuestas_incorrectas}", -10, 27, 0, 30, 255, 0, 0, 0, 0, 0)
            tx.text("Presiona ENTER para reiniciar o ESC para salir", -20, 20, 0, 20, 255, 255, 0, 0, 0, 0)
        else:
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - tiempo_inicio

            if tiempo_transcurrido <= tiempo_total_mensajes:
                indice_msg = int(tiempo_transcurrido // duracion_mensaje)
                tx.text(mensajes[indice_msg], -10, 37, 0, 30, 255, 255, 255, 0, 0, 0)
                tx.text("¡Bienvenido al laberinto de Decisiones!", -16, 46, 0, 30, 255, 255, 255, 0, 0, 0)
                tx.text("Presiona ESC para regresar a los niveles", -14, 44, 0, 20, 255, 255, 255, 0, 0, 0)
                tx.text("USA W A S D PARA MOVERTE", -12, 40, 0, 30, 255, 255, 0, 0, 0, 0)
            else:
                if tiempo_pregunta_inicio is None:
                    tiempo_pregunta_inicio = tiempo_actual

                tiempo_restante = duracion_pregunta - (tiempo_actual - tiempo_pregunta_inicio)
                if tiempo_restante < 0:
                    tiempo_restante = 0
                tx.text("¡Tiempo!", -1, 35, 0, 45, 255, 255, 255, 0, 0, 0)
                tx.text("¡Bienvenido al laberinto de Decisiones!", -16, 46, 0, 30, 255, 255, 255, 0, 0, 0)
                tx.text("Presiona ESC para regresar", -8, 44, 0, 20, 255, 255, 255, 0, 0, 0)
                tx.text("USA W A S D PARA MOVERTE", -12, 40, 0, 30, 255, 255, 0, 0, 0, 0)
                pregunta, respuestas, indice_correcto = preguntas[indice_pregunta]
                tx.text(pregunta, -20, 25, 0, 30, 255, 255, 255, 0, 0, 0)
                tx.text(f"Tiempo restante: {int(tiempo_restante)}", -6, 22, 0, 25, 255, 255, 255, 0, 0, 0)

                for i, pos in enumerate(posiciones_puertas):
                    tx.text(respuestas[i], pos - len(respuestas[i]) * 0.5, 18, z_puerta, 22, 255, 255, 0, 0, 0, 0)
                tx.text("¡Tiempo!", -1, 35, 0, 45, 255, 255, 255, 0, 0, 0)
                tx.text("¡Bienvenido al laberinto de Decisiones!", -16, 46, 0, 30, 255, 255, 255, 0, 0, 0)
                tx.text("Presiona ESC para regresar", -8, 44, 0, 20, 255, 255, 255, 0, 0, 0)
                tx.text("USA W A S D PARA MOVERTE", -12, 40, 0, 30, 255, 255, 0, 0, 0, 0)
                resultado = detectar_colision_puertas(posx, posz, posiciones_puertas, indice_correcto, z_puerta=z_puerta)
                if resultado == "correcta":
                    respuestas_correctas += 1
                    avanzar_pregunta = True
                elif resultado == "incorrecta":
                    respuestas_incorrectas += 1
                    avanzar_pregunta = True

                if tiempo_actual - tiempo_pregunta_inicio > duracion_pregunta:
                    if not avanzar_pregunta:
                        respuestas_incorrectas += 1  # No respondió
                        avanzar_pregunta = True

                if avanzar_pregunta:
                    indice_pregunta += 1
                    if indice_pregunta >= len(preguntas):
                        sonidoOff()
                        mostrar_resultados = True
                    else:
                        tiempo_pregunta_inicio = None
                        avanzar_pregunta = False
                        posx, posy, posz = 0, 0, 0

        pygame.display.flip()
        pygame.time.wait(10)
