import pygame
import os

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

bg_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.png')).convert(), (WIDTH, HEIGHT))

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(45)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(bg_image, (0, 0))

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()