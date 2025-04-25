import pygame 
import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *

def esfera(radio, slices, segmentos):
    for i in range(slices):
        lat0 = math.pi * (-0.5 + i / slices)
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + (i + 1) / slices)
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        glBegin(GL_TRIANGLE_STRIP)
        for j in range(segmentos + 1):
            lng = 2 * math.pi * j / segmentos
            x = math.cos(lng)
            y = math.sin(lng)

            # Normales correctas (posición normalizada)
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(radio * x * zr0, radio * y * zr0, radio * z0)

            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(radio * x * zr1, radio * y * zr1, radio * z1)
        glEnd()

def cilindro(radio, altura, segmentos):
    # Cuerpo del cilindro
    glBegin(GL_QUAD_STRIP)
    for i in range(segmentos + 1):
        angulo = 2 * math.pi * i / segmentos
        x = math.cos(angulo) * radio
        y = math.sin(angulo) * radio

        # Normal para la superficie lateral
        glNormal3f(x, y, 0)
        glVertex3f(x, y, 0)
        glVertex3f(x, y, altura)
    glEnd()

def cono(radio, altura, segmentos):
    # DIBUJAR LA BASE DEL CONO
    glBegin(GL_TRIANGLE_FAN)
    glNormal3f(0, 0, -1)  # Normal hacia abajo
    glVertex3f(0, 0, 0)  # Centro de la base
    for i in range(segmentos + 1):
        angulo = 2 * math.pi * i / segmentos
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        glVertex3f(x, y, 0)
    glEnd()

    # DIBUJAR LA CARA LATERAL DEL CONO
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(segmentos + 1):
        angulo = 2 * math.pi * i / segmentos
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)

        # Normal calculada para suavizar iluminación
        normal_x = x
        normal_y = y
        normal_z = radio  # Aproximación normal de un cono

        glNormal3f(normal_x, normal_y, normal_z)
        glVertex3f(x, y, 0)  # Punto en la base
        glVertex3f(0, 0, altura)  # Punta del cono
    glEnd()

def cubo():
    glBegin(GL_QUADS)
    glNormal3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(1, 1, 0)
    glVertex3f(0, 1, 0)

    glNormal3f(0, 0, -1)
    glVertex3f(0, 0, 1)
    glVertex3f(0, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 0, 1)

    glNormal3f(0, 1, 0)
    glVertex3f(0, 1, 0)
    glVertex3f(1, 1, 0)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 1, 1)

    glNormal3f(0, -1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 0, 0)

    glNormal3f(1, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, 0)

    glNormal3f(-1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)
    glVertex3f(0, 1, 1)
    glVertex3f(0, 0, 1)
    glEnd()

def piramide(base=2.0, altura=3.0):
    mitad = base / 2.0
    glBegin(GL_TRIANGLES)

    glVertex3f(-mitad, 0.0, mitad)
    glVertex3f(mitad, 0.0, mitad)
    glVertex3f(0.0, altura, 0.0)

    glVertex3f(mitad, 0.0, mitad)
    glVertex3f(mitad, 0.0, -mitad)
    glVertex3f(0.0, altura, 0.0)

    glVertex3f(mitad, 0.0, -mitad)
    glVertex3f(-mitad, 0.0, -mitad)
    glVertex3f(0.0, altura, 0.0)

    glVertex3f(-mitad, 0.0, -mitad)
    glVertex3f(-mitad, 0.0, mitad)
    glVertex3f(0.0, altura, 0.0)

    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-mitad, 0.0, mitad)
    glVertex3f(mitad, 0.0, mitad)
    glVertex3f(mitad, 0.0, -mitad)
    glVertex3f(-mitad, 0.0, -mitad)
    glEnd()

