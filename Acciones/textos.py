import pygame 
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def text(texto,posx,posy,posz,sizefont,r,g,b,rb,gb,bb):
    font = pygame.font.Font(None, sizefont)
    text_surface = font.render(texto, True, (r,g,b), (rb,gb,bb))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(posx,posy,posz)
    glDrawPixels(
                text_surface.get_width(),
                text_surface.get_height(), 
                GL_RGBA, GL_UNSIGNED_BYTE,
                text_data)

