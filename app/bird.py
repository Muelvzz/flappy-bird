import pygame, math
from random import randint

class Bird(pygame.sprite.Sprite):
    WIDTH = HEIGHT = 40 # width and height of the bird
    SINK_SPEED = 0.20 # the speed when the bird is falling down
    CLIMB_SPEED = 0.2 # the speed of the bird when going up
    CLIMB_DURATION = 233.3 # the time for the bird when it is flying

    def __init__(self, x, y, msc_to_climb, images, bird_img):
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.msc_to_climb = msc_to_climb
        self.bird_img = bird_img

        flap_path, unflap_path = images
        self._img_wingup = pygame.image.load(flap_path).convert_alpha()
        self._img_wingdown = pygame.image.load(unflap_path).convert_alpha()

        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)

    def update(self, delta_frames=1):
        if self.msc_to_climb > 0:
            climb_distance = delta_frames * self.CLIMB_SPEED

            self.y -= climb_distance
            self.bird_img = self._img_wingup

            self.msc_to_climb -= delta_frames
        else:
            sink_distance = self.SINK_SPEED * delta_frames
            self.y += sink_distance
            self.bird_img = self._img_wingdown

        if self.msc_to_climb < 0:
            self.msc_to_climb = 0