from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# --------- FUNCIONES DE MATERIALES (ILUMINADOS) ---------
# Estas vienen del rapero Mike(segundo codigo)

def aplicarMaterial(ambiente, difuso, especular, brillo):
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambiente)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, difuso)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, especular)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, brillo)

def matNegro():  # ← Segundo código
    aplicarMaterial([0.0, 0.0, 0.0, 1.0], [0.05, 0.05, 0.05, 1.0], [0.2, 0.2, 0.2, 1.0], 30.0)

def matNaranja():  # ← Segundo código
    aplicarMaterial([1.0, 0.4, 0.0, 1.0], [1.0, 0.5, 0.0, 1.0], [0.2, 0.1, 0.0, 1.0], 25.0)

def matRojo():  # ← Segundo código
    aplicarMaterial([0.7, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 1.0], [0.3, 0.1, 0.1, 1.0], 40.0)

def matAzulMarino():  # ← Segundo código
    aplicarMaterial([0.0, 0.0, 0.4, 1.0], [0.0, 0.0, 0.7, 1.0], [0.2, 0.2, 0.4, 1.0], 35.0)

def matBlanco():  # ← Segundo código
    aplicarMaterial([0.8, 0.8, 0.8, 1.0], [1.0, 1.0, 1.0, 1.0], [0.6, 0.6, 0.6, 1.0], 60.0)

def matAmarillo():  # ← Segundo código
    aplicarMaterial([0.8, 0.8, 0.0, 1.0], [1.0, 1.0, 0.0, 1.0], [0.3, 0.3, 0.0, 1.0], 30.0)

def matDuraznoPiel():  # ← Segundo código
    aplicarMaterial([1.0, 0.7, 0.5, 1.0], [1.0, 0.6, 0.4, 1.0], [0.3, 0.2, 0.2, 1.0], 40.0)

def matVerde():  # ← Segundo código
    aplicarMaterial([0.0, 0.7, 0.0, 1.0], [0.0, 0.8, 0.0, 1.0], [0.2, 0.3, 0.2, 1.0], 35.0)

def matAzulClaro():  # ← Segundo código
    aplicarMaterial([0.5, 0.7, 1.0, 1.0], [0.4, 0.6, 1.0, 1.0], [0.2, 0.3, 0.4, 1.0], 45.0)

def matMorado():  # ← Segundo código
    aplicarMaterial([0.4, 0.0, 0.4, 1.0], [0.5, 0.2, 0.6, 1.0], [0.3, 0.2, 0.4, 1.0], 50.0)

def matBeige():  # ← Este también es del primer código, pero estaba en formato de material
    aplicarMaterial([208/255, 188/255, 189/255, 1.0],
                    [208/255, 188/255, 189/255, 1.0],
                    [0.15, 0.15, 0.15, 1.0], 18.0)

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
