'''
Created on Mar 29, 2013

@author: Dennis
'''
import pygame
import csv#from PIL import GIFImage
import random
import math

def load(savefile):
    with open(savefile, 'rt') as f:
        reader = csv.reader(f)
        save = list(reader)
        loadsavetext = save[0], save[2], save[4]
        return loadsavetext

def save(newsavearray):
    writer = csv.writer(open('Save1.csv', 'w'), delimiter=' ')
    writer.writerow([newsavearray[0]])
    writer.writerow([newsavearray[1]])
    writer.writerow([newsavearray[2]])


# pic = [image, x, y, x size, y size, x speed, y speed, direction]
# direction right = True, left = false

def draw(pic):
    if pic[7] == True:
        screen.blit(pygame.transform.scale(pic[0], (pic[3], pic[4])), (pic[1], pic[2]))
    else:
        screen.blit(pygame.transform.scale(pygame.transform.flip(pic[0], True, False), (pic[3], pic[4])), (pic[1], pic[2]))

def rowdraw(pic, row):
    if offscreen(pic, row, 0) == False:
        if pic[row][7] == True:
            screen.blit(pygame.transform.scale(pic[row][0], (pic[row][3], pic[row][4])), (pic[row][1], pic[row][2]))
        else:
            screen.blit(pygame.transform.scale(pygame.transform.flip(pic[row][0], True, False), (pic[row][3], pic[row][4])), (pic[row][1], pic[row][2]))

def corner_in_object(x, y, x21, y21, x22, y22):
    if x > x21 and x < x22 and y > y21 and y < y22:
        return True

def collision(object1, object2, offset):
    x1 = object1[1] + offset
    y1 = object1[2] + offset
    dimx1 = object1[3] - offset
    dimy1 = object1[4] - offset
    x2 = object2[1] + offset
    y2 = object2[2] + offset
    dimx2 = object2[3] - offset
    dimy2 = object2[4] - offset
    x11 = x1
    y11 = y1
    x12 = x1 + dimx1
    y12 = y1 + dimy1
    x21 = x2
    y21 = y2
    x22 = x2 + dimx2
    y22 = y2 + dimy2
    if corner_in_object(x11, y11, x21, y21, x22, y22):
        return True
    elif corner_in_object(x12, y11, x21, y21, x22, y22):
        return True
    elif corner_in_object(x11, y12, x21, y21, x22, y22):
        return True
    elif corner_in_object(x12, y12, x21, y21, x22, y22):
        return True
    elif corner_in_object(x21, y21, x11, y11, x12, y12):
        return True
    elif corner_in_object(x22, y21, x11, y11, x12, y12):
        return True   
    elif corner_in_object(x21, y22, x11, y11, x12, y12):
        return True
    elif corner_in_object(x22, y22, x11, y11, x12, y12):
        return True
    else:
        return False
    
def clicked(pic): # must go under a for event in pygame.event.get
        x = pic[1]
        y = pic[2]
        dim_x = pic[3]
        dim_y = pic[4]
        mouse_pos = pygame.mouse.get_pos()
        x_mouse = mouse_pos[0]
        y_mouse = mouse_pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if x_mouse > x and x_mouse < x + dim_x and y_mouse > y and y_mouse < y + dim_y:
                return True
            else:
                return False

def keys():
    global done
    global level
    global level_1_initialized
    global level_2_initialized
    global left
    global right
    global up
    global down
    global lr_just_pressed
    global ud_just_pressed
    global event
    global restartlevel
    global orangedead
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_BACKSPACE:
                level = 0
                level_1_initialized = False
                level_2_initialized = False
                
            if orangedead == False:
                if event.key == pygame.K_a: 
                    left = True
                    lr_just_pressed = 1
                if event.key == pygame.K_d:
                    right = True
                    lr_just_pressed = 2
                if event.key == pygame.K_w:
                    up = True
                    ud_just_pressed = 3
                if event.key == pygame.K_s:
                    down = True
                    ud_just_pressed = 4
            if event.key == pygame.K_SPACE:
                restartlevel = True
                down = False
        if event.type == pygame.KEYUP:
            if orangedead == False:
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_d:
                    right = False
                if event.key == pygame.K_w:
                    up = False
                if event.key == pygame.K_s:
                    down = False
            if event.key == pygame.K_SPACE:
                restartlevel = False
             
def move(pic, xs, ys):
    start_x = pic[1]
    start_y = pic[2]
    x_speed = xs
    y_speed = ys
    move_direction = pic[7]
    start_x = start_x + x_speed
    start_y = start_y + y_speed
    if x_speed < 0:
        move_direction = False
    elif x_speed > 0:
        move_direction = True
    return [pic[0], start_x, start_y, pic[3], pic[4], x_speed, y_speed, move_direction]

def rowmove(pic, row):
    start_x = pic[row][1]
    start_y = pic[row][2]
    x_speed = pic[row][5]
    y_speed = pic[row][6]
    move_direction = pic[row][7]
    start_x = start_x + x_speed
    start_y = start_y + y_speed
    if x_speed < 0:
        move_direction = False
    else:
        move_direction = True
    return [pic[row][0], start_x, start_y, pic[row][3], pic[row][4], x_speed, y_speed, move_direction]

