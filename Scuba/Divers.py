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

def fancycollision(object1, object2, ox1, oy1, ox2, oy2, offset):
    x1 = object1[1]
    y1 = object1[2]
    x2 = object2[1]
    y2 = object2[2]
    
    x11 = x1 + ox1 - offset
    y11 = y1 + oy1 - offset
    x12 = x1 + ox1 + offset
    y12 = y1 + oy1 + offset
    
    x21 = x2 + ox2 - offset
    y21 = y2 + oy2 - offset
    x22 = x2 + ox2 + offset
    y22 = y2 + oy2 + offset
    
    
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
def mouseover(pic): # must go under a for event in pygame.event.get
        x = pic[1]
        y = pic[2]
        dim_x = pic[3]
        dim_y = pic[4]
        mouse_pos = pygame.mouse.get_pos()
        x_mouse = mouse_pos[0]
        y_mouse = mouse_pos[1]
        if x_mouse > x and x_mouse < x + dim_x and y_mouse > y and y_mouse < y + dim_y:
            return True
        else:
            return False

def rowclicked(pic, row): # must go under a for event in pygame.event.get
        x = pic[row][1]
        y = pic[row][2]
        dim_x = pic[row][3]
        dim_y = pic[row][4]
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
    global level_initialized
    global level_1_initialized
    global level_2_initialized
    global left
    global right
    global up
    global down
    global lr_just_pressed
    global ud_just_pressed
    global event
    global orangedead
    global airRate
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT+1 and orangedead == False:
            consumeAir() 
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_BACKSPACE:
                level = 0
                level_initialized = False
                level_1_initialized = False
                level_2_initialized = False
                pygame.time.set_timer(pygame.USEREVENT+1, 0)
            if orangedead == False:
                airRate = 2
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
                level_initialized = False
                level_1_initialized = False
                level_2_initialized = False
        if event.type == pygame.KEYUP:
            if orangedead == False:
                airRate = 1
                if event.key == pygame.K_a:
                    airRate = 1
                    left = False
                if event.key == pygame.K_d:
                    airRate = 1
                    right = False
                if event.key == pygame.K_w:
                    airRate = 1
                    up = False
                if event.key == pygame.K_s:
                    airRate = 1
                    down = False
            
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
    return [pic[row][0], start_x, start_y, pic[row][3], pic[row][4], x_speed, y_speed, move_direction, pic[row][8]]

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
   
def keyaccel(pic): # True is right;  Need to fix the coordinates of the diver with depth and scroll
    global Orangediver
    global depth
    global scroll
    global x_min
    global x_max
    global y_min
    global y_max
    
    global orangelength
    global greenlength

    global x_min_edge
    global x_max_edge
    global y_min_edge
    global y_max_edge
    global orangedead
    global accel
    
    #accel = 0.5 #0.2
    kickaccel = 0.5
    
    start_x = pic[1]
    start_y = pic[2]
    x_move_speed = pic[5]
    y_move_speed = pic[6]
    move_direction = pic[7]
    
    if left == True and right == False and x_min_edge == False:
        x_move_speed = x_move_speed - accel
        move_direction = False
    elif right == True and left == False and x_max_edge == False:
        x_move_speed = x_move_speed + accel
        move_direction = True
    if up == True and down == False and y_min_edge == False:
        y_move_speed = y_move_speed - accel
    elif down == True and up == False and y_max_edge == False:
        y_move_speed = y_move_speed + accel
    if left == True and right == True:
        if lr_just_pressed == 1 and x_min_edge == False:
            x_move_speed = x_move_speed - accel
            move_direction = False
        elif lr_just_pressed == 2 and x_max_edge == False:
            x_move_speed = x_move_speed + accel
            move_direction = True
    if up == True and down == True:
        if ud_just_pressed == 3 and y_min_edge == False:
            y_move_speed = y_move_speed - accel
        elif ud_just_pressed == 4 and y_max_edge == False:
            y_move_speed = y_move_speed + accel
    if left == False and right == False:
        if x_move_speed > 0 + accel/8:
            x_move_speed = x_move_speed - accel/8
        elif x_move_speed < 0 - accel/8:
            x_move_speed = x_move_speed + accel/8
        else:
            x_move_speed = 0
   
    if up == False and down == False:
        if y_move_speed > 0 + accel/8:
            y_move_speed = y_move_speed - accel/8
        elif y_move_speed < 0 - accel/8:
            y_move_speed = y_move_speed + accel/8
        else:
            y_move_speed = 0
            
    if up == True or down == True or left == True or right == True:
        orangelength = orangelength - kickaccel
        greenlength = greenlength - kickaccel
    if up == False and down == False and left == False and right == False:
        orangelength = orangelength + kickaccel
        greenlength = greenlength + kickaccel
    
    kickmax = 20
    kickmin = 4
    if orangelength > kickmax:
        orangelength = kickmax
    if orangelength < kickmin:
        orangelength = kickmin
        
    if greenlength > kickmax:
        greenlength = kickmax
    if greenlength < kickmin:
        greenlength = kickmin
            

    if x_move_speed > 20:
        x_move_speed = 20
    elif x_move_speed < -20:
        x_move_speed = -20
    if y_move_speed > 20:
        y_move_speed = 20
    elif y_move_speed < -20:
        y_move_speed = 20
    
    #if math.fabs(x_move_speed) < 5 and math.fabs(y_move_speed)  < 5:
    #    orangelength = 20
    #    greenlength = 20
    #if (math.fabs(x_move_speed) > 5 and math.fabs(x_move_speed) < 10) or (math.fabs(y_move_speed) > 5 and math.fabs(y_move_speed) < 10):
    #    orangelength = 10
    #    greenlength = 10
    #if (math.fabs(x_move_speed) > 10 and math.fabs(x_move_speed) < 15) or (math.fabs(y_move_speed) > 10 and math.fabs(y_move_speed) < 15):
    #    orangelength = 5
    #    greenlength = 5
    #if (math.fabs(x_move_speed) > 15 and math.fabs(x_move_speed) < 20) or (math.fabs(y_move_speed) > 15 and math.fabs(y_move_speed) < 20):
    #    orangelength = 1
    #    greenlength = 1
    
    
    if (x_min_edge == True and x_move_speed < 0) or (x_max_edge == True and x_move_speed > 0):
        x_move_speed = 0
    else:
        start_x = start_x + x_move_speed
    if (y_min_edge == True and y_move_speed < 0) or (y_max_edge == True and y_move_speed > 0):
        y_move_speed = 0
    else:
        start_y = start_y + y_move_speed
    scroll = scroll + x_move_speed
    depth = depth + y_move_speed  
            
    
    if scroll < x_min + 1:
        x_min_edge = True
    else: x_min_edge =  False
    if scroll > x_max - 1:
        x_max_edge = True
    else: x_max_edge =  False
    if depth < y_min + 1:
        y_min_edge = True
    else: y_min_edge =  False
    if depth > y_max - 1:
        y_max_edge = True
    else: y_max_edge =  False
    
    return [pic[0], start_x, start_y, pic[3], pic[4], x_move_speed, y_move_speed, move_direction]

def animatedorange():
        global orangekicking
        global orangecycles
        global orangelength
        global Orangediver
        global Orangediverkick
        if orangekicking == False:
            Orangediverkick = [Orangediverkick[0], Orangediver[1], Orangediver[2], Orangediver[3], Orangediver[4], Orangediver[5], Orangediver[6], Orangediver[7]]
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
    global windowoffset
    if Orangediver[1] > 1023 - Orangediver[3] - windowoffset:
        Orangediver[1] = 1023 - Orangediver[3] - windowoffset
        Orangediverkick[1] = 1023 - Orangediverkick[3] - windowoffset
        Greendiver[7] = True
    if Orangediver[1] < 0 + windowoffset:
        Orangediver[1] = 0 + windowoffset
        Orangediverkick[1] = 0 + windowoffset
        Greendiver[7] = False
    if Orangediver[2] > 767 - Orangediver[4] - windowoffset:
        Orangediver[2] = 767 - Orangediver[4] - windowoffset
        Orangediverkick[2] = 767 - Orangediverkick[4] - windowoffset
    if Orangediver[2] < 0 + windowoffset:
        Orangediver[2] = 0 + windowoffset
        Orangediverkick[2] = 0 + windowoffset
        
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

