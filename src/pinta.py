import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
import math
#from Acciones.sonidos import *
#import Acciones.textos as tx
import Acciones.colores as cl
import Acciones.objetos as obj
import Acciones.luces as lc
import time


# Variables para la posición del objeto
posx = 0
posy = 5# 🔹 Ajustado para que empiece en el suelo
posz = 0

tiempo_inicial = time.time()

def pintaEsfera():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glPushMatrix()
    glTranslatef(posx,posy,posz) 
    lc.iluminacion(1.0,1.0,1.0)
    cl.matBeige()
    obj.esfera(2,40,80)
    glPopMatrix()

def pintaEsfera2():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glPushMatrix()
    glTranslatef(-15,-2,posz) 
    lc.iluminacion(1.0,1.0,1.0)
    cl.colorRojo()
    obj.esfera(2,40,80)
    glPopMatrix()

def pintaEsfera3():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glPushMatrix()
    glTranslatef(-3,-3,posz) 
    lc.iluminacion(0.0,0.0,1.0)
    cl.colorGrisOscuro()
    obj.esfera(2,40,80)
    glPopMatrix()  

#Inicio Mike

def pintaEsferaMike(x, y, z, r, sl, seg):
    glPushMatrix()
    glTranslatef(x, y, z)
    lc.iluminacion(0.0, 0.0, 0.0)  
    cl.matRojo()
    obj.esfera(r, sl, seg)
    glPopMatrix()

def pintaCilindroMike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    lc.iluminacion(0.0, 0.0, 0.0)  
    cl.matAzulMarino()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaCilindro():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glPushMatrix()
    glTranslatef(posx, posy, posz)  # Posición en la pantalla
    glRotatef(90, 1, 0, 0)  # Para que el cilindro quede "parado"
    lc.iluminacion(1.0, 1.0, 1.0)  # Iluminación blanca
    cl.colorGris()  # Color del cuerpo
    obj.cilindro(1, 2, 40)  # (radio, altura, segmentos)
    glPopMatrix()

def pintaCaraMike(x,y,z,r,a):
    glPushMatrix()
    glTranslatef(x,y,z)
    lc.iluminacion(0.0, 0.0, 0.0) 
    cl.matDuraznoPiel()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaZapatosMike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    lc.iluminacion(1.0, 1.0, 1.0) 
    cl.matBlanco()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaBrazoMike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(90, 0, 1, 0)
    lc.iluminacion(0.0, 0.0, 0.0) 
    cl.matAzulMarino()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaOjosMike(x, y, z, r, sl, seg):
    glPushMatrix()
    glTranslatef(x, y, z)
    lc.iluminacion(0.0, 0.0, 0.0) 
    cl.matAzulClaro()
    obj.esfera(r, sl, seg)
    glPopMatrix()

def pintaBocaSorpresaMike(x, y, z, r, sl, seg):
    glPushMatrix()
    glTranslatef(x, y, z)
    lc.iluminacion(0.0, 0.0, 0.0) 
    cl.matNegro()
    obj.esfera(r, sl, seg)
    glPopMatrix()

def pintaCilindro2Mike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    lc.iluminacion(0.0, 0.0, 0.0) 
    cl.matAmarillo()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaEsfera2Mike(x, y, z, r, sl, seg):
    glPushMatrix()
    glTranslatef(x, y, z)
    lc.iluminacion(0.0, 0.0, 0.0)  
    cl.matAmarillo()
    obj.esfera(r, sl, seg)
    glPopMatrix()

def pintaManosMike(x, y, z, r, sl, seg):
    glPushMatrix()
    glTranslatef(x, y, z)
    lc.iluminacion(0.0, 0.0, 0.0) 
    cl.matDuraznoPiel()
    obj.esfera(r, sl, seg)
    glPopMatrix()

def pintaCintasMike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    lc.iluminacion(0.0, 0.0, 0.0) 
    cl.matBlanco()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaCejasMike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(90, 0, 1, 0)
    lc.iluminacion(0.0, 0.0, 0.0)
    cl.matNegro()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaBrazo1Mike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-200, 0, 1, 0)
    lc.iluminacion(0.0, 0.0, 0.0) 
    cl.matAzulMarino()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintarSonrisaMike(cx, cy, cz, ancho=2.0, altura=0.5, resolucion=20):
    cl.matNegro()
    glLineWidth(4)  # Grosor de la línea
    glBegin(GL_LINE_STRIP)
    for i in range(resolucion + 1):
        x = -ancho / 2 + (i / resolucion) * ancho 
        y = -altura * (x ** 2) + altura  
        glVertex3f(cx + x, cy + y, cz)  
    glEnd()

def pintaCejasenojado1Mike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(45, 0, 1, 0)
    lc.iluminacion(0.0, 0.0, 0.0)
    cl.matNegro()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaCejasenojado2Mike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-45, 0, 1, 0)
    lc.iluminacion(0.0, 0.0, 0.0)
    cl.matNegro()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaPierna1Mike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(90, 1, 0, 0)
    lc.iluminacion(0.0, 0.0, 0.0)  
    cl.matAzulMarino()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaPierna2Mike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(45, 1, 0, 0)
    lc.iluminacion(0.0, 0.0, 0.0)  
    cl.matAzulMarino()
    obj.cilindro(r, a, 40)
    glPopMatrix()

def pintaPierna3Mike(x, y, z, r, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-45, 1, 0, 0)
    lc.iluminacion(0.0, 0.0, 0.0)  
    cl.matAzulMarino()
    obj.cilindro(r, a, 40)
    glPopMatrix()


# seccion para pintar movimientos (Mike)
def pintarLevantarBrazo():
    pintaCejasMike(0.5, 1.9, 11.9, 0.1, 1)
    pintaCejasMike(-1.5, 1.9, 11.9, 0.1, 1)
    pintaCejasMike(-.5, 2, 10.7, 0.1, 1)
    pintaCilindro(0, 0, 3, 2, 7)
    pintaCilindro(1, 0, 0.5, 0.3, 2.5)
    pintaCilindro(-1, 0, 0.5, 0.3, 2.5)
    pintaCaraMike(0, 0, 10, 2, 3.2)
    pintaZapatosMike(1, 0, 0, 0.6, 1)
    pintaZapatosMike(-1, 0, 0, 0.6, 1)
    pintaEsfera(0, 0, 12.8, 2.2, 16, 30)
    pintaOjosMike(1, 1.6, 11.5, 0.3, 15, 50)
    pintaOjosMike(-1, 1.6, 11.5, 0.3, 15, 50)
    pintaBrazo1Mike(-3, 0, 12, 0.6, 3.5)
    pintaBrazoMike(2, 0, 8.3, 0.6, 3.5)
    pintaCilindro2Mike(0, 2, 8, 0.2, 2)
    pintaEsfera2Mike(0, 2, 8, 0.5, 15, 50)
    pintaManosMike(-3, 0, 12, 0.5, 15, 50)
    pintaManosMike(5.5, 0, 8.3, 0.5, 15, 50)
    pintaCintasMike(-1, 1.8, 6, 0.1, 4)
    pintaCintasMike(1, 1.8, 6, 0.1, 4)

