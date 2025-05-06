import pygame
import sys
import os

def mostrar_nombres(fondo_path="Menu.jpg"):
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Nombres en pantalla")

    try:
        fuente = pygame.font.Font("PressStart2P.ttf", 25)
    except:
        fuente = pygame.font.SysFont("Courier New", 28, bold=True)

    clock = pygame.time.Clock()
    nombres = ["Ana Barbara Rivera Guia", "Gerardo Perez Sanchez", "Gustavo Antonio Campa"]

    if os.path.exists(fondo_path):
        fondo = pygame.image.load(fondo_path).convert()
        fondo = pygame.transform.scale(fondo, (800, 600))
    else:
        print(f"⚠️ No se encontró el archivo '{fondo_path}', usando gris.")
        fondo = None

    mostrando = True
    while mostrando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m:
                    mostrando = False  # Volver al menú

        if fondo:
            pantalla.blit(fondo, (0, 0))
        else:
            pantalla.fill((30, 30, 30))

        for i, nombre in enumerate(nombres):
            texto = fuente.render(nombre, True, (255, 255, 255))
            texto_rect = texto.get_rect(center=(400, 220 + i * 60))
            pantalla.blit(texto, texto_rect)

        pygame.display.flip()
        clock.tick(60)


# Ejecutar si se llama directamente
if __name__ == "__main__":
    mostrar_nombres()

