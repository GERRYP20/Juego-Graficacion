import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
import math
import tkinter.messagebox as messagebox
import Acciones.sonidos as sd
import Acciones.escenarios as es
import Acciones.luces as lc
import src.pinta as pt
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
        print("Configurando nivel: Tormenta")
        escenario_actual = 1
        suelo_actual = 0
    elif nivel == "laberinto":
        print("Configurando nivel: Laberinto")
        escenario_actual = 2
        suelo_actual = 1
    elif nivel == "lobby":
        print("Configurando el lobby")
        escenario_actual = 0
        suelo_actual = 0

    print(f"Escenario inicial: {escenario_actual}, Suelo inicial: {suelo_actual}")

    es.ultimo_fondo = None
    es.ultimo_suelo = None
    mostrar_mike = False
    mostrar_huesos = False

    global pelota_pos, pelota_direccion, pelota_activa    
    global pelota2_pos, pelota2_direccion, pelota2_activa

    velocidad_camara = 0.1
    velocidad_rotacion = 0.2
    raton = 0.1

    escenarios = [
        'Imagenes/fondo.jpg',
        'Imagenes/fondo2.jpg',
        'Imagenes/fondo3.jpg',
        'Imagenes/fondo4.jpg',
        'Imagenes/fondo5.jpg',
        'Imagenes/fondo6.jpg',
        'Imagenes/fondo7.jpg',
    ]

    suelos = [
        'Imagenes/suelo1.jpg',
        'Imagenes/suelo7.jpg'
    ]

    angulo_brazo_derecho = 0
    direccion_brazo = 1
    saludando = False

    escenario_actual = 0
    suelo_actual = 0

    pygame.quit()
    pygame.init()
    pygame.mixer.init()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 50, -10, 1))

    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)
    pos_inicial = [0, -20, -50]
    glTranslatef(*pos_inicial)

    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)

    def reset_camera():
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)
        glTranslatef(*pos_inicial)

    if personaje == "mapache":
        personaje_dibujar = pt.pintaMapache
    elif personaje == "huesos":
        personaje_dibujar = pt.pintaHuesos
    elif personaje == "mike":
        personaje_dibujar = pt.pintarsincambiosMike
    else:
        personaje_dibujar = pt.pintaMapache

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_p:
                    sd.sonidoOn('Sonidos/start.wav')
                if event.key == pygame.K_o:
                    sd.sonidoOff()
                if event.key == pygame.K_c:
                    reset_camera()
                if event.key == pygame.K_1:
                    escenario_actual = 0
                    suelo_actual = 0
                    personaje_dibujar = pt.pintaMapache if personaje == "mapache" else pt.pintarsincambiosMike if personaje == "mike" else pt.pintaHuesos
                    sd.sonidoOn('Sonidos/campanas.wav')
                elif event.key == pygame.K_2:
                    escenario_actual = 1
                    suelo_actual = 0
                    personaje_dibujar = pt.pintaMapacheEnojado if personaje == "mapache" else pt.pintaMike1 if personaje == "mike" else pt.pintaHuesos2
                    sd.sonidoOn('Sonidos/rayos.wav')
                elif event.key == pygame.K_3:
                    escenario_actual = 2
                    suelo_actual = 0
                    personaje_dibujar = pt.pintaMapacheFeliz if personaje == "mapache" else pt.pintaMike2 if personaje == "mike" else pt.pintaHuesos
                    sd.sonidoOn('Sonidos/aves.wav')
                elif event.key == pygame.K_4:
                    escenario_actual = 3
                    suelo_actual = 0
                    personaje_dibujar = pt.pintaMapacheTriste if personaje == "mapache" else pt.pintaMike3 if personaje == "mike" else pt.pintaHuesos
                    sd.sonidoOn('Sonidos/estrella.wav')
                elif event.key == pygame.K_5:
                    escenario_actual = 4
                    suelo_actual = 0
                    personaje_dibujar = pt.pintaMapacheSaltando if personaje == "mapache" else pt.pintaMike4 if personaje == "mike" else pt.pintaHuesos
                    sd.sonidoOn('Sonidos/tada.wav')
                elif event.key == pygame.K_6:
                    escenario_actual = 5
                    suelo_actual = 0
                    personaje_dibujar = pt.pintaMapacheDuda if personaje == "mapache" else pt.pintaMike5 if personaje == "mike" else pt.pintaHuesos
                    sd.sonidoOn('Sonidos/insectos.wav')
                elif event.key == pygame.K_7:
                    escenario_actual = 6
                    suelo_actual = 1
                    personaje_dibujar = pt.pintaMapacheCaminando if personaje == "mapache" else pt.pintarsincambiosMike if personaje == "mike" else pt.pintaHuesos
                    sd.sonidoOn('Sonidos/mar.wav')
                if event.key == pygame.K_l and escenario_actual == 0:
                    saludando = not saludando
                if event.key == pygame.K_i:
                    pelota_activa = True
                    pelota_pos = [-100, 2, 0]
                    pelota_direccion = [1, 0, 0]
                    print("Pelota activada:", pelota_activa, "Posición inicial:", pelota_pos)
                if event.key == pygame.K_u:
                    pelota2_activa = True
                    pelota2_pos = [0, 100, 0]
                    pelota2_direccion = [0, -1, 0]
                if event.key == pygame.K_m:
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            glTranslatef(0, 0, 10)
        if keys[pygame.K_s]:
            glTranslatef(0, 0, -10)
        if keys[pygame.K_a]:
            glTranslatef(10, 0, 0)
        if keys[pygame.K_d]:
            glTranslatef(-10, 0, 0)
        if keys[pygame.K_x]:
            glTranslatef(0, 10, 0)
        if keys[pygame.K_z]:
            glTranslatef(0, -10, 0)

        x, y = pygame.mouse.get_rel()
        x *= raton
        y *= raton
        if x != 0:
            glRotatef(x, 0, 1, 0)
        pygame.mouse.set_pos(display[0] // 2, display[1] // 2)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        es.pinta_escenario(escenarios[escenario_actual], suelos[suelo_actual])
        personaje_dibujar()

        tx.text("Instrucciones:",-25,38,0,20,0,0,0,255,255,255)
        tx.text("Presiona de 1-7 para cambiar de escenario", -25,36,0,20,0,0,0,255,255,255)
        tx.text("Para mover la camara usar: a,s,d,w,z,x", -25,34,0,20,0,0,0,255,255,255)
        tx.text("Camara en posicion original: c", -25,32,0,20,0,0,0,255,255,255)
        tx.text("Encender sonido general: p", -25,30,0,20,0,0,0,255,255,255)
        tx.text("Colision 1: i", -25,28,0,20,0,0,0,255,255,255)
        tx.text("Colision 2: u", -25,26,0,20,0,0,0,255,255,255)
        tx.text("Salir: ESC", -25,24,0,20,0,0,0,255,255,255)
        tx.text("\u00a1PRESIONA ENTER PARA JUGAR!", -20,20,-3,50,0,0,0,255,255,255)

        if pelota_activa:
            col.dibujar_pelota()
            col.mover_pelota()

        if pelota2_activa:
            col.dibujar_pelota2()
            col.mover_pelota2()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    iniciar_juego()