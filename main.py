import pygame
import sys

def gameOver(score):
    global screen, clock, bird_pos
    clock.tick(24)
    pygame.display.update()
    score = "Score: " + str(score)
    overfont = pygame.font.SysFont("monospace", 40).render("Game Over", 1, (0, 0, 0))
    final_score = pygame.font.SysFont("monospace", 32).render(score, 1, (0, 0, 0))
    revanche = pygame.font.SysFont("monospace", 16).render("Press Space to Play Again.", 1, (0, 0, 0))
    execute = True
    while execute:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    execute = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        screen.fill("white")
        screen.blit(final_score, (200, 512))
        screen.blit(overfont, (180, 460))
        screen.blit(revanche, (157, 1000))
        pygame.display.update()

def gameLoop():
    global screen, bird, gravity, bird_pos, bird_rect, clock, pos1, speed, pos2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_pos -= 120
        screen.fill("#246A73")
        bird_pos += gravity
        screen.blit(bird, (100, bird_pos))
        if pos1 <= 0:
            pos1 = 546
        else:
            exec(f'pygame.draw.rect(screen, "#437C90", pygame.Rect({pos1}, 0, 30, 512))')
            pos1 -= speed
        if pos2 <= 0:
            pos2 = 546
        else:
            exec(f'pygame.draw.rect(screen, "#437C90", pygame.Rect({pos2}, 512, 30, 1024))')
            pos2 -= speed
        if bird_pos > 1024:
            gameOver(1)
            bird_pos = 0
            bird_pos -= 12
            pos1 = 546
            pos2 = 440
            screen.fill("#246A73")
            bird_pos += gravity
            screen.blit(bird, (100, bird_pos))
            pygame.display.update()
        if pos1 <= 102 and pos1 >= 98 and bird_pos <= 512:
            gameOver(1)
            pos1 = 546
            pos2 = 440
        if pos2 <= 102 and pos2 >= 98 and bird_pos >= 512:
            gameOver(1)
            pos2 = 440
            pos1 = 546
        pygame.display.update()

def init():
    global screen, bird, gravity, bird_pos, bird_rect, clock, pos1, speed, pos2
    gravity = 0.5 
    bird_pos = 0
    pos1 = 546
    pos2 = 440
    speed = 0.2
    pygame.init()
    pygame.display.set_caption('FlappyTriangle')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((576,1024))
    bird = pygame.image.load("assets/bird.png").convert()
    bird = pygame.transform.scale2x(bird)
    bird_rect = bird.get_rect(center=(100, 512))
    pygame.display.update()
    clock.tick(24)
def main():
    init() # Innit
    gameLoop()

if __name__ == "__main__":
    main() # Start main Function
