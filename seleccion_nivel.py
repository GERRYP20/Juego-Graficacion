import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from seleccion_personaje import seleccion_de_personaje
import Acciones.escenarios as es
import Acciones.textos as txt
import src.pinta as pt
from Acciones.sonidos import *
import pygame.time


def resetear_opengl():
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glDisable(GL_COLOR_MATERIAL)
    glDisable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    pygame.display.quit()
    pygame.quit()

def draw_pintamicrofono():
    glRotatef(-45, 1, 0, 0)
    pt.pinta_figuras_micro(
        x_cil=0, y_cil=0, z_cil=-1,
        r_cilindro=0.6, altura_cilindro=4, lados_cilindro=40,
        x_esp=0, y_esp=0, z_esp=3.5,
        r_esfera=1.0, slices_esfera=20, segmentos_esfera=30
    )

def draw_pino():
    glRotatef(-80, 1, 0, 0)
    pt.pinta_pino(
        x=0, y=0, z=0,
        radio_tronco=0.3, altura_tronco=2,
        radio_rama=1, altura_rama=1.5, segmentos=30
    )

def draw_puerta():
    glColor3f(0.6, 0.3, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 4, 1)
    glVertex3f(-1, 4, 1)
    glEnd()

    glColor3f(0.3, 0.15, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-1, 4, 1)
    glVertex3f(1, 4, 1)
    glVertex3f(1, 4, 0.8)
    glVertex3f(-1, 4, 0.8)
    glEnd()

def draw_base(x_offset, selected):
    base_size = 2.0
    glColor3f(1, 1, 0) if selected else glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(x_offset - base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, -base_size)
    glVertex3f(x_offset - base_size, -2, -base_size)
    glEnd()

# def draw_back_button():
#     button_width = 150
#     button_height = 40
#     x = 800 - button_width - 10
#     y = 10

#     glMatrixMode(GL_PROJECTION)
#     glPushMatrix()
#     glLoadIdentity()
#     gluOrtho2D(0, 800, 600, 0)
#     glMatrixMode(GL_MODELVIEW)
#     glPushMatrix()
#     glLoadIdentity()

#     glColor3f(0.2, 0.2, 0.8)
#     glBegin(GL_QUADS)
#     glVertex2f(x, y)
#     glVertex2f(x + button_width, y)
#     glVertex2f(x + button_width, y + button_height)
#     glVertex2f(x, y + button_height)
#     glEnd()

#     glDisable(GL_DEPTH_TEST)
#     txt.text("Volver", x + 25, y + 30, 0, 40, 255, 255, 255, 0, 0, 0)
#     glEnable(GL_DEPTH_TEST)

#     glMatrixMode(GL_PROJECTION)
#     glPopMatrix()
#     glMatrixMode(GL_MODELVIEW)
#     glPopMatrix()

def is_back_button_clicked(mx, my):
    button_width = 150
    button_height = 40
    x = 800 - button_width - 10  # Posición X en la parte derecha
    y = 10  # Posición Y en la parte superior

    # Verificar si el clic está dentro del área del botón
    if x <= mx <= x + button_width and y <= my <= y + button_height:
        return True
    return False

# def draw_base(x_offset, selected):
#     base_size = 2.0
#     glColor3f(1, 1, 0) if selected else glColor3f(0.5, 0.5, 0.5)
#     glBegin(GL_QUADS)
#     glVertex3f(x_offset - base_size, -2, base_size)
#     glVertex3f(x_offset + base_size, -2, base_size)
#     glVertex3f(x_offset + base_size, -2, -base_size)
#     glVertex3f(x_offset - base_size, -2, -base_size)
#     glEnd()

# def draw_puerta():
#     glColor3f(0.6, 0.3, 0.0)  # Color madera
#     glBegin(GL_QUADS)
#     # Frente de la puerta
#     glVertex3f(-1, 0, 1)
#     glVertex3f(1, 0, 1)
#     glVertex3f(1, 4, 1)
#     glVertex3f(-1, 4, 1)
def draw_volver_button(selected=False):
    # Guarda el estado actual de color
    glPushAttrib(GL_CURRENT_BIT)
     # Coordenadas para la esquina superior derecha (ajusta según tu cámara)
    x1, y1 = 12, 16   # esquina inferior izquierda del botón
    x2, y2 = 17, 17.2  # esquina superior derecha del botón
    z = -10  # Profundidad del botón
    # Fondo
    if selected:
        glColor3f(0, 1, 1)
    else:
        glColor3f(0, 0.12, 0.24)
    glBegin(GL_QUADS)
    glVertex3f(x1, y1, z)
    glVertex3f(x2, y1, z)
    glVertex3f(x2, y2, z)
    glVertex3f(x1, y2, z)
    glEnd()
    # Borde
    if selected:
        glColor3f(0, 1, 1)
    else:
        glColor3f(1, 0, 1)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex3f(x1, y1, z)
    glVertex3f(x2, y1, z)
    glVertex3f(x2, y2, z)
    glVertex3f(x1, y2, z)
    glEnd()
    # Texto
    txt.text("VOLVER", x1+.1, y1+0.1, z+0.5, 34, 255,255,255,0,0,0)
    # Restaura el color anterior
    glPopAttrib()

    # Borde superior
    glColor3f(0.3, 0.15, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-1, 4, 1)
    glVertex3f(1, 4, 1)
    glVertex3f(1, 4, 0.8)
    glVertex3f(-1, 4, 0.8)
    glEnd()
