import pygame
import sys
import os
import creditos as cred
from Acciones.sonidos import *

def mostrar_menu(fondo_path="Menu.jpg"):
    pygame.init()
    sonidoOn("sonidos/SoteMenu.mp3")
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menú Arcade")

    # Cargar fuente arcade con fallback
    try:
        fuente = pygame.font.Font("PressStart2P.ttf", 20)
    except FileNotFoundError:
        fuente = pygame.font.SysFont("Courier New", 25, bold=True)

    clock = pygame.time.Clock()
    opciones = ["INICIAR", "CREDITOS", "SALIR"]
    seleccion = 0

    # Cargar fondo
    if os.path.exists(fondo_path):
        fondo = pygame.image.load(fondo_path).convert()
        fondo = pygame.transform.scale(fondo, pantalla.get_size())
    else:
        print(f"⚠️ No se encontró el archivo '{fondo_path}', usando fondo gris.")
        fondo = None

    def dibujar_opciones():
        for i, opcion in enumerate(opciones):
            color_texto = (0, 255, 255) if i == seleccion else (255, 255, 255)
            texto = fuente.render(opcion, True, color_texto)
            texto_rect = texto.get_rect(center=(650, 150 + i * 80))
            boton_rect = texto_rect.inflate(60, 30)

            color_fondo = (0, 30, 60) if i == seleccion else (0, 0, 0)
            borde_color = (0, 255, 255) if i == seleccion else (255, 0, 255)

            pygame.draw.rect(pantalla, color_fondo, boton_rect)
            pygame.draw.rect(pantalla, borde_color, boton_rect, 5)
            pantalla.blit(texto, texto_rect)

        return [fuente.render(op, True, (0, 255, 255) if idx == seleccion else (255, 255, 255)).get_rect(center=(650, 150 + idx * 80)).inflate(60, 30) for idx, op in enumerate(opciones)]

    while True:
        if fondo:
            pantalla.blit(fondo, (0, 0))
        else:
            pantalla.fill((10, 10, 10))

        boton_rects = dibujar_opciones()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if seleccion == 0:
                        return "jugar"
                    elif seleccion == 1:
                        cred.mostrar_nombres(fondo_path)
                    elif seleccion == 2:
                        pygame.quit()
                        sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mx, my = evento.pos
                for i, rect in enumerate(boton_rects):
                    if rect.collidepoint(mx, my):
                        if i == 0:
                            return "jugar"
                        elif i == 1:
                            cred.mostrar_nombres(fondo_path)
                        elif i == 2:
                            pygame.quit()
                            sys.exit()

        pygame.display.flip()
        clock.tick(60)