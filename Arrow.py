import pygame
import math
import Constants
from DamageText import DamageText


class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.dx = math.cos(math.radians(self.angle)) * 10
        self.dy = -(math.sin(math.radians(self.angle)) * 10)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        conditions = [
            self.rect.right < 0,
            self.rect.left > Constants.SCREEN_WIDTH,
            self.rect.bottom < 0,
            self.rect.top > Constants.SCREEN_HEIGHT
        ]

        if any(conditions):
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, (
            (self.rect.centerx - int(self.image.get_width() / 2)),
            self.rect.centery - int(self.image.get_height() / 2)))

    def damage_enemy(self, enemies):
        damage = 0
        damage_text = None
        for enemy in enemies:
            if enemy.rect.colliderect(self.rect) and enemy.isAlive:
                damage = Constants.DAMAGE
                enemy.health -= damage
                self.kill()
                break

        if damage:
            damage_text = DamageText(enemy.rect.centerx, enemy.rect.y, str(enemy.health), Constants.RED)

        return damage_text