def piramide_truncada(base_inf=2.0, base_sup=0.5, altura=3.0):
    mi, ms = base_inf / 2.0, base_sup / 2.0
    A = [-mi, 0.0, mi]; B = [mi, 0.0, mi]
    C = [mi, 0.0, -mi]; D = [-mi, 0.0, -mi]
    E = [-ms, altura, ms]; F = [ms, altura, ms]
    G = [ms, altura, -ms]; H = [-ms, altura, -ms]

    glBegin(GL_QUADS)
    glVertex3fv(A); glVertex3fv(B); glVertex3fv(F); glVertex3fv(E)
    glVertex3fv(B); glVertex3fv(C); glVertex3fv(G); glVertex3fv(F)
    glVertex3fv(C); glVertex3fv(D); glVertex3fv(H); glVertex3fv(G)
    glVertex3fv(D); glVertex3fv(A); glVertex3fv(E); glVertex3fv(H)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3fv(A); glVertex3fv(B); glVertex3fv(C); glVertex3fv(D)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3fv(E); glVertex3fv(F); glVertex3fv(G); glVertex3fv(H)
    glEnd()

def cabeza_con_ojos():
    glPushMatrix()
    glTranslatef(0.0, 8.0, 0.0)
    glRotatef(180, 1, 0, 0)
    glColor3f(1.0, 0.0, 0.0)
    piramide(base=3.5, altura=4.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 8.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    piramide_truncada(base_inf=3.5, base_sup=2.0, altura=2.0)
    glPopMatrix()

    for x in [-1.0, 1.0]:
        glPushMatrix()
        glTranslatef(x, 9.0, 1.6)
        glColor3f(1.0, 1.0, 1.0)
        esfera(0.4, 20, 20)  # Llamada a la función esfera con radio, slices y segmentos
        glPopMatrix()

        glPushMatrix()
        glTranslatef(x, 9.0, 1.98)
        glColor3f(0.0, 0.0, 0.0)
        esfera(0.2, 20, 20)  # Llamada a la función esfera para los ojos, con tamaño más pequeño
        glPopMatrix()


def figura_completa():
    glPushMatrix()
    glTranslatef(0.0, 2.0, 0.0)  
    glColor3f(0.0, 0.5, 0.0)
    piramide(base=7.0, altura=5.0) 
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 2.0, 0.0)  
    glRotatef(180, 1, 0, 0)
    glColor3f(1.0, 0.0, 0.0)
    piramide_truncada(base_inf=5.0, base_sup=2.0, altura=2.0) 
    glPopMatrix()

    cabeza_con_ojos()  

    colores = [(0.0, 0.0, 1.0), (1.0, 1.0, 0.0), (0.0, 1.0, 1.0), (1.0, 0.0, 1.0)]
    posiciones = [(-3.0, 3.0), (3.0, 3.0), (-3.0, -3.0), (3.0, -3.0)] 

    for (x, z), color in zip(posiciones, colores):
        glPushMatrix()
        glTranslatef(x, -2.0, z)  # antes -1.0
        glColor3f(*color)
        piramide_truncada(base_inf=2.0, base_sup=1.0, altura=4.0)
        glPopMatrix()

def camina():
    global frame
    frame += 1
    angulo = math.sin(frame * 0.03) * 20  # Menor frecuencia y amplitud

    # Cuerpo
    glPushMatrix()
    glTranslatef(0.0, 1.0, 0.0)
    glColor3f(0.0, 0.5, 0.0)
    piramide(base=3.5, altura=2.5)
    glPopMatrix()

    # Parte inferior del torso
    glPushMatrix()
    glTranslatef(0.0, 1.0, 0.0)
    glRotatef(180, 1, 0, 0)
    glColor3f(1.0, 0.0, 0.0)
    piramide_truncada(base_inf=2.5, base_sup=1.0, altura=1.0)
    glPopMatrix()

    # Cabeza con ojos
    cabeza_con_ojos()

    # Piernas animadas
    posiciones = [(-1.5, 1.5), (1.5, 1.5), (-1.5, -1.5), (1.5, -1.5)]
    colores = [(0.0, 0.0, 1.0), (1.0, 1.0, 0.0), (0.0, 1.0, 1.0), (1.0, 0.0, 1.0)]

    for i, ((x, z), color) in enumerate(zip(posiciones, colores)):
        glPushMatrix()
        glTranslatef(x, -1.0, z)

        if i % 2 == 0:
            glRotatef(angulo, 1, 0, 0)
        else:
            glRotatef(-angulo, 1, 0, 0)

        glColor3f(*color)
        piramide_truncada(base_inf=1.0, base_sup=0.5, altura=2.0)
        glPopMatrix()

