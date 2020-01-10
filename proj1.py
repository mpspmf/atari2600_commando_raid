import pygame
import pygame.gfxdraw
import math
from random import randint

#colours
BROWN = (81, 52, 10)
DARK_BLUE = (89, 97, 219)
DARK_ORANGE = (204, 154, 71)
GREEN = (12, 78, 9)
GREY = (82, 82, 82)
LIGHT_BLUE = (104, 136, 204)
LIGHT_ORANGE = (224, 176, 90)
PURPLE = (131, 96, 217)
RED = (220, 86, 95) 
WHITE = (255, 255, 255)

#MESURES
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOUNT_WIDTH = 550
VALLEY_WIDTH = 40

#fundo
background = pygame.image.load('fundo.png')


#shots
pos_inicial = (400, 470)
angle = -90
tiros = []
n = 0
timer = 0

#casas-estado e coordenadas
#estado de cada casa varia entre 0 e 2
houses = [[0, (90, 415)],[0, (200, 415)],[0, (560, 415)],[0, (670, 415)]]

HOUSE_SIDE = 40
WINDOW_WIDTH = 7
HOUSE_DOOR_WIDTH = 6
HOUSE_DOOR_HEIGHT = 15

#new helicopter

heli = pygame.image.load('desenho12.png')
heli_v1 = pygame.image.load('image34.png')

heli1 = pygame.image.load('desenho13.png')
heli1_v1 = pygame.image.load('image35.png')

imagens = [heli, heli_v1]
imagens1 = [heli1, heli1_v1]

initial_counter = 300
initial_counter_decrease = 0.1

draw_heli_1 = True
draw_heli_2 = True
draw_delay_1 = 0 #200
draw_delay_2 = 0 #200
draw_delay_decrease = 0.1

heli_move = 0.13
heli_y_move = 1
heli_1_xpos = -50
heli_2_xpos = 800
heli_1_ypos = 60
change_pos = False

drop_1 = [randint(0, 1) for _ in range(4)]
drop_2 = [randint(0, 1) for _ in range(4)]

pd1 = True
pd1 = True

#paraquedista

move_jumper = 0.040
draw_list1=[]
draw_list2=[]
jumper_y = 60
drop1 = 0

jumper = pygame.image.load('p4.png')

#avião e bomba

plane = pygame.image.load('image18.png')
bomb = pygame.image.load('image65.png')

plane_delay = 30 #número de paraquedistas
plane_draw = False
plane_xpos = 800

bomb_draw = False
bomb_ypos = 90

#tunel
tunel = [0 for _ in range(5)]
explosion_timer = 0
explosion_timer_increase = 0.1

draw_special_tunel1 = 0
draw_special_tunel2 = 0

#helicóptero mover hélices
TIME_PER_FRAME = 50

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Commando Raid') 

  
#pontuação
score = 0
myfont = pygame.font.SysFont("monospace", 20)
myfont1 = pygame.font.SysFont("monospace", 40)
  


#image.set_colorkey

def overlaps(x1, y1, w1, h1, x2, y2, w2, h2):
    return not (x1+w1 < x2 or x1 > x2+w2 or y1+h1 < y2 or y1 > y2+h2)

