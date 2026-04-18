import pygame

class Bird(pygame.spirte.Sprite):
    WIDTH = HEIGHT = 40
    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.3
    CLIMB_DURATION = 333.3

    def __init__(self, x, y, msc_to_climb, images):
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.msc_to_climb = msc_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)