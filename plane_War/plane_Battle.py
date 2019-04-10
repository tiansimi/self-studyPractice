__author__ = '努力学习 不要让自己失望'
import pygame
import time
from pygame.locals import *
import random


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 180
        self.y = 440
        self.image = pygame.image.load("./feiji/hero1.png")
        self.screen = screen_temp
        self.bullet_list = []  # 存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # 显示子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.x -= 5

    def move_rigt(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class Bullet(object):
    '''子弹类'''

    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 40
        self.image = pygame.image.load("./feiji/bullet.png")
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyPlane(object):
    '''敌机类'''

    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.screen = screen_temp
        self.bullet_list = []  # 存储发射出去的子弹对象引用
        self.enemy_direction = "right"  # 敌机默认的运行方向

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move(self):  # 防止敌机越界
        if self.x > 480 - 50:
            self.enemy_direction = "left"
        elif self.x < 0:
            self.enemy_direction = "right"

        if self.enemy_direction == "right":
            self.x += 5
        elif self.enemy_direction == "left":
            self.x -= 5


    def fire(self):
        random_num = random.randint(1, 100)  # 生成1-100的整数
        if random_num == 80 or random_num == 60:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class EnemyBullet():  # 敌机子弹类
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y + 40
        self.image = pygame.image.load("./feiji/bullet1.png")
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 550:
            return True
        else:
            return False


def key_control(hero_temp):
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
                hero_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print('right')
                hero_temp.move_rigt()
            # 检测按键是否是空格键
            elif event.key == pygame.K_SPACE:
                print('space')
                hero_temp.fire()


def main():
    # 创建一个窗口，用来显示界面
    screen = pygame.display.set_mode((480, 550), 0, 32)
    # 创建一个窗口大小的图片。来充当背景
    background = pygame.image.load("./feiji/background.png")
    # 创建一个飞机对象
    hero = HeroPlane(screen)
    # 创建一个敌机
    enemy = EnemyPlane(screen)
    while True:
        # 吧背景图片放到窗口中
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()

        # 更新显示的内容
        pygame.display.update()
        # 获取事件，比如按键等
        key_control(hero)
        time.sleep(0.02)  # 降低cpu负担


if __name__ == "__main__":
    main()
