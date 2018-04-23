import pygame
import sys
from pygame.sprite import Group
import copy
from pygame.sprite import Sprite
import random
import pygame.font

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1120,840))
    pygame.display.set_caption('tanshishe')
    she = She(screen)
    food = Food(screen,she)
    foods = Group()
    while True:
        check_event(she)
        # check_peng()
        record = Record(she,screen)
        she.update()
        check_out(she)
        check_eat(foods,she)
        creat_food(screen,she,foods)
        update_screen(screen,she,foods,record)
        clock = pygame.time.Clock()
        clock.tick(8)

class She(Sprite):
    def __init__(self,screen):
        super(She,self).__init__()
        self.p_list = [[560,420],[546,420],[532,420]]
        self.direction = 'R'
        self.rect = pygame.Rect(self.p_list[0][0],self.p_list[0][1],14,14)
        self.rects = [pygame.Rect(p[0],p[1],14,14) for p in self.p_list]
        self.screen = screen
        self.speed = 14
    def update(self):
        self.yidong()
        if self.direction == 'R':
            self.p_list[0][0] += self.speed
        elif self.direction == 'L':
            self.p_list[0][0] -= self.speed
        elif self.direction == 'U':
            self.p_list[0][1] -= self.speed
        elif self.direction == 'D':
            self.p_list[0][1] += self.speed
        self.rect.x= self.p_list[0][0]
        self.rect.y = self.p_list[0][1]
    def yidong(self):
        self.p_list_copy = copy.deepcopy(self.p_list)
        for i in range(1,len(self.p_list)):
             self.p_list[i] = self.p_list_copy[i-1]
    def draw_she(self):
        for pp in self.p_list:
            pygame.draw.rect(self.screen,(255,0,0),pygame.Rect(pp[0],pp[1],14,14))
        pygame.draw.rect(self.screen,(148,0,211),[self.p_list[0][0],self.p_list[0][1],14,14])

class Food(Sprite):
    def __init__(self,screen,she):
        super(Food,self).__init__()
        self.screen = screen
        self.color = (255,239,213)
        self.list = copy.copy(she.p_list)
        self.creat()
    def creat(self):
        self.xy = [random.randint(1,79)*14,random.randint(1,59)*14]
        if  self.xy not in self.list :
            self.rect = pygame.Rect(self.xy[0],self.xy[1],14,14)
        else:
            self.creat()
    def draw_food(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

def creat_food(screen,she,foods):
    if len(foods) < 3 :
        new_food = Food(screen,she)
        foods.add(new_food)

def update_screen(screen,she,foods,record):
    screen.fill((182,215,168))
    she.draw_she()
    for food in foods:
        food.draw_food()
    record.blit_rec()
    pygame.display.flip()

def check_event(she):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down(event,she)
def check_down(event,she):
    if event.key == pygame.K_RIGHT and she.direction != 'L':
        she.direction = 'R'
    elif event.key == pygame.K_LEFT and she.direction != 'R':
        she.direction = 'L'
    elif event.key == pygame.K_DOWN and she.direction != 'U':
        she.direction = 'D'
    elif event.key == pygame.K_UP and she.direction != 'D':
        she.direction = 'U'
    elif event.key == pygame.K_SPACE and she.speed == 14 :
        she.speed = 28
    elif event.key == pygame.K_SPACE and she.speed == 28 :
        she.speed = 14
def check_eat(foods,she):
    for food in foods:
        if food.xy in she.p_list:
            foods.remove(food)
            she.p_list.extend(she.p_list[-3:])
def check_out(she):
    if she.p_list[0][0] < 0:
        she.p_list[0][0] +=  1120
    elif she.p_list[0][0] > 1120:
        she.p_list[0][0] -=  1120
    elif she.p_list[0][1] < 0:
        she.p_list[0][1] += 840
    elif she.p_list[0][1] > 840:
        she.p_list[0][1] -= 840

class Record:
    def __init__(self,she,screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None,36)
        self.text = self.font.render('Length: '+str(len(she.p_list)),True,(255,0,0))
        self.record_rect = [980,20]
    def blit_rec(self):
        self.screen.blit(self.text,self.record_rect)

run_game()