while running == True:
    dt = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    tempo = pygame.time.get_ticks()
    frame_atual = (tempo // TIME_PER_FRAME) % len(imagens)
    
    if score > 1500:
        heli_y_move = 1.3
        heli_move = 0.16
        move_jumper = 0.055
    if score > 3000:
        heli_y_move = 1.6
        heli_move = 0.2
        move_jumper = 0.07
    #céu
    pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, 800, 155))
    pygame.draw.rect(screen, DARK_BLUE, (0, 155, 800, 100))
    pygame.draw.rect(screen, PURPLE, (0, 255, 800, 85))
    pygame.draw.rect(screen, RED, (0, 340, 800, 100))
    pygame.draw.rect(screen, DARK_ORANGE, (0, 400, 800, 300))
    pygame.draw.rect(screen, LIGHT_ORANGE, (0, 450, 800, 500))
    screen.blit(background, (0, 0))


    #canhão
    if tunel[2] != 1:
        pygame.draw.circle(screen, GREY, (SCREEN_WIDTH//2, 490), 20)
        pygame.draw.circle(screen, (224, 176, 90), (SCREEN_WIDTH//2, 492), 5)
    
    #montanhas
    screen.set_clip(0, 455, SCREEN_WIDTH, 600-455)
    pygame.draw.ellipse(screen, BROWN, (SCREEN_WIDTH//2+VALLEY_WIDTH-MOUNT_WIDTH, 450, MOUNT_WIDTH, 200))
    pygame.draw.ellipse(screen, BROWN, (SCREEN_WIDTH//2-VALLEY_WIDTH, 450, MOUNT_WIDTH, 200))
    pygame.draw.rect(screen, BROWN, (0, SCREEN_HEIGHT-50, SCREEN_WIDTH, 50))
    screen.set_clip(None)
     
    #casas
    for i in houses:
        if i[0] == 0:
            pygame.draw.rect(screen, GREEN, (i[1][0], i[1][1], HOUSE_SIDE, HOUSE_SIDE))
            pygame.draw.rect(screen, WHITE, (i[1][0]+WINDOW_WIDTH, i[1][1]+WINDOW_WIDTH, WINDOW_WIDTH, WINDOW_WIDTH))
            pygame.draw.rect(screen, WHITE, (i[1][0]+HOUSE_SIDE-2*WINDOW_WIDTH, i[1][1]+WINDOW_WIDTH, WINDOW_WIDTH, WINDOW_WIDTH))
            pygame.draw.rect(screen, WHITE, (i[1][0]+WINDOW_WIDTH, i[1][1]+HOUSE_SIDE-2*WINDOW_WIDTH, WINDOW_WIDTH-2, WINDOW_WIDTH))
            pygame.draw.rect(screen, WHITE, (i[1][0]+HOUSE_SIDE-2*WINDOW_WIDTH+2, i[1][1]+HOUSE_SIDE-2*WINDOW_WIDTH, WINDOW_WIDTH-2, WINDOW_WIDTH))
            pygame.draw.rect(screen, GREY, (i[1][0]+HOUSE_SIDE/2-HOUSE_DOOR_WIDTH/2, i[1][1]+HOUSE_SIDE-HOUSE_DOOR_HEIGHT, HOUSE_DOOR_WIDTH, HOUSE_DOOR_HEIGHT))
            pygame.gfxdraw.filled_polygon(screen, ((i[1][0], i[1][1]),(i[1][0]+HOUSE_SIDE//2, i[1][1]-HOUSE_SIDE//4),(i[1][0]+HOUSE_SIDE-1, i[1][1])), GREEN)
        elif i[0] == 1:
            pygame.draw.rect(screen, GREEN, (i[1][0], i[1][1], HOUSE_SIDE, HOUSE_SIDE))
            pygame.draw.rect(screen, WHITE, (i[1][0]+WINDOW_WIDTH, i[1][1]+WINDOW_WIDTH, WINDOW_WIDTH, WINDOW_WIDTH))
            pygame.draw.rect(screen, WHITE, (i[1][0]+HOUSE_SIDE-2*WINDOW_WIDTH, i[1][1]+WINDOW_WIDTH, WINDOW_WIDTH, WINDOW_WIDTH))
            pygame.draw.rect(screen, WHITE, (i[1][0]+WINDOW_WIDTH, i[1][1]+HOUSE_SIDE-2*WINDOW_WIDTH, WINDOW_WIDTH-2, WINDOW_WIDTH))
            pygame.draw.rect(screen, WHITE, (i[1][0]+HOUSE_SIDE-2*WINDOW_WIDTH+2, i[1][1]+HOUSE_SIDE-2*WINDOW_WIDTH, WINDOW_WIDTH-2, WINDOW_WIDTH))
            pygame.draw.rect(screen, GREY, (i[1][0]+HOUSE_SIDE/2-HOUSE_DOOR_WIDTH/2, i[1][1]+HOUSE_SIDE-HOUSE_DOOR_HEIGHT, HOUSE_DOOR_WIDTH, HOUSE_DOOR_HEIGHT))
            pygame.draw.rect(screen, DARK_ORANGE, (i[1][0]+1, i[1][1]+3, 8, 14))
            pygame.draw.rect(screen, DARK_ORANGE, (i[1][0]+25, i[1][1]+20, 8, 14))
            pygame.gfxdraw.filled_polygon(screen, ((i[1][0], i[1][1]),(i[1][0]+HOUSE_SIDE//2, i[1][1]-HOUSE_SIDE//4),(i[1][0]+HOUSE_SIDE/2+10, i[1][1]-HOUSE_SIDE/6), (i[1][0]+HOUSE_SIDE/2+10, i[1][1])), GREEN)
        elif i[0] == 2:
            pygame.draw.rect(screen, GREEN, (i[1][0], i[1][1], HOUSE_SIDE, HOUSE_SIDE))
            pygame.draw.rect(screen, WHITE, (i[1][0]+WINDOW_WIDTH, i[1][1]+WINDOW_WIDTH, WINDOW_WIDTH, WINDOW_WIDTH))
            pygame.draw.rect(screen, WHITE, (i[1][0]+HOUSE_SIDE-2*WINDOW_WIDTH, i[1][1]+WINDOW_WIDTH, WINDOW_WIDTH, WINDOW_WIDTH))
            pygame.draw.rect(screen, WHITE, (i[1][0]+WINDOW_WIDTH, i[1][1]+HOUSE_SIDE-2*WINDOW_WIDTH, WINDOW_WIDTH-2, WINDOW_WIDTH))
            pygame.draw.rect(screen, WHITE, (i[1][0]+HOUSE_SIDE-2*WINDOW_WIDTH+2, i[1][1]+HOUSE_SIDE-2*WINDOW_WIDTH, WINDOW_WIDTH-2, WINDOW_WIDTH))
            pygame.draw.rect(screen, GREY, (i[1][0]+HOUSE_SIDE/2-HOUSE_DOOR_WIDTH/2, i[1][1]+HOUSE_SIDE-HOUSE_DOOR_HEIGHT, HOUSE_DOOR_WIDTH, HOUSE_DOOR_HEIGHT))
            pygame.draw.rect(screen, DARK_ORANGE, (i[1][0]+1, i[1][1]+3, 8, 14))
            pygame.draw.rect(screen, DARK_ORANGE, (i[1][0]+25, i[1][1]+20, 8, 14))
            #pygame.gfxdraw.filled_polygon(screen, ((i[1][0], i[1][1]),(i[1][0]+HOUSE_SIDE//2, i[1][1]-HOUSE_SIDE//4),(i[1][0]+HOUSE_SIDE/2+10, i[1][1]-HOUSE_SIDE/6), (i[1][0]+HOUSE_SIDE/2+10, i[1][1])), GREEN)
            pygame.draw.rect(screen, DARK_ORANGE, (i[1][0]+15, i[1][1] -10, 3, 10))
            pygame.draw.rect(screen, DARK_ORANGE, (i[1][0]+10, i[1][1]+20, 7, 9))
            pygame.draw.rect(screen, DARK_ORANGE, (i[1][0]+25, i[1][1]+5, 9, 4))
            
            
    
    #mover o canhão
    
    keys = pygame.key.get_pressed()
    if tunel[2] != 1:
        if keys[pygame.K_LEFT] and angle >= -145:
            angle += -0.2 * dt
        if keys[pygame.K_RIGHT] and angle <= -35:
            angle += 0.2 * dt
    
    pos_final = (400 + 20 * math.cos(angle * math.pi/180),470 + 20 * math.sin(angle * math.pi/180))
    if tunel[2] != 1:
        pygame.draw.line(screen, GREY, pos_inicial, pos_final, 5)
    
    #tiros
    if tunel[2] != 1:
        if timer>0:
            timer = timer - 0.015
        if keys[pygame.K_SPACE] and timer <= 0:
            timer = 0.5
            tiros.append([list(pos_final), angle])
            
         
            
    for i in tiros:
        if 0 < i[0][0] < 800 and 0 < i[0][1] < 600:
            i[0] = [i[0][0]+math.cos(i[1] * math.pi/180)*dt, i[0][1]+math.sin(i[1] * math.pi/180)*dt]
            
            pos_final_tiro = (i[0][0] + 7 * math.cos(i[1] * math.pi/180),i[0][1]+ 7 * math.sin(i[1] * math.pi/180))
            pygame.draw.line(screen, GREY, (i[0][0], i[0][1]), pos_final_tiro, 5)
        else:
            tiros.remove(i)
            
            
    #helicopter
    pd1 = False
    pd2 = False
    
    if initial_counter > 0:
        initial_counter -= initial_counter_decrease * dt
    
    else:
        
        #draw and move heli 1
        if draw_delay_1 > 0:
            draw_delay_1 -= draw_delay_decrease * dt
            
        if heli_1_xpos < 800 and draw_heli_1 == True and draw_delay_1 <= 0:
            heli_1_xpos +=  heli_move * dt
            pd1 = True
            #screen.blit(heli,(heli_1_xpos, heli_1_ypos))
            
        elif tunel[2] != 1:
            heli_1_xpos = -50
            if (heli_1_xpos + 150 >= heli_2_xpos) and draw_heli_2 == True:
                heli_1_ypos = 10
            else:
                heli_1_ypos = 60
            
            draw_heli_1 = True
            drop_1 = [randint(0, 1) for _ in range(4)]

#draw and move heli 2
        if draw_delay_2 > 0:
            draw_delay_2 -= draw_delay_decrease * dt
            
        if heli_2_xpos > -50 and draw_heli_2 == True and draw_delay_2 <= 0:
            heli_2_xpos -=  heli_move * dt
            pd2 = True
            #screen.blit(heli1,(heli_2_xpos, 60))
            
        elif tunel[2] != 1:
            heli_2_xpos = 800
            draw_heli_2 = True        
            drop_2 = [randint(0, 1) for _ in range(4)]
            
        if ((heli_1_xpos + 150 > heli_2_xpos and heli_1_xpos -140 < heli_2_xpos) or (heli_1_xpos + 150 > 800 and heli_2_xpos < 100)) and draw_heli_1 == True:
            change_pos = True
        else:
            change_pos = False
            
        if change_pos == True:
            if heli_1_ypos > 10:
                heli_1_ypos -= heli_y_move
        else:
            if heli_1_ypos < 60:
                heli_1_xpos -= heli_move * dt
                heli_1_ypos += heli_y_move
                
        if pd1:
            screen.blit(imagens[frame_atual], (heli_1_xpos, heli_1_ypos))
            #screen.blit(heli,(heli_1_xpos, heli_1_ypos))
        if pd2:
            screen.blit(imagens1[frame_atual], (heli_2_xpos, 60))
            #screen.blit(heli1,(heli_2_xpos, 60))
    
            
            
#paraquedista 
        
    for i in range(4):
        if heli_1_xpos > houses[i][1][0] and drop_1[i] == 1 and pd1 == True and tunel[2] != 1:
            draw_list1.append([houses[i][1][0], 60])
            drop_1[i] = 0
            if plane_delay == 0 and plane_draw == False:
                plane_draw = True
            else:
                plane_delay -= 1
            
    for i in range(3, -1, -1):
        if heli_2_xpos < houses[i][1][0]+40 and drop_2[i] == 1 and pd2 == True and tunel[2] != 1:
            draw_list2.append([houses[i][1][0]+11, 60])
            drop_2[i] = 0
            if plane_delay == 0 and plane_draw == False:
                plane_draw = True
            else:
                plane_delay -= 1
            
    #tunel
    
    a = draw_list1.copy()  
    b = draw_list2.copy()      
    for i in a:
        if i[1] > 405:
            #draw_list1.remove(i)
            if i[0]<120 :
                if houses[0][0] < 2:
                    houses[0][0] += 1
                else:
                    if tunel[0] < 2:
                        tunel[0] += 1
                    elif tunel[0] == 2 and tunel[1] == 0 :
                        if draw_special_tunel1 == 0:
                            draw_special_tunel1 = 1
                        else:
                            tunel[2] = 1
                    elif tunel[0] == 2 and tunel[1] == 1:
                        tunel[1] += 1
                    elif tunel[0] == 2 and tunel[1] == 2:
                        tunel[2] = 1
                        
            elif i[0] < 250 :
                
                if houses[1][0] < 2:
                    houses[1][0] += 1
                else:
                    if tunel[1] < 2:
                        tunel[1] += 1
                    elif tunel[1] == 2:
                        tunel[2] = 1
                        
            elif i[0]<600 :
                if houses[2][0] < 2:
                    houses[2][0] += 1
                else:
                    
                    if tunel[3] < 2:
                        tunel[3] += 1
                    elif tunel[3] == 2:
                        tunel[2] = 1
                        
            elif i[0]<800 :
                if houses[3][0] < 2:
                    houses[3][0] += 1
                else:
                    
                    if tunel[4] < 2:
                        tunel[4] += 1
                    elif tunel[4] == 2 and tunel[3] == 0 :
                        if draw_special_tunel2 == 0:
                            draw_special_tunel2 = 1
                        else:
                            tunel[2] = 1
                    elif tunel[4] == 2 and tunel[3] == 1:
                        tunel[3] += 1
                    elif tunel[4] == 2 and tunel[3] == 2:
                        tunel[2] = 1
                        
            draw_list1.remove(i)
            
            
    for i in b:
        if i[1] > 405:
            #draw_list1.remove(i)
            if i[0]<120 :
                if houses[0][0] < 2:
                    houses[0][0] += 1
                else:
                    if tunel[0] < 2:
                        tunel[0] += 1
                    elif tunel[0] == 2 and tunel[1] == 0 :
                        if draw_special_tunel1 == 0:
                            draw_special_tunel1 = 1
                        else:
                            tunel[2] = 1
                    elif tunel[0] == 2 and tunel[1] == 1:
                        tunel[1] += 1
                    elif tunel[0] == 2 and tunel[1] == 2:
                        tunel[2] = 1
                        
            elif i[0] < 250 :
                
                if houses[1][0] < 2:
                    houses[1][0] += 1
                else:
                    if tunel[1] < 2:
                        tunel[1] += 1
                    elif tunel[1] == 2:
                        tunel[2] = 1
                        
            elif i[0]<600 :
                if houses[2][0] < 2:
                    houses[2][0] += 1
                else:
                    
                    if tunel[3] < 2:
                        tunel[3] += 1
                    elif tunel[3] == 2:
                        tunel[2] = 1
                        
            elif i[0]<800 :
                if houses[3][0] < 2:
                    houses[3][0] += 1
                else:
                    if tunel[4] < 2:
                        tunel[4] += 1
                    elif tunel[4] == 2 and tunel[3] == 0:
                        if draw_special_tunel2 == 0 :
                            draw_special_tunel2 = 1
                        else: 
                            tunel[2] = 1
                    elif tunel[4] == 2 and tunel[3] == 1:
                        tunel[3] += 1
                    elif tunel[4] == 2 and tunel[3] == 2:
                        tunel[2] = 1    
            draw_list2.remove(i)
              
    
    for i in draw_list1:
        i[1] += move_jumper * dt
        #pygame.draw.rect(screen, GREY, (i[0], i[1], 20, 40))
        screen.blit(jumper, (i[0], i[1]+10))
        
    for i in draw_list2:
        i[1] += move_jumper * dt
        #pygame.draw.rect(screen, GREY, (i[0], i[1], 20, 40))
        screen.blit(jumper, (i[0], i[1]+10))
        
        
    #colisão tiro helicopter e paraquedista
    
    for i in tiros:
        if overlaps(heli_1_xpos, heli_1_ypos, 56, 27, i[0][0], i[0][1], 4, 4):
            draw_heli_1 = False
            tiros.remove(i)
            draw_delay_1 = 100
            score += 100
        
    for i in tiros:
        if overlaps(heli_2_xpos, 60 ,56, 27, i[0][0], i[0][1], 4, 4):
            draw_heli_2 = False
            tiros.remove(i)
            draw_delay_2 = 100
            score += 100
    for i in tiros:
        for k in draw_list1:
            if overlaps(k[0], k[1], 30, 35,i[0][0], i[0][1], 4, 4):
                tiros.remove(i)
                draw_list1.remove(k)
                score += 50
                
    for i in tiros:
        for k in draw_list2:
            if overlaps(k[0], k[1], 30, 35,i[0][0], i[0][1], 4, 4):
                tiros.remove(i)
                draw_list2.remove(k)     
                score += 50
     
    #avião e bomba
    if tunel[2] != 1:
        if plane_draw:
            if plane_xpos < -100:
                plane_xpos = 800
                plane_draw = False
                plane_delay = 25
            else:
                plane_xpos -= dt * heli_move * 1.5
                screen.blit(plane, (plane_xpos, 90))
                
                if plane_xpos < 380 and bomb_draw == False:
                    bomb_draw = True
        if bomb_draw:
            bomb_ypos += move_jumper * dt * 1.5
            screen.blit(bomb, (390, bomb_ypos))
            
            if bomb_ypos > 430:
                bomb_draw = False
                bomb_ypos = 90
            
    #colisão avião-tiro bomba-tiro
    for i in tiros:
        if overlaps(plane_xpos, 90, 75, 25, i[0][0], i[0][1], 4, 4) and plane_draw == True:
            tiros.remove(i)
            plane_draw = False
            plane_xpos = 800
            plane_delay = 25
            score += 200
        
        elif overlaps(390, bomb_ypos, 24, 21, i[0][0], i[0][1], 4, 4) and bomb_draw == True:
            tiros.remove(i)
            bomb_draw = False
            bomb_ypos = 90
            score += 150
            
    #túnel desenhar

    for k,i in enumerate(tunel):
        
        if k == 0 and i == 1:
            pygame.draw.rect(screen, LIGHT_ORANGE, (100, 455, 20, 60))
        elif k == 0 and i == 2:
            pygame.draw.rect(screen, LIGHT_ORANGE, (100, 455, 20, 60))
            pygame.draw.rect(screen, LIGHT_ORANGE, (100, 515, 130, 20))   
        if k == 1 and i == 1:
            pygame.draw.rect(screen, LIGHT_ORANGE, (210, 455, 20, 60))
        elif k == 1 and i == 2:
            pygame.draw.rect(screen, LIGHT_ORANGE, (210, 455, 20, 60))
            pygame.draw.rect(screen, LIGHT_ORANGE, (210, 515, 180, 20))
        if k == 2 and i == 1:
            pygame.draw.rect(screen, LIGHT_ORANGE, (390, 515, 20, 25))
            pygame.draw.rect(screen, LIGHT_ORANGE, (395, 540, 10, 4))
            pygame.draw.rect(screen, LIGHT_ORANGE, (395, 495, 10, 20))
        
        if k == 3 and i == 1:
            pygame.draw.rect(screen, LIGHT_ORANGE, (570, 455, 20, 60))
        elif k == 3 and i == 2:
            pygame.draw.rect(screen, LIGHT_ORANGE, (570, 455, 20, 60))
            pygame.draw.rect(screen, LIGHT_ORANGE, (410, 515, 180, 20))
        
        if k == 4 and i == 1:
            pygame.draw.rect(screen, LIGHT_ORANGE, (680, 455, 20, 60))
        elif  k == 4 and i == 2:
            pygame.draw.rect(screen, LIGHT_ORANGE, (680, 455, 20, 60))
            pygame.draw.rect(screen, LIGHT_ORANGE, (570, 515, 130, 20))
        if draw_special_tunel1 == 1:
            pygame.draw.rect(screen, LIGHT_ORANGE, (210, 515, 180, 20))
        if draw_special_tunel2 == 1:
            pygame.draw.rect(screen, LIGHT_ORANGE, (410, 515, 180, 20))
            
            
    #pontuação
    if tunel[2] != 1:
        scoretext = myfont.render("Score = "+str(score), 1, BROWN)
        screen.blit(scoretext, (300, 10))
    
    #explosão final
    
    if tunel[2] == 1:
        explosion_timer += explosion_timer_increase * dt
        
        if explosion_timer < 50:
            pygame.draw.rect(screen, RED, (0, 0, 800, 455, ))
        elif 100 < explosion_timer < 150:
            pygame.draw.rect(screen, WHITE, (0, 0, 800, 455, ))
        elif 200 < explosion_timer < 225:
            pygame.draw.rect(screen, RED, (0, 0, 800, 455, ))
        else:
            scoretext = myfont1.render("Score = "+str(score), 1, BROWN)
            screen.blit(scoretext, (250, 100))
            
        
    
            
    pygame.display.flip()
pygame.display.quit()
pygame.quit()