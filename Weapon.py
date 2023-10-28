import pygame
import math
from Arrow import Arrow


class Weapon:
    def __init__(self, image, arrow_image):
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.arrow_image = arrow_image
        self.rect = self.image.get_rect()
        self.fired = False
        self.last_shot = pygame.time.get_ticks()

    def create_arrow(self, player):
        self.rect.center = player.rect.center

        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.centerx
        y_dist = -(pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_dist, x_dist))

        arrow = None
        shot_cooldown = 300
        time_to_shoot = pygame.time.get_ticks() - self.last_shot
        if pygame.mouse.get_pressed()[0] and self.fired is False and time_to_shoot >= shot_cooldown:
            arrow = Arrow(self.arrow_image, self.rect.centerx, self.rect.centery, self.angle)
            self.fired = True
            self.last_shot = pygame.time.get_ticks()

        if not pygame.mouse.get_pressed()[0]:
            self.fired = False

        return arrow

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        image_width = self.image.get_width() / 2
        image_height = self.image.get_height() / 2

        surface.blit(self.image, ((self.rect.centerx - int(image_width)), self.rect.centery - int(image_height)))
