import pygame
import sys
import os

def mostrar_nombres(fondo_path="Menu.jpg"):
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Nombres en pantalla")

    try:
        fuente = pygame.font.Font("PressStart2P.ttf", 35)
    except:
        fuente = pygame.font.SysFont("Courier New", 35, bold=True)

    clock = pygame.time.Clock()
    nombres = ["Ana Barbara Rivera Guia", "Gerardo Perez Sanchez", "Gustavo Antonio Campa"]

    if os.path.exists(fondo_path):
        fondo = pygame.image.load(fondo_path).convert()
        fondo = pygame.transform.scale(fondo, (800, 600))
    else:
        print(f"⚠️ No se encontró el archivo '{fondo_path}', usando gris.")
        fondo = None

    mostrando = True
    seleccionando_volver = False

    # Botón "VOLVER" (posición y tamaño)
    btn_width, btn_height = 220, 60
    btn_left = 800 - btn_width - 30
    btn_top = 30
    boton_rect = pygame.Rect(btn_left, btn_top, btn_width, btn_height)

    while mostrando:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if not seleccionando_volver:
                    if evento.key == pygame.K_DOWN or evento.key == pygame.K_UP:
                        seleccionando_volver = True
                else:
                    if evento.key == pygame.K_DOWN or evento.key == pygame.K_UP:
                        seleccionando_volver = False
                    elif evento.key == pygame.K_RETURN:
                        mostrando = False  # Volver al menú
                if evento.key == pygame.K_m or evento.key == pygame.K_ESCAPE:
                    mostrando = False  # Volver al menú
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_rect.collidepoint(mouse_x, mouse_y):
                    mostrando = False  # Volver al menú

        if fondo:
            pantalla.blit(fondo, (0, 0))
        else:
            pantalla.fill((30, 30, 30))

        # Nombres
        for i, nombre in enumerate(nombres):
            texto = fuente.render(nombre, True, (255, 255, 255))
            texto_rect = texto.get_rect(center=(400, 220 + i * 60))
            pantalla.blit(texto, texto_rect)

        # --- Dibuja el botón VOLVER ---
        color_fondo = (0, 30, 60) if seleccionando_volver or boton_rect.collidepoint(mouse_x, mouse_y) else (0, 0, 0)
        borde_color = (0, 255, 255) if seleccionando_volver or boton_rect.collidepoint(mouse_x, mouse_y) else (255, 0, 255)
        pygame.draw.rect(pantalla, color_fondo, boton_rect)
        pygame.draw.rect(pantalla, borde_color, boton_rect, 5)
        texto_volver = fuente.render("VOLVER", True, (0, 255, 255) if (seleccionando_volver or boton_rect.collidepoint(mouse_x, mouse_y)) else (255, 255, 255))
        texto_volver_rect = texto_volver.get_rect(center=boton_rect.center)
        pantalla.blit(texto_volver, texto_volver_rect)

        pygame.display.flip()
        clock.tick(60)

# Ejecutar si se llama directamente
if __name__ == "__main__":
    mostrar_nombres()