def keymove(pic): # True is right;  Need to fix the coordinates of the diver with depth and scroll
    # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]  
    global Orangediver
    global depth
    global scroll
    global x_min
    global x_max
    global y_min
    global y_max
    
    global x_min_edge
    global x_max_edge
    global y_min_edge
    global y_max_edge
    
    global orangedead
    
    start_x = pic[1]
    start_y = pic[2]
    x_move_speed = pic[5]
    y_move_speed = pic[6]
    move_direction = pic[7]
    if left == True and right == False and x_min_edge == False:
        start_x = start_x - x_move_speed
        scroll = scroll - x_move_speed        
        move_direction = False
    elif right == True and left == False and x_max_edge == False:
        start_x = start_x + x_move_speed
        scroll = scroll + x_move_speed
        move_direction = True
    if up == True and down == False and y_min_edge == False:
        start_y = start_y - y_move_speed
        depth = depth - y_move_speed
    elif down == True and up == False and y_max_edge == False:
        start_y = start_y + y_move_speed
        depth = depth + y_move_speed

    if left == True and right == True:
        if lr_just_pressed == 1 and x_min_edge == False:
            start_x = start_x - x_move_speed
            scroll = scroll - x_move_speed
            move_direction = False
        elif lr_just_pressed == 2 and x_max_edge == False:
            start_x = start_x + x_move_speed
            scroll = scroll + x_move_speed
            move_direction = True
        
    if up == True and down == True:
        if ud_just_pressed == 3 and y_min_edge == False:
            start_y = start_y - y_move_speed
            depth = depth - y_move_speed
        elif ud_just_pressed == 4 and y_max_edge == False:
            start_y = start_y + y_move_speed
            depth = depth + y_move_speed
    
    if left == False and right == False:
        start_x = start_x
        scroll = scroll
    if up == False and down == False:
        start_y = start_y
        depth = depth
    
    if scroll < x_min + 1:
        #scroll = x_min
        x_min_edge = True
    else: x_min_edge =  False
    if scroll > x_max - 1:
        #scroll = x_max
        x_max_edge = True
    else: x_max_edge =  False
    if depth < y_min + 1:
        #depth = y_min
        y_min_edge = True
    else: y_min_edge =  False
    if depth > y_max - 1:
        #depth = y_max
        y_max_edge = True
    else: y_max_edge =  False
    
    return [pic[0], start_x, start_y, pic[3], pic[4], pic[5], pic[6], move_direction]

def animatedorange():
        global orangekicking
        global orangecycles
        global orangelength
        global Orangediver
        global Orangediverkick
        if orangekicking == False:
            Orangediverkick = [Orangediverkick[0], Orangediver[1], Orangediver[2], Orangediver[3], Orangediver[4], Orangediver[5], Orangediver[5], Orangediver[7]]
            draw(Orangediverkick)
            if orangecycles > orangelength:
                orangekicking = True
                orangecycles = 0
        else:
            draw(Orangediver)
            if orangecycles > orangelength:
                orangekicking = False
                orangecycles = 0
        orangecycles = orangecycles + 1
        
def animatedgreen():
        global greenkicking
        global greencycles
        global greenlength
        global Greendiver
        global Greendiverkick
        if greenkicking:
            Greendiverkick = [Greendiverkick[0], Greendiver[1], Greendiver[2], Greendiver[3], Greendiver[4], Greendiver[5], Greendiver[5], Greendiver[7]]
            draw(Greendiverkick)
            if greencycles > greenlength:
                greenkicking = False
                greencycles = 0
        else:
            draw(Greendiver)
            if greencycles > greenlength:
                greenkicking = True
                greencycles = 0
        greencycles = greencycles + 1

def binddiver():
    global Orangediver
    if Orangediver[1] > 1023 - Orangediver[3] - 100:
        Orangediver[1] = 1023 - Orangediver[3] - 100
        Orangediverkick[1] = 1023 - Orangediverkick[3] - 100
    if Orangediver[1] < 0 + 100:
        Orangediver[1] = 0 + 100
        Orangediverkick[1] = 0 + 100
    if Orangediver[2] > 767 - Orangediver[4] - 100:
        Orangediver[2] = 767 - Orangediver[4] - 100
        Orangediverkick[2] = 767 - Orangediverkick[4] - 100
    if Orangediver[2] < 0 + 100:
        Orangediver[2] = 0 + 100
        Orangediverkick[2] = 0 + 100
        
def bind(pic):
    x = pic[1]
    y = pic[2]
    xdim = pic[3]
    ydim = pic[4]

    if x > 1023 - xdim - 100:
        x = 1023 - xdim - 100
    if x < 0 + 100:
        x = 0 + 100
    if y > 767 - ydim - 100:
        y = 767 - ydim - 100
    if y < 0 + 100:
        y = 0 + 100
    return [pic[0], x, y, pic[3], pic[4], pic[5], pic[6], pic[7]]

