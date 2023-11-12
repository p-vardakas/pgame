import math
import pygame
import Constants


class Character:
    def __init__(self, x, y, animation_images, character_index):
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)
        self.image = None
        self.flip = False
        self.image_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_list = animation_images[character_index]
        self.running = False
        self.action = 0
        self.frame_index = 0
        self.health = Constants.HEALTH
        self.isAlive = True

    def move(self, dx, dy):
        self.running = False

        if dx != 0 or dy != 0:
            self.running = True

        if dx < 0:
            self.flip = True
        else:
            self.flip = False

        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)

        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        if self.running:
            self.update_action(1)  # 1:run
        else:
            self.update_action(0)  # 0:idle

        if self.health <= 0:
            self.health = 0
            self.isAlive = False

        animation_speed = 150

        self.image = self.animation_list[self.action][self.image_index]

        if (pygame.time.get_ticks() - self.update_time) > animation_speed:
            self.image_index += 1
            self.update_time = pygame.time.get_ticks()

        if self.image_index >= len(self.animation_list[self.action]):
            self.image_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action

            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, Constants.BLACK, self.rect, 1)
