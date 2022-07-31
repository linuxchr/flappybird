import pygame
import sys
import random as rd

def gameOver(score):
    global screen
    pygame.display.update()
    score = "Score: " + str(score)
    overfont = pygame.font.SysFont("monospace", 40).render("Game Over", 1, (0, 0, 0))
    final_score = pygame.font.SysFont("monospace", 32).render(score, 1, (0, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill("white")
        screen.blit(final_score, (200, 512))
        screen.blit(overfont, (180, 460))
        pygame.display.update()

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
                    bird_movement -= 12
                    bird_rect.center = (100, 512)
        screen.fill("#246A73")
        bird_movement += gravity
        bird_rect.centery += gravity
        screen.blit(bird, (100, bird_movement))
        print(bird_movement)
        pygame.display.update()

def init():
    global screen, bird, gravity, bird_movement, bird_rect
    gravity = 0.7
    bird_movement = 0
    pygame.init()
    pygame.display.set_caption('FlappyTriangle')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((576,1024))
    bird = pygame.image.load("assets/bird.png").convert()
    bird = pygame.transform.scale2x(bird)
    bird_rect = bird.get_rect(center=(100, 512))
    pygame.display.update()
    clock.tick(360)

def main():
    global screen
    init()
    #gameLoop()
    gameOver(16)

if __name__ == "__main__":
    main()