def maxbinddiver():  # Not in use
    global x_max
    global y_max
    global x_min
    global y_min
    global depth
    global x_edge
    global y_edge
    x_edge = False
    y_edge = False
    if Orangediver[1] > x_max - Orangediver[3]:
        Orangediver[1] = x_max - Orangediver[3]
        Orangediverkick[1] = x_max - Orangediverkick[3]
        x_edge = True
    if Orangediver[1] < x_min:
        Orangediver[1] = x_min
        Orangediverkick[1] = x_min
        x_edge = True
    if Orangediver[2] > y_max - Orangediver[4]:
        Orangediver[2] = y_max - Orangediver[4]
        Orangediverkick[2] = y_max - Orangediverkick[4]
        depth = y_max - Orangediver[4]
        y_edge = True
    if Orangediver[2] < y_min:
        Orangediver[2] = y_min
        Orangediverkick[2] = y_min
        depth = y_min
        y_edge = True

def maxbind(pic):  # Not in use
    global x_max
    global y_max
    global x_min
    global y_min
    global scroll
    global depth
    global x_edge
    global y_edge
    x_edge = False
    y_edge = False
    x = scroll
    y = depth
    xdim = pic[3]
    ydim = pic[4]
    if x > x_max - xdim:
        x = x_max - xdim
        x_edge = True
    if x < x_min:
        x = x_min
        x_edge = True
    if y > y_max - ydim:
        y = y_max - ydim
        depth = y_max - ydim
        y_edge = True
    if y < y_min:
        y = y_min
        depth = y_min
        y_edge = True
    return [pic[0], x, y, pic[3], pic[4], pic[5], pic[6], pic[7]]

def movebackground(pic):  # Doesn't use the row system
    start_x = pic[1]
    start_y = pic[2]
    global Orangediver
    if Orangediver[1] > 1023 - Orangediver[3] - 100:
        start_x = start_x - Orangediver[5]
    if Orangediver[1] < 0 + 100:
        start_x = start_x + Orangediver[5]
    if Orangediver[2] > 767 - Orangediver[4] - 100:
        start_y = start_y - Orangediver[6]
    if Orangediver[2] < 0 + 100:
        start_y = start_y + Orangediver[6]
    return [pic[0], start_x, start_y, pic[3], pic[4], pic[5], pic[6], pic[7]]

def moveedges():      # Not in use
    global Orangediver
    global x_max
    global y_max
    global x_edge
    global y_edge
    if x_edge == False:
        if Orangediver[1] > 1023 - Orangediver[3] - 100:
            x_max = x_max - Orangediver[5]
        if Orangediver[1] < 0 + 100:
            x_max = x_max + Orangediver[5]
    if y_edge == False:
        if Orangediver[2] > 767 - Orangediver[4] - 100:
            y_max = y_max - Orangediver[6]
        if Orangediver[2] < 0 + 100:
            y_max = y_max + Orangediver[6]

def rowmovebackground(pic, row, following):
    start_x = pic[row][1]
    start_y = pic[row][2]
    global x_edge
    global y_edge
    if following[1] > 1023 - following[3] - 100:
        start_x = start_x - following[5]
    if following[1] < 0 + 100:
        start_x = start_x + following[5]
    if following[2] > 767 - following[4] - 100:
        start_y = start_y - following[6]
    if following[2] < 0 + 100:
            start_y = start_y + following[6]
    return [pic[row][0], start_x, start_y, pic[row][3], pic[row][4], pic[row][5], pic[row][6], pic[row][7]]

def greenfollow():
    global Orangediver
    global Greendiver
    global Greendiverkick
    if Orangediver[1] > Greendiver[1] + 224:
        Greendiver[7] = True
        Greendiver[1] = Orangediver[1] - 224
        Greendiverkick[7] = True
        Greendiverkick[1] = Orangediver[1] - 224
    if Orangediver[1] < Greendiver[1] - 224:
        Greendiver[7] = False
        Greendiver[1] = Orangediver[1] + 224
        Greendiverkick[7] = False
        Greendiverkick[1] = Orangediver[1] + 224
    if Orangediver[2] > Greendiver[2] + 188:
        Greendiver[2] = Orangediver[2] - 188
        Greendiverkick[2] = Orangediver[2] - 188
    if Orangediver[2] < Greendiver[2] - 188:
        Greendiver[2] = Orangediver[2] + 188  
        Greendiverkick[2] = Orangediver[2] + 188                      

    if Greendiver[1] < 0:
        Greendiver[1] = 0
        Greendiverkick[1] = 0
    if Greendiver[2] < 0:
        Greendiver[2] = 0
        Greendiverkick[2] = 0
    if Greendiver[1] > 1024-224:
        Greendiver[1] = 1024-224
        Greendiverkick[1] = 1024-224
    if Greendiver[2] > 768-188:
        Greendiver[2] = 768-188
        Greendiverkick[2] = 768-188

