import pygame.draw

import Constants


class HeartInfo:

    def draw_heart_info(self, player, screen, hearts):
        pygame.draw.rect(screen, Constants.GREY, (0, 0, Constants.SCREEN_WIDTH, Constants.HEART_INFO_HEIGHT))
        pygame.draw.line(screen, Constants.RED, (0, 50), (Constants.SCREEN_WIDTH, Constants.HEART_INFO_HEIGHT))

        half_heart_drawn = False
        for i in range(5):
            if player.health >= (i + 1) * 20:
                screen.blit(hearts[2], (10 + i * 50, 0))
            elif player.health % 20 > 0 and half_heart_drawn == False:
                screen.blit(hearts[1], (10 + i * 50, 0))
                half_heart_drawn = True
            else:
                screen.blit(hearts[0], (10 + i * 50, 0))
