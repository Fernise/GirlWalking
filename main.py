import pygame
import Actividad1

pygame.init()

# Se define el tamaño de la ventana
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)

# Se define el color del fondo
black = (0, 0, 0)

clock = pygame.time.Clock()

# Ubicación del comienzo del personaje
character_ubication = (0, 350)
player = Actividad1.Character(character_ubication)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    player.process_event(event)
    screen.fill(black)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(20)

pygame.quit ()