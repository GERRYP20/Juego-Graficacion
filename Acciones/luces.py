import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Función para ajustar la iluminación por personaje
def iluminacion(r, g, b):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    
    # Posición de la luz
    pos_luz = (5.0, 5.0, 5.0, 1.0)  # Puedes moverla para obtener diferentes efectos
    
    # Luz ambiental más brillante (aumentada para mayor luminosidad)
    luz_ambiente = (0.6, 0.6, 0.6, 1.0)  # Luz ambiental más fuerte
    
    # Luz difusa ajustada al color del personaje
    luz_difusa = (r, g, b, 1.0)
    
    # Configurar las luces
    glLightfv(GL_LIGHT0, GL_POSITION, pos_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)  # Luz ambiental más fuerte
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)    # Mantén la luz difusa según el color


# Configura la iluminación global para toda la escena
def configurar_iluminacion():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    # Posición de la luz (más cerca de la escena)
    pos_luz = (0.0, 10.0, 0.0, 1.0)  # Más cerca de la escena
    
    # Luz ambiental más brillante (aumentada)
    luz_ambiente = (0.8, 0.8, 0.8, 1.0)  # Luz ambiental más fuerte
    
    # Luz difusa más brillante
    luz_difusa = (1.0, 1.0, 1.0, 1.0)  # Luz blanca brillante

    # Configura la luz
    glLightfv(GL_LIGHT0, GL_POSITION, pos_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)  # Luz ambiental aumentada
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)    # Luz difusa blanca más brillante

    # Añadir luz especular para crear brillos en los objetos
    luz_especular = (1.0, 1.0, 1.0, 1.0)  # Blanco puro para reflejos brillantes
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)  # Añadir componente especular