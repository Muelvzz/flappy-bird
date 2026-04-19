import pygame

pygame.init()

def draw_window(screen, bg_image, bird):
    screen.blit(bg_image, (0, 0))
    screen.blit(bird.bird_img, bird.rect) # bird.rect

    pygame.display.flip()