import pygame
from pygame.locals import *

# Variáveis constantes
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED = 10

# Construção do Objeto Pássaro


class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha(),
                        pygame.image.load(
                            'assets/sprites/bluebird-midflap.png').convert_alpha(),
                        pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha()]

        self.speed = SPEED

        '''Imagem inicial'''
        self.current_image = 0

        '''Define a imagem, considerando a transparencia'''
        self.image = pygame.image.load(
            'assets/sprites/bluebird-upflap.png').convert_alpha()
        '''Posiciona a imagem'''
        self.rect = self.image.get_rect()
        '''Posiciona o pássaro a partir da metade da tela'''
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2

        print(self.rect)

        def update(self):
            self.current_image = (self.current_image + 1) % 3
            self.image = self.images[self.current_image]

            # Update height
            self.rect[1] += self.speed

        def bump(self):


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

'''Carregar backgroud e escalar tamanho'''
BACKGROUND = pygame.image.load('assets/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
'''Instânciar o objeto'''
bird = Bird()
bird_group.add(bird)


clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    '''Posição do backgroud'''
    screen.blit((BACKGROUND, (0, 0))

    bird_group.update()
    bird_group.draw(screen)

    pygame.display.update()
