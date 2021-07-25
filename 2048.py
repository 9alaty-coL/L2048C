import pygame, sys
from pygame.locals import *
import random

### Hằng số trong game
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

### Các màu cơ bản
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLACK = (  0,   0,   0)
SP = 5
pygame.init()

### Xác định FPS ###
FPS = 240
fpsClock = pygame.time.Clock()
### Thiết lập cửa sổ chơi game và caption
BackGround = pygame.display.set_mode((800, 600))
pygame.display.set_caption('2048 by Tấn Lộc ^^')
### Font chữ cho các layer text
font = pygame.font.SysFont('consolas', 30)

Coor = [[200,100],[300,100],[400,100],[500,100]
     ,[200,200],[300,200],[400,200],[500,200]
     ,[200,300],[300,300],[400,300],[500,300]
     ,[200,400],[300,400],[400,400],[500,400]]

Value = [0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0]
Trash = [0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0]
stop = 0
up = 1
left = 2
down = 3
right = 4

### Tạo các lớp có trong game      
class Powof2():
    def __init__(self, pos, value):
        self.surface = pygame.image.load('Num_IMG\\' + str(value) + '.png')
        self.value = value
        self.x = Coor[pos][0]
        self.y = Coor[pos][1]
        self.state = [0, 0, 0, 0, 4]
        self.pos = pos
        self.app = 100
    def Move(self):
        if self.state[self.state[4]] == 0:
            self.state[4] = 4
        if self.state[4] == 4:
            for i in range (0, 4):
                if self.state[i] != 0:
                    self.state[4] = i     
        if self.state[4] == 4:
            return
        if self.state[4] == 0:
            self.y -= SP
            self.state[self.state[4]] -= SP
        if self.state[4] == 1:
            self.x -= SP
            self.state[self.state[4]] -= SP
        if self.state[4] == 2:
            self.y += SP
            self.state[self.state[4]] -= SP
        if self.state[4] == 3:
            self.x += SP
            self.state[self.state[4]] -= SP
            
##    def State(self, state):
##        self.state = state
    def Up(self):
        while self.pos > 3:
            if Value[self.pos - 4] == 0:
                Value[self.pos - 4] = Value[self.pos]
                Value[self.pos] = 0
                self.pos -= 4
                self.state[0] += 100
            elif Value[self.pos - 4].value == Value[self.pos].value:
                Trash[self.pos] = Value[self.pos]
                Value[self.pos] = 0
                Value[self.pos - 4].value *= 2
                Value[self.pos - 4].surface = pygame.image.load('Num_IMG\\' + str(self.value*2) + '.png')
                break
            else:
                break               
    def Left(self):
        while self.pos % 4 != 0:
            if Value[self.pos - 1] == 0:
                Value[self.pos - 1] = Value[self.pos]
                Value[self.pos] = 0
                self.pos -= 1
                self.state[1] += 100
            elif Value[self.pos - 1].value == Value[self.pos].value:
                Trash[self.pos] = Value[self.pos]
                Value[self.pos] = 0
                Value[self.pos - 1].value *= 2
                Value[self.pos - 1].surface = pygame.image.load('Num_IMG\\' + str(self.value*2) + '.png')
                break
            else:
                break
    def Down(self):
        while self.pos < 12:
            if Value[self.pos + 4] == 0:
                Value[self.pos + 4] = Value[self.pos]
                Value[self.pos] = 0               
                self.pos += 4
                self.state[2] += 100
            elif Value[self.pos + 4].value == Value[self.pos].value:
                Trash[self.pos] = Value[self.pos]
                Value[self.pos] = 0
                Value[self.pos + 4].value *= 2
                Value[self.pos + 4].surface = pygame.image.load('Num_IMG\\' + str(self.value*2) + '.png')
                break
            else:
                break             
    def Right(self):
        while self.pos % 4 != 3:
            if Value[self.pos + 1] == 0:
                Value[self.pos + 1] = Value[self.pos]
                Value[self.pos] = 0
                self.pos += 1
                self.state[3] += 100
            elif Value[self.pos + 1].value == Value[self.pos].value:
                Trash[self.pos] = Value[self.pos]
                Value[self.pos] = 0
                Value[self.pos + 1].value *= 2
                Value[self.pos + 1].surface = pygame.image.load('Num_IMG\\' + str(self.value*2) + '.png')
                break
            else:
                break
                
    def Draw(self):
        if self.app != 0:
            ani = pygame.image.load('Load_IMG\\' + 'target-loader' + str(self.app%29+1) + '.png')
            self.app -= 1
            BackGround.blit(ani, (self.x, self.y))
            return
        BackGround.blit(self.surface, (self.x, self.y))
    

def AddBlock():
    arr = []
    for i in range (0, 16):
        if Value[i] == 0:
            arr.append(i)
    if len(arr) > 0:
        pos = random.choice(arr)
        Value[pos] = Powof2(pos, 2)

    


Value[5] = Powof2(5, 2)

### Phần thực thi vòng lặp
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                for i in range(0, 16):
                    if Value[i] != 0:
                        Value[i].Up()
            if event.key == K_LEFT:
                for i in range(0, 16):
                    if Value[i] != 0:
                        Value[i].Left()
            if event.key == K_DOWN:
                for i in range(15, -1, -1):
                    if Value[i] != 0:
                        Value[i].Down()
            if event.key == K_RIGHT:
                for i in range(15, -1, -1):
                    if Value[i] != 0:
                        Value[i].Right()
            AddBlock()


    BackGround.fill(BLACK)

    
    for i in range(0, 16):
        if Value[i] != 0:
            Value[i].Move()
            Value[i].Draw()
        if Trash[i] != 0:
            Trash[i].Move()
            for j in range(0, 4):
                if Trash[i].state[j] != 0:
                    Trash[i].Draw()



    pygame.display.update() # Cập nhật các chỉnh sửa giao diện
    fpsClock.tick(FPS) 











    

