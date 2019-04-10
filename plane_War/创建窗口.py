__author__ = '努力学习 不要让自己失望'
import pygame
import time
from pygame.locals import *


def main():
    # 创建一个窗口，用来显示界面
    screen = pygame.display.set_mode((480, 550), 0, 32)
    # 创建一个窗口大小的图片。来充当背景
    background = pygame.image.load("./feiji/background.png")
    # 创建一个飞机的图片
    hero = pygame.image.load("./feiji/hero1.png")
    x = 210
    y = 440
    while True:
        # 吧背景图片放到窗口中
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        # 更新显示的内容
        pygame.display.update()
        # 获取事件，比如按键等
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == pygame.QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == pygame.KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('left')
                    x -= 5
                # 检测按键是否是d或者right
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print('right')
                    x += 5
                # 检测按键是否是空格键
                elif event.key == pygame.K_SPACE:
                    print('space')

        time.sleep(0.02)


if __name__ == "__main__":
    main()