def movebubbles(pic, first, offstep):
    global bubblecycles
    if bubblecycles[first] == 0 + offstep:
        if pic[7] == False:
            Bubbles[first][1] = pic[1] + 55
            Bubbles[first][2] = pic[2] + 60 - 51
        else:
            Bubbles[first][1] = pic[1] - 55 + pic[3]
            Bubbles[first][2] = pic[2] + 60 - 51
    bubblecycles[first] = bubblecycles[first] + 1
    if bubblecycles[first] > 360:
        bubblecycles[first] = 0
    Bubbles[first][2] = Bubbles[first][2] - Bubbles[first][6]

    if bubblecycles[first + 1] == 90 + offstep:
        if pic[7] == False:
            Bubbles[first + 1][1] = pic[1] + 55
            Bubbles[first + 1][2] = pic[2] + 60 - 51
        else:
            Bubbles[first + 1][1] = pic[1] - 55 + pic[3]
            Bubbles[first + 1][2] = pic[2] + 60 - 51
    bubblecycles[first + 1] = bubblecycles[first + 1] + 1
    if bubblecycles[first + 1] > 455:
        bubblecycles[first + 1] = 90
    Bubbles[first + 1][2] = Bubbles[first + 1][2] - Bubbles[first + 1][6]

    if bubblecycles[first + 2] == 180 + offstep:
        if pic[7] == False:
            Bubbles[first + 2][1] = pic[1] + 55
            Bubbles[first + 2][2] = pic[2] + 60 - 51
        else:
            Bubbles[first + 2][1] = pic[1] - 55 + pic[3]
            Bubbles[first + 2][2] = pic[2] + 60 - 51
    bubblecycles[first + 2] = bubblecycles[first + 2] + 1
    if bubblecycles[first + 2] > 540:
        bubblecycles[first + 2] = 180
    Bubbles[first + 2][2] = Bubbles[first + 2][2] - Bubbles[first + 2][6]        

    if bubblecycles[first + 3] == 270 + offstep:
        if pic[7] == False:
            Bubbles[first + 3][1] = pic[1] + 55
            Bubbles[first + 3][2] = pic[2] + 60 - 51
        else:
            Bubbles[first + 3][1] = pic[1] - 55 + pic[3]
            Bubbles[first + 3][2] = pic[2] + 60 - 51
    bubblecycles[first + 3] = bubblecycles[first + 3] + 1
    if bubblecycles[first + 3] > 630:
        bubblecycles[first + 3] = 270
    Bubbles[first + 3][2] = Bubbles[first + 3][2] - Bubbles[first + 3][6]         

    for b in range(first, first + 4):
        Bubbles[b] = rowmovebackground(Bubbles, b, Orangediver)
        rowdraw(Bubbles, b)

def random_direction_move(pic, row, speed): # speed must be even
    sx = speed
    sy = speed
    c = random.randrange(1, 13)
    if c == 1:
        sx = speed/2
        sy = 0
    if c == 2:
        sx = 0
        sy = speed/2   
    if c == 3:
        sx = speed
        sy = 0 
    if c == 4:
        sx = speed
        sy = -speed/2
    if c == 5:
        sx = speed/2
        sy = -speed
    #if c == 6:
     #   sx = 0
      #  sy = speed
    if c == 7:
        sx = speed/2
        sy = -speed
    if c == 8:
        sx = speed
        sy = -speed/2
    if c == 9:
        sx = -speed
        sy = 0
    if c == 10:
        sx = -speed
        sy = speed/2
    if c == 11:
        sx = -speed/2
        sy = speed
    #if c == 12:
     #   sx = 0
      #  sy = -speed
    return [pic[row][0], pic[row][1], pic[row][2], pic[row][3], pic[row][4], sx, sy, pic[row][7]]

def outofbounds(pic, row, faroff):
    global x_min
    global x_max
    global y_min
    global y_max
    #newpic = rowmovebackground(pic, row)
    newpic = pic
    x = newpic[row][1]
    y = newpic[row][2]
    dimx = newpic[row][3]
    dimy = newpic[row][4]
    if x > x_max + faroff: return True
    if x < x_min -dimx - faroff: return True
    if y > y_max + faroff: return True
    if y < y_min - dimy - faroff: return True
    else: return False
    
def offscreen(pic, row, faroff):
    newpic = pic
    x = newpic[row][1]
    y = newpic[row][2]
    dimx = newpic[row][3]
    dimy = newpic[row][4]
    if x > 1023 + faroff: return True
    if x < 0 -dimx - faroff: return True
    if y > 767 + faroff: return True
    if y < 0 - dimy - faroff: return True
    else: return False
   
