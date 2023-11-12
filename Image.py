import pygame


class Image:
    def __init__(self):
        self.names = ["big_demon", "elf", "goblin", "imp", "muddy", "skeleton", "tiny_zombie"]
        self.actions = ["idle", "run"]

    def scale_img(self, image, scale):
        w = image.get_width()
        h = image.get_height()
        return pygame.transform.scale(image, (w * scale, h * scale))

    def get_animation_list(self):
        animations = []
        for character in self.names:
            images_by_actions = []
            for action in self.actions:
                images = []
                for i in range(4):
                    img = pygame.image.load(f"assets/images/characters/{character}/{action}/{i}.png").convert_alpha()
                    img = self.scale_img(img, 3)
                    images.append(img)
                images_by_actions.append(images)
            animations.append(images_by_actions)

        return animations

    def get_weapons(self):
        weapons = []
        weapon_names = ["bow", "arrow"]
        for weapon_name in weapon_names:
            weapon_image = pygame.image.load(f"assets/images/weapons/{weapon_name}.png").convert_alpha()
            weapon_image = self.scale_img(weapon_image, 1.5)
            weapons.append(weapon_image)
        return weapons

    def get_hearts(self):
        hearts = []
        heart_names = ["heart_empty", "heart_half", "heart_full"]
        for heart_name in heart_names:
            heart_image = pygame.image.load(f"assets/images/items/{heart_name}.png").convert_alpha()
            heart_image = self.scale_img(heart_image, 3)
            hearts.append(heart_image)
        return hearts
