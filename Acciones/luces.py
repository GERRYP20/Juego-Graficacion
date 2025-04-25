import pygame 
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def iluminacion(r, g, b):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    
    # Posición de la luz (es posible moverla para crear sombras o efectos interesantes)
    pos_luz = (5.0, 5.0, 5.0, 1.0)
    
    # Luz ambiental más suave (menos amarilla, más neutra)
    luz_ambiente = (0.2, 0.2, 0.2, 1.0)  # Menos intensa, más gris/neutral
    
    # Luz difusa ajustada por el color del personaje
    luz_difusa = (r, g, b, 1.0)
    
    # Configurar las luces
    glLightfv(GL_LIGHT0, GL_POSITION, pos_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)  # Menos luz ambiental
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)    # Mantén la luz difusa según el color


# Configura la iluminación global una vez, fuera de pintaMapache()
def configurar_iluminacion():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    
    # Posición de la luz
    pos_luz = (0.0, 10.0, 0.0, 0.0)
    
    # Luz ambiental más suave (reduciendo la intensidad para evitar el brillo excesivo)
    luz_ambiente = (0.8, 0.8, 0.8, 1.0)  # Menos intensa, más neutral
    
    # Luz difusa ajustada a un valor de color blanco (o más suave si lo deseas)
    luz_difusa = (0.7, 0.7, 0.7, 0.7)  # Color blanco puro

    # Configura la luz
    glLightfv(GL_LIGHT0, GL_POSITION, pos_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
