from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from pygame.locals import *
import random
import time
import os

import src.pinta as pt
import Acciones.escenarios as es
import Acciones.textos as tx
from Acciones.sonidos import *
import Acciones.luces as lc
from shared import resource_path

# --- Variables globales ---
posx, posy, posz = 0, 0, 0
cartas = []
seleccionadas = []
textura_poker = 0  # textura para la parte trasera de las cartas (ID numérico)
juego_ganado = False  # NUEVO: para controlar cuando se gana

def cargar_textura(ruta):
    ruta = resource_path(ruta)  # Asegurarse de que la ruta es correcta
    if not os.path.isfile(ruta):
        print(f"[ERROR] No se encontró la imagen: {ruta}")
        return 0
    try:
        surface = pygame.image.load(ruta)
    except Exception as e:
        print(f"[ERROR] No se pudo cargar la imagen {ruta}: {e}")
        return 0

    data = pygame.image.tostring(surface, "RGBA", 1)
    width = surface.get_width()
    height = surface.get_height()
    texture_id = glGenTextures(1)
    if texture_id == 0:
        print(f"[ERROR] No se pudo generar textura OpenGL para {ruta}")
        return 0

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return texture_id

def generar_cartas():
    global cartas
    imagenes = ["cepillo.jpg", "jabon.jpg", "banio.png", "manos.jpg", "peine.jpg"] * 2
    random.shuffle(imagenes)
    cartas.clear()

    for i, img in enumerate(imagenes):
        ruta = "imagenes/" + img
        textura_id = cargar_textura(ruta)
        if textura_id == 0:
            print(f"[WARN] La carta {img} no tendrá textura válida.")
        y_pos = 0 if i < 5 else 24
        x_pos = -44 + (i % 5) * 22
        cartas.append({
            "id": i,
            "textura": img,
            "textura_id": textura_id,
            "descubierta": False,
            "pos": (x_pos, y_pos, -30)
        })

def liberar_texturas():
    global cartas, textura_poker
    for carta in cartas:
        if carta["textura_id"]:
            glDeleteTextures([carta["textura_id"]])
    if textura_poker:
        glDeleteTextures([textura_poker])
    cartas.clear()
    textura_poker = 0

def resetear_opengl():
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glDisable(GL_COLOR_MATERIAL)
    glDisable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    pygame.display.quit()
    pygame.quit()

