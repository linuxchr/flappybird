import pygame
import sys
import random as rd

def gameLoop():
    global screen, bird, gravity, bird_movement, bird_rect
    #background = pygame.image.load("assets/background.png").convert()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = 0
                    bird_movement += 0
                    bird_rect.center = (100, 512)
        screen.fill("#246A73")
        bird_movement += gravity
        bird_rect.centery += gravity
        screen.blit(bird, (100, bird_movement))
        pygame.display.update()

def init():
    global screen, bird, gravity, bird_movement, bird_rect
    gravity = 0.25
    bird_movement = 0
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((576,1024))
    bird = pygame.image.load("assets/bird.png").convert()
    bird = pygame.transform.scale2x(bird)
    bird_rect = bird.get_rect(center=(100, 512))
    clock.tick(120)

def main():
    global screen
    init()
    gameLoop()

if __name__ == "__main__":
    main()