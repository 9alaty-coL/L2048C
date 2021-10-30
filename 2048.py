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
font = pygame.font.SysFont('consolas', 15)

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
Load = [[0,100,120],[0,260,120],[0,420,120],[0,580,120]
     ,[0,100,270],[0,260,270],[0,420,270],[0,580,270]
     ,[0,100,420],[0,260,420],[0,420,420],[0,580,420]]
stop = 0
up = 1
left = 2
down = 3
right = 4


LayBGr = pygame.image.load('Background\\0.png')
Lay2 = pygame.Surface((400, 400))
Lay2.fill(BLACK)
pygame.draw.line(Lay2, GREEN, (0, 0), (0, 400), 1)
pygame.draw.line(Lay2, GREEN, (100, 0), (100, 400), 1)
pygame.draw.line(Lay2, GREEN, (200, 0), (200, 400), 1)
pygame.draw.line(Lay2, GREEN, (300, 0), (300, 400), 1)
pygame.draw.line(Lay2, GREEN, (400, 0), (400, 400), 1)

pygame.draw.line(Lay2, GREEN, (0, 0), (400, 0), 1)
pygame.draw.line(Lay2, GREEN, (0, 100), (400, 100), 1)
pygame.draw.line(Lay2, GREEN, (0, 200), (400, 200), 1)
pygame.draw.line(Lay2, GREEN, (0, 300), (400, 300), 1)
pygame.draw.line(Lay2, GREEN, (0, 400), (400, 400), 1)

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
    
class Menu():
    def __init__(self):
        self.statecur = 0
        self.data = [[0,250,50],[0,250,160],[0,250,270],[0,250,380],[0,250,490]]
        self.bg = 0
    def draw(self):
        
        for i in range(0, 5):
            if self.statecur == i:
                self.data[i][0] = 1
            else:
                self.data[i][0] = 0
            BackGround.blit(pygame.image.load('Menu_IMG\\' + str(self.data[i][0]) + str(i) + '.png'), (self.data[i][1], self.data[i][2]))
        BackGround.blit(pygame.image.load('Menu_IMG\\l.png'), (130, self.data[self.statecur][2] + 14))
        BackGround.blit(pygame.image.load('Menu_IMG\\r.png'), (600, self.data[self.statecur][2] + 14))
    def move(self, direct):
        if direct == 1:
            self.statecur += 1
        if direct == 2:
            self.statecur -= 1
        

        if self.statecur == 5:
            self.statecur = 0
        if self.statecur == -1:
            self.statecur = 4
    def run(self):
        if self.statecur == 0:
            StartGame()
        if self.statecur == 1:
            runMenuLoad()
                
        if self.statecur == 2:
            self.bg += 1
            global LayBGr 
            LayBGr = pygame.image.load('Background\\' + str(self.bg % 4) + '.png')
        if self.statecur == 4:
            pygame.quit()
            sys.exit()



def runMenuLoad():
    while True:
        pick = 99
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    VarMenu.move(2)
                if event.key == K_LEFT:
                    VarMenu.move(3)
                if event.key == K_DOWN:
                    VarMenu.move(1)
                if event.key == K_RIGHT:
                    VarMenu.move(4)
                if event.key == 13:
                    VarMenu.run()
                if event.key == 27:
                    runMenuLoad()

        BackGround.fill(BLACK)
        f = open('Secret.txt', 'r')
        while True:
            line = f.readline()
            if not line:
                break
            if line.find(' ') == -1:
                Load[int(line)][0] = f.readline()
        f.close()
        f = open('Secret.txt', 'r')
        while True:
            if not line:
                break
            if line.find(' ') == -1 and int(line) == pick:
                line1 = f.readline()
                while True:
                    line2 = f.readline()
                    if not line2 or line2.find(' ') == -1:
                        break
                    pos = int(line2[0:line2.find(' ')])
                    value = int(line2[line2.find(' ')+1:])
                    Value[pos] = Powof2(pos, value) 
                StartGame()      

            

        pygame.display.update() # Cập nhật các chỉnh sửa giao diện
        fpsClock.tick(FPS)


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
def StartGame():
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
                if event.key == 27:
                    pygame.quit()
                    sys.exit()
                AddBlock()



        BackGround.fill(BLACK)
        BackGround.blit(LayBGr, (0, 0))
        BackGround.blit(Lay2, (200, 100))

        
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


VarMenu = Menu()

def StartMenu():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    VarMenu.move(2)
                if event.key == K_LEFT:
                    VarMenu.move(3)
                if event.key == K_DOWN:
                    VarMenu.move(1)
                if event.key == K_RIGHT:
                    VarMenu.move(4)
                if event.key == 13:
                    VarMenu.run()
                if event.key == 27:
                    pygame.quit()
                    sys.exit()

        BackGround.fill(BLACK)
        BackGround.blit(LayBGr, (0, 0))
        VarMenu.draw()


        pygame.display.update() # Cập nhật các chỉnh sửa giao diện
        fpsClock.tick(FPS)

def main():
    StartMenu()
    StartGame()



if __name__ == "__main__":
    main()









    