def pintarLevantarPierna():
    pintaCejasMike(0.5, 1.9, 11.9, 0.1, 1)
    pintaCejasMike(-1.5, 1.9, 11.9, 0.1, 1)
    pintaCejasMike(-.5, 2, 10.7, 0.1, 1)
    pintaCilindro(0, 0, 3, 2, 7)
    pintaPierna1Mike(1, 3, 3, 0.3, 2.5)
    pintaCilindro(-1, 0, 0.5, 0.3, 2.5)
    pintaCaraMike(0, 0, 10, 2, 3.2)
    pintaZapatosMike(1, 3,2.8, 0.6, 1)
    pintaZapatosMike(-1, 0, 0, 0.6, 1)
    pintaEsfera(0, 0, 12.8, 2.2, 16, 30)
    pintaOjosMike(1, 1.6, 11.5, 0.3, 15, 50)
    pintaOjosMike(-1, 1.6, 11.5, 0.3, 15, 50)
    pintaBrazoMike(-5.5, 0, 8.3, 0.6, 3.5)
    pintaBrazoMike(2, 0, 8.3, 0.6, 3.5)
    pintaCilindro2Mike(0, 2, 8, 0.2, 2)
    pintaEsfera2(0, 2, 8, 0.5, 15, 50)
    pintaManosMike(-5.5, 0, 8.3, 0.5, 15, 50)
    pintaManosMike(5.5, 0, 8.3, 0.5, 15, 50)
    pintaCintasMike(-1, 1.8, 6, 0.1, 4)
    pintaCintasMike(1, 1.8, 6, 0.1, 4)

def pintarSaltar():
    pintaCejasMike(0.5, 1.9, 14.9, 0.1, 1)
    pintaCejasMike(-1.5, 1.9, 14.9, 0.1, 1)
    pintaCejasMike(-.5, 2, 13.7, 0.1, 1)
    pintaCilindro(0, 0, 6, 2, 7)
    pintaPierna1Mike(1, 3, 6, 0.3, 2.5)
    pintaCilindro(-1, 0, 3.5, 0.3, 2.5)
    pintaCaraMike(0, 0, 13, 2, 3.2)
    pintaZapatosMike(1, 3,5.8, 0.6, 1)
    pintaZapatosMike(-1, 0, 3, 0.6, 1)
    pintaEsfera(0, 0, 15.8, 2.2, 16, 30)
    pintaOjosMike(1, 1.6, 14.5, 0.3, 15, 50)
    pintaOjosMike(-1, 1.6, 14.5, 0.3, 15, 50)
    pintaBrazoMike(-5.5, 0, 11.3, 0.6, 3.5)
    pintaBrazoMike(2, 0, 11.3, 0.6, 3.5)
    pintaCilindro2Mike(0, 2, 11, 0.2, 2)
    pintaEsfera2(0, 2, 11, 0.5, 15, 50)
    pintaManosMike(-5.5, 0, 11.3, 0.5, 15, 50)
    pintaManosMike(5.5, 0, 11.3, 0.5, 15, 50)
    pintaCintasMike(-1, 1.8, 9, 0.1, 4)
    pintaCintasMike(1, 1.8, 9, 0.1, 4)

def pintarAgacharse():
    pintaCejasMike(0.5, 1.9, 8.9, 0.1, 1)
    pintaCejasMike(-1.5, 1.9, 8.9, 0.1, 1)
    pintaCejasMike(-.5, 2, 7.7, 0.1, 1)
    pintaCilindro(0, 0, 0, 2, 7)
    pintaPierna1Mike(1, -1.5, .5, 0.3, 2.5)
    pintaPierna1Mike(-1, -1.5, .5, 0.3, 2.5)
    pintaCaraMike(0, 0, 7, 2, 3.2)
    pintaZapatosMike(1, -3.5, .5, 0.6, 1)
    pintaZapatosMike(-1, -3.5, .5, 0.6, 1)
    pintaEsfera(0, 0, 9.8, 2.2, 16, 30)
    pintaOjosMike(1, 1.6, 8.5, 0.3, 15, 50)
    pintaOjosMike(-1, 1.6, 8.5, 0.3, 15, 50)
    pintaBrazoMike(-5.5, 0, 5.3, 0.6, 3.5)
    pintaBrazoMike(2, 0, 5.3, 0.6, 3.5)
    pintaCilindro2Mike(0, 2, 5, 0.2, 2)
    pintaEsfera2(0, 2, 5, 0.5, 15, 50)
    pintaManosMike(-5.5, 0, 5.3, 0.5, 15, 50)
    pintaManosMike(5.5, 0, 5.3, 0.5, 15, 50)
    pintaCintasMike(-1, 1.8, 3, 0.1, 4)
    pintaCintasMike(1, 1.8, 3, 0.1, 4)

def pintarFlexionar():
    pintaCejasMike(0.5, 1.9, 11.4, 0.1, 1)
    pintaCejasMike(-1.5, 1.9, 11.4, 0.1, 1)
    pintaCejasMike(-.5, 2, 10.2, 0.1, 1)
    pintaCilindro(0, 0, 2.5, 2, 7)
    pintaPierna2Mike(1, 2, 2, 0.3, 1)
    pintaPierna2Mike(-1, 2, 2, 0.3, 1)
    pintaPierna3Mike(1, 1.3, 1.5, 0.3, 1)
    pintaPierna3Mike(-1, 1.3, 1.5, 0.3, 1)
    pintaCaraMike(0, 0, 9.5, 2, 3.2)
    pintaZapatosMike(1, 0.7, .5, 0.6, 1)
    pintaZapatosMike(-1, .7, .5, 0.6, 1)
    pintaEsfera(0, 0, 12.3, 2.2, 16, 30)
    pintaOjosMike(1, 1.6, 11, 0.3, 15, 50)
    pintaOjosMike(-1, 1.6, 11, 0.3, 15, 50)
    pintaBrazoMike(-5.5, 0, 7.8, 0.6, 3.5)
    pintaBrazoMike(2, 0, 7.8, 0.6, 3.5)
    pintaCilindro2Mike(0, 2, 7.5, 0.2, 2)
    pintaEsfera2(0, 2, 7.5, 0.5, 15, 50)
    pintaManosMike(-5.5, 0, 7.8, 0.5, 15, 50)
    pintaManosMike(5.5, 0, 7.8, 0.5, 15, 50)
    pintaCintasMike(-1, 1.8, 5.5, 0.1, 4)
    pintaCintasMike(1, 1.8, 5.5, 0.1, 4)

#huesos

def pintaHuesos():
    obj.figura_completa()

#Inicio Mapache