def rand_start_side(pic, row, offsides):
    dimx = pic[row][3]
    dimy = pic[row][4]
    side = random.randrange(1, 4)
    global y_min
    global y_max
    global x_min    
    global x_max
    # 1 is right, 2 is top, 3 is left, 4 is bottom
    if side == 1: # right
        x = x_max + dimx + offsides
        y = random.randrange(0, y_max - dimy)
    elif side == 2: # top
        x = random.randrange(x_min, x_max - dimx)
        y = y_min - dimy - offsides
    elif side == 3: # left
        x = x_min - dimx - offsides
        y = random.randrange(0, y_max - dimy)
    elif side == 4: # bottom
        x = random.randrange(x_min, x_max - dimx)
        y = y_max + dimy + offsides
    return [pic[row][0], x, y, pic[row][3], pic[row][4], pic[row][5], pic[row][6], pic[row][7]]

def multifish(pic, number):
    global greenrise
    for a in range(number):
        if outofbounds(pic, a, pic[a][3]):
            pic[a] = rand_start_side(pic, a, pic[a][3])
            pic[a] = random_direction_move(pic, a, 2*a + 2)
        if greenrise == False:
            pic[a] = rowmovebackground(pic, a, Orangediver)
        pic[a] = rowmove(pic, a)
        rowdraw(pic, a)
        
def restart_fish():
    global Eel
    global Clownfish
    global Dolphin
    global Lanturnfish
    global Jellyfish
    global Bubble
    global Bubbles
    global orangedead
    global greenrise
    orangedead = False
    greenrise = False
    
    Eel = [[pygame.image.load("Eel.png"), -1000, -1000, 100, 25, 6, 6, True],
           [pygame.image.load("Eel.png"), -1000, -1000, 100, 25, 6, 6, True],
           [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 6, 6, True],
           [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 6, 6, True]]
    
    Clownfish = [[pygame.image.load("Clownfish.png"), -1000, -1000, 200, 100, 4, 4, True],
                 [pygame.image.load("Clownfish.png"), -1000, -1000, 100, 50, 4, 4, True],
                 [pygame.image.load("Clownfish.png"), -1000, -1000, 50, 25, 4, 4, True],
                 [pygame.image.load("Clownfish.png"), -1000, -1000, 200, 100, 4, 4, True]]
    
    Dolphin = [[pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True],
               [pygame.image.load("Dolphin.png"), -1000, -1000, 300, 200, 8, 8, True],
               [pygame.image.load("Dolphin.png"), -1000, -1000, 500, 400, 8, 8, True],
               [pygame.image.load("Dolphin.png"), -1000, -1000, 100, 50, 8, 8, True]]
    
    Lanturnfish = [pygame.image.load("Lanturnfish.png"), 200, 200, 100, 100, 10, 10, True]
    Jellyfish = [pygame.image.load("Jellyfish.png"), 200, 200, 100, 100, 10, 10, True]
    Bubble = [pygame.image.load("Bubble.png"), 200, 200, 100, 100, 10, 10, True]
    
    Bubbles = [[pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True]]

def Level0():
    global level
    global Islandbutton
    global Treasuremap
    pygame.mouse.set_visible(1)
    draw(Treasuremap)
    Outerbanks = [Islandbutton[0], 220, 280, 50, 50, 0, 0, True]  # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Outerbanks)
    if clicked(Outerbanks):
        level = 1
        pygame.mouse.set_visible(0)
    Singapore = [Islandbutton[0], 750, 385, 50, 50, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Singapore)
    if clicked(Singapore):
        level = 2
        pygame.mouse.set_visible(0)

angle = 0
greentime = 0
greenrise = False
clasped = False