def mouse_sobre_volver(mouse_x, mouse_y, ancho=800, alto=600):
    # Ajusta estos valores para que coincidan con el área visual del botón
    btn_left = int(ancho * 0.75)      # 600
    btn_top = int(alto * 0.03)        # 18
    btn_width = int(ancho * 0.22)     # 176
    btn_height = int(alto * 0.10)     # 60
    return btn_left <= mouse_x <= btn_left + btn_width and btn_top <= mouse_y <= btn_top + btn_height

def configurar_opengl():
    pygame.init()
    pygame.mixer.init()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)

    glClearColor(0.9, 0.9, 0.95, 1.0)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 50, -10, 1))

    gluPerspective(45, (800 / 600), 0.1, 500.0)
    glTranslatef(0, -7, -30)
    glRotatef(15, 1, 0, 0)

figuras_nivel = [draw_pino, draw_puerta, draw_pintamicrofono]

def seleccion_de_nivel():
    configurar_opengl()
    sonidoOn("sonidos/Nivel.mp3")
    clock = pygame.time.Clock()
    selected_level = 0
    seleccionando_volver = False
    level_angles = [0, 0, 0]
    nombres_niveles = ["memorama", "tormenta", "laberinto"]
    textos_niveles = ["NIVEL 1: TORMENTA", "NIVEL 2: MEMORAMA", "NIVEL 3: LABERINTO"]
    textos_lugares = ["EL BOSQUE DE KEVIN", "RUINAS DE HUESOS", "CIUDAD MIKE"]
    posiciones = [-12, 0, 12]
    base_hitboxes = [
        pygame.Rect(100, 400, 180, 120),
        pygame.Rect(310, 400, 180, 120),
        pygame.Rect(520, 400, 180, 120),
    ]
    last_click_time = 0
    last_clicked_index = None
    DOUBLE_CLICK_TIME = 400


    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if not seleccionando_volver:
                    if event.key == K_LEFT:
                        selected_level = (selected_level - 1) % 3
                    elif event.key == K_RIGHT:
                        selected_level = (selected_level + 1) % 3
                    elif event.key == K_UP:
                        seleccionando_volver = True
                    elif event.key == K_RETURN:
                        sonidoOff()
                        resetear_opengl()
                        return nombres_niveles[selected_level]
                else:
                    if event.key == K_DOWN:
                        seleccionando_volver = False
                    elif event.key == K_RETURN:
                        sonidoOff()
                        resetear_opengl()
                        return None  # Volver al menú principal
                if event.key == K_ESCAPE:
                    sonidoOff()
                    resetear_opengl()
                    return None
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if mouse_sobre_volver(mx, my):
                    sonidoOff()
                    resetear_opengl()
                    return None
                for i, rect in enumerate(base_hitboxes):
                    if rect.collidepoint(mx, my):
                        now = pygame.time.get_ticks()
                        if last_clicked_index == i and (now - last_click_time) < DOUBLE_CLICK_TIME:
                            selected_level = i
                            sonidoOff()
                            return nombres_niveles[selected_level]
                        else:
                            selected_level = i
                            seleccionando_volver = False
                            last_clicked_index = i
                            last_click_time = now

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        es.pinta_escenario2("Imagenes/SoteImage.png", "Imagenes/pisoSote.png")
        txt.text("¡SELECCIONA UN NIVEL!", -12, 12, -18, 50, 255, 255, 0, 0, 0, 0)

        for i in range(3):
            draw_base(posiciones[i], selected_level == i and not seleccionando_volver)
            level_angles[i] = (level_angles[i] + 2) % 360 if selected_level == i and not seleccionando_volver else level_angles[i]
            glPushMatrix()
            glTranslatef(posiciones[i], 0, 0)
            glRotatef(level_angles[i], 0, 1, 0)
            glScalef(1.5, 1.5, 1.5)
            figuras_nivel[i]()
            glPopMatrix()
            txt.text(textos_niveles[i], posiciones[i] - 3, -3, 2, 25, 255, 255, 0, 0, 0, 0)
            txt.text(textos_lugares[i], posiciones[i] - 3, 7, 0, 25, 255, 255, 0, 0, 0, 0)

        # Dibuja el botón "Volver", resaltado si está seleccionado
        draw_volver_button(seleccionando_volver)
        glClearColor(0.9, 0.9, 0.95, 1.0)
        pygame.display.flip()
        clock.tick(60)