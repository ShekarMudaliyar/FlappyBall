import pygame
from random import randint
black = (0,0,0)
bg = (0,255,255)
green = (16, 104, 29)
red = (255,0,0)
yellow = (255,255,0)
gotext = (9, 10, 71)
pygame.init()
size = 700,500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

done = False
clock = pygame.time.Clock()
def background():
    pygame.draw.rect(screen,(76, 39, 5),(0,size[1]-20,size[0],20))
    pygame.draw.rect(screen,(132, 68, 9),(0,size[1]-50,size[0],30))

    
def ball(x,y):
    pygame.draw.circle(screen,yellow,(x,y),20)
    pygame.draw.circle(screen,black,(x,y),20,3)

def gameover():
    font = pygame.font.SysFont(None,75)
    text = font.render("Game Over",True,gotext)
    font = pygame.font.SysFont(None,35)
    text2 = font.render("down arrow to play again",True,gotext)
    font = pygame.font.SysFont(None,35)
    text3 = font.render("up arrow to exit",True,gotext)
    screen.blit(text,[50,250])
    screen.blit(text2,[50,250+75])
    screen.blit(text3,[50,250+75+40])

def obstacle(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen,green,(xloc,yloc,xsize,ysize))
    pygame.draw.rect(screen,(13, 51, 5),(xloc,yloc,xsize,ysize),3)
    pygame.draw.rect(screen,green,(xloc,int(yloc+ysize+space),xsize,ysize+500))
    pygame.draw.rect(screen,(13, 51, 5),(xloc,int(yloc+ysize+space),xsize,ysize+500),3)

def Score(score):
    font = pygame.font.SysFont(None,75)
    textScore = font.render("Score: "+str(score),True,black)
    screen.blit(textScore,[0,0])

    
x = int(size[0]/2)
y = int(size[1]/2)
x_speed = 0
y_speed = 0
ground = size[1]-20
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0,350)
space = randint(150,180)
obspeed = 2.5
score = 0    
time=60    

while not done:
	#time = 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_speed = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                y_speed = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                x = int(size[0]/2)
                y = int(size[1]/2)
                x_speed = 0
                y_speed = 0
                ground = 480
                xloc = 700
                yloc = 0
                xsize = 70
                ysize = randint(0,350)
                space = 150
                obspeed = 2.5
                score = 0
                time=60
                obstacle(xloc,yloc,xsize,ysize)
                ball(x,y)
                Score(score)    


    screen.fill(bg)
    background()
    obstacle(xloc,yloc,xsize,ysize)
    ball(x,y)
    Score(score)
    y+=y_speed
    xloc -=obspeed

    
    if y > ground:
        gameover()
        y_speed = 0
        obspeed = 0
 
    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 0
 

    if x+20 > xloc and y+20 >ysize+space and x-15 <xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 0
        
    if xloc < 50:
        xloc = 700
        ysize = randint(0,350)

    if x > xloc and x < xloc+5:
        score = score+1
    
    pygame.display.flip()
    clock.tick(time)
    time+=0.01


pygame.quit()
quit()
