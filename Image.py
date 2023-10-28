import pygame


class Image:
    def __init__(self):
        self.names = ["big_demon", "elf", "goblin", "imp", "muddy", "skeleton", "tiny_zombie"]
        self.actions = ["idle", "run"]

    def get_animation_list(self):
        def scale_img(image, scale):
            w = image.get_width()
            h = image.get_height()
            return pygame.transform.scale(image, (w * scale, h * scale))

        animations = []
        for character in self.names:
            images_by_actions = []
            for action in self.actions:
                images = []
                for i in range(4):
                    img = pygame.image.load(f"assets/images/characters/{character}/{action}/{i}.png").convert_alpha()
                    img = scale_img(img, 3)
                    images.append(img)
                images_by_actions.append(images)
            animations.append(images_by_actions)

        return animations

    def get_weapons(self):
        def scale_img(image, scale):
            w = image.get_width()
            h = image.get_height()
            return pygame.transform.scale(image, (w * scale, h * scale))

        weapons = []
        bow = pygame.image.load("assets/images/weapons/bow.png").convert_alpha()
        bow_image = scale_img(bow, 1.5)
        weapons.append(bow_image)

        arrow = pygame.image.load("assets/images/weapons/arrow.png").convert_alpha()
        arrow_image = scale_img(arrow, 1.5)
        weapons.append(arrow_image)

        return weapons
