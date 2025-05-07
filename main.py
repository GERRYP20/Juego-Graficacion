import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
import math
import tkinter.messagebox as messagebox
import Acciones.sonidos as sd
import Acciones.escenarios as es
import Acciones.luces as lc
import src.pinta as pt
import Acciones.textos as tx

 # Variables para la pelota
pelota_pos = [-50, 5, -10]  # Posición inicial al lado izquierdo del personaje
pelota_direccion = [1, 0, 0]  # Dirección hacia el personaje
pelota_velocidad = 2 # Aumenté la velocidad
pelota_activa = False  # Solo activa cuando presiones 'i'
radio_pelota = 1.5


# Variables para la segunda pelota
pelota2_pos = [0, 50, 0]  # Empieza arriba
pelota2_direccion = [0, -1, 0]  # Baja hacia el personaje
pelota2_velocidad = 1.5
pelota2_activa = False
radio_pelota2 = 1.5


def iniciar_juego(personaje):
    
    es.ultimo_fondo = None
    es.ultimo_suelo = None
    mostrar_mike = False
    mostrar_huesos = False
    global pelota_activa
    global pelota2_pos, pelota2_direccion, pelota2_activa
    
    velocidad_camara = 0.1
    velocidad_rotacion = 0.2
    raton = 0.1

    # Lista de imágenes de escenario
    escenarios = [
        'Imagenes/fondo.jpg',  # Escenario 1
        'Imagenes/fondo2.jpg',  # Escenario 2
        'Imagenes/fondo3.jpg',  # Escenario 3
        'Imagenes/fondo4.jpg',  # Escenario 4
        'Imagenes/fondo5.jpg',  # Escenario 5
        'Imagenes/fondo6.jpg',  # Escenario 6
        'Imagenes/fondo7.jpg',  # Escenario 7
    ]

    suelos = [
        'Imagenes/suelo1.jpg',  # Escenario 1
        'Imagenes/suelo7.jpg'  # Escenario 2  
    ]

    angulo_brazo_derecho = 0  # Inicializar el ángulo del brazo derecho
    direccion_brazo = 1  # 1 para subir, -1 para bajar
    saludando = False  # Estado inicial del saludo

    # Índice del escenario actual
    escenario_actual = 0
    #indice del suelo actual
    suelo_actual = 0
    # Variable para controlar el tipo de mapache

    pygame.quit()
    pygame.init()
    pygame.mixer.init()
    pygame.init()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)  # Usa los colores definidos con glColor3f
    glEnable(GL_DEPTH_TEST)
    # Luz ambiental (ilumina todo)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))

    # Luz direccional desde arriba
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 50, -10, 1))

    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)  # Se amplía la perspectiva
    # Posición inicial de la cámara
    pos_inicial = [0, -20, -50]
    glTranslatef(*pos_inicial)

    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)

    def reset_camera():
        glLoadIdentity()  # Restablece la transformación
        gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)  # Configura la perspectiva
        glTranslatef(*pos_inicial)  # Restablece la posición inicial

    def mover_pelota():
        global pelota_pos, pelota_direccion, pelota_activa
        if pelota_activa:
            pelota_pos[0] += pelota_direccion[0] * pelota_velocidad
            pelota_pos[1] += pelota_direccion[1] * pelota_velocidad
            pelota_pos[2] += pelota_direccion[2] * pelota_velocidad

            # Si colisiona, cambia la dirección
            if detectar_colision():
                print("¡Colisión detectada!")  # Para que confirmes que sí detecta
                pelota_direccion[0] *= -1  # Rebote en X
                pelota_direccion[2] *= -1  # Rebote en Z (opcional)

            # Si la pelota se aleja mucho, desactívala
            if abs(pelota_pos[0]) > 100 or abs(pelota_pos[2]) > 100:
                pelota_activa = False
                print("Pelota desactivada")

    def mover_pelota2():
        global pelota2_pos, pelota2_direccion, pelota2_activa
        if pelota2_activa:
            pelota2_pos[0] += pelota2_direccion[0] * pelota2_velocidad
            pelota2_pos[1] += pelota2_direccion[1] * pelota2_velocidad
            pelota2_pos[2] += pelota2_direccion[2] * pelota2_velocidad

            if detectar_colision2():
                print("¡Colisión con pelota 2!")
                pelota2_direccion[1] *= -1  # Rebote hacia arriba

            # Si cae muy abajo, se desactiva
            if pelota2_pos[1] > 80:
                pelota2_activa = False
                print("Pelota 2 desactivada")

    def dibujar_pelota2():
        glPushMatrix()
        glTranslatef(*pelota2_pos)
        glColor3f(0, 0, 1)  # Azul
        quadric = gluNewQuadric()
        gluSphere(quadric, radio_pelota2, 20, 20)
        gluDeleteQuadric(quadric)
        glPopMatrix()

    def detectar_colision2():
        distancia = math.sqrt(
            (pelota2_pos[0] - 0)**2 +
            (pelota2_pos[1] - 0)**2 +
            (pelota2_pos[2] - 0)**2
        )
        return distancia < (radio_pelota2 + 10)


    def dibujar_pelota():
        glPushMatrix()
        glTranslatef(*pelota_pos)
        glColor3f(1, 0, 0)  # Color rojo
        quadric = gluNewQuadric()
        gluSphere(quadric, radio_pelota, 20, 20)
        gluDeleteQuadric(quadric)
        glPopMatrix()



    radio_personaje = 1

    def detectar_colision():
        distancia = math.sqrt(
            (pelota_pos[0] - 0)**2 +
            (pelota_pos[1] - 0)**2 +
            (pelota_pos[2] - 0)**2
        )
        return distancia < (radio_pelota + radio_personaje)

    # Funciones para pintar
   
    def pintarsincambiosMike():
        glPushMatrix()
        glRotatef(-90, 1, 0, 0)
        glRotatef(180, 0, 0, 1)
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

        glPopMatrix()


    # Elegir personaje según lo seleccionado en el menú
    if personaje == "mapache":
        personaje_dibujar = pt.pintaMapache
    elif personaje == "huesos":
        personaje_dibujar = pt.pintaHuesos
    elif personaje == "mike":
        personaje_dibujar = pintarsincambiosMike
    else:
        personaje_dibujar = pt.pintaMapache


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                # Cambiar escenario con teclas 1 al 5
                if event.key == pygame.K_p:
                    sd.sonidoOn('Sonidos/start.wav')
                if event.key == pygame.K_o:
                    sd.sonidoOff()
                if event.key == pygame.K_c:
                    reset_camera()
                if event.key == pygame.K_1:
                    escenario_actual = 0
                    suelo_actual = 0
                    if personaje == "mapache":
                        personaje_dibujar = pt.pintaMapache
                    elif personaje == "mike":
                        personaje_dibujar = pintarsincambiosMike
                    elif personaje == "huesos":
                        personaje_dibujar = pt.pintaHuesos
                    sd.sonidoOn('Sonidos/campanas.wav')

                elif event.key == pygame.K_2:
                    escenario_actual = 1
                    suelo_actual = 0
                    if personaje == "mapache":
                        personaje_dibujar = pt.pintaMapacheEnojado
                    elif personaje == "mike":
                        personaje_dibujar = pt.pintaMike1
                    elif personaje == "huesos":
                        personaje_dibujar = pt.pintaHuesos2
                    sd.sonidoOn('Sonidos/rayos.wav')

                elif event.key == pygame.K_3:
                    escenario_actual = 2
                    suelo_actual = 0
                    if personaje == "mapache":
                        personaje_dibujar = pt.pintaMapacheFeliz
                    elif personaje == "mike":
                        personaje_dibujar = pt.pintaMike2
                    elif personaje == "huesos":
                        personaje_dibujar = pt.pintaHuesos
                    sd.sonidoOn('Sonidos/aves.wav')

                elif event.key == pygame.K_4:
                    escenario_actual = 3
                    suelo_actual = 0
                    if personaje == "mapache":
                        personaje_dibujar = pt.pintaMapacheTriste
                    elif personaje == "mike":
                        personaje_dibujar = pt.pintaMike3
                    elif personaje == "huesos":
                        personaje_dibujar = pt.pintaHuesos
                    sd.sonidoOn('Sonidos/estrella.wav')

                elif event.key == pygame.K_5:
                    escenario_actual = 4
                    suelo_actual = 0
                    if personaje == "mapache":
                        personaje_dibujar = pt.pintaMapacheSaltando
                    elif personaje == "mike":
                        personaje_dibujar = pt.pintaMike4
                    elif personaje == "huesos":
                        personaje_dibujar = pt.pintaHuesos
                    sd.sonidoOn('Sonidos/tada.wav')

                elif event.key == pygame.K_6:
                    escenario_actual = 5
                    suelo_actual = 0
                    if personaje == "mapache":
                        personaje_dibujar = pt.pintaMapacheDuda
                    elif personaje == "mike":
                        personaje_dibujar = pt.pintaMike5
                    elif personaje == "huesos":
                        personaje_dibujar = pt.pintaHuesos
                    sd.sonidoOn('Sonidos/insectos.wav')

                elif event.key == pygame.K_7:
                    escenario_actual = 6
                    suelo_actual = 1
                    if personaje == "mapache":
                        personaje_dibujar = pt.pintaMapacheCaminando
                    elif personaje == "mike":
                        personaje_dibujar = pintarsincambiosMike
                    elif personaje == "huesos":
                        personaje_dibujar = pt.pintaHuesos
                    sd.sonidoOn('Sonidos/mar.wav')

                if event.key == pygame.K_l and escenario_actual == 0:  # Solo en el escenario 1
                    saludando = not saludando  # Alternar el estado de saludo
                if event.key == pygame.K_i:
                    pelota_activa = True
                    pelota_pos = [-20, 2, 0]  # <-- Aquí la colocamos al nivel de la cámara
                    pelota_direccion = [1, 0, 0]  # Dirección hacia el personaje 
                if event.key == pygame.K_u:
                    pelota2_activa = True
                    pelota2_pos = [0, 50, 0]  # Reinicia posición
                    pelota2_direccion = [0, -1, 0]  # Hacia abajo
                if event.key == pygame.K_m:
                    sd.sonidoOff()
                    return  # Esto te saca del juego y vuelve al menú
   
        # Movimiento de cámara con teclado
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            glTranslatef(0, 0, 10)
        if keys[pygame.K_s]:
            glTranslatef(0, 0, -10)
        if keys[pygame.K_a]:
            glTranslatef(10, 0, 0)
        if keys[pygame.K_d]:
            glTranslatef(-10, 0, 0)
        if keys[pygame.K_x]:
            glTranslatef(0, 10, 0)
        if keys[pygame.K_z]:
            glTranslatef(0, -10, 0)

        # Movimiento de cámara con mouse
        x, y = pygame.mouse.get_rel()
        x *= raton
        y *= raton
        if x != 0:
            glRotatef(x, 0, 1, 0)
        pygame.mouse.set_pos(display[0] // 2, display[1] // 2)
  
        # Dibujar la escena
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        es.pinta_escenario(escenarios[escenario_actual],suelos[suelo_actual])  # Dibujar el escenario actual

        # Llamar a la función de dibujo del personaje
        personaje_dibujar()                        

        # Mostrar texto solo en el escenario 7
        if escenario_actual == 6:  # Escenario 7 (índice 6)
            tx.text("Figura Caminando", 20, 36, 0, 20, 0, 0, 0, 255, 255, 255)

        tx.text("Instrucciones:",-25,38,0,20,0,0,0,255,255,255)
        tx.text("Presiona de 1-7 para cambiar de escenario",-25,36,0,20,0,0,0,255,255,255)
        tx.text("Para mover la camara usar: a,s,d,w,z,x",-25,34,0,20,0,0,0,255,255,255)
        tx.text("Camara en posicion original: c",-25,32,0,20,0,0,0,255,255,255)
        tx.text("Encender sonido general: p",-25,30,0,20,0,0,0,255,255,255)
        tx.text("Colision 1: i",-25,26,0,20,0,0,0,255,255,255)
        tx.text("Colision 2: u",-25,24,0,20,0,0,0,255,255,255)
        tx.text("Salir: ESC",-25,22,0,20,0,0,0,255,255,255)
        tx.text("Graficacion",30,38,0,20,0,0,0,255,255,255)
        mover_pelota()
        if pelota_activa:
            dibujar_pelota()
        mover_pelota2()
        if pelota2_activa:
            dibujar_pelota2()
        pygame.display.flip()
        pygame.time.wait(10)
    
if __name__ == "__main__":
    iniciar_juego()
