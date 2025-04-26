import pygame

pygame.init()
pygame.mixer.init()

def sonidoOn(archivo):
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()
    pygame.mixer.music.play(-1) 

def sonidoOff():
    pygame.mixer.music.stop()
