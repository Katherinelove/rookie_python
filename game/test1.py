import pygame,sys
from pygame.locals import *

pygame.init()

fonts=pygame.font.get_fonts()           #返回列表
font=fonts.pop()                        #得到列表最后一种字体
while fonts:
    screen = pygame.display.set_mode((400, 300))
    screen.fill((255, 255, 225))
    pygame.display.update()
    try:
        new_font=pygame.font.SysFont(font,30)      #取字体可以直接取   font=pygame.font.SysFont（“字体”，大小）
    except:
        pass
    text=new_font.render(font,True,(0,255,0),)
    screen.blit(text,(40,40))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            font=fonts.pop()
        if event.type==QUIT:
            sys.exit()
