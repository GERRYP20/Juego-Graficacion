import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import src.pinta as pt
import Acciones.escenarios as es

def pintarsincambiosMike():
        glRotatef(-90, 1, 0, 0) 
        pt.pintaCejasMike(0.5, 1.9, 11.9, 0.1, 1)
        pt.pintaCejasMike(-1.5, 1.9, 11.9, 0.1, 1)
        pt.pintaCejasMike(-.5, 2, 10.7, 0.1, 1)
        pt.pintaCilindroMike(0, 0, 3, 2, 7)
        pt.pintaCilindroMike(1, 0, 0.5, 0.3, 2.5)
        pt.pintaCilindroMike(-1, 0, 0.5, 0.3, 2.5)
        pt.pintaCaraMike(0, 0, 10, 2, 3.2)
        pt.pintaZapatosMike(1, 0, 0, 0.6, 1)
        pt.pintaZapatosMike(-1, 0, 0, 0.6, 1)
        pt.pintaEsferaMike(0, 0, 12.8, 2.2, 16, 30)
        pt.pintaOjosMike(1, 1.6, 11.5, 0.3, 15, 50)
        pt.pintaOjosMike(-1, 1.6, 11.5, 0.3, 15, 50)
        pt.pintaBrazoMike(-5.5, 0, 8.3, 0.6, 3.5)
        pt.pintaBrazoMike(2, 0, 8.3, 0.6, 3.5)
        pt.pintaCilindro2Mike(0, 2, 8, 0.2, 2)
        pt.pintaEsfera2Mike(0, 2, 8, 0.5, 15, 50)
        pt.pintaManosMike(-5.5, 0, 8.3, 0.5, 15, 50)
        pt.pintaManosMike(5.5, 0, 8.3, 0.5, 15, 50)
        pt.pintaCintasMike(-1, 1.8, 6, 0.1, 4)
        pt.pintaCintasMike(1, 1.8, 6, 0.1, 4)

# Función para dibujar las bases más pequeñas
def draw_base(x_offset, selected):
    base_size = 2.0  # Mitad del tamaño original (anteriormente 4.0)
    if selected:
        glColor3f(1, 1, 0)  # Amarillo
    else:
        glColor3f(0.5, 0.5, 0.5)  # Gris
    glBegin(GL_QUADS)
    glVertex3f(x_offset - base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, base_size)
    glVertex3f(x_offset + base_size, -2, -base_size)
    glVertex3f(x_offset - base_size, -2, -base_size)
    glEnd()

# Configura la cámara e iluminación
def configurar_opengl():
    pygame.init()
    pygame.mixer.init()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)

    # Luz ambiental y direccional
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 50, -10, 1))

    # Perspectiva y posición de cámara
    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)

    # Baja la cámara y acércala un poquito más
    glTranslatef(0, -7, -40)  # Baja la cámara a -7 en el eje Y y la aleja a -40 en el eje Z
    glRotatef(15, 1, 0, 0)

    pygame.event.set_grab(True)
    pygame.mouse.set_visible(True)

def main():
    configurar_opengl()

    selected_character = 0
    character_changed = False
    character_angles = [0, 0, 0]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT and not character_changed:
                    selected_character = (selected_character - 1) % 3
                    character_changed = True
                if event.key == K_RIGHT and not character_changed:
                    selected_character = (selected_character + 1) % 3
                    character_changed = True

            if event.type == KEYUP:
                if event.key in (K_LEFT, K_RIGHT):
                    character_changed = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Posiciones más separadas
        posiciones = [-12, 0, 12]
        personajes = [pt.pintaHuesos, pt.pintaMapache, pintarsincambiosMike]

        for i, (pos_x, personaje) in enumerate(zip(posiciones, personajes)):
            draw_base(pos_x, selected_character == i)
            glPushMatrix()
            glTranslatef(pos_x, 0, 0)
            if selected_character == i:
                character_angles[i] += 1
            glRotatef(character_angles[i], 0, 1, 0)
            
            # Reducir el tamaño de los personajes aplicando escala (0.5 en cada eje)
            glScalef(0.5, 0.5, 0.5)  # Reducción a la mitad

            personaje()
            glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
