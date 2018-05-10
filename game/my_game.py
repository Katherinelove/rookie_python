import pygame,sys
from pygame.locals import *  #输入事件，导入一些常用的全局变量


x=40
y=40
black=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
pygame.init()
screen=pygame.display.set_mode((1200,600))
screen.fill(black)

while True:
    pygame.draw.circle(screen,red,(20,20),10)
    pygame.draw.circle(screen, green, (50, 20), 10)
    pygame.draw.circle(screen, blue, (80, 20), 10)
    pygame.display.update()
    #移动形状   （讲位置参数设置成变量即可）
    pygame.draw.circle(screen, red, (x, y), 10)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:        #比如这里的QUIT
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                x-=1
            elif event.key==K_RIGHT:
                x+=1
            elif event.key==K_UP:
                y-=1
            elif event.key==K_DOWN:
                y+=1