def Level1():
    global level_1_initialized
    global Coral1
    global Orangediver
    global Orangediverkick
    global Greendiver
    global Greendiverkick
    global orangekicking
    global greenkicking
    global scroll
    global depth
    global ocean
    global myfont  
    global x_min
    global x_max
    global y_min
    global y_max
    global y_max_edge
    global Bubbles
    global bubblecycles
    global angle
    global Lanturnfish
    global orangedead
    global Orangediverdead
    global up
    global down
    global left 
    global right
    global greentime
    global greenrise
 
    if level_1_initialized == False or restartlevel == True:
        greenkicking = True
        orangekicking = True
       
        restart_fish()
        down = False
        up = False
        left = False
        right = False
        
        level_1_initialized = True
        
        initial_Coral1_x = -200
        for n in range(10):
            Coral1[n][1] = initial_Coral1_x
            Coral1[n][2] = 2150
            initial_Coral1_x = initial_Coral1_x + 400
        
        initial_Rock5_y = -100
        for n in range(10):
            Rock5[n][1] = -200
            Rock5[n][2] = initial_Rock5_y
            initial_Rock5_y = initial_Rock5_y + 250
            
        initial_Rock5_y2 = -100
        for n in range(10, 20):
            Rock5[n][1] = 3675
            Rock5[n][2] = initial_Rock5_y2
            initial_Rock5_y2 = initial_Rock5_y2 + 250
        
        Treasurechest[0][1] = 2100
        Treasurechest[0][2] = 2245
                
        Orangediver = [pygame.image.load("Orangediver.png"), 200, 200, 224, 188, 10, 10, True]
        Orangediverkick = [pygame.image.load("Orangediverkick.png"), 200, 200, 224, 188, 10, 10, True]
        Greendiver = [pygame.image.load("Greendiver.png"), 0, 200, 224, 188, 10, 10, True]

        orangekicking = True
        orangecycles = 0
        orangelength = 20 
        bubblecycles = [0, 0, 0, 0, 0, 0, 0, 0]
        scroll = Orangediver[1]  
        depth = Orangediver[2]
        x_min = 0
        x_max = 3500
        y_min = 0
        y_max = 2000 + 100
        Orangediver[5] = 10
        Orangediver[6] = 10
        orangedead = False
    
    screen.fill(ocean)    
  
    if orangedead == False:
        Orangediver = keymove(Orangediver)
        movebubbles(Orangediver, 0, 0)
        greenfollow()
    elif greenrise == False:
        down = True
        up = False
        left = False
        right  = False
        Orangediver = keymove(Orangediver)
        Orangediver[0] = Orangediverdead[0]
        Orangediverkick[0] = Orangediverdead[0]
        if y_max_edge == True:
            greenrise = True
        greenfollow()
    elif greenrise == True:
        if collision(Greendiver, Orangediver, 180) == False:
            if Greendiver[1] < Orangediver[1] - 12:
                Greendiver[7] = True
                Greendiver = move(Greendiver, 2, 0)
            elif Greendiver[1] > Orangediver[1] + 12:
                Greendiver[7] = False
                Greendiver = move(Greendiver, -2, 0)
            if Greendiver[2] < Orangediver[2] - 12 + 50:
                Greendiver = move(Greendiver, 0, 2)
            elif Greendiver[2] > Orangediver[2] + 12 + 50:
                Greendiver = move(Greendiver, 0, -2)
        else:
            Greendiver[7] = Orangediver[7]
            Greendiver = move(Greendiver, 0, -5)
            Orangediver = move(Orangediver, 0, -5)
   
    movebubbles(Greendiver, 4, 40)
    for n in range(20):
        if greenrise == False:
            Rock5[n] = rowmovebackground(Rock5, n, Orangediver)
        rowdraw(Rock5, n)
    for n in range(10):
        if greenrise == False:
            Coral1[n] = rowmovebackground(Coral1, n, Orangediver)
        rowdraw(Coral1, n)
    if greenrise == False:
        Treasurechest[0] = rowmovebackground(Treasurechest, 0, Orangediver)
            
    rowdraw(Treasurechest, 0)
    rowdraw(Coral1, 5)

    multifish(Eel, 4)
    multifish(Clownfish, 4)
    multifish(Dolphin, 4)
        
    draw(Depthguage)
    
    draw(Needle)

    animatedgreen()
    
    if greenrise == False:
        binddiver()
    animatedorange()

    scrolltext = myfont.render(str(scroll), 1, (255, 255, 0))
    screen.blit(scrolltext, (1024 - 150 - 150, 10))
    depthtext = myfont.render(str(depth), 1, (255, 255, 0))
    screen.blit(depthtext, (1024 - 150, 10))
    
    for n in range(4):
        if collision(Eel[n], Orangediver, 75):
            orangedead = True
    
    if collision(Treasurechest[0], Orangediver, 50):
        if greenrise == False:
            Treasurechest[0][2] = Orangediver[2] + Orangediver[4]/2 - Treasurechest[0][4]/2 + 50
            Treasurechest[0][3] = 150
            Treasurechest[0][4] = 100
            if Orangediver[7]:
                Treasurechest[0][1] = Orangediver[1] + Orangediver[3]/2 - Treasurechest[0][3]/2 + 25
            else:
                Treasurechest[0][1] = Orangediver[1] + Orangediver[3]/2 - Treasurechest[0][3]/2 - 25
            