def moveedges():      # Not in use
    global Orangediver
    global x_max
    global y_max
    global x_min
    global y_min
    global x_max_edge
    global y_max_edge
    global x_min_edge
    global y_min_edge
    if x_max_edge == False:
        if Orangediver[1] > 1023 - Orangediver[3] - windowoffset:
            x_max = x_max - Orangediver[5]
    if x_min_edge == False:
        if Orangediver[1] < 0 + windowoffset:
            x_max = x_max - Orangediver[5]
    if y_max_edge == False:
        if Orangediver[2] > 767 - Orangediver[4] - windowoffset:
            y_max = y_max - Orangediver[6]
    if y_min_edge == False:
        if Orangediver[2] < 0 + windowoffset:
            y_max = y_max - Orangediver[6]
    return [x_min, y_min, x_max, y_max]

def movebackground(pic, following):
    global windowoffset
    start_x = pic[1]
    start_y = pic[2]
    global x_edge
    global y_edge
    if following[1] > 1023 - following[3] - windowoffset:
        start_x = start_x - following[5]
    if following[1] < 0 + windowoffset:
        start_x = start_x - following[5]
    if following[2] > 767 - following[4] - windowoffset:
        start_y = start_y - following[6]
    if following[2] < 0 + windowoffset:
        start_y = start_y - following[6]
    return [pic[0], start_x, start_y, pic[3], pic[4], pic[5], pic[6], pic[7]]

def rowmovebackground(pic, row, following):
    global windowoffset
    start_x = pic[row][1]
    start_y = pic[row][2]
    global x_edge
    global y_edge
    if following[1] > 1023 - following[3] - windowoffset:
        start_x = start_x - following[5]
    if following[1] < 0 + windowoffset:
        start_x = start_x - following[5]
    if following[2] > 767 - following[4] - windowoffset:
        start_y = start_y - following[6]
    if following[2] < 0 + windowoffset:
        start_y = start_y - following[6]
    return [pic[row][0], start_x, start_y, pic[row][3], pic[row][4], pic[row][5], pic[row][6], pic[row][7], pic[row][8]]

def greenfollow():
    global Orangediver
    global Greendiver
    global Greendiverkick
    xoff = 200
    yoff = 130
    if Orangediver[1] > Greendiver[1] + xoff:
        Greendiver[7] = True
        Greendiver[1] = Orangediver[1] - xoff
        Greendiverkick[7] = True
        Greendiverkick[1] = Orangediver[1] - xoff
    if Orangediver[1] < Greendiver[1] - xoff:
        Greendiver[7] = False
        Greendiver[1] = Orangediver[1] + xoff
        Greendiverkick[7] = False
        Greendiverkick[1] = Orangediver[1] + xoff
    if Orangediver[2] > Greendiver[2] + yoff:
        Greendiver[2] = Orangediver[2] - yoff
        Greendiverkick[2] = Orangediver[2] - yoff
    if Orangediver[2] < Greendiver[2] - yoff:
        Greendiver[2] = Orangediver[2] + yoff  
        Greendiverkick[2] = Orangediver[2] + yoff                      

    if Greendiver[1] < 0:
        Greendiver[1] = 0
        Greendiverkick[1] = 0
    if Greendiver[2] < 0:
        Greendiver[2] = 0
        Greendiverkick[2] = 0
    if Greendiver[1] > 1024-xoff:
        Greendiver[1] = 1024-xoff
        Greendiverkick[1] = 1024-xoff
    if Greendiver[2] > 768-yoff:
        Greendiver[2] = 768-yoff
        Greendiverkick[2] = 768-yoff

def movebubbles(pic, first, offstep):
    global bubblecycles
    global Orangediver
    bubblemax = 0
    if bubblecycles[first] == 0 + offstep:
        if pic[7] == False:
            Bubbles[first][1] = pic[1] + 55 - 30
            Bubbles[first][2] = pic[2] + 60 - 51
        else:
            Bubbles[first][1] = pic[1] - 55 + pic[3]
            Bubbles[first][2] = pic[2] + 60 - 51
    bubblecycles[first] = bubblecycles[first] + 1
    if bubblecycles[first] > 360:
        bubblecycles[first] = 0
    Bubbles[first][2] = Bubbles[first][2] - Bubbles[first][6]
    bubbledepth = depth - (Orangediver[2] - Bubbles[first][2])
    if bubbledepth < bubblemax:
        Bubbles[first][2] = -10000

    if bubblecycles[first + 1] == 90 + offstep:
        if pic[7] == False:
            Bubbles[first + 1][1] = pic[1] + 55 - 30
            Bubbles[first + 1][2] = pic[2] + 60 - 51
        else:
            Bubbles[first + 1][1] = pic[1] - 55 + pic[3]
            Bubbles[first + 1][2] = pic[2] + 60 - 51
    bubblecycles[first + 1] = bubblecycles[first + 1] + 1
    if bubblecycles[first + 1] > 455:
        bubblecycles[first + 1] = 90
    Bubbles[first + 1][2] = Bubbles[first + 1][2] - Bubbles[first + 1][6]
    bubbledepth = depth - (Orangediver[2] - Bubbles[first + 1][2])
    if bubbledepth < bubblemax:
        Bubbles[first + 1][2] = -10000
        
    if bubblecycles[first + 2] == 180 + offstep:
        if pic[7] == False:
            Bubbles[first + 2][1] = pic[1] + 55 - 30
            Bubbles[first + 2][2] = pic[2] + 60 - 51
        else:
            Bubbles[first + 2][1] = pic[1] - 55 + pic[3]
            Bubbles[first + 2][2] = pic[2] + 60 - 51
    bubblecycles[first + 2] = bubblecycles[first + 2] + 1
    if bubblecycles[first + 2] > 540:
        bubblecycles[first + 2] = 180
    Bubbles[first + 2][2] = Bubbles[first + 2][2] - Bubbles[first + 2][6]        
    bubbledepth = depth - (Orangediver[2] - Bubbles[first + 2][2])
    if bubbledepth < bubblemax:
        Bubbles[first + 2][2] = -10000
    if bubblecycles[first + 3] == 270 + offstep:
        if pic[7] == False:
            Bubbles[first + 3][1] = pic[1] + 55 - 30
            Bubbles[first + 3][2] = pic[2] + 60 - 51
        else:
            Bubbles[first + 3][1] = pic[1] - 55 + pic[3]
            Bubbles[first + 3][2] = pic[2] + 60 - 51
    bubblecycles[first + 3] = bubblecycles[first + 3] + 1
    if bubblecycles[first + 3] > 630:
        bubblecycles[first + 3] = 270
    Bubbles[first + 3][2] = Bubbles[first + 3][2] - Bubbles[first + 3][6] 
    bubbledepth = depth - (Orangediver[2] - Bubbles[first + 3][2])
    if bubbledepth < bubblemax:
            Bubbles[first + 3][2] = -10000        

    for b in range(first, first + 4):
        if greenrise == False:
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
    return [pic[row][0], pic[row][1], pic[row][2], pic[row][3], pic[row][4], sx, sy, pic[row][7], pic[row][8]]

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
    side = random.randrange(1, 100)
    global y_min
    global y_max
    global x_min    
    global x_max
    # 1 is right, 2 is top, 3 is left, 4 is bottom
    # Never spawn a fish at the top, because it will look like it's out of the water
    # Weight it more heavily to spawn them at the bottom
    if side == 1: # right
        x = x_max + dimx + offsides
        y = random.randrange(0, y_max - dimy)
    #elif side == 2: # top
     #   x = random.randrange(x_min, x_max - dimx)
      #  y = y_min - dimy - offsides
    elif side == 2: # left
        x = x_min - dimx - offsides
        y = random.randrange(0, y_max - dimy)
    else: # bottom
        x = random.randrange(x_min, x_max - dimx)
        y = y_max + dimy + offsides
    return [pic[row][0], x, y, pic[row][3], pic[row][4], pic[row][5], pic[row][6], pic[row][7], pic[row][8]]

