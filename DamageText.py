import pygame


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage_info, color):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("assets/fonts/AtariClassic.ttf")
        self.image = self.font.render(damage_info, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.timer = 0

    def update(self):
        self.rect.y -= 1
        self.timer += 1

        if self.timer > 20:
            self.kill()