def Level2():
    global level_2_initialized
    global Coral1
    global Orangediver
    global Orangediverkick
    global Greendiver
    global Greendiverkick
    global orangekicking
    global greenkicking
    global scroll
    global depth
    global ocean
    global myfont  
    global x_min
    global x_max
    global y_min
    global y_max
    global y_max_edge
    global Bubbles
    global bubblecycles
    global angle
    global Lanturnfish
    global orangedead
    global Orangediverdead
    global up
    global down
    global left 
    global right
    global greentime
    global greenrise
 
    if level_2_initialized == False or restartlevel == True:
        greenkicking = True
        orangekicking = True
       
        restart_fish()
        down = False
        up = False
        left = False
        right = False
        
        level_2_initialized = True
        
        initial_Coral1_x = -200
        for n in range(10):
            Coral1[n][1] = initial_Coral1_x
            Coral1[n][2] = 2150
            initial_Coral1_x = initial_Coral1_x + 400
        
        initial_Rock5_y = -100
        for n in range(10):
            Rock5[n][1] = -200
            Rock5[n][2] = initial_Rock5_y
            initial_Rock5_y = initial_Rock5_y + 250
            
        initial_Rock5_y2 = -100
        for n in range(10, 20):
            Rock5[n][1] = 3675
            Rock5[n][2] = initial_Rock5_y2
            initial_Rock5_y2 = initial_Rock5_y2 + 250
        
        Treasurechest[0][1] = 2100
        Treasurechest[0][2] = 2245
                
        Orangediver = [pygame.image.load("Orangediver.png"), 200, 200, 224, 188, 10, 10, True]
        Orangediverkick = [pygame.image.load("Orangediverkick.png"), 200, 200, 224, 188, 10, 10, True]
        Greendiver = [pygame.image.load("Greendiver.png"), 0, 200, 224, 188, 10, 10, True]

        orangekicking = True
        orangecycles = 0
        orangelength = 20 
        bubblecycles = [0, 0, 0, 0, 0, 0, 0, 0]
        scroll = Orangediver[1]  
        depth = Orangediver[2]
        x_min = 0
        x_max = 3500
        y_min = 0
        y_max = 2000 + 100
        Orangediver[5] = 10
        Orangediver[6] = 10
        orangedead = False
    
    screen.fill(ocean)    
  
    if orangedead == False:
        Orangediver = keymove(Orangediver)
        movebubbles(Orangediver, 0, 0)
        greenfollow()
    elif greenrise == False:
        down = True
        up = False
        left = False
        right  = False
        Orangediver = keymove(Orangediver)
        Orangediver[0] = Orangediverdead[0]
        Orangediverkick[0] = Orangediverdead[0]
        if y_max_edge == True:
            greenrise = True
        greenfollow()
    elif greenrise == True:
        if collision(Greendiver, Orangediver, 180) == False:
            if Greendiver[1] < Orangediver[1] - 12:
                Greendiver[7] = True
                Greendiver = move(Greendiver, 2, 0)
            elif Greendiver[1] > Orangediver[1] + 12:
                Greendiver[7] = False
                Greendiver = move(Greendiver, -2, 0)
            if Greendiver[2] < Orangediver[2] - 12 + 50:
                Greendiver = move(Greendiver, 0, 2)
            elif Greendiver[2] > Orangediver[2] + 12 + 50:
                Greendiver = move(Greendiver, 0, -2)
        else:
            Greendiver[7] = Orangediver[7]
            Greendiver = move(Greendiver, 0, -5)
            Orangediver = move(Orangediver, 0, -5)
   
    movebubbles(Greendiver, 4, 40)
    for n in range(20):
        if greenrise == False:
            Rock5[n] = rowmovebackground(Rock5, n, Orangediver)
        rowdraw(Rock5, n)
    for n in range(10):
        if greenrise == False:
            Coral1[n] = rowmovebackground(Coral1, n, Orangediver)
        rowdraw(Coral1, n)
    if greenrise == False:
        Treasurechest[0] = rowmovebackground(Treasurechest, 0, Orangediver)
            
    rowdraw(Treasurechest, 0)
    rowdraw(Coral1, 5)

    multifish(Eel, 4)
    multifish(Clownfish, 4)
    multifish(Dolphin, 4)
        
    draw(Depthguage)
    
    draw(Needle)

    animatedgreen()
    
    if greenrise == False:
        binddiver()
    animatedorange()

    scrolltext = myfont.render(str(scroll), 1, (255, 255, 0))
    screen.blit(scrolltext, (1024 - 150 - 150, 10))
    depthtext = myfont.render(str(depth), 1, (255, 255, 0))
    screen.blit(depthtext, (1024 - 150, 10))
    
    for n in range(4):
        if collision(Eel[n], Orangediver, 75):
            orangedead = True
    
    if collision(Treasurechest[0], Orangediver, 50):
        if greenrise == False:
            Treasurechest[0][2] = Orangediver[2] + Orangediver[4]/2 - Treasurechest[0][4]/2 + 50
            Treasurechest[0][3] = 150
            Treasurechest[0][4] = 100
            if Orangediver[7]:
                Treasurechest[0][1] = Orangediver[1] + Orangediver[3]/2 - Treasurechest[0][3]/2 + 25
            else:
                Treasurechest[0][1] = Orangediver[1] + Orangediver[3]/2 - Treasurechest[0][3]/2 - 25
            
def nothing():
    cool = True
    return cool

#### Surface Variables #######################################################################
# list = [image, x, y, x size, y size, x speed, y speed, right]
Orangediver = [pygame.image.load("Orangediver.png"), 200, 200, 224, 188, 10, 10, True]
Orangediverkick = [pygame.image.load("Orangediver.png"), 200, 200, 224, 188, 10, 10, True]
Orangediverdead = [pygame.transform.flip(Orangediver[0], False, True), Orangediver[1], Orangediver[2], Orangediver[3], Orangediver[4], Orangediver[5], Orangediver[5], Orangediver[7]]

Greendiver = [pygame.image.load("Greendiver.png"), 0, 200, 224, 188, 10, 10, True]
Greendiverkick = [pygame.image.load("Greendiverkick.png"), 0, 200, 224, 188, 10, 10, True]

Eel = [[pygame.image.load("Eel.png"), -1000, -1000, 100, 25, 6, 6, True],
       [pygame.image.load("Eel.png"), -1000, -1000, 100, 25, 6, 6, True],
       [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 6, 6, True],
       [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 6, 6, True]]

