import pygame
import os

from app.bird import Bird
from app.display import draw_window

pygame.init()
pygame.mixer.init()

# setting-up the game
FPS = 60
WIDTH, HEIGHT = 480, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

icon_image = os.path.join('Assets/sprites', 'yellowbird-midflap.png')
icon = pygame.image.load(icon_image)
pygame.display.set_icon(icon)

# setting the bird sprites
bird_images_effect = (os.path.join('Assets/sprites', 'yellowbird-upflap.png'), os.path.join('Assets/sprites', 'yellowbird-downflap.png'))
bird_img = pygame.image.load(os.path.join('Assets/sprites', 'yellowbird-midflap.png')).convert()
bird_img_rect = bird_img.get_rect()

# positioning the bird
bird_img_rect.topleft = (WIDTH / 4, HEIGHT / 2)

# loading the bird on window
bg_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.png')).convert(), (WIDTH, HEIGHT))

start_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets/sprites', 'message.png')).convert_alpha(), (WIDTH, HEIGHT))

def main():
    is_playing = False
    run = True
    clock = pygame.time.Clock()
    bird = Bird(bird_img_rect.x, bird_img_rect.y, bird_images_effect, bird_img) # calling the Bird class

    start_sound_path = os.path.join('Assets/audio', 'swoosh.wav')
    start_sound = pygame.mixer.Sound(start_sound_path)
    start_sound.play()

    while run:
        delta_time = clock.tick(FPS) # This is critical to actually create the downfall gravity

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    is_playing = True

                if event.key == pygame.K_SPACE:
                    fly_sound_path = os.path.join('Assets/audio', 'wing.wav')
                    fly_sound = pygame.mixer.Sound(fly_sound_path)
                    fly_sound.play()

                    bird.msc_to_climb = bird.CLIMB_DURATION # refreshing the time to ascend

        if is_playing:
            bird.update(delta_time)
        draw_window(screen, is_playing, start_img, bg_image, bird)

        # updates the window
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()