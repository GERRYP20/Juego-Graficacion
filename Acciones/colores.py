from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# --------- FUNCIONES DE COLOR PLANO (SIN ILUMINACIÓN) ---------
# Estas vienen del PRIMER CÓDIGO (usa glColor3f sin iluminación)

def matNegro():  # Color plano (negro)
    usarColorPlano(0.0, 0.0, 0.0)

def matNaranja():  # Color plano (naranja)
    usarColorPlano(1.0, 0.4, 0.0)

def matRojo():  # Color plano (rojo)
    usarColorPlano(0.7, 0.0, 0.0)

def matAzulMarino():  # Color plano (azul marino)
    usarColorPlano(0.0, 0.0, 0.4)

def matBlanco():  # Color plano (blanco)
    usarColorPlano(0.8, 0.8, 0.8)

def matAmarillo():  # Color plano (amarillo)
    usarColorPlano(0.8, 0.8, 0.0)

def matDuraznoPiel():  # Color plano (durazno piel)
    usarColorPlano(1.0, 0.7, 0.5)

def matVerde():  # Color plano (verde)
    usarColorPlano(0.0, 0.7, 0.0)

def matAzulClaro():  # Color plano (azul claro)
    usarColorPlano(0.5, 0.7, 1.0)

def matMorado():  # Color plano (morado)
    usarColorPlano(0.4, 0.0, 0.4)

def matBeige():  # Color plano (beige)
    usarColorPlano(208/255, 188/255, 189/255)

# --------- FUNCIONES DE COLOR PLANO (SIN ILUMINACIÓN) ---------
# Estas vienen del PRIMER CÓDIGO (usa glColor3f sin iluminación)

def usarColorPlano(r, g, b):
    glColor3f(r, g, b)

def colorGris():  # ← Primer código
    usarColorPlano(0.5, 0.5, 0.5)

def colorGrisOscuro():  # ← Primer código
    usarColorPlano(0.35, 0.35, 0.35)

def colorNegroPlano():  # ← Primer código
    usarColorPlano(0.0, 0.0, 0.0)

def colorBlancoPlano():  # ← Primer código
    usarColorPlano(1.0, 1.0, 1.0)

def colorRosa():  # ← Primer código
    usarColorPlano(201/255, 159/255, 160/255)
