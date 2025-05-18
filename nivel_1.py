from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from pygame.locals import *  # Importar las constantes necesarias
from colisiones import mover_esferas, dibujar_esferas, esferas_pos, esferas_activas, esferas_direcciones
import src.pinta as pt
import Acciones.escenarios as es
import Acciones.textos as tx
import time
from Acciones.sonidos import *
# Variables globales para la posición del personaje
posx = 0  # Posición inicial en el eje X
posy = 0  # Posición inicial en el eje Y
posz = 0  # Posición inicial en el eje Z

def iniciar_memorama(personaje):
    
    es.ultimo_fondo = None
    es.ultimo_suelo = None
    # Variables globales para las esferas
    esferas_pos [:] = [
        [-30, 40, 0],  # Esfera 1
        [-15, 40, 0],   # Esfera 2
        [0, 40, 0],   # Esfera 3
        [15, 40, 0],    # Esfera 4
        [30, 40, 0],      # Esfera 5 (centro)
    ]
    esferas_activas [:] = [True, True, True, True, True]  # Estado de las esferas (activas o no)

    esferas_direcciones [:] = [
    [0, -1, 0],  # Dirección inicial de la esfera 1 (hacia abajo)
    [0, -1, 0],  # Dirección inicial de la esfera 2
    [0, -1, 0],  # Dirección inicial de la esfera 3
    [0, -1, 0],  # Dirección inicial de la esfera 4
    [0, -1, 0],  # Dirección inicial de la esfera 5
]
    global posx, posy, posz  # Usar las variables globales
    velocidad = 1.0  # Velocidad de movimiento del personaje
    teclas_activas = set()  # Conjunto para almacenar teclas activas
    inicio_tiempo = time.time()

    # Inicializar Pygame y OpenGL
    pygame.init()
    pygame.mixer.init()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    sonidoOn("sonidos/nivel 1.mp3")
    # Configuración de OpenGL
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)

    # Configuración de la luz
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 50, -10, 1))

    # Configuración de la perspectiva
    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)
    glTranslatef(0, -20, -70)

    # Determinar la función de dibujo del personaje
    if personaje == "mapache":
        personaje_dibujar = pt.pintaMapache
    elif personaje == "huesos":
        personaje_dibujar = pt.pintaHuesos
    elif personaje == "mike":
        personaje_dibujar = pt.pintarsincambiosMike
    else:
        personaje_dibujar = pt.pintaMapache

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sonidoOff()  # Detener el sonido al salir
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sonidoOff()
                    return  # Salir del nivel y regresar al menú principal
                teclas_activas.add(event.key)  # Agregar la tecla al conjunto
            if event.type == pygame.KEYUP:
                teclas_activas.discard(event.key)  # Eliminar la tecla del conjunto
                # Movimiento del personaje
                # Movimiento continuo del personaje
        ##if pygame.K_w in teclas_activas:  # Adelante
            ##posz -= velocidad
        ##if pygame.K_s in teclas_activas:  # Atrás
            ##posz += velocidad
        if pygame.K_a in teclas_activas:  # Izquierda
            posx -= velocidad
        if pygame.K_d in teclas_activas:  # Derecha
            posx += velocidad

      # Verificar si han pasado 10 segundos
        if time.time() - inicio_tiempo > 10:
            mover_esferas(posx, posy, posz)  # Mover las esferas después de 10 segundos
        # Dibujar la escena
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Configurar la cámara
        #glLoadIdentity()
        #glTranslatef(0, 0, -50)  # Ajustar la posición de la cámara

        # Dibujar el fondo, suelo y personaje
        es.pinta_escenario("Imagenes/fondo2.jpg", "Imagenes/suelo1.jpg")  # Fondo y suelo del nivel
        glPushMatrix()
        glTranslatef(posx, posy, posz)  # Posicionar al personaje
        personaje_dibujar()  # Dibujar el personaje seleccionado
        glPopMatrix()

         # Dibujar las esferas
        dibujar_esferas()

        # Mostrar texto en pantalla
        tx.text("¡Bienvenido a la Tormenta de Decisiones!", -1, 46, 0, 30, 255, 255, 255, 0, 0, 0)
        tx.text("Presiona ESC para regresar al menú", -1, 44, 0, 20, 255, 255, 255, 0, 0, 0)

        pygame.display.flip()
        pygame.time.wait(10)