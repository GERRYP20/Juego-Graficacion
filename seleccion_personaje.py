import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import src.pinta as pt
import Acciones.escenarios as es
import Acciones.textos as txt
from Acciones.sonidos import *

def resetear_opengl():
    # Limpia estados OpenGL para no afectar otros módulos
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glDisable(GL_COLOR_MATERIAL)
    glDisable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Cierra ventana y libera pygame y OpenGL
    pygame.display.quit()
    pygame.quit()

def draw_base(x_offset, selected):
    base_size = 2.0
    if selected:
        glColor3f(1, 1, 0)
    else:
        glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(x_offset - base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, -base_size)
    glVertex3f(x_offset - base_size, -2, -base_size)
    glEnd()

def configurar_opengl():
    pygame.init()
    pygame.mixer.init()
    sonidoOff()
    sonidoOn("sonidos/seleccion.mp3")
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClearColor(0.9, 0.9, 0.95, 1.0)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 50, -10, 1))

    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)

    glTranslatef(0, -7, -30)
    glRotatef(15, 1, 0, 0)

    pygame.event.set_grab(True)
    pygame.mouse.set_visible(True)

def seleccion_de_personaje():
    configurar_opengl()

    selected_character = 0
    character_changed = False
    character_angles = [0, 0, 0]

    personajes = [pt.pintaMapache, pt.pintaHuesos, pt.pintarsincambiosMike]
    nombres_personajes = ["mapache", "huesos", "mike"]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and not character_changed:
                    selected_character = (selected_character - 1) % len(personajes)
                    character_changed = True
                elif event.key == K_RIGHT and not character_changed:
                    selected_character = (selected_character + 1) % len(personajes)
                    character_changed = True
                elif event.key == K_RETURN:
                    sonidoOff()
                    resetear_opengl()
                    return nombres_personajes[selected_character]
                elif event.key == K_ESCAPE:
                    resetear_opengl()
                    running = False
            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_RIGHT):
                    character_changed = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        es.pinta_escenario2("Imagenes/SoteImage.png", "Imagenes/pisoSote.png")

        txt.text("¡SELECCIONA TU PERSONAJE!", -17, 12, -18, 50, 255, 255, 255, 0, 0, 255)
        txt.text("HUESOS", -1.5, 0, 7.5, 30, 255, 255, 255, 0, 0, 255)
        txt.text("GATOPACHE KEVIN", -11, 0, 7.5, 30, 255, 255, 255, 0, 0, 255)
        txt.text("RAPERO MIKEE", 7, 0, 7.5, 30, 255, 255, 255, 0, 0, 255)

        posiciones = [-12, 0, 12]

        for i, personaje in enumerate(personajes):
            draw_base(posiciones[i], selected_character == i)
            glPushMatrix()
            glTranslatef(posiciones[i], 0, 0)
            if selected_character == i:
                character_angles[i] = (character_angles[i] + 15) % 360
            glRotatef(character_angles[i], 0, 1, 0)
            glScalef(0.5, 0.5, 0.5)
            personaje()
            glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

    # Si salimos del loop sin seleccionar, limpiamos y cerramos
    resetear_opengl()
    return None