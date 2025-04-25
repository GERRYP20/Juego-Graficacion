import pygame
import os
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image

pygame.init()
pygame.mixer.init()

# Variable global para almacenar la textura y evitar recargarla en cada frame
textura_id = None  

def cargar_textura(filename):
    """Carga una imagen y la convierte en textura para OpenGL."""
    # Obtener la ruta correcta del archivo
    ruta_base = os.path.dirname(os.path.abspath(__file__))  # Directorio actual
    ruta_imagen = os.path.join(ruta_base, '..', filename)   # Subir un nivel
    if not os.path.exists(ruta_imagen):
        raise FileNotFoundError(f"⚠️ No se encontró la imagen: {ruta_imagen}")
    
    # Cargar la imagen con PIL
    img = Image.open(ruta_imagen)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Invertir verticalmente
    img = img.convert("RGBA")  # Convertir a RGBA para compatibilidad
    ix, iy = img.size
    image = img.tobytes("raw", "RGBA")

    # 🔹 Generar nueva textura en OpenGL
    textura_id = glGenTextures(1)  # SIEMPRE crear nueva textura
    glBindTexture(GL_TEXTURE_2D, textura_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

    # Configuración de la textura
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return textura_id  # 🔹 Ahora cada imagen tiene su propia textura



# Variables globales para las texturas
textura_paredes_id = None
textura_suelo_id = None
ultimo_fondo = None
ultimo_suelo = None

# Variables globales para las texturas
textura_paredes_id = None
textura_suelo_id = None
ultimo_fondo = None
ultimo_suelo = None

def pinta_escenario(filename_paredes, filename_suelo):
    """Dibuja un escenario con diferentes texturas para paredes y suelo."""
    global textura_paredes_id, textura_suelo_id, ultimo_fondo, ultimo_suelo

    # Cargar textura de paredes si ha cambiado
    if filename_paredes != ultimo_fondo:
        if textura_paredes_id is not None:
            glDeleteTextures(1, [textura_paredes_id])  # Eliminar textura anterior

        textura_paredes_id = cargar_textura(filename_paredes)  # Cargar nueva textura
        ultimo_fondo = filename_paredes

    # Cargar textura del suelo si ha cambiado
    if filename_suelo != ultimo_suelo:
        if textura_suelo_id is not None:
            glDeleteTextures(1, [textura_suelo_id])  # Eliminar textura anterior

        textura_suelo_id = cargar_textura(filename_suelo)  # Cargar nueva textura
        ultimo_suelo = filename_suelo

    glEnable(GL_TEXTURE_2D)
    
    # Aplicar textura a las paredes
    glBindTexture(GL_TEXTURE_2D, textura_paredes_id)
    glColor3f(1.0, 1.0, 1.0)

    # 🔹 Pared 1
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-50, 0, 50)
    glTexCoord2f(1, 0); glVertex3f(50, 0, 50)
    glTexCoord2f(1, 1); glVertex3f(50, 100, 50)
    glTexCoord2f(0, 1); glVertex3f(-50, 100, 50)
    glEnd()

    # 🔹 Pared 2
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(50, 0, 50)
    glTexCoord2f(1, 0); glVertex3f(50, 0, -50)
    glTexCoord2f(1, 1); glVertex3f(50, 100, -50)
    glTexCoord2f(0, 1); glVertex3f(50, 100, 50)
    glEnd()

    # 🔹 Pared 3
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(50, 0, -50)
    glTexCoord2f(1, 0); glVertex3f(-50, 0, -50)
    glTexCoord2f(1, 1); glVertex3f(-50, 100, -50)
    glTexCoord2f(0, 1); glVertex3f(50, 100, -50)
    glEnd()

    # 🔹 Pared 4
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-50, 0, -50)
    glTexCoord2f(1, 0); glVertex3f(-50, 0, 50)
    glTexCoord2f(1, 1); glVertex3f(-50, 100, 50)
    glTexCoord2f(0, 1); glVertex3f(-50, 100, -50)
    glEnd()

      # 🔹 Techo
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-50, 100, -50)
    glTexCoord2f(1, 0); glVertex3f(50, 100, -50)
    glTexCoord2f(1, 1); glVertex3f(50, 100, 50)
    glTexCoord2f(0, 1); glVertex3f(-50, 100, 50)
    glEnd()

    # 🔹 Aplicar textura diferente al suelo
    glBindTexture(GL_TEXTURE_2D, textura_suelo_id)  # Cambiar textura
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-50, 0, -50)
    glTexCoord2f(1, 0); glVertex3f(50, 0, -50)
    glTexCoord2f(1, 1); glVertex3f(50, 0, 50)
    glTexCoord2f(0, 1); glVertex3f(-50, 0, 50)
    glEnd()

    glDisable(GL_TEXTURE_2D)  # Desactivar texturas después de pintar

