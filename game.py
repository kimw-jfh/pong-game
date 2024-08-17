import pygame
import sys    
import random

# === set display ===
pygame.init()
display=pygame.display.set_mode((800,400))  # WIDTH , HEIGHT =800,400
pygame.display.set_caption("Pong Game")    # Game Title

delay_harif = 500
lastmovetime = 0
harif_direction = random.choice([-5, 5])


# === color ===
white=(255, 255, 255) # RGB
pink=(204, 0, 102)
blue=(19, 16, 205)
light_blue = (112,146,190)

# === font ===
font= pygame.font.Font(None,36)

# === speed ===
paddle_speed=7
ball_speed=5

# === create paddles and ball ===
harif=pygame.Rect(20, 170, 10, 60)    # PADDLE_WIDTH=10 , PADDLE_HEIGHT=60
player=pygame.Rect(770, 170, 10, 60)
ball= pygame.Rect(390, 190, 20, 20)

ball_xd= ball_speed
ball_yd= ball_speed

# === setting the speed of the game ===                     
clock=pygame.time.Clock()



# === location of scores ===
player_score=0
harif_score=0
def show_score(Surface, str, color, which):
    str_object= font.render(str, True, color)   # true for sharpness
    position= list(str_object.get_size())
    if which:
        position[0]=400-position[0]-20
    else: 
        position[0]=400+20   
    Surface.blit(str_object, position)

# === event, keys, movement ===
collision=False    
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys= pygame.key.get_pressed() 
    if keys[pygame.K_UP] and player.top>=0 :
        player.y-=paddle_speed
    if keys[pygame.K_DOWN] and player.bottom<=400:
        player.y+=paddle_speed

# === ball movement ===
    if ball.bottom>=400 or ball.top<=0:
        ball_yd*=-1

    if (ball.colliderect(player) and not collision) or (ball.colliderect(harif) and collision):
        ball_xd*=-1 
        collision= not collision 

    ball.x+=ball_xd
    ball.y+=ball_yd   

    if ball.right>player.center[0] :
        harif_score+=1
        ball.x , ball.y = 390,190

    elif ball.left<harif.center[0] :
        player_score+=1
        ball.x , ball.y = 390,190
        

        
    intime = pygame.time.get_ticks()
    if intime - lastmovetime > delay_harif:
        lastmovetime = intime
        if harif.center[1] < ball.center[1] and harif.bottom<400 :
            harif.y += harif_direction * paddle_speed +60
        if harif.center[1] > ball.center[1] and harif.top>0:
            harif.y -= harif_direction * paddle_speed +60
        harif_direction *= -1  # change direction after each move

    
    # if harif.top < 0:
    #     harif.y = 60
    # if harif.bottom > 400:
    #     harif.y = 400 - 60


                         
    display.fill(light_blue) # background color

    show_score(display,str(harif_score) , white, True)  
    show_score(display, str(player_score) , white, False)

    # braye nmayesh
    pygame.draw.ellipse(display, blue, ball) 
    pygame.draw.rect(display,pink,player)  
    pygame.draw.rect(display,pink,harif)
    pygame.draw.line(display, white ,(400,0),(400,400))  

    pygame.display.update()    # add end of loop

    clock.tick(60) # for speed  



