import pygame
import sys
import os
import datos as dat
def mostrar_menu(fondo_path="Menu.jpg"):
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menú Arcade")
    
    # Fuente arcade (puedes cambiarla por una .ttf si tienes una)
    try:
        fuente = pygame.font.Font("PressStart2P.ttf", 20)  # fuente arcade personalizada
    except:
        fuente = pygame.font.SysFont("Courier New", 25, bold=True)  # alternativa tipo arcade

    clock = pygame.time.Clock()

    seleccion = 0
    opciones = ["INICIAR", "CREDITOS", "SALIR"]

    # Fondo
    if os.path.exists(fondo_path):
        fondo = pygame.image.load(fondo_path).convert()
        fondo = pygame.transform.scale(fondo, (800, 600))
    else:
        print(f"⚠️ No se encontró el archivo '{fondo_path}', usando gris.")
        fondo = None

    while True:
        if fondo:
            pantalla.blit(fondo, (0, 0))
        else:
            pantalla.fill((10, 10, 10))

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
                        dat.mostrar_nombres(fondo_path)
                    elif seleccion == 2:
                        pygame.quit()
                        sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, opcion in enumerate(opciones):
                    texto = fuente.render(opcion, True, (0, 255, 255) if i == seleccion else (255, 255, 255))
                    texto_rect = texto.get_rect(center=(650, 150 + i * 80))
                    boton_rect = texto_rect.inflate(60, 30)

                    # Comprobar si el clic está dentro del rectángulo del botón
                    if boton_rect.collidepoint(mouse_x, mouse_y):
                        if i == 0:
                            return "jugar"
                        elif i == 1:
                            print("Opciones aún no implementadas.")
                        elif i == 2:
                            pygame.quit()
                            sys.exit()

        for i, opcion in enumerate(opciones):
            texto = fuente.render(opcion, True, (0, 255, 255) if i == seleccion else (255, 255, 255))
            texto_rect = texto.get_rect(center=(650, 150 + i * 80))

            
            boton_rect = texto_rect.inflate(60, 30)
            color_fondo = (0, 30, 60) if i == seleccion else (0, 0, 0)
            borde_color = (0, 255, 255) if i == seleccion else (255, 0, 255)

            pygame.draw.rect(pantalla, color_fondo, boton_rect)
            pygame.draw.rect(pantalla, borde_color, boton_rect, 5)

            pantalla.blit(texto, texto_rect)

        pygame.display.flip()
        clock.tick(60)
