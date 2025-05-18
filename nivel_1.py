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
from Acciones.sonidos import *

# Variables globales para la posición del personaje
posx = 0
posy = 0
posz = 0

def reiniciar_esferas():
    esferas_pos[:] = [
        [-30, 40, 0],
        [-15, 40, 0],
        [0, 40, 0],
        [15, 40, 0],
        [30, 40, 0],
    ]
    esferas_activas[:] = [True, True, True, True, True]
    esferas_direcciones[:] = [
        [0, -1, 0],
        [0, -1, 0],
        [0, -1, 0],
        [0, -1, 0],
        [0, -1, 0],
    ]

def iniciar_memorama(personaje):
    es.ultimo_fondo = None
    es.ultimo_suelo = None

    reiniciar_esferas()

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
    sonidoOn("sonidos/nivel 1.mp3")

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

    preguntas = [
        "¿Cuál de las siguientes opciones es la más importante para mantener una buena higiene bucal?",
        "¿Qué debes hacer para evitar caries y mantener tus dientes saludables?",
        "¿Con qué frecuencia se recomienda bañarse para mantener una buena higiene personal?",
        "¿Cuál es la mejor forma de mantener las manos limpias?",
        "¿Qué es importante para cuidar tu cabello?",
        "¿Por qué es importante cambiarse de ropa limpia regularmente?"
    ]

    opciones_preguntas = [
        [
            "1. Cepillarse los dientes",
            "2. Comer dulces diario",
            "3. No usar hilo dental",
            "4. Dormir con la boca abierta",
            "5. Evitar ir al dentista"
        ],
        [
            "1. Visitar al dentista regularmente",
            "2. Ignorar el mal aliento",
            "3. Beber refrescos a diario",
            "4. No usar pasta dental",
            "5. Dejar de cepillarse"
        ],
        [
            "1. Todos los días",
            "2. Una vez al mes",
            "3. Solo cuando huela mal",
            "4. Cada semana",
            "5. Nunca"
        ],
        [
            "1. Lavarse con agua y jabón",
            "2. Solo enjuagarse con agua",
            "3. Usar solo alcohol en gel",
            "4. No lavarse las manos",
            "5. Usar guantes todo el tiempo"
        ],
        [
            "1. Lavarlo regularmente",
            "2. No lavarlo nunca",
            "3. Usar productos dañinos",
            "4. Dejarlo sucio",
            "5. Peinarlo con las manos sucias"
        ],
        [
            "1. Para evitar enfermedades",
            "2. No es importante",
            "3. Solo por moda",
            "4. Para gastar ropa",
            "5. Porque sí"
        ]
    ]

    tiempo_preguntas = [10, 30,50,70,90,110]  # segundos en que aparece cada pregunta
    pregunta_mostrada = -1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sonidoOff()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sonidoOff()
                    return
                teclas_activas.add(event.key)
            if event.type == pygame.KEYUP:
                teclas_activas.discard(event.key)

        if pygame.K_a in teclas_activas:
            posx -= velocidad
        if pygame.K_d in teclas_activas:
            posx += velocidad

        tiempo_actual = time.time() - inicio_tiempo

        # Determinar qué pregunta mostrar según el tiempo
        pregunta_actual = pregunta_mostrada
        for i, t in enumerate(tiempo_preguntas):
            if tiempo_actual > t:
                pregunta_actual = i

        # Si cambia la pregunta, reiniciar esferas
        if pregunta_actual != pregunta_mostrada:
            reiniciar_esferas()

        pregunta_mostrada = pregunta_actual

        # Mover esferas después de 20 segundos para la primera pregunta,
        # y después de 40 segundos para la segunda (20 segundos tras inicio de la pregunta)
        if pregunta_mostrada == 0 and tiempo_actual > 20:
            mover_esferas(posx, posy, posz)
        elif pregunta_mostrada == 1 and tiempo_actual > 40:
            mover_esferas(posx, posy, posz)
        elif pregunta_mostrada == 2 and tiempo_actual > 60:
            mover_esferas(posx, posy, posz)
        elif pregunta_mostrada == 3 and tiempo_actual > 80:
            mover_esferas(posx, posy, posz)
        elif pregunta_mostrada == 4 and tiempo_actual > 100:
            mover_esferas(posx, posy, posz)
        elif pregunta_mostrada == 5 and tiempo_actual > 120:
            mover_esferas(posx, posy, posz) 
        

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        es.pinta_escenario("Imagenes/fondo2.jpg", "Imagenes/suelo1.jpg")
        glPushMatrix()
        glTranslatef(posx, posy, posz)
        personaje_dibujar()
        glPopMatrix()

        # Mostrar pregunta y opciones solo si ya toca mostrarlas
        if pregunta_mostrada >= 0:
            dibujar_esferas()
            for i, (x, y, z) in enumerate(esferas_pos):
                if esferas_activas[i]:
                    tx.text(opciones_preguntas[pregunta_mostrada][i], x - 6, y + 5, z, 18, 255, 255, 255, 0, 0, 0)

            tx.text(preguntas[pregunta_mostrada], -37, 20, 0, 24, 255, 255, 0, 0, 0, 0)

        tx.text("¡Bienvenido a la Tormenta de Decisiones!", -17, 30, 0, 30, 255, 255, 255, 0, 0, 0)
        tx.text("Presiona ESC para regresar al menú", -13, 25, 0, 20, 255, 255, 255, 0, 0, 0)

        pygame.display.flip()
        pygame.time.wait(10)