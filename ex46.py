from time import sleep
import pygame
for cont in range(10, -1, -1):
  print(cont)
  sleep(0.5)
print('É ANO NOVO')
pygame.init()
pygame.mixer.music.load('C:/Users/geowa/OneDrive/Documentos/python/exercicios/ex46.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
   