def dibujar_carta(carta):
    if carta["textura_id"] == 0:
        return  # No se dibuja carta con textura inválida

    glPushMatrix()
    x, y, z = carta["pos"]
    glTranslatef(x, y, z)
    glEnable(GL_TEXTURE_2D)

    ancho = 9
    alto = 18

    if carta["descubierta"]:
        glBindTexture(GL_TEXTURE_2D, carta["textura_id"])
    else:
        if textura_poker != 0:
            glBindTexture(GL_TEXTURE_2D, textura_poker)
        else:
            glBindTexture(GL_TEXTURE_2D, 0)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-ancho, 0, 0)
    glTexCoord2f(1, 0); glVertex3f(ancho, 0, 0)
    glTexCoord2f(1, 1); glVertex3f(ancho, alto, 0)
    glTexCoord2f(0, 1); glVertex3f(-ancho, alto, 0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

def detectar_carta_click(mouse_x, mouse_y):
    viewport = glGetIntegerv(GL_VIEWPORT)
    modelview = glGetDoublev(GL_MODELVIEW_MATRIX)
    projection = glGetDoublev(GL_PROJECTION_MATRIX)
    real_y = viewport[3] - mouse_y
    z = glReadPixels(mouse_x, real_y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)

    if z is None or z == 1.0:
        return None

    wx, wy, wz = gluUnProject(mouse_x, real_y, z, modelview, projection, viewport)
    for carta in cartas:
        x, y, z_pos = carta["pos"]
        if (x - 9 <= wx <= x + 9) and (y <= wy <= y + 18) and (abs(wz - z_pos) < 5):
            return carta
    return None

def todas_las_cartas_descubiertas():
    return all(carta["descubierta"] for carta in cartas)

def iniciar_ruinas(personaje):
    global posx, posy, posz, textura_poker, seleccionadas, juego_ganado

    es.ultimo_fondo = None
    es.ultimo_suelo = None

    pygame.init()
    pygame.mixer.init()
    glutInit()
    sonidoOn("Sonidos/huesos_soundtrack.mp3")

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 50, -10, 1))

    gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)
    glTranslatef(0, -20, -70)

    personaje_dibujar = {
        "mapache": pt.pintaMapache,
        "huesos": pt.pintaHuesos,
        "mike": pt.pintarsincambiosMike
    }.get(personaje, pt.pintaMapache)

    textura_poker = cargar_textura("imagenes/poker.png")
    if textura_poker == 0:
        print("[ERROR] No se pudo cargar la textura trasera de las cartas.")
    generar_cartas()
    generar_cartas()
    seleccionadas.clear()

    reloj = pygame.time.Clock()
    teclas_activas = set()
    velocidad = 1.0
    inicio_tiempo = time.time()
    mostrar_instrucciones = True
    tiempo_terminado = False
    tiempo_limite = 25
    juego_ganado = False  # Reiniciamos variable al iniciar

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                liberar_texturas()
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    liberar_texturas()
                    sonidoOff()
                    resetear_opengl()
                    return
                elif event.key == K_RETURN and tiempo_terminado:
                    posx, posy, posz = 0, 0, 0
                    generar_cartas()
                    seleccionadas.clear()
                    inicio_tiempo = time.time()
                    tiempo_terminado = False
                    juego_ganado = False  # Reiniciar estado juego ganado
                else:
                    teclas_activas.add(event.key)
            elif event.type == KEYUP:
                teclas_activas.discard(event.key)
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and not tiempo_terminado and not juego_ganado:
                mx, my = pygame.mouse.get_pos()
                carta_seleccionada = detectar_carta_click(mx, my)
                if carta_seleccionada and not carta_seleccionada["descubierta"]:
                    carta_seleccionada["descubierta"] = True
                    seleccionadas.append(carta_seleccionada)
                    if len(seleccionadas) == 2:
                        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                        glDisable(GL_LIGHTING)
                        es.pinta_escenario("Imagenes/hueso type.png", "Imagenes/suelo3.jpg")
                        for carta in cartas:
                            dibujar_carta(carta)
                        glEnable(GL_LIGHTING)
                        glPushMatrix()
                        glTranslatef(posx, posy, posz)
                        personaje_dibujar()
                        glPopMatrix()
                        tx.text("¡Bienvenido al Memorama!", -12, 46, 0, 30, 255, 255, 255, 0, 0, 0)
                        tx.text("Presiona ESC para regresar", -8, 44, 0, 20, 255, 255, 255, 0, 0, 0)
                        tiempo_restante = max(0, int(tiempo_limite - (time.time() - inicio_tiempo)))
                        tx.text(f"Tiempo restante: {tiempo_restante} s", -26, 0, 15, 26, 255, 255, 0, 0, 0, 0)
                        pygame.display.flip()
                        pygame.time.wait(800)
                        if seleccionadas[0]["textura"] != seleccionadas[1]["textura"]:
                            for c in seleccionadas:
                                c["descubierta"] = False
                        seleccionadas.clear()

        if not tiempo_terminado and not juego_ganado:
            if K_w in teclas_activas: posz -= velocidad
            if K_s in teclas_activas: posz += velocidad
            if K_a in teclas_activas: posx -= velocidad
            if K_d in teclas_activas: posx += velocidad
        posx = max(-36, min(36, posx))

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glDisable(GL_LIGHTING)
        es.pinta_escenario("Imagenes/hueso type.png", "Imagenes/suelo3.jpg")

        for carta in cartas:
            dibujar_carta(carta)

        glEnable(GL_LIGHTING)
        glPushMatrix()
        glTranslatef(posx, posy, posz)
        personaje_dibujar()
        glPopMatrix()

        tx.text("¡Bienvenido al Memorama!", -12, 46, 0, 32, 255, 255, 255, 0, 0, 0)
        tx.text("Presiona ESC para regresar", -8, 44, 0, 20, 255, 255, 255, 0, 0, 0)

        tiempo_transcurrido = time.time() - inicio_tiempo
        tiempo_restante = max(0, int(tiempo_limite - tiempo_transcurrido))
        if tiempo_restante == 0:
            tiempo_terminado = True


        if not juego_ganado:
            tx.text(f"Tiempo restante: {tiempo_restante} s", -26, 0, 15, 26, 255, 255, 0, 0, 0, 0)
            
        if mostrar_instrucciones:
            if tiempo_transcurrido < 5:
                tx.text("Empareja las cartas iguales haciendo clic sobre ellas", -18, 42, 0, 22, 255, 255, 0, 0, 0, 0)
                tx.text("Completa el juego antes de que se acabe el tiempo", -16, 40, 0, 22, 255, 100, 100, 0, 0, 0)
            else:
                mostrar_instrucciones = False

        # Verificar si ganó
        if not juego_ganado and todas_las_cartas_descubiertas():
            juego_ganado = True
            tiempo_terminado = True

        if juego_ganado:
            tx.text("¡Has ganado!", -10, 37, 0, 35, 0, 255, 0, 0, 0, 0)
            tx.text("Presiona ENTER para volver a jugar", 15, 0, 0, 20, 255, 255, 255, 0, 0, 0)
        elif tiempo_terminado:
            tx.text("¡Se te acabó el tiempo!", -16, 10, 0, 40, 255, 0, 0, 0, 0, 0)
            tx.text("Presiona ENTER para reiniciar", 15, 0, 0, 20, 255, 255, 255, 0, 0, 0)

        pygame.display.flip()
        reloj.tick(30)
