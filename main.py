import pygame
import Constants
from Character import Character
from Image import Image
from Weapon import Weapon
from HeartInfo import HeartInfo


class Game:
    def __init__(self):
        self.run = None
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Dungeon Crawler")

        self.player = Character(100, 100, Image.get_animations(Image()), 3)
        self.enemies = [Character(200, 200, Image.get_animations(Image()), 1)]
        self.weapon = Weapon(*Image.get_weapons(Image()))

        self.arrow_group = pygame.sprite.Group()
        self.damage_text_group = pygame.sprite.Group()

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN:
                self.handle_key(event.key, True)
            elif event.type == pygame.KEYUP:
                self.handle_key(event.key, False)

    def handle_key(self, key, key_pressed):
        if key == pygame.K_a:
            self.moving_left = key_pressed
        elif key == pygame.K_s:
            self.moving_right = key_pressed
        elif key == pygame.K_w:
            self.moving_up = key_pressed
        elif key == pygame.K_z:
            self.moving_down = key_pressed

    def update(self):
        dx = Constants.SPEED * (self.moving_right - self.moving_left)
        dy = Constants.SPEED * (self.moving_down - self.moving_up)

        self.player.move(dx, dy)
        self.player.update_animation()

        for enemy in self.enemies:
            enemy.update_animation()

        arrow = self.weapon.create_arrow(self.player)

        if arrow:
            self.arrow_group.add(arrow)

        for arrow in self.arrow_group:
            arrow.update()
            damage_text = arrow.damage_enemy(self.enemies)
            if damage_text:
                self.damage_text_group.add(damage_text)

        self.damage_text_group.update()

    def draw(self):
        self.screen.fill(Constants.BLACK)

        self.player.draw(self.screen)
        self.weapon.draw(self.screen)

        for arrow in self.arrow_group:
            arrow.draw(self.screen)

        self.damage_text_group.draw(self.screen)
        HeartInfo.draw_heart_info(HeartInfo(), self.enemies[0], self.screen, Image.get_hearts(Image()))

        for enemy in self.enemies:
            enemy.draw(self.screen)

        pygame.display.update()

    def run_game(self):
        self.run = True
        while self.run:
            self.clock.tick(Constants.FPS)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_game()
