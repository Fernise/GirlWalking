import pygame


# Clase Character que hereda de la superclase Sprite
class Character(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, position):
        # Se carga y se procesa la imagen
        self.girl_animation = pygame.image.load('walking_animation.png')
        self.girl_animation.set_clip(pygame.Rect(0, 0, 64, 130))
        self.image = self.girl_animation.subsurface(self.girl_animation.get_clip())
        self.rect = self.image.get_rect()
        # Coordenadas del personaje en cada momento
        self.rect.topleft = position
        self.frame = 0
        # Coordenadas de cada movimiento del personaje en la imagen fuente (Moviéndose a la izquierda)
        self.left_move = {0: (64, 130, 64, 130), 1: (128, 130, 64, 130), 2: (192, 130, 64, 130), 3: (256, 130, 64, 130),
                           4: (320, 130, 64, 130), 5: (384, 130, 64, 130), 6: (448, 130, 64, 130), 7: (512, 130, 64, 130), 8: (576, 130, 64, 130)}
        # Coordenadas de cada movimiento del personaje en la imagen fuente (Moviéndose a la derecha)
        self.right_move = {0: (64, 0, 64, 130), 1: (128, 0, 64, 130), 2: (192, 0, 64, 130), 3: (256, 0, 64, 130),
                           4: (320, 0, 64, 130), 5: (384, 0, 64, 130), 6: (448, 0, 64, 130), 7: (512, 0, 64, 130), 8: (576, 0, 64, 130)}

    # Método get_frame: devuelve el frame del personaje en cada momento
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    # Método clip: devuelve el recorte del personaje
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.girl_animation.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.girl_animation.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    # Método update: movimiento del personaje
    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_move)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_move)
            self.rect.x += 5

        if direction == 'stop_left':
            self.clip(self.left_move[0])
        if direction == 'stop_right':
            self.clip(self.right_move[0])

        # Bloquea al personaje de salirse de los bordes de la pantalla
        if self.rect.x > 560:
            self.rect.x = 560
        if self.rect.x < 0:
            self.rect.x = 0

        self.image = self.girl_animation.subsurface(self.girl_animation.get_clip())

    # Controla los eventos del teclado
    def process_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        # Se mueve el personaje hacia los lados
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')

        # Se para el personaje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.update('stop_left')
            if event.key == pygame.K_RIGHT:
                self.update('stop_right')
