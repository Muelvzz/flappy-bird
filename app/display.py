import pygame

pygame.init()

def draw_window(screen, bg_image, bird):
    screen.blit(bg_image, (0, 0))
    screen.blit(bird.bird_img, (bird.x, bird.y))

    pygame.display.flip()