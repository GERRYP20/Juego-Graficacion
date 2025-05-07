import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import src.pinta as pt
import Acciones.escenarios as es
import Acciones.textos as txt
import math

def draw_base(x_offset):
    base_size = 2.0
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

    glTranslatef(0, -15, -45)  # Cámara más baja y más alejada
    glRotatef(20, 1, 0, 0)

    pygame.event.set_grab(True)
    pygame.mouse.set_visible(True)

class Juego:
    def __init__(self):
        self.personaje = pt.pintaMapache
        self.base_index = 1
        self.base_positions = [-12, 0, 12]
        self.jump_progress = 0
        self.jumping = False
        self.jump_origin = 0
        self.jump_target = 0
        self.angle = 0

    def seleccion_de_personaje(self):
        configurar_opengl()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN:
                    if not self.jumping:
                        if event.key == K_LEFT and self.base_index > 0:
                            self.jump_origin = self.base_positions[self.base_index]
                            self.base_index -= 1
                            self.jump_target = self.base_positions[self.base_index]
                            self.jump_progress = 0
                            self.jumping = True
                        elif event.key == K_RIGHT and self.base_index < len(self.base_positions) - 1:
                            self.jump_origin = self.base_positions[self.base_index]
                            self.base_index += 1
                            self.jump_target = self.base_positions[self.base_index]
                            self.jump_progress = 0
                            self.jumping = True
                        elif event.key == K_RETURN:
                            pygame.quit()
                            return "mapache"
                        elif event.key == K_ESCAPE:
                            pygame.quit()
                            quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Fondo y suelo
            es.pinta_escenario2("Imagenes/SoteImage.png", "Imagenes/pisoSote.png")

            # Títulos
            titulo = ["azul", "verde", "amarillo"]
            for idx, palabra in enumerate(titulo):
                txt.text(palabra, -17 + (idx * 12), 12, -18, 50, 255, 255, 255, 0, 0, 255)

            # Dibujar bases
            for pos in self.base_positions:
                draw_base(pos)

            # Movimiento con salto parabólico
            x = self.base_positions[self.base_index]
            y = 0
            if self.jumping:
                t = self.jump_progress
                if t >= 1.0:
                    self.jumping = False
                else:
                    x = self.jump_origin + (self.jump_target - self.jump_origin) * t
                    y = 5 * math.sin(math.pi * t)
                    self.jump_progress += 0.03

            glPushMatrix()
            glTranslatef(x, y, 0)
            self.angle += 5
            glRotatef(self.angle, 0, 1, 0)
            glScalef(0.5, 0.5, 0.5)
            self.personaje()
            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == "__main__":
    juego = Juego()
    personaje_seleccionado = juego.seleccion_de_personaje()
    print(f"Has seleccionado al personaje: {personaje_seleccionado}")
