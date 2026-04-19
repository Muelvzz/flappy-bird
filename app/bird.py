import pygame, os
from random import randint

class Bird(pygame.sprite.Sprite):
    WIDTH = HEIGHT = 40 # width and height of the bird
    SINK_SPEED = 0.20 # the speed when the bird is falling down
    CLIMB_SPEED = 0.3 # the speed of the bird when going up
    CLIMB_DURATION = 233.3 # the time for the bird when it is flying
    TARGET_UP = 45
    TARGET_DOWN = -45
    ROTATION_SPEED = 0.1

    def __init__(self, x, y, images, bird_img, current_angle=0, msc_to_climb=0):
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.msc_to_climb = msc_to_climb
        self.bird_img = bird_img
        self.current_angle = current_angle

        flap_path, unflap_path = images
        self._img_wingup = pygame.image.load(flap_path).convert_alpha()
        self._img_wingdown = pygame.image.load(unflap_path).convert_alpha()

        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)

        self.rect = self.bird_img.get_rect(center=(self.x, self.y))

    def update(self, delta_frames=1):
        if self.msc_to_climb > 0:
            climb_distance = delta_frames * self.CLIMB_SPEED
            self.current_angle += (self.TARGET_UP - self.current_angle) * self.ROTATION_SPEED
            self.bird_img = pygame.transform.rotate(self._img_wingup, self.current_angle)

            self.y -= climb_distance
            self.msc_to_climb -= delta_frames
        else:
            self.current_angle += (self.TARGET_DOWN - self.current_angle) * self.ROTATION_SPEED
            self.bird_img = pygame.transform.rotate(self._img_wingdown, self.current_angle)

            sink_distance = self.SINK_SPEED * delta_frames
            self.y += sink_distance

        new_rect = self.bird_img.get_rect(center=(self.x, self.y))
        self.rect = new_rect

        if self.msc_to_climb < 0:
            self.msc_to_climb = 0