Clownfish = [[pygame.image.load("Clownfish.png"), -1000, -1000, 200, 100, 4, 4, True],
             [pygame.image.load("Clownfish.png"), -1000, -1000, 100, 50, 4, 4, True],
             [pygame.image.load("Clownfish.png"), -1000, -1000, 50, 25, 4, 4, True],
             [pygame.image.load("Clownfish.png"), -1000, -1000, 200, 100, 4, 4, True]]

Dolphin = [[pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True],
           [pygame.image.load("Dolphin.png"), -1000, -1000, 300, 200, 8, 8, True],
           [pygame.image.load("Dolphin.png"), -1000, -1000, 500, 400, 8, 8, True],
           [pygame.image.load("Dolphin.png"), -1000, -1000, 100, 50, 8, 8, True]]

Lanturnfish = [pygame.image.load("Lanturnfish.png"), 200, 200, 100, 100, 10, 10, True]
Jellyfish = [pygame.image.load("Jellyfish.png"), 200, 200, 100, 100, 10, 10, True]
Bubble = [pygame.image.load("Bubble.png"), 200, 200, 100, 100, 10, 10, True]

Bubbles = [[pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 2, 2, True]]


Coral1 = [[pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True]]

Coral2 = [pygame.image.load("Coral2.png"), 200, 200, 100, 100, 10, 10, True]
Coral3 = [pygame.image.load("Coral3.png"), 200, 200, 100, 100, 10, 10, True]
Rock1 = [pygame.image.load("Rock1.png"), 200, 200, 100, 100, 10, 10, True]
Rock2 = [pygame.image.load("Rock2.png"), 200, 200, 100, 100, 10, 10, True]
Rock3 = [pygame.image.load("Rock3.png"), 200, 200, 100, 100, 10, 10, True]
Rock4 = [pygame.image.load("Rock4.png"), 200, 200, 100, 100, 10, 10, True]

Rock5 = [[pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True]]

Treasurechest = [[pygame.image.load("Treasurechest.png"), 200, 200, 250, 200, 10, 10, True]]

Sandcastle = [pygame.image.load("Sandcastle.png"), 0, 0, 6000, 768, 10, 0, True]
Seafloor = [pygame.image.load("Seafloor.png"), 0, 0, 6000, 768, 10, 0, True]
Undersea = [pygame.image.load("Undersea.png"), 0, 0, 1024, 768, 0, 0, True]
Bottomsea = [pygame.image.load("Bottomsea.png"), 0, 0, 1024, 768, 0, 0, True]

Bigback = [pygame.image.load("Bigback.png"), 0, 0, 6000, 6000, 10, 10, True]
Treasuremap = [pygame.image.load("Treasuremap.png"), 0, 0, 1024, 768, 10, 10, True]
Pressureguage = [pygame.image.load("Pressureguage.png"), 200, 200, 100, 100, 10, 10, True]
Depthguage = [pygame.image.load("Depthguage.png"), 0, 0, 200, 200, 0, 0, True]
Needle = [pygame.image.load("Needle.png"), 93, 93, 14, 100, 0, 0, True]

Islandbutton = [pygame.image.load("Islandbutton.png"), 200, 200, 100, 100, 10, 10, True]
Menubutton = [pygame.image.load("Menubutton.png"), 200, 200, 100, 100, 10, 10, True]
#### Surface Variables ###################################################################

pygame.init()
size=[1024,768]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Diver Test")
clock=pygame.time.Clock()
pygame.mouse.set_visible(1)

### Level 1 Variables ###########################################
level_1_initialized = False
#################################################################
### Level 2 Variables ###########################################
level_2_initialized = False
#################################################################
### Universal Variables #########################################
level = 0
done=False
left = False
right = False
up = False
down = False
lr_just_pressed = 0
ud_just_pressed = 0

greenkicking = True
greencycles = 0
greenlength = 20

orangekicking = True
orangecycles = 0
orangelength = 20

orangedead = False
depth = 0
scroll = 0
myfont = pygame.font.SysFont("monospace", 40, "bold")
#ocean = [135, 206, 250] 
ocean = [0, 100, 255] 
red = [255, 0, 0]

bubblecycles = [0, 0, 0, 0, 0, 0, 0, 0] # for more bubbles, add more zeros

restartlevel = False

x_max = 2000
y_max = 1000
x_min = -100
y_min = -100
x_min_edge = False
y_min_edge = False
x_max_edge = False
y_max_edge = False
#################################################################
# -------- Main Program Loop -----------
while done == False:
    keys()
################# Map Level 0 ###########################
    if level == 0:
        Level0()
            
##################################################################
################# Seafloor Level 1 ###############################
    if level == 1:
        Level1()
        
        
####################################################################
################# Sandcastle Level 2 ###############################
    if level == 2:
        Level2()
########################################################
####  END   ############################################   
    pygame.display.flip()
    clock.tick(30)
pygame.quit ()