def multifish(pic, number, speed, fishmaxdepth):
    global greenrise
    global Orangediver
    global depth
    global y_min
    for a in range(number):
        if outofbounds(pic, a, pic[a][3]):
            pic[a] = rand_start_side(pic, a, pic[a][3])
            pic[a] = random_direction_move(pic, a, speed)
        if greenrise == False:
            pic[a] = rowmovebackground(pic, a, Orangediver)
        pic[a] = rowmove(pic, a)
        fishdepth = depth - (Orangediver[2] - pic[a][2])
        if fishdepth < fishmaxdepth:
            pic[a][2] = Orangediver[2] - (depth - fishmaxdepth - 1)
            pic[a] = random_direction_move(pic, a, speed)
        randomturn = random.randrange(0, 100)
        if randomturn == 5:
            pic[a] = random_direction_move(pic, a, speed)
        if pic[a][8] == False:
            rowdraw(pic, a)
        speed = speed + 2
        
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
    global fish_collected
    global Shark
    
    orangedead = False
    greenrise = False
    fish_collected = 0
        
    Eel = [[pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 2, 2, True, False],
           [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 2, 2, True, False],
           [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 2, 2, True, False],
           [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 2, 2, True, False]]
    
    Shark = [[pygame.image.load("Shark.png"), -1000, -1000, 400, 100, 6, 6, True, False],
             [pygame.image.load("Shark.png"), -1000, -1000, 400, 100, 6, 6, True, False],
             [pygame.image.load("Shark.png"), -1000, -1000, 400, 100, 6, 6, True, False],
             [pygame.image.load("Shark.png"), -1000, -1000, 400, 100, 6, 6, True, False]]
    
    Jellyfish = [[pygame.image.load("Jellyfish.png"), -1000, -1000, 200, 50, 2, 2, True, False],
                 [pygame.image.load("Jellyfish.png"), -1000, -1000, 200, 50, 2, 2, True, False],
                 [pygame.image.load("Jellyfish.png"), -1000, -1000, 200, 50, 2, 2, True, False],
                 [pygame.image.load("Jellyfish.png"), -1000, -1000, 200, 50, 2, 2, True, False]]

    Lanturnfish = [[pygame.image.load("Lanturnfish.png"), -1000, -1000, 300, 100, 2, 2, True, False],
               [pygame.image.load("Lanturnfish.png"), -1000, -1000, 300, 100, 2, 2, True, False],
               [pygame.image.load("Lanturnfish.png"), -1000, -1000, 300, 100, 2, 2, True, False],
               [pygame.image.load("Lanturnfish.png"), -1000, -1000, 300, 100, 2, 2, True, False]]

    Clownfish = [[pygame.image.load("Clownfish.png"), -1000, -1000, 150, 100, 4, 4, True, False], #Clownfish[n][8] is if it is collected
                 [pygame.image.load("Clownfish.png"), -1000, -1000, 150, 100, 4, 4, True, False],
                 [pygame.image.load("Clownfish.png"), -1000, -1000, 150, 100, 4, 4, True, False],
                 [pygame.image.load("Clownfish.png"), -1000, -1000, 150, 100, 4, 4, True, False]]
    
    Dolphin = [[pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True, False],
               [pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True, False],
               [pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True, False],
               [pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True, False]]

    Bubble = [pygame.image.load("Bubble.png"), 200, 200, 100, 100, 10, 10, True]
    
    Bubbles = [[pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
               [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False]]


########Air Consumption##########################
########Air Consumption##########################
totalAir = 0
airRate = 0
degrees = 0

#Notes for rotation: Radius is 150
########Air Consumption##########################
def airSetup():
    
    global totalAir
    global airRate
    global degrees
    degrees = 0
    #global Pressuregauge 
    totalAir = 180
    airRate = 1
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)
    print("Air Setup Called"+str(totalAir) +str(airRate))
    global gaugerect
    gaugerect = Pressuregauge[0].get_rect()
    global needle
    pygame.draw.line(Pressuregauge[0], (120,0,0), (gaugerect.centerx, gaugerect.centery), (gaugerect.centerx+150, gaugerect.centery), 5)
 

def consumeAir():
    global totalAir
    global airRate
    global gaugerect
    global needle
    global orangedead
    global degrees
    #global Pressuregauge
    pi = 3.141592653589793238462643383279502884197169399375
    radius = 150 #Radius of gauge, if time try to make that actually use the gauge rect to calculate width
    print("ConsumeAir Called"+str(totalAir)+str(airRate))
    totalAir -= airRate
    degrees += airRate
    startx = gaugerect.centerx
    starty = gaugerect.centery
    endx = 150*math.cos((degrees*pi)/180.0) + startx
    endy = -150*math.sin((degrees*pi)/180.0)+starty
    #Pressuregauge[0].fill((0,0,0))
    
    pygame.draw.line(Pressuregauge[0], (120,0,0), (startx, starty), (endx, endy), 5)
    
    if totalAir <= 0:
        orangedead = True
  
#################################################
#################################################################

