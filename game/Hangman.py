import pygame,sys
from pygame.locals import *
from random import choice

def get_word():
    f=open("11.txt")
    temp=f.readlines()
    words=[]
    for word in temp:
        words.append(word)
        return words

def draw_gallows(screen):
    pygame.draw.rect(screen,purple,(450,350,100,10))      #bottom底座
    pygame.draw.rect(screen,purple,(495,250,10,100))       #support  支撑杆
    pygame.draw.rect(screen,purple,(450,250,50,10))         #crossbar 横木
    pygame.draw.rect(screen, purple, (450, 250, 10, 25))     #noose  套索

def draw_word(screen,spaces):
    """绘制空格"""
    x=10
    for i in range(spaces):
        pygame.draw.line(screen,yellow,(x,350),(x+20,350),3)
        x+=30
def draw_letter(screen,font,word,guess):
    """判断匹配单词"""
    x=10
    for letter in word:
        if letter==guess:
            letter=font.render(letter,3,(255,255,255))
            screen.blit(letter,(x,300))
        x+=30

def draw_man(screen,body_part):
    if body_part=="head":
        pygame.draw.circle(screen,red,(455,270),10)   #head
    if body_part=="body":
        pygame.draw.line(screen,red,(455,280),(455,320),3)
    if body_part=="l_arm":
        pygame.draw.line(screen,red,(455,300),(455,285),3)
    if body_part == "r_arm":
        pygame.draw.line(screen, red, (455, 300), (465, 285), 3)
    if body_part == "l_leg":
        pygame.draw.line(screen,red,(455, 320), (445, 330),3)
    if body_part=="r_arm":
        pygame.draw.line(screen,red,(455,320),(465,285),3)

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
orange=(255,100,0)
purple=(100,0,255)

pygame.init()
screen_caption=pygame.display.set_caption("Hangman")
screen=pygame.display.set_mode((600,400))
screen.fill((0,0,0))
font=pygame.font.SysFont("monospace",30)

draw_gallows(screen)
draw_man(screen,body_part="head")

words=get_word()
word=choice(words)
word=word.strip("\n")
draw_word(screen,len(word))
pygame.display.update()

body=["r_leg","l_leg","r_arm","l_arm","body","head"]

while body:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        if event.type==KEYDOWN:
            if event.unicode.isalpha():
                guess=event.unicode
                if guess in word:
                    draw_letter(screen,font,word,guess)
                    pygame.display.update()
                else:
                    body_part=body.pop()
                    draw_man(screen,body_part)
                    pygame.display.update()