def pintaMapache():
    global tiempo_inicial
    
    tiempo_actual = time.time() - tiempo_inicial
    angulo_brazo = 40 * math.sin(tiempo_actual * 5)  # Oscilación de brazo 
 
    # 🔹 Dibujar el cuerpo (cilindro) alineado con Z
    glPushMatrix()
    glTranslatef(posx, posy, posz)  # Asegurar que está en el centro
    glRotatef(270, 1, 0, 0) # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Cuerpo en color gris
    obj.cilindro(1.5, 4, 40)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Dibujar la cabeza (esfera superior en Z)
    glPushMatrix()
    glTranslatef(posx, posy+4, posz )  # Se mueve en Z, no en Y
    glRotatef(270, 1, 0, 0)  # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Color de la cabeza
    obj.esfera(1.6, 40, 80)  # radio, slices, segmentos
    glPopMatrix()

        # 🔹 Ojo derecho
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorNegroPlano()  # Ojos en color negro
    obj.esfera(0.3, 20, 20)  # Esfera pequeña para el ojo
    glPopMatrix()

    # 🔹 Ojo izquierdo
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    cl.colorNegroPlano()
    obj.esfera(0.3, 20, 20)
    glPopMatrix()

    # 🔹 Oreja derecha (cono aplastado con punta redondeada)
    glPushMatrix()
    glTranslatef(posx + 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()  
    obj.cono(0.5, 1.3, 20)  # Cono base
    glPopMatrix()


    # 🔹 Oreja izquierda
    glPushMatrix()
    glTranslatef(posx - 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(-25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()
    obj.cono(0.5, 1.3, 20)  
    glPopMatrix()

    # 🔹 Dibujar la base (esfera inferior en Z)
    glPushMatrix()
    glTranslatef(posx, posy, posz )  # Se mueve en Z
    glRotatef(270, 1, 0, 0)
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Parte inferior más oscura
    obj.esfera(1.5, 40, 80)  # radio, slices, segmentos
    glPopMatrix()
   
    # 🔹 Brazo derecho
    glPushMatrix()
    glTranslatef(posx+1 , posy + 3, posz)  # Lado derecho
    glRotatef(45, 1, 0, 0)  # Hacia afuera
    glRotatef(40, 0, 1, 0)  # Ajustar inclinación
    glRotatef(angulo_brazo, 0, 1, 0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Brazo izquierdo
    glPushMatrix()
    glTranslatef(posx , posy + 3, posz)  # Lado izquierdo
    glRotatef(270, 0, 1, 0)  # Hacia afuera
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna derecha
    glPushMatrix()
    glTranslatef(posx + 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna izquierda
    glPushMatrix()
    glTranslatef(posx - 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGrisOscuro()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Base de la cola (Cono grande)
    glPushMatrix()
    glTranslatef(posx, posy , posz - 3.5)  # Un poco debajo y detrás del cuerpo
    glRotatef(15, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.2, 1.5, 1.2)  # Ajusta la forma
    cl.colorGrisOscuro()  # Parte más oscura de la cola
    obj.cono(1.0, 3.0, 20)  # Base de la cola
    glPopMatrix()

    # 🔹 Parte media (Esfera esponjosa)
    glPushMatrix()
    glTranslatef(posx, posy+0.1 , posz - 4)  # Más atrás y arriba de la base
    glScalef(1.2, 1.5, 1.3)  # Más grande para dar volumen
    cl.colorGris()  # Color más claro
    obj.esfera(1.1, 30, 30)  # Esfera mediana
    glPopMatrix()

    # 🔹 Punta de la cola (Cono más pequeño)
    glPushMatrix()
    glTranslatef(posx, posy +0.4, posz - 4.8)  # Más arriba y atrás
    glRotatef(-165, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.1, 1.5, 1.1)  # Tamaño de la punta
    cl.colorGrisOscuro()  # La punta puede ser más oscura
    obj.cono(1, 2.0, 20)  # Cono más pequeño
    glPopMatrix()

    # 🔹 Cejas derecha
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo derecho
    glRotatef(90, 1, 0, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea más delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Cejas izquierda
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo izquierdo
    glRotatef(90, 1, 0, 0)  # Igual que la ceja derecha
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Base de la boca (Esfera achatada blanca)
    glPushMatrix()
    glTranslatef(posx, posy + 4.2, posz + 1)  # Justo debajo de los ojos
    glScalef(1.2, 0.8, 1.0)  # Aplastar la esfera en el eje Y
    cl.colorBlancoPlano()  # Color blanco para la base
    obj.esfera(0.7, 30, 30)  # Esfera base de la boca
    glPopMatrix()

    # 🔹 Parte superior de la boca (Esfera achatada negra)
    glPushMatrix()
    glTranslatef(posx, posy + 4.3, posz + 1.55)  # Un poco más arriba y adelante
    glScalef(1.0, 0.8, 0.8)  # Más achatada en Y para dar efecto de sombra
    cl.colorNegroPlano()  # Color negro para la parte superior
    obj.esfera(0.3, 30, 30)  # Esfera superior
    glPopMatrix()

def pintaMapacheEnojado():
    global tiempo_inicial
    tiempo_actual = time.time() - tiempo_inicial
    angulo_brazo = 70 * math.sin(tiempo_actual * 5)  # Oscilación de brazo 
    # 🔹 Dibujar el cuerpo (cilindro) alineado con Z
    glPushMatrix()
    glTranslatef(posx, posy, posz)  # Asegurar que está en el centro
    glRotatef(270, 1, 0, 0) # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Cuerpo en color gris
    obj.cilindro(1.5, 4, 40)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Dibujar la cabeza (esfera superior en Z)
    glPushMatrix()
    glTranslatef(posx, posy+4, posz )  # Se mueve en Z, no en Y
    glRotatef(270, 1, 0, 0)  # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Color de la cabeza
    obj.esfera(1.6, 40, 80)  # radio, slices, segmentos
    glPopMatrix()

        # 🔹 Ojo derecho
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorNegroPlano()  # Ojos en color negro
    obj.esfera(0.3, 20, 20)  # Esfera pequeña para el ojo
    glPopMatrix()

    # 🔹 Ojo izquierdo
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    cl.colorNegroPlano()
    obj.esfera(0.3, 20, 20)
    glPopMatrix()

    # 🔹 Oreja derecha (cono aplastado con punta redondeada)
    glPushMatrix()
    glTranslatef(posx + 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()  
    obj.cono(0.5, 1.3, 20)  # Cono base
    glPopMatrix()


    # 🔹 Oreja izquierda
    glPushMatrix()
    glTranslatef(posx - 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(-25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()
    obj.cono(0.5, 1.3, 20)  
    glPopMatrix()

    # 🔹 Dibujar la base (esfera inferior en Z)
    glPushMatrix()
    glTranslatef(posx, posy, posz )  # Se mueve en Z
    glRotatef(270, 1, 0, 0)
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Parte inferior más oscura
    obj.esfera(1.5, 40, 80)  # radio, slices, segmentos
    glPopMatrix()

      # 🔹 Brazo derecho
    glPushMatrix()
    glTranslatef(posx+1 , posy + 3, posz)  # Lado derecho
    glRotatef(-40, 1, 0, 0)  # Hacia afuera
    glRotatef(90, 0, 1, 0)  # Ajustar inclinación
    glRotatef(0, 0, 0, 1)  # Ajustar inclinación
    glRotatef(angulo_brazo, 0, 1, 0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Brazo izquierdo
    glPushMatrix()
    glTranslatef(posx-1 , posy + 3, posz)  # Lado derecho
    glRotatef(40, 1, 0, 0)  # Hacia afuera
    glRotatef(-90, 0, 1, 0)  # Ajustar inclinación
    glRotatef(-10, 0, 0, 1)  # Ajustar inclinación
    glRotatef(angulo_brazo, 0, 1, 0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna derecha
    glPushMatrix()
    glTranslatef(posx + 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna izquierda
    glPushMatrix()
    glTranslatef(posx - 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGrisOscuro()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Base de la cola (Cono grande)
    glPushMatrix()
    glTranslatef(posx, posy , posz - 3.5)  # Un poco debajo y detrás del cuerpo
    glRotatef(15, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.2, 1.5, 1.2)  # Ajusta la forma
    cl.colorGrisOscuro()  # Parte más oscura de la cola
    obj.cono(1.0, 3.0, 20)  # Base de la cola
    glPopMatrix()

    # 🔹 Parte media (Esfera esponjosa)
    glPushMatrix()
    glTranslatef(posx, posy+0.1 , posz - 4)  # Más atrás y arriba de la base
    glScalef(1.2, 1.5, 1.3)  # Más grande para dar volumen
    cl.colorGris()  # Color más claro
    obj.esfera(1.1, 30, 30)  # Esfera mediana
    glPopMatrix()

    # 🔹 Punta de la cola (Cono más pequeño)
    glPushMatrix()
    glTranslatef(posx, posy +0.4, posz - 4.8)  # Más arriba y atrás
    glRotatef(-165, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.1, 1.5, 1.1)  # Tamaño de la punta
    cl.colorGrisOscuro()  # La punta puede ser más oscura
    obj.cono(1, 2.0, 20)  # Cono más pequeño
    glPopMatrix()

    # 🔹 Cejas derecha
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo derecho
    glRotatef(90, 1, 0, 0)  # Para que la ceja quede recta horizontalmente
    glRotatef(20, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea más delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Cejas izquierda
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo izquierdo
    glRotatef(90, 1, 0, 0)  # Igual que la ceja derecha
    glRotatef(-20, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Base de la boca (Esfera achatada blanca)
    glPushMatrix()
    glTranslatef(posx, posy + 4.2, posz + 1)  # Justo debajo de los ojos
    glScalef(1.2, 0.8, 1.0)  # Aplastar la esfera en el eje Y
    cl.colorBlancoPlano()  # Color blanco para la base
    obj.esfera(0.7, 30, 30)  # Esfera base de la boca
    glPopMatrix()

    # 🔹 Parte superior de la boca (Esfera achatada negra)
    glPushMatrix()
    glTranslatef(posx, posy + 4.3, posz + 1.55)  # Un poco más arriba y adelante
    glScalef(1.0, 0.8, 0.8)  # Más achatada en Y para dar efecto de sombra
    cl.colorNegroPlano()  # Color negro para la parte superior
    obj.esfera(0.3, 30, 30)  # Esfera superior
    glPopMatrix()

def pintaMapacheFeliz():
    # 🔹 Dibujar el cuerpo (cilindro) alineado con Z
    glPushMatrix()
    glTranslatef(posx, posy, posz)  # Asegurar que está en el centro
    glRotatef(270, 1, 0, 0) # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Cuerpo en color gris
    obj.cilindro(1.5, 4, 40)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Dibujar la cabeza (esfera superior en Z)
    glPushMatrix()
    glTranslatef(posx, posy+4, posz )  # Se mueve en Z, no en Y
    glRotatef(270, 1, 0, 0)  # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Color de la cabeza
    obj.esfera(1.6, 40, 80)  # radio, slices, segmentos
    glPopMatrix()

        # 🔹 Ojo derecho
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorNegroPlano()  # Ojos en color negro
    obj.esfera(0.3, 20, 20)  # Esfera pequeña para el ojo
    glPopMatrix()

    # 🔹 Ojo izquierdo
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    cl.colorNegroPlano()
    obj.esfera(0.3, 20, 20)
    glPopMatrix()

    # 🔹 Oreja derecha (cono aplastado con punta redondeada)
    glPushMatrix()
    glTranslatef(posx + 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()  
    obj.cono(0.5, 1.3, 20)  # Cono base
    glPopMatrix()


    # 🔹 Oreja izquierda
    glPushMatrix()
    glTranslatef(posx - 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(-25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()
    obj.cono(0.5, 1.3, 20)  
    glPopMatrix()

    # 🔹 Dibujar la base (esfera inferior en Z)
    glPushMatrix()
    glTranslatef(posx, posy, posz )  # Se mueve en Z
    glRotatef(270, 1, 0, 0)
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Parte inferior más oscura
    obj.esfera(1.5, 40, 80)  # radio, slices, segmentos
    glPopMatrix()
    # 🔹 Brazo derecho 
    glPushMatrix()
    glTranslatef(posx + 1, posy + 2.8, posz)  # Más alto y un poco hacia el lado
    glRotatef(-45, 1, 0, 0)  # Rotar hacia arriba
    glRotatef(20, 0, 0, 1)  # Ajustar inclinación
    glRotatef(40, 0, 1, 0)  # Ajustar inclinación
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # Radio, altura, segmentos
    glPopMatrix()

    # 🔹 Brazo izquierdo
    glPushMatrix()
    glTranslatef(posx-1 , posy + 2.8, posz)  # Lado izquierdo
    glRotatef(-45, 1, 0, 0)  # Hacia afuera
    glRotatef(-20, 0, 0, 1)  # Ajustar inclinación
    glRotatef(-40, 0, 1, 0)  # Ajustar inclinación
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna derecha
    glPushMatrix()
    glTranslatef(posx + 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna izquierda
    glPushMatrix()
    glTranslatef(posx - 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGrisOscuro()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Base de la cola (Cono grande)
    glPushMatrix()
    glTranslatef(posx, posy , posz - 3.5)  # Un poco debajo y detrás del cuerpo
    glRotatef(15, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.2, 1.5, 1.2)  # Ajusta la forma
    cl.colorGrisOscuro()  # Parte más oscura de la cola
    obj.cono(1.0, 3.0, 20)  # Base de la cola
    glPopMatrix()

    # 🔹 Parte media (Esfera esponjosa)
    glPushMatrix()
    glTranslatef(posx, posy+0.1 , posz - 4)  # Más atrás y arriba de la base
    glScalef(1.2, 1.5, 1.3)  # Más grande para dar volumen
    cl.colorGris()  # Color más claro
    obj.esfera(1.1, 30, 30)  # Esfera mediana
    glPopMatrix()

    # 🔹 Punta de la cola (Cono más pequeño)
    glPushMatrix()
    glTranslatef(posx, posy +0.4, posz - 4.8)  # Más arriba y atrás
    glRotatef(-165, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.1, 1.5, 1.1)  # Tamaño de la punta
    cl.colorGrisOscuro()  # La punta puede ser más oscura
    obj.cono(1, 2.0, 20)  # Cono más pequeño
    glPopMatrix()

    # 🔹 Cejas derecha
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo derecho
    glRotatef(90, 1, 0, 0)  # Para que la ceja quede recta horizontalmente
    glRotatef(0, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea más delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Cejas izquierda
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo izquierdo
    glRotatef(90, 1, 0, 0)  # Igual que la ceja derecha
    glRotatef(0, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

      # 🔹 Cejas derecha
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 4.3, posz + 1.2)  # Ajusta la posición sobre el ojo derecho
    glRotatef(90, 1, 0, 0)  # Para que la ceja quede recta horizontalmente
    glRotatef(20, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea más delgada
    cl.colorRosa()  # Color negro para la ceja
    obj.cilindro(0.50, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Cejas izquierda
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 4.3, posz + 1.2)  # Ajusta la posición sobre el ojo izquierdo
    glRotatef(90, 1, 0, 0)  # Igual que la ceja derecha
    glRotatef(-20, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea delgada
    cl.colorRosa()  # Color negro para la ceja
    obj.cilindro(0.50, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Base de la boca (Esfera achatada blanca)
    glPushMatrix()
    glTranslatef(posx, posy + 4.2, posz + 1)  # Justo debajo de los ojos
    glScalef(1.2, 0.8, 1.0)  # Aplastar la esfera en el eje Y
    cl.colorBlancoPlano()  # Color blanco para la base
    obj.esfera(0.7, 30, 30)  # Esfera base de la boca
    glPopMatrix()

    # 🔹 Parte superior de la boca (Esfera achatada negra)
    glPushMatrix()
    glTranslatef(posx, posy + 4.3, posz + 1.55)  # Un poco más arriba y adelante
    glScalef(1.0, 0.8, 0.8)  # Más achatada en Y para dar efecto de sombra
    cl.colorNegroPlano()  # Color negro para la parte superior
    obj.esfera(0.3, 30, 30)  # Esfera superior
    glPopMatrix()

def pintaMapacheTriste():
    # 🔹 Dibujar el cuerpo (cilindro) alineado con Z
    glPushMatrix()
    glTranslatef(posx, posy, posz)  # Asegurar que está en el centro
    glRotatef(270, 1, 0, 0) # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Cuerpo en color gris
    obj.cilindro(1.5, 4, 40)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Dibujar la cabeza (esfera superior en Z)
    glPushMatrix()
    glTranslatef(posx, posy+4, posz )  # Se mueve en Z, no en Y
    glRotatef(270, 1, 0, 0)  # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Color de la cabeza
    obj.esfera(1.6, 40, 80)  # radio, slices, segmentos
    glPopMatrix()

        # 🔹 Ojo derecho
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorNegroPlano()  # Ojos en color negro
    obj.esfera(0.3, 20, 20)  # Esfera pequeña para el ojo
    glPopMatrix()

    # 🔹 Ojo izquierdo
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    cl.colorNegroPlano()
    obj.esfera(0.3, 20, 20)
    glPopMatrix()

    # 🔹 Oreja derecha (cono aplastado con punta redondeada)
    glPushMatrix()
    glTranslatef(posx + 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()  
    obj.cono(0.5, 1.3, 20)  # Cono base
    glPopMatrix()


    # 🔹 Oreja izquierda
    glPushMatrix()
    glTranslatef(posx - 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(-25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()
    obj.cono(0.5, 1.3, 20)  
    glPopMatrix()

    # 🔹 Dibujar la base (esfera inferior en Z)
    glPushMatrix()
    glTranslatef(posx, posy, posz )  # Se mueve en Z
    glRotatef(270, 1, 0, 0)
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Parte inferior más oscura
    obj.esfera(1.5, 40, 80)  # radio, slices, segmentos
    glPopMatrix()
    # 🔹 Brazo derecho (levantado)
    glPushMatrix()
    glTranslatef(posx + 1, posy + 2.8, posz)  # Más alto y un poco hacia el lado
    glRotatef(45, 1, 0, 0)  # Rotar hacia arriba
    glRotatef(10, 0, 0, 1)  # Ajustar inclinación
    glRotatef(40, 0, 1, 0)  # Ajustar inclinación
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # Radio, altura, segmentos
    glPopMatrix()

    # 🔹 Brazo izquierdo
    glPushMatrix()
    glTranslatef(posx-1 , posy + 2.8, posz)  # Lado izquierdo
    glRotatef(45, 1, 0, 0)  # Hacia afuera
    glRotatef(-10, 0, 0, 1)   # Ajustar inclinación
    glRotatef(-40, 0, 1, 0)  # Ajustar inclinación
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna derecha
    glPushMatrix()
    glTranslatef(posx + 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna izquierda
    glPushMatrix()
    glTranslatef(posx - 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGrisOscuro()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Base de la cola (Cono grande)
    glPushMatrix()
    glTranslatef(posx, posy , posz - 3.5)  # Un poco debajo y detrás del cuerpo
    glRotatef(15, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.2, 1.5, 1.2)  # Ajusta la forma
    cl.colorGrisOscuro()  # Parte más oscura de la cola
    obj.cono(1.0, 3.0, 20)  # Base de la cola
    glPopMatrix()

    # 🔹 Parte media (Esfera esponjosa)
    glPushMatrix()
    glTranslatef(posx, posy+0.1 , posz - 4)  # Más atrás y arriba de la base
    glScalef(1.2, 1.5, 1.3)  # Más grande para dar volumen
    cl.colorGris()  # Color más claro
    obj.esfera(1.1, 30, 30)  # Esfera mediana
    glPopMatrix()

    # 🔹 Punta de la cola (Cono más pequeño)
    glPushMatrix()
    glTranslatef(posx, posy +0.4, posz - 4.8)  # Más arriba y atrás
    glRotatef(-165, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.1, 1.5, 1.1)  # Tamaño de la punta
    cl.colorGrisOscuro()  # La punta puede ser más oscura
    obj.cono(1, 2.0, 20)  # Cono más pequeño
    glPopMatrix()

    # 🔹 Cejas derecha
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo derecho
    glRotatef(90, 1, 0, 0)  # Para que la ceja quede recta horizontalmente
    glRotatef(-20, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea más delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Cejas izquierda
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo izquierdo
    glRotatef(90, 1, 0, 0)  # Igual que la ceja derecha
    glRotatef(20, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Base de la boca (Esfera achatada blanca)
    glPushMatrix()
    glTranslatef(posx, posy + 4.2, posz + 1)  # Justo debajo de los ojos
    glScalef(1.2, 0.8, 1.0)  # Aplastar la esfera en el eje Y
    cl.colorBlancoPlano()  # Color blanco para la base
    obj.esfera(0.7, 30, 30)  # Esfera base de la boca
    glPopMatrix()

    # 🔹 Parte superior de la boca (Esfera achatada negra)
    glPushMatrix()
    glTranslatef(posx, posy + 4.3, posz + 1.55)  # Un poco más arriba y adelante
    glScalef(1.0, 0.8, 0.8)  # Más achatada en Y para dar efecto de sombra
    cl.colorNegroPlano()  # Color negro para la parte superior
    obj.esfera(0.3, 30, 30)  # Esfera superior
    glPopMatrix()


# Establecer el tiempo inicial
tiempo_inicio = time.time()

# Definir la altura y velocidad del salto
altura_salto = 3 # Cuánto sube el mapache
velocidad_salto = 3  # Qué tan rápido sube y baja


def pintaMapacheSaltando():
    # Calcular el tiempo transcurrido desde el inicio
    tiempo_actual = time.time() - tiempo_inicio

    # Calcular la posición Y durante el salto (movimiento oscilatorio)
    posy_salto = posy + altura_salto * abs(math.sin(tiempo_actual * velocidad_salto))
    # 🔹 Dibujar el cuerpo (cilindro) alineado con Z
    glPushMatrix()
    glTranslatef(posx, posy_salto, posz)  # Asegurar que está en el centro
    glRotatef(270, 1, 0, 0) # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Cuerpo en color gris
    obj.cilindro(1.5, 4, 40)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Dibujar la cabeza (esfera superior en Z)
    glPushMatrix()
    glTranslatef(posx, posy_salto+4, posz )  # Se mueve en Z, no en Y
    glRotatef(270, 1, 0, 0)  # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Color de la cabeza
    obj.esfera(1.6, 40, 80)  # radio, slices, segmentos
    glPopMatrix()

        # 🔹 Ojo derecho
    glPushMatrix()
    glTranslatef(posx + 0.6, posy_salto + 4.8, posz + 1.3)  # Ajusta la posición
    lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorNegroPlano()  # Ojos en color negro
    obj.esfera(0.3, 20, 20)  # Esfera pequeña para el ojo
    glPopMatrix()

    # 🔹 Ojo izquierdo
    glPushMatrix()
    glTranslatef(posx - 0.6, posy_salto + 4.8, posz + 1.3)  # Ajusta la posición
    cl.colorNegroPlano()
    obj.esfera(0.3, 20, 20)
    glPopMatrix()

    # 🔹 Oreja derecha (cono aplastado con punta redondeada)
    glPushMatrix()
    glTranslatef(posx + 1, posy_salto + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()  
    obj.cono(0.5, 1.3, 20)  # Cono base
    glPopMatrix()


    # 🔹 Oreja izquierda
    glPushMatrix()
    glTranslatef(posx - 1, posy_salto + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(-25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()
    obj.cono(0.5, 1.3, 20)  
    glPopMatrix()

    # 🔹 Dibujar la base (esfera inferior en Z)
    glPushMatrix()
    glTranslatef(posx, posy_salto, posz )  # Se mueve en Z
    glRotatef(270, 1, 0, 0)
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Parte inferior más oscura
    obj.esfera(1.5, 40, 80)  # radio, slices, segmentos
    glPopMatrix()
    # 🔹 Brazo derecho 
    glPushMatrix()
    glTranslatef(posx + 1, posy_salto + 2.8, posz)  # Más alto y un poco hacia el lado
    glRotatef(-45, 1, 0, 0)  # Rotar hacia arriba
    glRotatef(20, 0, 0, 1)  # Ajustar inclinación
    glRotatef(40, 0, 1, 0)  # Ajustar inclinación
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # Radio, altura, segmentos
    glPopMatrix()

    # 🔹 Brazo izquierdo
    glPushMatrix()
    glTranslatef(posx-1 , posy_salto + 2.8, posz)  # Lado izquierdo
    glRotatef(-45, 1, 0, 0)  # Hacia afuera
    glRotatef(-20, 0, 0, 1)  # Ajustar inclinación
    glRotatef(-40, 0, 1, 0)  # Ajustar inclinación
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

   # 🔹 Pierna derecha (doblada)
    glPushMatrix()
    glTranslatef(posx + 0.8, posy_salto - 1, posz)  # Más arriba
    glRotatef(60, 1, 0, 0)  # Doblada hacia atrás
    cl.colorGris()
    obj.cilindro(0.4, 3, 20)  # Un poco más corto
    glPopMatrix()

    # 🔹 Pierna izquierda (doblada)
    glPushMatrix()
    glTranslatef(posx - 0.8, posy_salto - 1, posz)  
    glRotatef(60, 1, 0, 0)  
    cl.colorGris()
    obj.cilindro(0.4, 3, 20)  
    glPopMatrix()


    # 🔹 Base de la cola (Cono grande)
    glPushMatrix()
    glTranslatef(posx, posy_salto-1.8 , posz - 3.5)  # Un poco debajo y detrás del cuerpo
    #glRotatef(15, 1, 0, 0)  # Inclinación hacia atrás
    glRotatef(-30, 1, 0, 0)  # Inclina la cola hacia abajo
    glScalef(1.2, 1.5, 1.2)  # Ajusta la forma
    cl.colorGrisOscuro()  # Parte más oscura de la cola
    obj.cono(1.0, 3.0, 20)  # Base de la cola
    glPopMatrix()

    # 🔹 Parte media (Esfera esponjosa)
    glPushMatrix()
    glTranslatef(posx, posy_salto-2 , posz - 4)  # Más atrás y arriba de la base
    glScalef(1.2, 1.5, 1.3)  # Más grande para dar volumen
    cl.colorGris()  # Color más claro
    obj.esfera(1.1, 30, 30)  # Esfera mediana
    glPopMatrix()

    # 🔹 Punta de la cola (Cono más pequeño)
    glPushMatrix()
    glTranslatef(posx, posy_salto -2.2, posz - 4.6)  # Más arriba y atrás
    glRotatef(-195, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.1, 1.5, 1.1)  # Tamaño de la punta
    cl.colorGrisOscuro()  # La punta puede ser más oscura
    obj.cono(1, 2.0, 20)  # Cono más pequeño
    glPopMatrix()

    # 🔹 Cejas derecha
    glPushMatrix()
    glTranslatef(posx + 0.6, posy_salto + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo derecho
    glRotatef(90, 1, 0, 0)  # Para que la ceja quede recta horizontalmente
    glRotatef(0, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea más delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Cejas izquierda
    glPushMatrix()
    glTranslatef(posx - 0.6, posy_salto + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo izquierdo
    glRotatef(90, 1, 0, 0)  # Igual que la ceja derecha
    glRotatef(0, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Base de la boca (Esfera achatada blanca)
    glPushMatrix()
    glTranslatef(posx, posy_salto + 4.2, posz + 1)  # Justo debajo de los ojos
    glScalef(1.2, 0.8, 1.0)  # Aplastar la esfera en el eje Y
    cl.colorBlancoPlano()  # Color blanco para la base
    obj.esfera(0.7, 30, 30)  # Esfera base de la boca
    glPopMatrix()

    # 🔹 Parte superior de la boca (Esfera achatada negra)
    glPushMatrix()
    glTranslatef(posx, posy_salto + 4.3, posz + 1.55)  # Un poco más arriba y adelante
    glScalef(1.0, 0.8, 0.8)  # Más achatada en Y para dar efecto de sombra
    cl.colorNegroPlano()  # Color negro para la parte superior
    obj.esfera(0.3, 30, 30)  # Esfera superior
    glPopMatrix()


# Variable para alternar las posiciones de las patas (0 o 1)
paso = 0  

def pintaMapacheDuda():
    global tiempo_inicial
    
    tiempo_actual = time.time() - tiempo_inicial
    angulo_brazo = 40 * math.sin(tiempo_actual * 5)  # Oscilación de brazo 
 
    # 🔹 Dibujar el cuerpo (cilindro) alineado con Z
    glPushMatrix()
    glTranslatef(posx, posy, posz)  # Asegurar que está en el centro
    glRotatef(270, 1, 0, 0) # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Cuerpo en color gris
    obj.cilindro(1.5, 4, 40)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Dibujar la cabeza (esfera superior en Z)
    glPushMatrix()
    glTranslatef(posx, posy+4, posz )  # Se mueve en Z, no en Y
    glRotatef(270, 1, 0, 0)  # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Color de la cabeza
    obj.esfera(1.6, 40, 80)  # radio, slices, segmentos
    glPopMatrix()

        # 🔹 Ojo derecho
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorNegroPlano()  # Ojos en color negro
    obj.esfera(0.3, 20, 20)  # Esfera pequeña para el ojo
    glPopMatrix()

    # 🔹 Ojo izquierdo
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 4.8, posz + 1.3)  # Ajusta la posición
    cl.colorNegroPlano()
    obj.esfera(0.3, 20, 20)
    glPopMatrix()

    # 🔹 Oreja derecha (cono aplastado con punta redondeada)
    glPushMatrix()
    glTranslatef(posx + 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()  
    obj.cono(0.5, 1.3, 20)  # Cono base
    glPopMatrix()


    # 🔹 Oreja izquierda
    glPushMatrix()
    glTranslatef(posx - 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(-25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()
    obj.cono(0.5, 1.3, 20)  
    glPopMatrix()

    # 🔹 Dibujar la base (esfera inferior en Z)
    glPushMatrix()
    glTranslatef(posx, posy, posz )  # Se mueve en Z
    glRotatef(270, 1, 0, 0)
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Parte inferior más oscura
    obj.esfera(1.5, 40, 80)  # radio, slices, segmentos
    glPopMatrix()
   
    # 🔹 Brazo derecho
    glPushMatrix()
    glTranslatef(posx+1 , posy + 3, posz)  # Lado derecho
    glRotatef(45, 1, 0, 0)  # Hacia afuera
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Brazo izquierdo
    glPushMatrix()
    glTranslatef(posx -1, posy + 3, posz)  # Lado izquierdo
    glRotatef(270, 0, 1, 0)  # Hacia afuera
    glRotatef(40, 0, 1, 0)  # Ajustar inclinación
    glRotatef(angulo_brazo, 0, 1, 0)
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna derecha
    glPushMatrix()
    glTranslatef(posx + 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna izquierda
    glPushMatrix()
    glTranslatef(posx - 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)  # Hacia abajo
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGrisOscuro()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Base de la cola (Cono grande)
    glPushMatrix()
    glTranslatef(posx, posy , posz - 3.5)  # Un poco debajo y detrás del cuerpo
    glRotatef(15, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.2, 1.5, 1.2)  # Ajusta la forma
    cl.colorGrisOscuro()  # Parte más oscura de la cola
    obj.cono(1.0, 3.0, 20)  # Base de la cola
    glPopMatrix()

    # 🔹 Parte media (Esfera esponjosa)
    glPushMatrix()
    glTranslatef(posx, posy+0.1 , posz - 4)  # Más atrás y arriba de la base
    glScalef(1.2, 1.5, 1.3)  # Más grande para dar volumen
    cl.colorGris()  # Color más claro
    obj.esfera(1.1, 30, 30)  # Esfera mediana
    glPopMatrix()

    # 🔹 Punta de la cola (Cono más pequeño)
    glPushMatrix()
    glTranslatef(posx, posy +0.4, posz - 4.8)  # Más arriba y atrás
    glRotatef(-165, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.1, 1.5, 1.1)  # Tamaño de la punta
    cl.colorGrisOscuro()  # La punta puede ser más oscura
    obj.cono(1, 2.0, 20)  # Cono más pequeño
    glPopMatrix()

    # 🔹 Cejas derecha
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo derecho
    glRotatef(90, 1, 0, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea más delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

   # 🔹 Cejas izquierda
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo izquierdo
    glRotatef(90, 1, 0, 0)  # Igual que la ceja derecha
    glRotatef(-20, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Base de la boca (Esfera achatada blanca)
    glPushMatrix()
    glTranslatef(posx, posy + 4.2, posz + 1)  # Justo debajo de los ojos
    glScalef(1.2, 0.8, 1.0)  # Aplastar la esfera en el eje Y
    cl.colorBlancoPlano()  # Color blanco para la base
    obj.esfera(0.7, 30, 30)  # Esfera base de la boca
    glPopMatrix()

    # 🔹 Parte superior de la boca (Esfera achatada negra)
    glPushMatrix()
    glTranslatef(posx, posy + 4.3, posz + 1.55)  # Un poco más arriba y adelante
    glScalef(1.0, 0.8, 0.8)  # Más achatada en Y para dar efecto de sombra
    cl.colorNegroPlano()  # Color negro para la parte superior
    obj.esfera(0.3, 30, 30)  # Esfera superior
    glPopMatrix()

def pintaMapacheCaminando():
    global tiempo_inicial
    
    tiempo_actual = time.time() - tiempo_inicial
    angulo_pierna = 20 * math.sin(tiempo_actual * 5)  # Oscilación de piernas
    angulo_brazo = -angulo_pierna  # Los brazos se mueven en sentido contrario
    
     # 🔹 Dibujar el cuerpo (cilindro) alineado con Z
    glPushMatrix()
    glTranslatef(posx, posy, posz)  # Asegurar que está en el centro
    glRotatef(270, 1, 0, 0) # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Cuerpo en color gris
    obj.cilindro(1.5, 4, 40)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Dibujar la cabeza (esfera superior en Z)
    glPushMatrix()
    glTranslatef(posx, posy+4, posz )  # Se mueve en Z, no en Y
    glRotatef(270, 1, 0, 0)  # Para que quede parado
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Color de la cabeza
    obj.esfera(1.6, 40, 80)  # radio, slices, segmentos
    glPopMatrix()

     # 🔹 Cejas derecha
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 4.8, posz + 1.2)  # Ajusta la posición sobre el ojo derecho
    glRotatef(90, 1, 0, 0)  # Para que la ceja quede recta horizontalmente
    glRotatef(0, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea más delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.8, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Cejas izquierda
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 4.8, posz + 1.2)  # Ajusta la posición sobre el ojo izquierdo
    glRotatef(90, 1, 0, 0)  # Igual que la ceja derecha
    glRotatef(0, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.8, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Oreja derecha (cono aplastado con punta redondeada)
    glPushMatrix()
    glTranslatef(posx + 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()  
    obj.cono(0.5, 1.3, 20)  # Cono base
    glPopMatrix()


    # 🔹 Oreja izquierda
    glPushMatrix()
    glTranslatef(posx - 1, posy + 4.8, posz )  
    glRotatef(-90, 1, 0, 0)  
    glRotatef(-10, 0, 0, 1)  # Inclina hacia afuera en el eje Z
    glRotatef(-25, 0, 1, 0) 
    glScalef(1.5, 0.6, 1.5)  
    cl.colorGrisOscuro()
    obj.cono(0.5, 1.3, 20)  
    glPopMatrix()

    # 🔹 Dibujar la base (esfera inferior en Z)
    glPushMatrix()
    glTranslatef(posx, posy, posz )  # Se mueve en Z
    glRotatef(270, 1, 0, 0)
    #lc.iluminacion(1.0, 1.0, 1.0)
    cl.colorGris()  # Parte inferior más oscura
    obj.esfera(1.5, 40, 80)  # radio, slices, segmentos
    glPopMatrix()

    # 🔹 Brazo derecho
    glPushMatrix()
    glTranslatef(posx+1 , posy + 3, posz)  # Lado derecho
    glRotatef(45, 1, 0, 0)  # Hacia afuera
    glRotatef(40, 0, 1, 0)  # Ajustar inclinación
    glRotatef(-angulo_brazo, 1, 0, 0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Brazo izquierdo
    glPushMatrix()
    glTranslatef(posx-1 , posy + 3, posz)  # Lado izquierdo
    glRotatef(45, 1, 0, 0)  # Hacia afuera
    glRotatef(-40, 0, 1, 0)  # Ajustar inclinación
    glRotatef(angulo_brazo, 1, 0, 0)
    cl.colorGris()
    obj.cilindro(0.5, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna derecha
    glPushMatrix()
    glTranslatef(posx + 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0)
    glRotatef(-angulo_pierna, 1, 0, 0)
    cl.colorGris()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()

    # 🔹 Pierna izquierda
    glPushMatrix()
    glTranslatef(posx - 0.8, posy , posz)  # Debajo del cuerpo
    glRotatef(90, 1, 0, 0) 
    glRotatef(angulo_pierna, 1, 0, 0)  # Hacia abajo
    cl.colorGrisOscuro()
    obj.cilindro(0.4, 4, 20)  # radio, altura, segmentos
    glPopMatrix()


    # 🔹 Base de la cola (Cono grande)
    glPushMatrix()
    glTranslatef(posx, posy-1.8 , posz - 3.5)  # Un poco debajo y detrás del cuerpo
    #glRotatef(15, 1, 0, 0)  # Inclinación hacia atrás
    glRotatef(-30, 1, 0, 0)  # Inclina la cola hacia abajo
    glScalef(1.2, 1.5, 1.2)  # Ajusta la forma
    cl.colorGrisOscuro()  # Parte más oscura de la cola
    obj.cono(1.0, 3.0, 20)  # Base de la cola
    glPopMatrix()

    # 🔹 Parte media (Esfera esponjosa)
    glPushMatrix()
    glTranslatef(posx, posy-2 , posz - 4)  # Más atrás y arriba de la base
    glScalef(1.2, 1.5, 1.3)  # Más grande para dar volumen
    cl.colorGris()  # Color más claro
    obj.esfera(1.1, 30, 30)  # Esfera mediana
    glPopMatrix()

    # 🔹 Punta de la cola (Cono más pequeño)
    glPushMatrix()
    glTranslatef(posx, posy -2.2, posz - 4.6)  # Más arriba y atrás
    glRotatef(-195, 1, 0, 0)  # Inclinación hacia atrás
    glScalef(1.1, 1.5, 1.1)  # Tamaño de la punta
    cl.colorGrisOscuro()  # La punta puede ser más oscura
    obj.cono(1, 2.0, 20)  # Cono más pequeño
    glPopMatrix()

    # 🔹 Cejas derecha
    glPushMatrix()
    glTranslatef(posx + 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo derecho
    glRotatef(90, 1, 0, 0)  # Para que la ceja quede recta horizontalmente
    glRotatef(0, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea más delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Cejas izquierda
    glPushMatrix()
    glTranslatef(posx - 0.6, posy + 5.3, posz + 1.2)  # Ajusta la posición sobre el ojo izquierdo
    glRotatef(90, 1, 0, 0)  # Igual que la ceja derecha
    glRotatef(0, 0, 1, 0)  # Para que la ceja quede recta horizontalmente
    glScalef(1.2, 0.2, 0.2)  # Escala para que sea delgada
    cl.colorNegroPlano()  # Color negro para la ceja
    obj.cilindro(0.35, 0.7, 10)  # Radio, altura y segmentos del cilindro
    glPopMatrix()

    # 🔹 Base de la boca (Esfera achatada blanca)
    glPushMatrix()
    glTranslatef(posx, posy + 4.2, posz + 1)  # Justo debajo de los ojos
    glScalef(1.2, 0.8, 1.0)  # Aplastar la esfera en el eje Y
    cl.colorBlancoPlano()  # Color blanco para la base
    obj.esfera(0.7, 30, 30)  # Esfera base de la boca
    glPopMatrix()

    # 🔹 Parte superior de la boca (Esfera achatada negra)
    glPushMatrix()
    glTranslatef(posx, posy + 4.3, posz + 1.55)  # Un poco más arriba y adelante
    glScalef(1.0, 0.8, 0.8)  # Más achatada en Y para dar efecto de sombra
    cl.colorNegroPlano()  # Color negro para la parte superior
    obj.esfera(0.3, 30, 30)  # Esfera superior
    glPopMatrix()
        
def pintaCono():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glPushMatrix()
    # Posicionamos el cono más centrado y un poco más profundo
    glTranslatef(-3, 7, -5)  
    # Rotamos para que la base quede abajo y la punta arriba
    glRotatef(270, 1, 0, 0)
    # Configurar iluminación y color
    lc.iluminacion(0.0, 1.0, 1.0)
    cl.colorAzul()

    # Dibujar el cono (radio base=2, altura=4, resolución=40)
    obj.cono(2, 8, 40)

    glPopMatrix()

def pintaCubo():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glPushMatrix()
    glTranslatef(6,3,posz) 
    lc.iluminacion(0.0,0.0,1.0)
    cl.colorRosa()
    obj.cubo()
    glPopMatrix()