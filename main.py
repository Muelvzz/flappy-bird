import pygame
import os

pygame.init()

FPS = 60
WIDTH, HEIGHT = 480, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

bird_img = pygame.image.load(os.path.join('Assets/sprites', 'yellowbird-midflap.png')).convert()
bird_img_rect = bird_img.get_rect()

bird_img_rect.topleft = (120, HEIGHT / 2)

bg_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.png')).convert(), (WIDTH, HEIGHT))

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        screen.blit(bg_image, (0, 0))
        clock.tick(60)
        screen.blit(bird_img, (120, 270))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Spacebar pressed")

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()