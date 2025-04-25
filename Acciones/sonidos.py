import pygame

pygame.init()
pygame.mixer.init()

def sonidoOn(archivo):
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()

def sonidoOff():
    pygame.mixer.music.stop()
