import pygame

pygame.init()

def draw_window(screen, is_playing, start_image, bg_image, bird):
    screen.blit(bg_image, (0, 0))

    if is_playing:
        screen.blit(bird.bird_img, bird.rect) # bird.rect

    if not is_playing:
        screen.blit(start_image, (0, 0))