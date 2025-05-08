import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from seleccion_personaje import seleccion_de_personaje
import Acciones.escenarios as es
import Acciones.textos as txt
from Acciones.sonidos import *

# Función para dibujar el botón en la parte superior derecha
def draw_back_button():
    button_width = 150
    button_height = 40
    x = 800 - button_width - 10  # Posición X en la parte derecha
    y = 10  # Posición Y en la parte superior

    # Cambiar a proyección ortográfica con (0,0) en la esquina superior izquierda
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 800, 600, 0)  # Invertimos eje Y
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Dibujar rectángulo del botón
    glColor3f(0.2, 0.2, 0.8)  # Azul
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + button_width, y)
    glVertex2f(x + button_width, y + button_height)
    glVertex2f(x, y + button_height)
    glEnd()

    # Desactivar el búfer de profundidad para dibujar el texto sobre el botón
    glDisable(GL_DEPTH_TEST)
    txt.text("Volver", x + 25, y + 10, 0, 20, 255, 255, 255, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)  # Reactivar el búfer de profundidad

    # Restaurar proyección
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

# Función para verificar si se ha hecho clic en el botón
def is_back_button_clicked(mx, my):
    button_width = 150
    button_height = 40
    x = 800 - button_width - 10  # Posición X en la parte derecha
    y = 10  # Posición Y en la parte superior

    # Verificar si el clic está dentro del área del botón
    if x <= mx <= x + button_width and y <= my <= y + button_height:
        return True
    return False

def draw_base(x_offset, selected):
    base_size = 2.0
    glColor3f(1, 1, 0) if selected else glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(x_offset - base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, -base_size)
    glVertex3f(x_offset - base_size, -2, -base_size)
    glEnd()

def draw_puerta():
    glColor3f(0.6, 0.3, 0.0)  # Color madera
    glBegin(GL_QUADS)
    # Frente de la puerta
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 4, 1)
    glVertex3f(-1, 4, 1)
    glEnd()

    # Borde superior
    glColor3f(0.3, 0.15, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-1, 4, 1)
    glVertex3f(1, 4, 1)
    glVertex3f(1, 4, 0.8)
    glVertex3f(-1, 4, 0.8)
    glEnd()

def configurar_opengl():
    pygame.init()
    pygame.mixer.init()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClearColor(0.9, 0.9, 0.95, 1.0)
    sonidoOn("sonidos/SoteMenu.mp3")

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 50, -10, 1))

    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)

    glTranslatef(0, -7, -30)
    glRotatef(15, 1, 0, 0)

    pygame.event.set_grab(True)
    pygame.mouse.set_visible(True)

def seleccion_de_nivel():
    configurar_opengl()

    selected_level = 0
    level_changed = False
    level_angles = [0, 0, 0]

    nombres_niveles = ["memorama", "tormenta", "laberinto"]
    textos_niveles = ["NIVEL 1: TORMENTA", "NIVEL 2: MEMORAMA", "NIVEL 3: LABERINTO"]
    posiciones = [-12, 0, 12]
    hitboxes = [(pos - 2, pos + 2) for pos in posiciones]

    while True:
        mouse_clicked = False
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT and not level_changed:
                    selected_level = (selected_level - 1) % 3
                    level_changed = True
                elif event.key == K_RIGHT and not level_changed:
                    selected_level = (selected_level + 1) % 3
                    level_changed = True
                elif event.key == K_RETURN:
                    pygame.quit()
                    return nombres_niveles[selected_level]
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == KEYUP:
                if event.key in (K_LEFT, K_RIGHT):
                    level_changed = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        # Verificar si se hizo clic en el botón "Volver"
        if is_back_button_clicked(mx, my) and mouse_clicked:
            pygame.quit()
            seleccion_de_personaje()  # Llama a la pantalla de selección de personaje
            return  # Salir de la función actual  # Regresar a la selección de personaje

        # Convertir coordenadas de pantalla a coordenadas de selección
        norm_x = (mx / 800.0) * 2 - 1
        world_x = norm_x * (30 / 0.75)  # aproximación rápida

        # Detectar clic solo si está dentro del área de la puerta
        for i, (x_min, x_max) in enumerate(hitboxes):
            if x_min <= world_x <= x_max:
                if mouse_clicked:
                    pygame.quit()
                    return nombres_niveles[i]
                selected_level = i

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        es.pinta_escenario2("Imagenes/SoteImage.png", "Imagenes/pisoSote.png")
        txt.text("¡SELECCIONA UN NIVEL!", -17, 12, -18, 50, 255, 255, 255, 0, 0, 255)

        for i in range(3):
            draw_base(posiciones[i], selected_level == i)
            if selected_level == i:
                level_angles[i] += 10

            glPushMatrix()
            glTranslatef(posiciones[i], 0, 0)
            glRotatef(level_angles[i], 0, 1, 0)
            glScalef(1.5, 1.5, 1.5)
            draw_puerta()
            glPopMatrix()

            # Mostrar texto del nivel frente a la puerta
            txt.text(textos_niveles[i], posiciones[i] - 3, -3, 2, 25, 255, 255, 0, 0, 0, 0)

        # Dibujar el botón "Volver"
        draw_back_button()

        pygame.display.flip()
        pygame.time.wait(10)
