from pickle import HIGHEST_PROTOCOL
from turtle import width
import pygame
import random
pygame.init()
width = 900
height = 500
white = (255,255,255)
red = (255,0,0)
green = (0,255,26)
black = (0,0,0)
yellow = (239,255,0)
clock = pygame.time.Clock()
# TITLE
gamewindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("SNAKES_ZILLA")

font = pygame.font.SysFont(None,55)
def text_Screen(text,colour,x,y):
    screen_text = font.render(text,True,colour)
    gamewindow.blit(screen_text,[x,y])
def plot_snake(gamewindow,colour,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,black,[x,y,snake_size,snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(red)
        text_Screen("Welcome to snakes zilla!!",black,170,220)
        clock.tick(60)    
        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    gameloop()    

def gameloop():
    exit_game = False
    game_over = False 
    snk_list = []
    snk_length = 1
    score = 0
    #EVENT
    speed = 6
    velocity_x = 0
    velocity_y = 0
    snake_x = 45
    snake_y = 40
    snake_size = 15
    fps =30
    food_x = random.randint(20,width/2)
    food_y = random.randint(20,height/2)
    with open("hiscore.txt","r") as f:
        hiscore = f.read()

    while not exit_game:
        # snake_x += 0.1
        if game_over == True:
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))
            gamewindow.fill(black) 
            text_Screen("Game Over! Your score:"+str(score),white,170,220)
            pygame.display.update() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x += speed
                        velocity_y = 0
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x -= speed
                        velocity_y = 0
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y -= speed
                        velocity_x = 0
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y += speed
                        velocity_x = 0
            
            
            gamewindow.fill(yellow)   
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            #snake body*****************************************************8
            plot_snake(gamewindow,black,snk_list,snake_size)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size]) 
            snake_x += velocity_x
            snake_y += velocity_y
            text_Screen("Your score is: "+ str(score),red,5,5)
            text_Screen("hiscore: "+ str(hiscore),red,650,5) 
            if abs(snake_x - food_x)<6 and ( snake_y - food_y)<6:
                score+=10
                snk_length += 5
                food_x = random.randint(20,width/2)
                food_y = random.randint(20,height/2)
                speed =speed + 0.01
            if score>=int(hiscore):
                hiscore = score
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True    
            if snake_x<0 or snake_x>width or snake_y<0 or snake_y>height:
                game_over = True
            clock.tick(fps)    
            pygame.display.update()       
    #QUITING
    pygame.display.quit()
    quit()                
# gameloop()
welcome()