def Level0():
    global level
    global Islandbutton
    global Treasuremap
    pygame.mouse.set_visible(1)
    draw(Treasuremap)
    Outerbanks = [Islandbutton[0], 245, 330, 25, 25, 0, 0, True]  # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Outerbanks)
    if clicked(Outerbanks):
        level = 1
        pygame.mouse.set_visible(0)
    Singapore = [Islandbutton[0], 760, 425, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Singapore)
    if clicked(Singapore):
        level = 2
        pygame.mouse.set_visible(0)
    Sydney = [Islandbutton[0], 885, 560, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Sydney)
    if clicked(Sydney):
        level = 3
        pygame.mouse.set_visible(0)
    Panama = [Islandbutton[0], 260, 415, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Panama)
    if clicked(Panama):
        level = 4
        pygame.mouse.set_visible(0)
    SanDiego = [Islandbutton[0], 155, 335, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(SanDiego)
    if clicked(SanDiego):
        level = 5
        pygame.mouse.set_visible(0)
    Tokyo = [Islandbutton[0], 860, 325, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Tokyo)
    if clicked(Tokyo):
        level = 6
        pygame.mouse.set_visible(0)
    CapeTown = [Islandbutton[0], 535, 555, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(CapeTown)
    if clicked(CapeTown):
        level = 7
        pygame.mouse.set_visible(0)
    DiveShop = [Islandbutton[0], 475, 275, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(DiveShop)
    if clicked(DiveShop):
        level = 8
        pygame.mouse.set_visible(0)
    Santiago = [Islandbutton[0], 290, 550, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Santiago)
    if clicked(Santiago):
        level = 9
        pygame.mouse.set_visible(0)
    Antarctica = [Islandbutton[0], 630, 695, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Antarctica)
    if clicked(Antarctica):
        level = 10
        pygame.mouse.set_visible(0)
    KeyWest = [Islandbutton[0], 243, 363, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(KeyWest)
    if clicked(KeyWest):
        level = 11
        pygame.mouse.set_visible(0)
    Unknown = [Islandbutton[0], 123, 567, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Unknown)
    if clicked(Unknown):
        level = 12
        pygame.mouse.set_visible(0)

def Level8():
    global level
    global Islandbutton
    global Shelves
    global equipment
    global MONEY
    global levels
    
    ### Level Limit is the number of times the player can do the level and earn money ###
    levellimit = 1
    if levels[1] == 1 and levelsdone[1] < levellimit:
        MONEY = MONEY + 100
        levels[1] = 0
        levelsdone[1] = levelsdone[1] + 1
    if levels[2] == 1 and levelsdone[2] < levellimit:
        MONEY = MONEY + 50
        levels[2] = 0
        levelsdone[2] = levelsdone[2] + 1

    pygame.mouse.set_visible(1)
    draw(Shelves)
    pricefont = pygame.font.SysFont("monospace", 15, "bold")
    infofont = pygame.font.SysFont("monospace", 30, "bold")

    pricecolor = [250, 250, 0]
    infocolor = [255, 255, 255]
    infopos = [100, 50]

    ### Snorkel ###
    snorkelprice = 20
    snorkeltext = pricefont.render('Snorkel: $' + str(snorkelprice), 1, (pricecolor))
    screen.blit(snorkeltext, (320, 420))
    
    if equipment[0] == 0:
        ShopSnorkel = [pygame.image.load("Snorkel.png"), 320, 320, 100, 100, 0, 0, True]
        draw(ShopSnorkel)
        if MONEY > snorkelprice and clicked(ShopSnorkel):
            equipment[0] = 1
            MONEY = MONEY - snorkelprice
    else:
        ShopSnorkel = [pygame.image.load("Snorkel.png"), 320, 650, 50, 50, 0, 0, True]
        draw(ShopSnorkel)
    if mouseover(ShopSnorkel):
        snorkelinfotext = infofont.render('Snorkels allow you to conserve air at the surface', 1, (infocolor))
        screen.blit(snorkelinfotext, (infopos))

    ### Goggles ###
    Gogglesprice = 20
    Gogglestext = pricefont.render('Goggles: $' + str(Gogglesprice), 1, (pricecolor))
    screen.blit(Gogglestext, (480, 420))
    if equipment[1] == 0:
        ShopGoggles = [pygame.image.load("Goggles.jpg"), 480, 320, 100, 100, 0, 0, True]
        draw(ShopGoggles)
        if MONEY > Gogglesprice and clicked(ShopGoggles):
            equipment[1] = 1
            MONEY = MONEY - Gogglesprice
    else:
        ShopGoggles = [pygame.image.load("Goggles.jpg"), 480, 650, 50, 50, 0, 0, True]
        draw(ShopGoggles)
    if mouseover(ShopGoggles):
        Gogglesinfotext = infofont.render('You need goggles to see underwater', 1, (infocolor))
        screen.blit(Gogglesinfotext, (infopos))  
        
    ### Flashlight ###
    flashlightprice = 100
    flashlighttext = pricefont.render('Light: $' + str(flashlightprice), 1, (pricecolor))
    screen.blit(flashlighttext, (640, 420))
    if equipment[11] == 0:
        ShopFlashlight = [pygame.image.load("Flashlight.png"), 640, 320, 100, 100, 0, 0, True] # 11
        draw(ShopFlashlight)
        if MONEY > flashlightprice and clicked(ShopFlashlight):
            equipment[11] = 1
            MONEY = MONEY - flashlightprice
    else:
        ShopFlashlight = [pygame.image.load("Flashlight.png"), 640, 650, 50, 50, 0, 0, True] # 11
        draw(ShopFlashlight)  
    if mouseover(ShopFlashlight):
        Flashlightinfotext = infofont.render('You need a flashlight when night diving', 1, (infocolor))
        screen.blit(Flashlightinfotext, (infopos))

    ### BCD ###
    BCDprice = 300
    BCDtext = pricefont.render('BCD: $' + str(BCDprice), 1, (pricecolor))
    screen.blit(BCDtext, (250, 220))
    if equipment[2] == 0:
        ShopBCD = [pygame.image.load("BCD.jpg"), 250, 120, 100, 100, 0, 0, True]
        draw(ShopBCD)
        if MONEY > BCDprice and clicked(ShopBCD):
            equipment[2] = 1
            MONEY = MONEY - BCDprice
    else:
        ShopBCD = [pygame.image.load("BCD.jpg"), 250, 600, 50, 50, 0, 0, True]
        draw(ShopBCD)   
    if mouseover(ShopBCD):
        BCDinfotext = infofont.render('Buoyancy Control Devices control your buoyancy', 1, (infocolor))
        screen.blit(BCDinfotext, (infopos))
        
    ### Fins ###
    Finsprice = 200
    Finstext = pricefont.render('Fins: $' + str(Finsprice), 1, (pricecolor))
    screen.blit(Finstext, (420, 220))
    if equipment[3] == 0:
        ShopFins = [pygame.image.load("Fins.jpg"), 420, 120, 100, 100, 0, 0, True]
        draw(ShopFins)
        if MONEY > Finsprice and clicked(ShopFins):
            equipment[3] = 1
            MONEY = MONEY - Finsprice
    else:
        ShopFins = [pygame.image.load("Fins.jpg"), 420, 600, 50, 50, 0, 0, True]
        draw(ShopFins)   
    if mouseover(ShopFins):
        Finsinfotext = infofont.render('You need fins to swim', 1, (infocolor))
        screen.blit(Finsinfotext, (infopos))
         
    ### Regulator ###
    Regulatorprice = 200
    Regulatortext = pricefont.render('Regulator: $' + str(Regulatorprice), 1, (pricecolor))
    screen.blit(Regulatortext, (590, 220))
    if equipment[4] == 0:
        ShopRegulator = [pygame.image.load("Regulator.jpg"), 590, 120, 100, 100, 0, 0, True]
        draw(ShopRegulator)
        if MONEY > Regulatorprice and clicked(ShopRegulator):
            equipment[4] = 1
            MONEY = MONEY - Regulatorprice
    else:
        ShopRegulator = [pygame.image.load("Regulator.jpg"), 590, 600, 50, 50, 0, 0, True]
        draw(ShopRegulator)
    if mouseover(ShopRegulator):
        Regulatorinfotext = infofont.render('You need a regulator to breathe', 1, (infocolor))
        screen.blit(Regulatorinfotext, (infopos))   
       
    ### ExtraRegulator ###
    ExtraRegulatorprice = 200
    ExtraRegulatortext = pricefont.render('2nd Regulator: $' + str(ExtraRegulatorprice), 1, (pricecolor))
    screen.blit(ExtraRegulatortext, (590, 560))
    if equipment[5] == 0:
        ShopExtraRegulator = [pygame.image.load("ExtraRegulator.jpg"), 590, 460, 100, 100, 0, 0, True]
        draw(ShopExtraRegulator)
        if MONEY > ExtraRegulatorprice and clicked(ShopExtraRegulator):
            equipment[5] = 1
            MONEY = MONEY - ExtraRegulatorprice
    else:
        ShopExtraRegulator = [pygame.image.load("ExtraRegulator.jpg"), 590, 700, 50, 50, 0, 0, True]
        draw(ShopExtraRegulator)
    if mouseover(ShopExtraRegulator):
        ExtraRegulatorinfotext = infofont.render('You need an extra regulator just in case', 1, (infocolor))
        screen.blit(ExtraRegulatorinfotext, (infopos))
        
    ### AirTank ###
    AirTankprice = 250
    AirTanktext = pricefont.render('Air Tank: $' + str(AirTankprice), 1, (pricecolor))
    screen.blit(AirTanktext, (420, 560))
    if equipment[6] == 0:
        ShopAirTank = [pygame.image.load("AirTank.jpg"), 420, 460, 100, 100, 0, 0, True]
        draw(ShopAirTank)
        if MONEY > AirTankprice and clicked(ShopAirTank):
            equipment[6] = 1
            MONEY = MONEY - AirTankprice
    else:
        ShopAirTank = [pygame.image.load("AirTank.jpg"), 420, 700, 50, 50, 0, 0, True]
        draw(ShopAirTank)     
    if mouseover(ShopAirTank):
        AirTankinfotext = infofont.render('You need an Air Tank for air', 1, (infocolor))
        screen.blit(AirTankinfotext, (infopos)) 

    ### Gauges ###
    Gaugesprice = 150
    Gaugestext = pricefont.render('Gauges: $' + str(Gaugesprice), 1, (pricecolor))
    screen.blit(Gaugestext, (250, 560))
    if equipment[7] == 0:
        ShopGauges = [pygame.image.load("Gauges.jpg"), 250, 460, 100, 100, 0, 0, True]
        draw(ShopGauges)
        if MONEY > Gaugesprice and clicked(ShopGauges):
            equipment[7] = 1
            MONEY = MONEY - Gaugesprice
    else:
        ShopGauges = [pygame.image.load("Gauges.jpg"), 250, 700, 50, 50, 0, 0, True]
        draw(ShopGauges)
    if mouseover(ShopGauges):
        Gaugesinfotext = infofont.render('Gauges display depth and tank pressure', 1, (infocolor))
        screen.blit(Gaugesinfotext, (infopos))
             
    ### Wetsuit ###
    Wetsuitprice = 200
    Wetsuittext = pricefont.render('Wetsuit: $' + str(Wetsuitprice), 1, (pricecolor))
    screen.blit(Wetsuittext, (101, 280))
    if equipment[8] == 0:
        ShopWetsuit = [pygame.image.load("Wetsuit.jpg"), 101, 180, 100, 100, 0, 0, True]
        draw(ShopWetsuit)
        if MONEY > Wetsuitprice and clicked(ShopWetsuit):
            equipment[8] = 1
            MONEY = MONEY - Wetsuitprice
    else:
        ShopWetsuit = [pygame.image.load("WetSuit.jpg"), 101, 600, 50, 50, 0, 0, True]
        draw(ShopWetsuit)  
    if mouseover(ShopWetsuit):
        Wetsuitinfotext = infofont.render('Wet suits keep you warm and prevent scratches', 1, (infocolor))
        screen.blit(Wetsuitinfotext, (infopos)) 
        
    ### Drysuit ###
    Drysuitprice = 900
    Drysuittext = pricefont.render('Dry Suit: $' + str(Drysuitprice), 1, (pricecolor))
    screen.blit(Drysuittext, (101, 480))
    if equipment[9] == 0:
        ShopDrysuit = [pygame.image.load("Drysuit.jpg"), 101, 380, 100, 100, 0, 0, True]
        draw(ShopDrysuit)
        if MONEY > Drysuitprice and clicked(ShopDrysuit):
            equipment[9] = 1
            MONEY = MONEY - Drysuitprice
    else:
        ShopDrysuit = [pygame.image.load("Drysuit.jpg"), 101, 650, 50, 50, 0, 0, True]
        draw(ShopDrysuit)  
    if mouseover(ShopDrysuit):
        Drysuitinfotext = infofont.render('Dry Suits are for extremely cold environments', 1, (infocolor))
        screen.blit(Drysuitinfotext, (infopos)) 
        
    ### Slate ###
    Slateprice = 10
    Slatetext = pricefont.render('Slate: $' + str(Slateprice), 1, (pricecolor))
    screen.blit(Slatetext, (101, 680))
    if equipment[10] == 0:
        ShopSlate = [pygame.image.load("Slate.jpg"), 101, 580, 100, 100, 0, 0, True]
        draw(ShopSlate)
        if MONEY > Slateprice and clicked(ShopSlate):
            equipment[10] = 1
            MONEY = MONEY - Slateprice
    else:
        ShopSlate = [pygame.image.load("Slate.jpg"), 101, 700, 50, 50, 0, 0, True]
        draw(ShopSlate)   
    if mouseover(ShopSlate):
        Slateinfotext = infofont.render('Slates let you write messages to your buddy', 1, (infocolor))
        screen.blit(Slateinfotext, (infopos)) 

    ### Glowstick ###
    Glowstickprice = 5
    Glowsticktext = pricefont.render('Glowstick: $' + str(Glowstickprice), 1, (pricecolor))
    screen.blit(Glowsticktext, (840, 280))
    if equipment[12] == 0:
        ShopGlowstick = [pygame.image.load("Glowstick.jpg"), 840, 180, 100, 100, 0, 0, True]
        draw(ShopGlowstick)
        if MONEY > Glowstickprice and clicked(ShopGlowstick):
            equipment[12] = 1
            MONEY = MONEY - Glowstickprice
    else:
        ShopGlowstick = [pygame.image.load("Glowstick.jpg"), 840, 600, 50, 50, 0, 0, True]
        draw(ShopGlowstick) 
    if mouseover(ShopGlowstick):
        Glowstickinfotext = infofont.render('Glow Sticks let you keep you buddy in sight on night dives', 1, (infocolor))
        screen.blit(Glowstickinfotext, (infopos))  
        
    ### Scooter ###
    Scooterprice = 2000
    Scootertext = pricefont.render('Scooter: $' + str(Scooterprice), 1, (pricecolor))
    screen.blit(Scootertext, (840, 480))
    if equipment[13] == 0:
        ShopScooter = [pygame.image.load("Scooter.jpg"), 840, 380, 100, 100, 0, 0, True]
        draw(ShopScooter)
        if MONEY > Scooterprice and clicked(ShopScooter):
            equipment[13] = 1
            MONEY = MONEY - Scooterprice
    else:
        ShopScooter = [pygame.image.load("Scooter.jpg"), 840, 650, 50, 50, 0, 0, True]
        draw(ShopScooter)   
    if mouseover(ShopScooter):
        Scooterinfotext = infofont.render('Under water scooters can be a lot of fun', 1, (infocolor))
        screen.blit(Scooterinfotext, (infopos))
        
    ### ExtraFlashlight ###
    ExtraFlashlightprice = 40
    ExtraFlashlighttext = pricefont.render('2nd Light: $' + str(ExtraFlashlightprice), 1, (pricecolor))
    screen.blit(ExtraFlashlighttext, (840, 680))
    if equipment[14] == 0:
        ShopExtraFlashlight = [pygame.image.load("ExtraFlashlight.jpg"), 840, 580, 100, 100, 0, 0, True]
        draw(ShopExtraFlashlight)
        if MONEY > ExtraFlashlightprice and clicked(ShopExtraFlashlight):
            equipment[14] = 1
            MONEY = MONEY - ExtraFlashlightprice
    else:
        ShopExtraFlashlight = [pygame.image.load("ExtraFlashlight.jpg"), 840, 700, 50, 50, 0, 0, True]
        draw(ShopExtraFlashlight)
    if mouseover(ShopExtraFlashlight):
        ExtraFlashlightinfotext = infofont.render('Carry an extra light on night dives', 1, (infocolor))
        screen.blit(ExtraFlashlightinfotext, (infopos))

                
    moneyfont = pygame.font.SysFont("monospace", 30, "bold")
    moneytext = moneyfont.render('Wallet = $' + str(MONEY), 1, (0, 0, 0))
    screen.blit(moneytext, (350, 5))

def nothing():
    cool = True
    return cool

#### Surface Variables #######################################################################
# list = [image, x, y, x size, y size, x speed, y speed, right]
### Equipment #####
equipment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
# Snorkel, Goggles, BCD, Fins, Regulator, ExtraRegulator, AirTank, Gauges, Wetsuit, Drysuit, Slate, Flashlight, Glowstick, Scooter, ExtraFlashlight 


Snorkel = [[pygame.transform.rotate(pygame.image.load("Snorkel.png"), -30), 0, 0, 100, 100, 0, 0, True], # 0
           [pygame.transform.rotate(pygame.image.load("Snorkel.png"), -30), 0, 0, 100, 100, 0, 0, True]]


Flashlight = [[pygame.image.load("Flashlight.png"), 0, 0, 100, 100, 0, 0, True], # 11
              [pygame.image.load("Flashlight.png"), 0, 0, 100, 100, 0, 0, True]]
#######################
Orangediver = [pygame.image.load("Orangediver.png"), 200, 200, 224, 188, 10, 10, True]
Orangediverkick = [pygame.image.load("Orangediverkick.png"), 200, 200, 224, 188, 10, 10, True]
Orangediverdead = [pygame.image.load("Orangediverdead.png"), Orangediver[1], Orangediver[2], 230, 145, Orangediver[5], Orangediver[6], Orangediver[7]]

Greendiver = [pygame.image.load("Greendiver.png"), 0, 200, 224, 188, 10, 10, True]
Greendiverkick = [pygame.image.load("Greendiverkick.png"), 0, 200, 224, 188, 10, 10, True]

Eel = [[pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 2, 2, True, False],
       [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 2, 2, True, False],
       [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 2, 2, True, False],
       [pygame.image.load("Eel.png"), -1000, -1000, 300, 100, 2, 2, True, False]]

Shark = [[pygame.image.load("Shark.png"), -1000, -1000, 400, 100, 6, 6, True, False],
         [pygame.image.load("Shark.png"), -1000, -1000, 400, 100, 6, 6, True, False],
         [pygame.image.load("Shark.png"), -1000, -1000, 400, 100, 6, 6, True, False],
         [pygame.image.load("Shark.png"), -1000, -1000, 400, 100, 6, 6, True, False]]

Jellyfish = [[pygame.image.load("Jellyfish.png"), -1000, -1000, 200, 50, 2, 2, True, False],
             [pygame.image.load("Jellyfish.png"), -1000, -1000, 200, 50, 2, 2, True, False],
             [pygame.image.load("Jellyfish.png"), -1000, -1000, 200, 50, 2, 2, True, False],
             [pygame.image.load("Jellyfish.png"), -1000, -1000, 200, 50, 2, 2, True, False]]

Lanturnfish = [[pygame.image.load("Lanturnfish.png"), -1000, -1000, 300, 100, 2, 2, True, False],
               [pygame.image.load("Lanturnfish.png"), -1000, -1000, 300, 100, 2, 2, True, False],
               [pygame.image.load("Lanturnfish.png"), -1000, -1000, 300, 100, 2, 2, True, False],
               [pygame.image.load("Lanturnfish.png"), -1000, -1000, 300, 100, 2, 2, True, False]]

Clownfish = [[pygame.image.load("Clownfish.png"), -1000, -1000, 150, 100, 4, 4, True, False], #Clownfish[n][8] is if it is collected
             [pygame.image.load("Clownfish.png"), -1000, -1000, 150, 100, 4, 4, True, False],
             [pygame.image.load("Clownfish.png"), -1000, -1000, 150, 100, 4, 4, True, False],
             [pygame.image.load("Clownfish.png"), -1000, -1000, 150, 100, 4, 4, True, False]]

Dolphin = [[pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True, False],
           [pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True, False],
           [pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True, False],
           [pygame.image.load("Dolphin.png"), -1000, -1000, 400, 300, 8, 8, True, False]]

Bubble = [pygame.image.load("Bubble.png"), 200, 200, 100, 100, 10, 10, True, False]

Bubbles = [[pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
           [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False]]


Coral0 = [[pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False]]

Coral1 = [pygame.image.load("Coral1.png"), 200, 200, 100, 100, 10, 10, True]
Coral2 = [pygame.image.load("Coral2.png"), 200, 200, 100, 100, 10, 10, True]
Coral3 = [pygame.image.load("Coral3.png"), 200, 200, 100, 100, 10, 10, True]

Rock0 = [[pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False],
         [pygame.image.load("Rock5.png"), 200, 200, 250, 350, 10, 10, True, False]]

Rock1 = [pygame.image.load("Rock1.png"), 200, 200, 100, 100, 10, 10, True]
Rock2 = [pygame.image.load("Rock2.png"), 200, 200, 100, 100, 10, 10, True]
Rock3 = [pygame.image.load("Rock3.png"), 200, 200, 100, 100, 10, 10, True]
Rock4 = [pygame.image.load("Rock4.png"), 200, 200, 100, 100, 10, 10, True]
Rock5 = [pygame.image.load("Rock5.png"), 200, 200, 100, 100, 10, 10, True]


Boat = [[pygame.image.load("Boat.png"), 0, 0, 800, 500, 0, 0, True, False]]
Treasurechest = [[pygame.image.load("Treasurechest.png"), -10000, -10000, 250, 200, 10, 10, True, False]]

Wave = [[pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False]]


Underwave = [[pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False],
             [pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False]]

Sandcastle = [pygame.image.load("Sandcastle.png"), 0, 0, 6000, 768, 10, 0, True]
Seafloor = [pygame.image.load("Seafloor.png"), 0, 0, 6000, 768, 10, 0, True]
Undersea = [pygame.image.load("Undersea.png"), 0, 0, 1024, 768, 0, 0, True]
Bottomsea = [pygame.image.load("Bottomsea.png"), 0, 0, 1024, 768, 0, 0, True]

Bigback = [pygame.image.load("Bigback.png"), 0, 0, 6000, 6000, 10, 10, True]
Treasuremap = [pygame.image.load("Treasuremap.png"), 0, 0, 1024, 768, 0, 0, True]
#Pressuregauge = [pygame.image.load("Pressuregauge.png"), 200, 200, 100, 100, 10, 10, True]
Pressuregauge = [pygame.image.load("Pressuregauge.png"),  0, 0, 150, 150, 0, 0, True]
Depthgauge = [pygame.image.load("Depthgauge.png"), 0, 0, 150, 150, 0, 0, True]
Shelves = [pygame.image.load("Shelves.png"), 0, 0, 1024, 768, 0, 0, True]

Islandbutton = [pygame.image.load("Islandbutton.png"), 200, 200, 100, 100, 10, 10, True]
Menubutton = [pygame.image.load("Menubutton.png"), 200, 200, 100, 100, 10, 10, True]
#### Surface Variables ###################################################################

pygame.init()
size=[1024,768]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Diver Test")
clock=pygame.time.Clock()
pygame.mouse.set_visible(1)

### Common Level Variables ###########################################
level_initialized = False
level_complete = False
#################################################################
### Level 1 Variables ###########################################
level_1_initialized = False
level_1_complete = False
#################################################################
### Level 2 Variables ###########################################
level_2_initialized = False
level_2_complete= False
fish_collected = 0
holding_a_fish = False
#################################################################
### Universal Variables #########################################
level = 8
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

greenrise = False

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

bubbleskilled = False
eelskilled = False
sharkskilled = False
lanturnskilled = False
jellyskilled = False

x_min = 0
y_min = 0
x_max = 2000
y_max = 1000

x_min_edge = False
y_min_edge = False
x_max_edge = False
y_max_edge = False

wintime = 0
MONEY = 1000
accel = 0.5 #0.2
    

#edges = [0, 0, 2000, 1000]
levels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
levelsdone = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
windowoffset = 200

#################################################################
# -------- Main Program Loop -----------
while done == False:
    keys()
    
    ################# Map Level 0 ###########################
    if level == 0:
        Level0()
    ################# Dive Shop Level 8
    elif level == 8:
        Level8()
                
    ############### Game Levels ###################################################
    else:
        if level_initialized == False:
            airSetup()
            x_min = 0
            y_min = 0
            x_max = 3500
            y_max = 1800
            y_min_edge = False
            y_max_edge = False
            x_min_edge = False
            x_max_edge = False
            
            level_initialized = True
            level_complete = False
            
            wintime = 0
            
            Boat = [[pygame.image.load("Boat.png"), 100, -400, 800, 500, 0, 0, True, False]]
            Treasurechest = [[pygame.image.load("Treasurechest.png"), x_max - x_max/2, y_max + 120, 250, 200, 0, 0, True, False]]
            
            eelskilled = False
            bubbleskilled = False
            sharkskilled = False
            jellyskilled = False
            lanturnskilled = False
           
            restart_fish()
            
            holding_a_fish = False
            fish_collected = 0
            
            down = False
            up = False
            left = False
            right = False
            
            Orangediver = [pygame.image.load("Orangediver.png"), 400, 200, 224, 188, 10, 10, True]
            Orangediverkick = [pygame.image.load("Orangediverkick.png"), 400, 200, 224, 188, 10, 10, True]
            Greendiver = [pygame.image.load("Greendiver.png"), 0, 200, 224, 188, 10, 10, True]
            Orangediver[5] = 0
            Orangediver[6] = 0
            orangedead = False
            greenrise = False
            greenkicking = True
            orangekicking = True
            orangekicking = True
            orangecycles = 0
            orangelength = 20 
            
            bubblecycles = [0, 0, 0, 0, 0, 0, 0, 0]
            scroll = Orangediver[1]  
            depth = Orangediver[2]
            
            #edges = [-100, -100, 3500, 1800]
            
            
            initial_Coral0_x = -100 - windowoffset
            for n in range(10):
                Coral0[n][3] = 600
                Coral0[n][4] = 400
                Coral0[n][1] = initial_Coral0_x
                Coral0[n][2] = y_max + 50 - 100 - 115 + windowoffset
                initial_Coral0_x = initial_Coral0_x + 400
                
            initial_Wave_x = -100 - windowoffset
            for n in range(10):
                Wave[n][3] = 600
                Wave[n][4] = 400
                Wave[n][1] = initial_Wave_x
                Wave[n][2] = y_min + 20 - windowoffset
                initial_Wave_x = initial_Wave_x + 536
                
            initial_Underwave_x = -100 - windowoffset
            for n in range(10):
                Underwave[n][3] = 300
                Underwave[n][4] = 100
                Underwave[n][1] = initial_Underwave_x
                Underwave[n][2] = y_min + 500 - windowoffset
                initial_Underwave_x = initial_Underwave_x + 536
                
            initial_Underwave_x = -400 - windowoffset
            for n in range(10, 20):
                Underwave[n][3] = 300
                Underwave[n][4] = 100
                Underwave[n][1] = initial_Underwave_x
                Underwave[n][2] = y_min + 1000 - windowoffset
                initial_Underwave_x = initial_Underwave_x + 536
                
            initial_Underwave_x = -100 - windowoffset
            for n in range(20, 30):
                Underwave[n][3] = 300
                Underwave[n][4] = 100
                Underwave[n][1] = initial_Underwave_x
                Underwave[n][2] = y_min + 1500 - windowoffset
                initial_Underwave_x = initial_Underwave_x + 536
                
            initial_Underwave_x = -400 - windowoffset
            for n in range(30, 40):
                Underwave[n][3] = 300
                Underwave[n][4] = 100
                Underwave[n][1] = initial_Underwave_x
                Underwave[n][2] = y_min + 2000 - windowoffset
                initial_Underwave_x = initial_Underwave_x + 536
            
            initial_Rock0_y = -windowoffset - 100
            for n in range(10):
                Rock0[n][3] = 400
                Rock0[n][1] = x_min - 200 + 100 - windowoffset
                Rock0[n][2] = initial_Rock0_y
                initial_Rock0_y = initial_Rock0_y + 250
                
            initial_Rock0_y2 = -windowoffset - 100
            for n in range(10, 20):
                Rock0[n][3] = 400
                Rock0[n][1] = x_max + 175  - 100 - 150 + windowoffset
                Rock0[n][2] = initial_Rock0_y2
                initial_Rock0_y2 = initial_Rock0_y2 + 250
        ##  Initialized #########################################################3 

        screen.fill(ocean)   
         
        if orangedead == False:
            Orangediver = keyaccel(Orangediver)
            greenfollow()
        elif greenrise == False:
            down = True
            up = False
            left = False
            right  = False
            Orangediver = keyaccel(Orangediver)
            Orangediver[0] = Orangediverdead[0]
            Orangediver[3] = Orangediverdead[3]
            Orangediver[4] = Orangediverdead[4]
            Orangediverkick[0] = Orangediverdead[0]
            Orangediverkick[3] = Orangediverdead[3]
            Orangediverkick[4] = Orangediverdead[4]
            if y_max_edge == True:
                greenrise = True
            Greendiver = movebackground(Greendiver, Orangediver)
        elif greenrise == True:
            if Orangediver[7] == True:
                ox1 = 129
                ox2 = 160
            else:
                ox1 = 95
                ox2 = 64
            oy1 = 118
            oy2 = 31
            offerness = 5
            if fancycollision(Greendiver, Orangediver, ox1, oy1, ox2, oy2, offerness) == False:
                if Greendiver[1] + ox1 + offerness < Orangediver[1] + ox2 - offerness:
                    Greendiver[7] = True
                    Greendiver = move(Greendiver, 8, 0)
                elif Greendiver[1] + ox1 - offerness > Orangediver[1] + ox2 + offerness:
                    Greendiver[7] = False
                    Greendiver = move(Greendiver, -8, 0)
                if Greendiver[2] + oy1 + offerness < Orangediver[2] + oy2 - offerness:
                    Greendiver = move(Greendiver, 0, 8)
                elif Greendiver[2] + oy1 - offerness > Orangediver[2] + oy2 + offerness:
                    Greendiver = move(Greendiver, 0, -8)
            else:
                Greendiver[7] = Orangediver[7]
                Greendiver = move(Greendiver, 0, -5)
                Orangediver = move(Orangediver, 0, -5)
        ######### Equipment coordinates ############
        if orangedead == False:
            Snorkel[0][7] = Orangediver[7]
            Snorkel[0][3] = 75
            Snorkel[0][4] = 75
            Snorkel[0][2] = Orangediver[2] - 10
            Flashlight[0][7] = Orangediver[7]
            Flashlight[0][3] = 60
            Flashlight[0][4] = 40
            Flashlight[0][2] = Orangediver[2] + 107
            
            if Orangediver[7] == True:
                Snorkel[0][1] = Orangediver[1] + Orangediver[3] - Snorkel[0][3] - 10
                Flashlight[0][1] = Orangediver[1] + Orangediver[3] - Flashlight[0][3] - 55
            else:
                Snorkel[0][1] = Orangediver[1] + 10
                Flashlight[0][1] = Orangediver[1] + 55
        Snorkel[1][7] = Greendiver[7]
        Snorkel[1][3] = 75
        Snorkel[1][4] = 75
        Snorkel[1][2] = Greendiver[2] - 10
        Flashlight[1][7] = Greendiver[7]
        Flashlight[1][3] = 60
        Flashlight[1][4] = 40
        Flashlight[1][2] = Greendiver[2] + 107
        
        if Greendiver[7] == True:
            Snorkel[1][1] = Greendiver[1] + Greendiver[3] - Snorkel[1][3] - 10
            Flashlight[1][1] = Greendiver[1] + Greendiver[3] - Flashlight[1][3] - 55
        else:
            Snorkel[1][1] = Greendiver[1] + 10
            Flashlight[1][1] = Greendiver[1] + 55

                
        #####################################################
        rowdraw(Boat, 0)        
        for n in range(10):
            if greenrise == False:
                Wave[n] = rowmovebackground(Wave, n, Orangediver)
            rowdraw(Wave, n)
        for n in range(40):
            if greenrise == False:
                Underwave[n] = rowmovebackground(Underwave, n, Orangediver)
            rowdraw(Underwave, n)
        for n in range(20):
            if greenrise == False:
                Rock0[n] = rowmovebackground(Rock0, n, Orangediver)
            rowdraw(Rock0, n)
        for n in range(10):
            if greenrise == False:
                Coral0[n] = rowmovebackground(Coral0, n, Orangediver)
            rowdraw(Coral0, n)
        if greenrise == False:
            Boat[0] = rowmovebackground(Boat, 0, Orangediver)
            Treasurechest[0] = rowmovebackground(Treasurechest, 0, Orangediver)

        #########################################################
        #### Level Initialization and Fish ############
          
        if level == 1: # Outer Banks
            if level_1_initialized == False:
                level_1_initialized = True
                for n in range(10):
                    Coral0[n][0] = Coral1[0]
                for n in range(10):
                    Rock0[n][0] = Rock5[0]
            multifish(Dolphin, 4, 3, 75)
            multifish(Jellyfish, 4, 1, 75)
            multifish(Shark, 4, 4, 75)
        
        if level == 2: # Singapore
            if level_2_initialized == False:
                level_2_initialized = True
                for n in range(10):
                    Coral0[n][0] = Coral2[0]
                for n in range(10):
                    Rock0[n][0] = Rock4[0]
            multifish(Eel, 4, 2, 1600)
            multifish(Clownfish, 4, 5, 200)
            multifish(Dolphin, 4, 3, 75)
            multifish(Jellyfish, 4, 1, 75)
            multifish(Lanturnfish, 4, 2, 1600)
            multifish(Shark, 4, 4, 75)
        
            
        #########################################################
        
        draw(Pressuregauge)
        
        depthtext = myfont.render("Y=" + str(depth), 1, (255, 255, 0))
        screen.blit(depthtext, (1024 - 240, 10))
        scrolltext = myfont.render("X=" + str(scroll), 1, (255, 255, 0))
        screen.blit(scrolltext, (1024 - 240, 50))
        
        for n in range(4):
            if collision(Eel[n], Orangediver, 75):
                orangedead = True
                eelskilled = True
                
        for n in range(4):
            if collision(Shark[n], Orangediver, 75):
                orangedead = True
                sharkskilled = True
                
        for n in range(4):
            if collision(Jellyfish[n], Orangediver, 75):
                orangedead = True
                jellyskilled = True
                
        for n in range(4):
            if collision(Lanturnfish[n], Orangediver, 75):
                orangedead = True
                lanturnskilled = True

        if level_complete == True and orangedead == False:
            winfont = pygame.font.SysFont("monospace", 100, "bold")
            wintext = winfont.render('YOU WIN!', 1, (255, 255, 0))
            screen.blit(wintext, (250, 100))
            if wintime > 1000:
                level = 0
            wintime = wintime + 1
            
        if orangedead == True:
            deadfont = pygame.font.SysFont("monospace", 100, "bold")
            deadtext = deadfont.render('YOU DEAD!', 1, (255, 255, 0))
            screen.blit(deadtext, (250, 100))
            
        if equipment[0] == 1: 
            if Orangediver[7]: ## Behind
                if orangedead == False:
                    rowdraw(Snorkel, 0)
            if Greendiver[7]:
                rowdraw(Snorkel, 1)
                
        animatedgreen()
        movebubbles(Greendiver, 4, 40)
        
        if equipment[0] == 1:
            if Greendiver[7] == False: ## In front
                rowdraw(Snorkel, 1)
        if equipment[11] == 1:
            rowdraw(Flashlight, 1)
            
        animatedorange()
        if orangedead == False:
            movebubbles(Orangediver, 0, 0)
            
        if equipment[0] == 1 and orangedead == False:
            if Orangediver[7] == False: ## In front
                rowdraw(Snorkel, 0)
        if equipment[11] == 1 and orangedead == False:
            rowdraw(Flashlight, 0)
      
        if greenrise == False:
            binddiver()
        
        if Orangediver[6] < -15:
            orangedead = True
            bubbleskilled = True
    
        if orangedead == True and greenrise == True:
            if bubbleskilled == True:
                bubbledeadfont = pygame.font.SysFont("monospace", 30, "bold")
                bubbledeadtext = bubbledeadfont.render('Never ascend faster than your bubbles.', 1, (255, 255, 0))
                screen.blit(bubbledeadtext, (100, 400))        
            if eelskilled == True or sharkskilled == True or jellyskilled or lanturnskilled:
                eeldeadfont = pygame.font.SysFont("monospace", 30, "bold")
                eeldeadtext = eeldeadfont.render('Watch out for dangerous fish.', 1, (255, 255, 0))
                screen.blit(eeldeadtext, (200, 450))
                
        
    

#### Level Gameplay
################# Outer Banks Level 1 ###############################

        if level == 1:

            if collision(Treasurechest[0], Orangediver, 50):
                Treasurechest[0][8] = True
                if greenrise == False:
                    Treasurechest[0][2] = Orangediver[2] + Orangediver[4]/2 - Treasurechest[0][4]/2 + 50
                    Treasurechest[0][3] = 150
                    Treasurechest[0][4] = 100
                    if Orangediver[7]:
                        Treasurechest[0][1] = Orangediver[1] + Orangediver[3]/2 - Treasurechest[0][3]/2 + 25
                    else:
                        Treasurechest[0][1] = Orangediver[1] + Orangediver[3]/2 - Treasurechest[0][3]/2 - 25
            if level_complete == False:
                rowdraw(Treasurechest, 0)
        
            if collision(Boat[0], Orangediver, 0) and Treasurechest[0][8] == True:
                    level_complete = True  
                    levels[1] = 1
            
        
####################################################################
################# Singapore Level 2 ###############################
        if level == 2:

            for f in range(4):
                if collision(Clownfish[f], Orangediver, 50):
                    if holding_a_fish == False:
                        Clownfish[f][8] = True
                        holding_a_fish = True              
                if Clownfish[f][8] == True:
                    if greenrise == False:
                        Clownfish[f][7] = Orangediver[7]
                        Clownfish[f][2] = Orangediver[2] + Orangediver[4]/2 - Clownfish[f][4]/2 + 50
                        Clownfish[f][3] = 150
                        Clownfish[f][4] = 100
                        if Orangediver[7]:
                            Clownfish[f][1] = Orangediver[1] + Orangediver[3]/2 - Clownfish[f][3]/2 + 25
                        else:
                            Clownfish[f][1] = Orangediver[1] + Orangediver[3]/2 - Clownfish[f][3]/2 - 25
                    rowdraw(Clownfish, f)
                    
            fishfont = pygame.font.SysFont("monospace", 40, "bold")
            fishtext = fishfont.render('You collected ' + str(fish_collected) + ' fish', 1, (255, 255, 0))
            screen.blit(fishtext, (250, 767 - 60))
            for f in range(4):
                if collision(Boat[0], Orangediver, 75) and Clownfish[f][8] == True:
                    holding_a_fish = False
                    Clownfish[f][8] = False
                    Clownfish[f][1] = -1000
                    Clownfish[f][2] = -1000
                    fish_collected = fish_collected + 1
            if fish_collected == 4:
                level_complete = True
                levels[2] = 1


########################################################
################# Key West Level 11 ###############################
        if level == 11:
            if equipment[11] == 0:
                screen.fill([0,0,0]) 
                darkfont = pygame.font.SysFont("monospace", 30, "bold")
                darktext = darkfont.render('Wow, it is really dark.', 1, (255, 255, 0))
                screen.blit(darktext, (250, 400))    
                #pygame.display.set_gamma(0.0)
########################################################
####  END   ############################################   
    pygame.display.flip()
    clock.tick(30)
pygame.quit ()