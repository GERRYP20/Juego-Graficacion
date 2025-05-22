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
<<<<<<< Updated upstream
=======
    global posx, posy, posz
    global resultado, resultado_tiempo, mostrar_resultado
    global resultado_incorrecto_tiempo, mostrar_resultado_incorrecto
    # Dentro de iniciar_memorama
    puntuacion = 0
    juego_terminado = False

>>>>>>> Stashed changes
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
    sonidoOn("sonidos/SoteMenu.mp3")

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
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Salir del nivel y regresar al menú principal
                teclas_activas.add(event.key)  # Agregar la tecla al conjunto
            if event.type == pygame.KEYUP:
                teclas_activas.discard(event.key)  # Eliminar la tecla del conjunto
                # Movimiento del personaje
                # Movimiento continuo del personaje
        '''if pygame.K_w in teclas_activas:  # Adelante
            posz -= velocidad
        if pygame.K_s in teclas_activas:  # Atrás
            posz += velocidad'''
        if pygame.K_a in teclas_activas:  # Izquierda
            posx -= velocidad
        if pygame.K_d in teclas_activas:  # Derecha
            posx += velocidad

<<<<<<< Updated upstream
      # Verificar si han pasado 10 segundos
        if time.time() - inicio_tiempo > 10:
            mover_esferas(posx, posy, posz)  # Mover las esferas después de 10 segundos
        # Dibujar la escena
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
=======
        # Limita el movimiento del personaje en X
        posx = max(-36, min(36, posx))  # Cambia  según el rango visible del juego

        tiempo_actual = time.time() - inicio_tiempo

        pregunta_actual = pregunta_mostrada
        for i, t in enumerate(tiempo_preguntas):
            if tiempo_actual > t:
                pregunta_actual = i

        if pregunta_actual != pregunta_mostrada:
            reiniciar_esferas()

        pregunta_mostrada = pregunta_actual

        if pregunta_mostrada == 0 and tiempo_actual > 20:
            resultado = mover_esferas(posx, posy, posz, 2)
        elif pregunta_mostrada == 1 and tiempo_actual > 40:
            resultado = mover_esferas(posx, posy, posz, 0)
        elif pregunta_mostrada == 2 and tiempo_actual > 60:
            resultado = mover_esferas(posx, posy, posz, 0)
        elif pregunta_mostrada == 3 and tiempo_actual > 80:
            resultado = mover_esferas(posx, posy, posz, 1)
        elif pregunta_mostrada == 4 and tiempo_actual > 100:
            resultado = mover_esferas(posx, posy, posz, 4)
        elif pregunta_mostrada == 5 and tiempo_actual > 120:
            resultado = mover_esferas(posx, posy, posz, 0)

        if resultado == "correcta":
            resultado_tiempo = time.time()
            mostrar_resultado = True
        elif resultado is not None:
            resultado_incorrecto_tiempo = time.time()
            mostrar_resultado_incorrecto = True

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        es.pinta_escenario("Imagenes/fondo6.jpg", "Imagenes/suelo1.jpg")
>>>>>>> Stashed changes

        # Configurar la cámara
        #glLoadIdentity()
        #glTranslatef(0, 0, -50)  # Ajustar la posición de la cámara

        # Dibujar el fondo, suelo y personaje
        es.pinta_escenario("Imagenes/fondo7.jpg", "Imagenes/suelo7.jpg")  # Fondo y suelo del nivel
        glPushMatrix()
        glTranslatef(posx, posy, posz)  # Posicionar al personaje
        personaje_dibujar()  # Dibujar el personaje seleccionado
        glPopMatrix()

<<<<<<< Updated upstream
         # Dibujar las esferas
        dibujar_esferas()

        # Mostrar texto en pantalla
        tx.text("¡Bienvenido a la Tormenta de Decisiones!", -1, 46, 0, 30, 255, 255, 255, 0, 0, 0)
        tx.text("Presiona ESC para regresar", -1, 44, 0, 20, 255, 255, 255, 0, 0, 0)
=======
     
        # TEXTO DE INSTRUCCIÓN (debajo)
        tx.text("Presiona ESC para regresar al men\u00fa", -28, 0, 18, 20, 255, 255, 255, 0, 0, 0)

        if juego_terminado:
            tx.text("¡Juego terminado!", -12, 30, 0, 32, 255, 255, 0, 0, 0, 0)
            tx.text(f"Tu puntuación: {puntuacion} de {len(preguntas)}", -14, 24, 0, 28, 0, 255, 0, 0, 0, 0)
            tx.text("Presiona ESC para salir", -12, 18, 0, 22, 255, 255, 255, 0, 0, 0)
        elif pregunta_mostrada < 0:
            tx.text("\u00a1Bienvenido a la Tormenta de Decisiones!", -17, 47, 0, 32, 255, 255, 255, 0, 0, 0)
            tx.text("Colócate debajo de la respuesta correcta", -20, 25, 0, 30, 255, 255, 255, 0, 0, 0)
            tx.text("Muévete con A y S ", -7, 21, 0, 26, 255, 255, 255, 0, 0, 0)
        elif pregunta_mostrada < len(preguntas):
            tx.text(preguntas[pregunta_mostrada], -37, 34, 0, 24, 255, 255, 0, 0, 0, 0)
            dibujar_esferas()
            for i, (x, y, z) in enumerate(esferas_pos):
                if esferas_activas[i]:
                    tx.text(opciones_preguntas[pregunta_mostrada][i], x - 6, y + 5, z, 18, 255, 255, 255, 0, 0, 0)


        if mostrar_resultado:
            if time.time() - resultado_tiempo < 5:
                tx.text("\u00a1CORRECTO!", -4, 0, 10, 30, 0, 255, 0, 0, 0, 0)
            else:
                mostrar_resultado = False

        if mostrar_resultado_incorrecto:
            if time.time() - resultado_incorrecto_tiempo < 5:
                tx.text("\u00a1INCORRECTO!", -7, 0, 10, 30, 255, 0, 0, 0, 0, 0)
            else:
                mostrar_resultado_incorrecto = False

        if resultado == "correcta":
            resultado_tiempo = time.time()
            mostrar_resultado = True
            puntuacion += 1
        elif resultado is not None:
            resultado_incorrecto_tiempo = time.time()
            mostrar_resultado_incorrecto = True

        # --- AGREGA ESTO ---
        if pregunta_mostrada == len(preguntas) - 1 and resultado is not None:
            juego_terminado = True
>>>>>>> Stashed changes

        pygame.display.flip()
        pygame.time.wait(10)