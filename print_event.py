import pygame
import sys

class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    test_settings = Settings()
    screen = pygame.display.set_mode((test_settings.screen_width, test_settings.screen_height))
    pygame.display.set_caption("Testing Print Events")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)
        pygame.display.flip()

run_game()