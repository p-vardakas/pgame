import pygame
import Constants
from Character import Character
from Image import Image
from Weapon import Weapon
from HeartInfo import HeartInfo

pygame.init()
clock = pygame.time.Clock()

# setup window dimensions
screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

# setup window caption
pygame.display.set_caption("Dungeon Crawler")

# player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

animation_images = Image.get_animation_list(Image())
heart_images = Image.get_hearts(Image())
weapon_images = Image.get_weapons(Image())
weapon = Weapon(weapon_images[0], weapon_images[1])
arrow_group = pygame.sprite.Group()
damage_text_group = pygame.sprite.Group()

enemies = []
enemy = Character(200, 200, animation_images, 4)
enemies.append(enemy)

player = Character(100, 100, animation_images, 3)

run = True

# main game loop
while run:
    # set game play speed
    clock.tick(Constants.FPS)

    # Fill background color
    screen.fill(Constants.BLACK)

    # calculate player movement
    dx = 0
    dy = 0
    if moving_right:
        dx = Constants.SPEED
    if moving_left:
        dx = -Constants.SPEED
    if moving_up:
        dy = -Constants.SPEED
    if moving_down:
        dy = Constants.SPEED

    # move player
    player.move(dx, dy)

    player.update_animation()

    for enemy in enemies:
        enemy.update_animation()

    arrow = weapon.create_arrow(player)
    if arrow:
        arrow_group.add(arrow)
    for arrow in arrow_group:
        arrow.update()

        damage_text = arrow.damage_enemy(enemies)
        if damage_text is not None:
            damage_text_group.add(damage_text)

    damage_text_group.update()

    player.draw(screen)
    weapon.draw(screen)
    for arrow in arrow_group:
        arrow.draw(screen)

    damage_text_group.draw(screen)
    HeartInfo.draw_heart_info(HeartInfo(), enemy, screen, heart_images)

    for enemy in enemies:
        enemy.draw(screen)

    # draw player on screen
    player.draw(screen)

    # event handler
    for event in pygame.event.get():
        # close window
        if event.type == pygame.QUIT:
            run = False

        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_s:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_z:
                moving_down = True

        # keyboard releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_s:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_z:
                moving_down = False

    pygame.display.update()

pygame.quit()
