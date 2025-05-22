import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import src.pinta as pt
import Acciones.escenarios as es
import Acciones.textos as txt

<<<<<<< Updated upstream


=======
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
>>>>>>> Stashed changes

def draw_base(x_offset, selected):
    base_size = 2.0
    glColor3f(1, 1, 0) if selected else glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(x_offset - base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, -base_size)
    glVertex3f(x_offset - base_size, -2, -base_size)
    glEnd()

def configurar_opengl():
    pygame.init()
    pygame.mixer.init()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClearColor(0.9, 0.9, 0.95, 1.0)

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

def mouse_sobre_volver(mouse_x, mouse_y, ancho=800, alto=600):
    # Ajusta estos valores para que coincidan con el área visual del botón
    btn_left = int(ancho * 0.75)      # 600
    btn_top = int(alto * 0.03)        # 18
    btn_width = int(ancho * 0.22)     # 176
    btn_height = int(alto * 0.10)     # 60
    return btn_left <= mouse_x <= btn_left + btn_width and btn_top <= mouse_y <= btn_top + btn_height


def seleccion_de_personaje():
    configurar_opengl()

 
    selected_character = 0
    character_changed = False
    character_angles = [0, 0, 0]
    personajes = [pt.pintaMapache, pt.pintaHuesos, pt.pintarsincambiosMike]
    nombres_personajes = ["mapache", "huesos", "mike"]

<<<<<<< Updated upstream
    while True:
        for event in pygame.event.get():    
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT and not character_changed:
                    selected_character = (selected_character - 1) % 3
                    character_changed = True
                elif event.key == K_RIGHT and not character_changed:
                    selected_character = (selected_character + 1) % 3
                    character_changed = True
                elif event.key == K_RETURN:
                    pygame.quit()
                    return nombres_personajes[selected_character]
                elif event.key == K_ESCAPE:  
                    pygame.quit()  
                    quit()    

            if event.type == KEYUP:
=======
    seleccionando_volver = False
    last_click_time = 0
    last_clicked_index = None
    DOUBLE_CLICK_TIME = 400  # milisegundos
    running = True
    volver_rect = pygame.Rect(0, 0, 0, 0)  # Inicializa para evitar error en el primer ciclo

    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if not seleccionando_volver:
                    if event.key == K_LEFT and not character_changed:
                        selected_character = (selected_character - 1) % len(personajes)
                        character_changed = True
                    elif event.key == K_RIGHT and not character_changed:
                        selected_character = (selected_character + 1) % len(personajes)
                        character_changed = True
                    elif event.key == K_UP:
                        seleccionando_volver = True
                    elif event.key == K_RETURN:
                        sonidoOff()
                        resetear_opengl()
                        return nombres_personajes[selected_character]
                else:
                    if event.key == K_DOWN:
                        seleccionando_volver = False
                    elif event.key == K_RETURN:
                        sonidoOff()
                        resetear_opengl()
                        return None  # Volver al menú principal
                if event.key == K_ESCAPE:
                    resetear_opengl()
                    running = False
            elif event.type == KEYUP:
>>>>>>> Stashed changes
                if event.key in (K_LEFT, K_RIGHT):
                    character_changed = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if mouse_sobre_volver(mouse_x, mouse_y):
                    sonidoOff()
                    resetear_opengl()
                    return None
                for idx, hitbox in enumerate(personaje_hitboxes):
                    if hitbox.collidepoint(mouse_x, mouse_y):
                        now = pygame.time.get_ticks()
                        if last_clicked_index == idx and (now - last_click_time) < DOUBLE_CLICK_TIME:
                            # Doble clic detectado: selecciona y sale
                            sonidoOff()
                            resetear_opengl()
                            return nombres_personajes[idx]
                        else:
                            # Primer clic: solo selecciona visualmente
                            selected_character = idx
                            seleccionando_volver = False
                            last_clicked_index = idx
                            last_click_time = now

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        es.pinta_escenario2("Imagenes/SoteImage.png", "Imagenes/pisoSote.png")
        txt.text("¡SELECCIONA TU PERSONAJE!", -17, 12, -18, 50, 255, 255, 255, 0, 0, 255)
        txt.text("HUESOS", -1.5, 0, 7.5, 30, 255, 255, 255, 0, 0, 255)
        txt.text("GATOPACHE KEVIN", -11, 0, 7.5, 30, 255, 255, 255, 0, 0, 255)
        txt.text("RAPERO MIKEE", 7, 0, 7.5, 30, 255, 255, 255, 0, 0, 255)
        posiciones = [-12, 0, 12]
                # ...dibuja personajes y escenario...
        personaje_hitboxes = [
            pygame.Rect(100, 400, 150, 120),   # Izquierda
            pygame.Rect(325, 400, 150, 120),   # Centro
            pygame.Rect(550, 400, 150, 120),   # Derecha
        ]

        for i, personaje in enumerate(personajes):
            draw_base(posiciones[i], selected_character == i and not seleccionando_volver)
            glPushMatrix()
            glTranslatef(posiciones[i], 0, 0)
            if selected_character == i:
                character_angles[i] += 15
            glRotatef(character_angles[i], 0, 1, 0)
            glScalef(0.5, 0.5, 0.5)
            personaje()
            glPopMatrix()

        # --- Dibuja el botón VOLVER con OpenGL ---
        draw_volver_button(seleccionando_volver)
        glClearColor(0.9, 0.9, 0.95, 1.0)


        pygame.display.flip()  # <-- SOLO AQUÍ, al final del ciclo
        pygame.time.wait(10)
<<<<<<< Updated upstream
=======

    resetear_opengl()
    return None
>>>>>>> Stashed changes
