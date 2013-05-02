'''
Created on Mar 29, 2013

@author: Dennis
'''
import pygame
import csv#from PIL import GIFImage
import random
import math
#import mixer

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
    global level_3_initialized
    global level_4_initialized
    global level_5_initialized
    global level_6_initialized
    global level_7_initialized
    global level_9_initialized
    global level_10_initialized
    global level_11_initialized
    global level_12_initialized
       
    global left
    global right
    global up
    global down
    global lr_just_pressed
    global ud_just_pressed
    global event
    global orangedead
    for event in pygame.event.get():
        
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
                level_3_initialized = False
                level_4_initialized = False
                level_5_initialized = False
                level_6_initialized = False
                level_7_initialized = False
                level_9_initialized = False
                level_10_initialized = False
                level_11_initialized = False
                level_12_initialized = False
                
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
                level_initialized = False
                level_1_initialized = False
                level_2_initialized = False
                level_3_initialized = False
                level_4_initialized = False
                level_5_initialized = False
                level_6_initialized = False
                level_7_initialized = False
                level_9_initialized = False
                level_10_initialized = False
                level_11_initialized = False
                level_12_initialized = False
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
    global equipment
    
    global numnum
    
    numnum = orangelength*6
    
    kickaccel = 0.5
    
    start_x = pic[1]
    start_y = pic[2]
    x_move_speed = pic[5]
    y_move_speed = pic[6]
    move_direction = pic[7]
    
    ## NO BCD ##
    if equipment[2] == 0:
        y_move_speed = y_move_speed + 0.07
    
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
    
    #speedmaximum = 20
    if equipment[13] == 0:
        speedmaximum = 20
    else:
        speedmaximum = 30
    if x_move_speed > speedmaximum:
        x_move_speed = speedmaximum
    elif x_move_speed < -speedmaximum:
        x_move_speed = -speedmaximum
    if y_move_speed > speedmaximum:
        y_move_speed = speedmaximum
    elif y_move_speed < -speedmaximum:
        y_move_speed = -speedmaximum
    
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
        global equipment
        global Fins
        global orangedead
        global aircap
        global kk
        global downair
        global equipment

        if orangekicking == False:
            if kk == True and orangedead == False:
                downair = True
                kk = False
            Orangediverkick = [Orangediverkick[0], Orangediver[1], Orangediver[2], Orangediver[3], Orangediver[4], Orangediver[5], Orangediver[6], Orangediver[7]]
            if equipment[13] == 0:
                draw(Orangediverkick)
            if equipment[13] == 0:
                if equipment[3] == 1:
                    if orangedead == False:
                        rowdraw(Fins, 1)
            if orangecycles > orangelength:
                orangekicking = True
                orangecycles = 0
        else:
            kk = True
            if equipment[13] == 0:
                draw(Orangediver)
            if equipment[3] == 1:
                if equipment[13] == 0:
                    rowdraw(Fins, 0)
            if orangecycles > orangelength:
                orangekicking = False
                orangecycles = 0
        orangecycles = orangecycles + 1
        if equipment[3] == 1:
            if orangedead:
                if equipment[13] == 0:
                    rowdraw(Fins, 0)
        
def animatedgreen():
        global greenkicking
        global greencycles
        global greenlength
        global Greendiver
        global Greendiverkick
        if greenkicking:
            Greendiverkick = [Greendiverkick[0], Greendiver[1], Greendiver[2], Greendiver[3], Greendiver[4], Greendiver[5], Greendiver[5], Greendiver[7]]
            if equipment[13] == 0:
                draw(Greendiverkick)
            if equipment[3] == 1:
                if equipment[13] == 0:
                    rowdraw(Fins, 3)
            if greencycles > greenlength:
                greenkicking = False
                greencycles = 0
        else:
            if equipment[13] == 0:
                draw(Greendiver)
            if equipment[3] == 1:
                if equipment[13] == 0:
                    rowdraw(Fins, 2)
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
    global numnum
    bubblemax = 0
    if bubblecycles[first] == 0 + offstep:
        if pic[7] == False:
            Bubbles[first][1] = pic[1] + 55 - 30
            Bubbles[first][2] = pic[2] + 60 - 51
        else:
            Bubbles[first][1] = pic[1] - 55 + pic[3]
            Bubbles[first][2] = pic[2] + 60 - 51
    bubblecycles[first] = bubblecycles[first] + 1
    if bubblecycles[first] > 4*numnum:
        bubblecycles[first] = 0
    Bubbles[first][2] = Bubbles[first][2] - Bubbles[first][6]
    bubbledepth = depth - (Orangediver[2] - Bubbles[first][2])
    if bubbledepth < bubblemax:
        Bubbles[first][2] = -10000

    if bubblecycles[first + 1] == numnum + offstep:
        if pic[7] == False:
            Bubbles[first + 1][1] = pic[1] + 55 - 30
            Bubbles[first + 1][2] = pic[2] + 60 - 51
        else:
            Bubbles[first + 1][1] = pic[1] - 55 + pic[3]
            Bubbles[first + 1][2] = pic[2] + 60 - 51
    bubblecycles[first + 1] = bubblecycles[first + 1] + 1
    if bubblecycles[first + 1] > 5*numnum:
        bubblecycles[first + 1] = numnum
    Bubbles[first + 1][2] = Bubbles[first + 1][2] - Bubbles[first + 1][6]
    bubbledepth = depth - (Orangediver[2] - Bubbles[first + 1][2])
    if bubbledepth < bubblemax:
        Bubbles[first + 1][2] = -10000
        
    if bubblecycles[first + 2] == 2*numnum + offstep:
        if pic[7] == False:
            Bubbles[first + 2][1] = pic[1] + 55 - 30
            Bubbles[first + 2][2] = pic[2] + 60 - 51
        else:
            Bubbles[first + 2][1] = pic[1] - 55 + pic[3]
            Bubbles[first + 2][2] = pic[2] + 60 - 51
    bubblecycles[first + 2] = bubblecycles[first + 2] + 1
    if bubblecycles[first + 2] > 6*numnum:
        bubblecycles[first + 2] = 2*numnum
    Bubbles[first + 2][2] = Bubbles[first + 2][2] - Bubbles[first + 2][6]        
    bubbledepth = depth - (Orangediver[2] - Bubbles[first + 2][2])
    if bubbledepth < bubblemax:
        Bubbles[first + 2][2] = -10000
    if bubblecycles[first + 3] == 3*numnum + offstep:
        if pic[7] == False:
            Bubbles[first + 3][1] = pic[1] + 55 - 30
            Bubbles[first + 3][2] = pic[2] + 60 - 51
        else:
            Bubbles[first + 3][1] = pic[1] - 55 + pic[3]
            Bubbles[first + 3][2] = pic[2] + 60 - 51
    bubblecycles[first + 3] = bubblecycles[first + 3] + 1
    if bubblecycles[first + 3] > 7*numnum:
        bubblecycles[first + 3] = 3*numnum
    Bubbles[first + 3][2] = Bubbles[first + 3][2] - Bubbles[first + 3][6] 
    bubbledepth = depth - (Orangediver[2] - Bubbles[first + 3][2])
    if bubbledepth < bubblemax:
            Bubbles[first + 3][2] = -10000        

    for b in range(first, first + 4):
        if greenrise == False:
            Bubbles[b] = rowmovebackground(Bubbles, b, Orangediver)
        rowdraw(Bubbles, b)

onbubble = 0
def newbubbles(pic, bubblepic):
    global bubblecycles
    global Orangediver
    global onbubble
    global equipment
    
    if equipment[13] == 0:
        if pic[7] == False:
            bubblepic[onbubble][1] = pic[1] + 55 - 30
            bubblepic[onbubble][2] = pic[2] + 60 - 51
        else:
            bubblepic[onbubble][1] = pic[1] - 55 + pic[3]
            bubblepic[onbubble][2] = pic[2] + 60 - 51
    else:
        if pic[7] == False:
            bubblepic[onbubble][1] = pic[1] + 55 - 30 + 50
            bubblepic[onbubble][2] = pic[2] + 60 - 51 + 50
        else:
            bubblepic[onbubble][1] = pic[1] - 55 + pic[3] - 50
            bubblepic[onbubble][2] = pic[2] + 60 - 51 + 50
    onbubble = onbubble + 1
    if onbubble > 7:
        onbubble = 0
    

    
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
    global orangeBubbles
    global greenBubbles
    global orangedead
    global greenrise
    global fish_collected
    global Shark
    global Snorkel
    global Goggles
    global BCD
    global Fins
    global Regulator
    global ExtraRegulator
    global AirTank
    global Gauges
    global Wetsuit
    #global Drysuit
    #global Slate
    global Flashlight
    #global Glowstick
    global Scooterdiver
    #global ExtraFlashlight

    Snorkel = [[pygame.transform.rotate(pygame.image.load("Snorkel.png"), -30), 0, 0, 100, 100, 0, 0, True], # 0
           [pygame.transform.rotate(pygame.image.load("Snorkel.png"), -30), 0, 0, 100, 100, 0, 0, True]]

    Goggles = [[pygame.image.load("Gogglesdiver.png"), 0, 0, 63, 40, 0, 0, True], # 1
                  [pygame.image.load("Gogglesdiver.png"), 0, 0, 63, 40, 0, 0, True]]
    
    BCD = [[pygame.image.load("BCDdiver.png"), 0, 0, 70, 50, 0, 0, True], # 2
                  [pygame.image.load("BCDdiver.png"), 0, 0, 70, 50, 0, 0, True]]
    
    Fins = [[pygame.image.load("Finsdiver1.png"), 0, 0, 53, 89, 0, 0, True], # 3
            [pygame.image.load("Finsdiver2.png"), 0, 0, 97, 160, 0, 0, True],
            [pygame.image.load("Finsdiver1.png"), 0, 0, 53, 89, 0, 0, True],
            [pygame.image.load("Finsdiver2.png"), 0, 0, 97, 160, 0, 0, True]]

    Regulator = [[pygame.image.load("Regulatordiver.png"), 0, 0, 45, 20, 0, 0, True], # 4
                  [pygame.image.load("Regulatordiver.png"), 0, 0, 45, 20, 0, 0, True]]
    
    ExtraRegulator = [[pygame.image.load("ExtraRegulatordiver.png"), 0, 0, 50, 45, 0, 0, True], # 5
                  [pygame.image.load("ExtraRegulatordiver.png"), 0, 0, 50, 45, 0, 0, True]]
    
    AirTank = [[pygame.image.load("AirTankdiver.png"), 0, 0, 70, 25, 0, 0, True], # 6
                  [pygame.image.load("AirTankdiver.png"), 0, 0, 70, 25, 0, 0, True]]
    
    Gauges = [[pygame.image.load("Gaugesdiver.png"), 0, 0, 97, 51, 0, 0, True], # 7
                  [pygame.image.load("Gaugesdiver.png"), 0, 0, 97, 51, 0, 0, True]]
    
    Wetsuit = [[pygame.image.load("Wetsuitdiver1.png"), 0, 0, 260, 186, 0, 0, True], # 8
                  [pygame.image.load("Wetsuitdiver2.png"), 0, 0, 260, 186, 0, 0, True]]
    
    #Drysuit = [[pygame.image.load("Drysuitdiver.png"), 0, 0, 100, 100, 0, 0, True], # 9
    #            [pygame.image.load("Drysuitdiver.png"), 0, 0, 100, 100, 0, 0, True]]
    
    #Slate = [[pygame.image.load("Slatediver.png"), 0, 0, 100, 100, 0, 0, True], # 10
    #              [pygame.image.load("Slatediver.png"), 0, 0, 100, 100, 0, 0, True]]
    
    Flashlight = [[pygame.image.load("Flashlight.png"), 0, 0, 100, 100, 0, 0, True], # 11
                  [pygame.image.load("Flashlight.png"), 0, 0, 100, 100, 0, 0, True]]
    
    #Glowstick = [[pygame.image.load("Glowstickdiver.png"), 0, 0, 100, 100, 0, 0, True], # 12
    #              [pygame.image.load("Glowstickdiver.png"), 0, 0, 100, 100, 0, 0, True]]
    
    Scooterdiver = [[pygame.image.load("Scooterdiver.png"), 0, 0, 250, 250, 0, 0, True], # 13
                  [pygame.image.load("Scooterdiver2.png"), 0, 0, 250, 250, 0, 0, True]]
    
    #ExtraFlashlight = [[pygame.image.load("ExtraFlashlightdiver.png"), 0, 0, 100, 100, 0, 0, True], # 14
    #              [pygame.image.load("ExtraFlashlightdiver.png"), 0, 0, 100, 100, 0, 0, True]]
    

    
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
    
    orangeBubbles = [[pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False]]
    
    greenBubbles = [[pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                     [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False]]

########Air Consumption##########################

#################################################
#################################################################

def Level0():
    global level
    global Islandbutton
    global Treasuremap
    global levels
    global MONEY
    global levelsdone
    global Clueback
    
    ## Level Limit is the number of times the player can do the level and earn money ###
    levellimit = 1
    if levels[1] == 1 and levelsdone[1] < levellimit:
        MONEY = MONEY + 200
        levels[1] = 0
        levelsdone[1] = levelsdone[1] + 1
        
    if levels[2] == 1 and levelsdone[2] < 1000:
        MONEY = MONEY + 150
        levels[2] = 0
        levelsdone[2] = 0
   
    if levels[3] == 1 and levelsdone[3] < levellimit:
        MONEY = MONEY + 200
        levels[3] = 0
        levelsdone[3] = levelsdone[3] + 1
        
    if levels[4] == 1 and levelsdone[4] < levellimit:
        MONEY = MONEY + 250
        levels[4] = 0
        levelsdone[4] = levelsdone[4] + 1
        
    if levels[5] == 1 and levelsdone[5] < levellimit:
        MONEY = MONEY + 150
        levels[5] = 0
        levelsdone[5] = levelsdone[5] + 1
    
    if levels[6] == 1 and levelsdone[6] < 1000000:
        MONEY = MONEY + 500
        levels[6] = 0
        levelsdone[6] = 0
    
    if levels[7] == 1 and levelsdone[7] < levellimit:
        MONEY = MONEY + 150
        levels[7] = 0
        levelsdone[7] = levelsdone[7] + 1
    
    if levels[9] == 1 and levelsdone[9] < 1000000000:
        MONEY = MONEY + 400
        levels[9] = 0
        levelsdone[9] = 0
    
    if levels[10] == 1 and levelsdone[10] < levellimit:
        MONEY = MONEY + 500
        levels[10] = 0
        levelsdone[10] = levelsdone[10] + 1
    
    if levels[11] == 1 and levelsdone[11] < levellimit:
        MONEY = MONEY + 300
        levels[11] = 0
        levelsdone[11] = levelsdone[11] + 1
    
    if levels[12] == 1 and levelsdone[12] < levellimit:
        MONEY = MONEY + 100000
        levels[12] = 0
        levelsdone[12] = levelsdone[12] + 1
        
    
            
    pygame.mouse.set_visible(1)
    draw(Treasuremap)
    Controls = [Islandbutton[0], 10, 10, 100, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Controls)
    if clicked(Controls):
        level = -2
    controlsfont = pygame.font.SysFont("monospace", 20, "bold")
    controlstext = controlsfont.render('Controls', 1, (0, 0, 0))
    screen.blit(controlstext, (10, 40))
  
    cluecolor = (0, 0, 0)
    if levelsdone.count(1) == 0:
        Clueback = [Clueback[0], 130, 0, 600, 50, 0, 0, True] 
        draw(Clueback)
        cluesfont = pygame.font.SysFont("monospace", 30, "bold")
        cluestext = cluesfont.render('We need to find some clues', 1, cluecolor)
        screen.blit(cluestext, (150, 10))
    elif levelsdone.count(1) == 1:
        Clueback = [Clueback[0], 130, 0, 750, 50, 0, 0, True] 
        draw(Clueback)
        cluesfont = pygame.font.SysFont("monospace", 30, "bold")
        cluestext = cluesfont.render('We still need to find more clues', 1, cluecolor)
        screen.blit(cluestext, (150, 10))
    elif levelsdone.count(1) == 2:
        Clueback = [Clueback[0], 130, 0, 750, 50, 0, 0, True] 
        draw(Clueback)
        cluesfont = pygame.font.SysFont("monospace", 30, "bold")
        cluestext = cluesfont.render('We just need one more clue', 1, cluecolor)
        screen.blit(cluestext, (150, 10))
    elif levelsdone.count(1) > 2:
        Clueback = [Clueback[0], 130, 0, 750, 90, 0, 0, True] 
        draw(Clueback)
        cluesfont = pygame.font.SysFont("monospace", 30, "bold")
        cluestext = cluesfont.render('The clues point to a sight ', 1, cluecolor)
        cluestext2 = cluesfont.render('west of Santiago', 1, cluecolor)
        screen.blit(cluestext, (150, 10))
        screen.blit(cluestext2, (150, 45))


    Closet = [Islandbutton[0], 180, 290, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Closet)
    if clicked(Closet):
        level = 50
    Closetfont = pygame.font.SysFont("monospace", 15, "bold")
    Closettext = Closetfont.render('Closet', 1, (0, 0, 0))
    screen.blit(Closettext, (120, 290))
    
    Outerbanks = [Islandbutton[0], 245, 330, 25, 25, 0, 0, True]  # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Outerbanks)
    if clicked(Outerbanks):
        MONEY = MONEY - 50
        level = 1
        pygame.mouse.set_visible(0)
    Singapore = [Islandbutton[0], 760, 425, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Singapore)
    if clicked(Singapore):
        MONEY = MONEY - 50
        level = 2
        pygame.mouse.set_visible(0)
    Sydney = [Islandbutton[0], 885, 560, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Sydney)
    if clicked(Sydney):
        MONEY = MONEY - 50
        level = 3
        pygame.mouse.set_visible(0)
    Panama = [Islandbutton[0], 260, 415, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Panama)
    if clicked(Panama):
        MONEY = MONEY - 50
        level = 4
        pygame.mouse.set_visible(0)
    SanDiego = [Islandbutton[0], 155, 335, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(SanDiego)
    if clicked(SanDiego):
        MONEY = MONEY - 50
        level = 5
        pygame.mouse.set_visible(0)
    Tokyo = [Islandbutton[0], 860, 325, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Tokyo)
    if clicked(Tokyo):
        MONEY = MONEY - 50
        level = 6
        pygame.mouse.set_visible(0)
    CapeTown = [Islandbutton[0], 535, 555, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(CapeTown)
    if clicked(CapeTown):
        MONEY = MONEY - 50
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
        MONEY = MONEY - 50
        level = 9
        pygame.mouse.set_visible(0)
    Antarctica = [Islandbutton[0], 630, 695, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Antarctica)
    if clicked(Antarctica):
        MONEY = MONEY - 50
        level = 10
        pygame.mouse.set_visible(0)
    KeyWest = [Islandbutton[0], 243, 363, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(KeyWest)
    if clicked(KeyWest):
        MONEY = MONEY - 50
        level = 11
        pygame.mouse.set_visible(0)
    Unknown = [Islandbutton[0], 123, 567, 25, 25, 0, 0, True] # list = [image, x pos, y pos, x size, y size, x speed, y speed, right]
    draw(Unknown)
    if clicked(Unknown):
        MONEY = MONEY - 50
        level = 12
        pygame.mouse.set_visible(0)

fakemoney = 10000000000 
def Level50():
    global level
    global Islandbutton
    global Shelves
    global equipment
    global fakemoney
    global levels
    global boughtequipment
    global everequipment
    
    ### Level Limit is the number of times the player can do the level and earn money ###
 
    pygame.mouse.set_visible(1)
    draw(Closetshelves)
    pricefont = pygame.font.SysFont("monospace", 15, "bold")
    infofont = pygame.font.SysFont("monospace", 30, "bold")

    pricecolor = [250, 250, 0]
    infocolor = [255, 255, 255]
    infopos = [100, 50]

    ### Snorkel ###
    if boughtequipment[0]:
        snorkelprice = 20
        #snorkeltext = pricefont.render('Snorkel: $' + str(snorkelprice), 1, (pricecolor))
        #screen.blit(snorkeltext, (320, 420))
        
        if equipment[0] == 0:
            ShopSnorkel = [pygame.image.load("Snorkel.png"), 320, 320, 100, 100, 0, 0, True]
            draw(ShopSnorkel)
            if fakemoney >= snorkelprice and clicked(ShopSnorkel):
                equipment[0] = 1
                fakemoney = fakemoney - snorkelprice
        else:
            ShopSnorkel = [pygame.image.load("Snorkel.png"), 320, 650, 50, 50, 0, 0, True]
            draw(ShopSnorkel)
            if clicked(ShopSnorkel):
                equipment[0] = 0
                fakemoney = fakemoney + snorkelprice
        if mouseover(ShopSnorkel):
            snorkelinfotext = infofont.render('Snorkels conserve air at the surface', 1, (infocolor))
            screen.blit(snorkelinfotext, (infopos))

    ### Goggles ###
    if boughtequipment[1]:
        Gogglesprice = 20
        #Gogglestext = pricefont.render('Goggles: $' + str(Gogglesprice), 1, (pricecolor))
        #screen.blit(Gogglestext, (480, 420))
        if equipment[1] == 0:
            ShopGoggles = [pygame.image.load("Goggles.jpg"), 480, 320, 100, 75, 0, 0, True]
            draw(ShopGoggles)
            if fakemoney >= Gogglesprice and clicked(ShopGoggles):
                equipment[1] = 1
                fakemoney = fakemoney - Gogglesprice
        else:
            ShopGoggles = [pygame.image.load("Goggles.jpg"), 480, 650, 50, 30, 0, 0, True]
            draw(ShopGoggles)
            if clicked(ShopGoggles):
                equipment[1] = 0
                fakemoney = fakemoney + Gogglesprice
        if mouseover(ShopGoggles):
            Gogglesinfotext = infofont.render('You need goggles to see underwater', 1, (infocolor))
            screen.blit(Gogglesinfotext, (infopos))  
            
    ### Flashlight ###
    if boughtequipment[11]:
        flashlightprice = 100
        #flashlighttext = pricefont.render('Light: $' + str(flashlightprice), 1, (pricecolor))
        #screen.blit(flashlighttext, (640, 420))
        if equipment[11] == 0:
            ShopFlashlight = [pygame.image.load("Flashlight.png"), 640, 320, 100, 100, 0, 0, True] # 11
            draw(ShopFlashlight)
            if fakemoney >= flashlightprice and clicked(ShopFlashlight):
                equipment[11] = 1
                fakemoney = fakemoney - flashlightprice
        else:
            ShopFlashlight = [pygame.image.load("Flashlight.png"), 640, 650, 50, 50, 0, 0, True] # 11
            draw(ShopFlashlight)  
            if clicked(ShopFlashlight):
                equipment[11] = 0
                fakemoney = fakemoney + flashlightprice
        if mouseover(ShopFlashlight):
            Flashlightinfotext = infofont.render('You need a flashlight when night diving', 1, (infocolor))
            screen.blit(Flashlightinfotext, (infopos))

    ### BCD ###
    if boughtequipment[2]:
        BCDprice = 300
        #BCDtext = pricefont.render('BCD: $' + str(BCDprice), 1, (pricecolor))
        #screen.blit(BCDtext, (250, 220))
        if equipment[2] == 0:
            ShopBCD = [pygame.image.load("BCD.jpg"), 250, 120 - 25, 100, 125, 0, 0, True]
            draw(ShopBCD)
            if fakemoney >= BCDprice and clicked(ShopBCD):
                equipment[2] = 1
                fakemoney = fakemoney - BCDprice
        else:
            ShopBCD = [pygame.image.load("BCD.jpg"), 250, 600, 50, 60, 0, 0, True]
            draw(ShopBCD)   
            if clicked(ShopBCD):
                equipment[2] = 0
                fakemoney = fakemoney + BCDprice
        if mouseover(ShopBCD):
            BCDinfotext = infofont.render('Buoyancy Control Devices control buoyancy', 1, (infocolor))
            screen.blit(BCDinfotext, (infopos))
        
    ### Fins ###
    if boughtequipment[3]:
        Finsprice = 200
        #Finstext = pricefont.render('Fins: $' + str(Finsprice), 1, (pricecolor))
        #screen.blit(Finstext, (420, 220))
        if equipment[3] == 0:
            ShopFins = [pygame.image.load("Fins.jpg"), 420 - 25, 120, 150, 100, 0, 0, True]
            draw(ShopFins)
            if fakemoney >= Finsprice and clicked(ShopFins):
                equipment[3] = 1
                fakemoney = fakemoney - Finsprice
        else:
            ShopFins = [pygame.image.load("Fins.jpg"), 420, 600, 75, 50, 0, 0, True]
            draw(ShopFins)   
            if clicked(ShopFins):
                equipment[3] = 0
                fakemoney = fakemoney + Finsprice
        if mouseover(ShopFins):
            Finsinfotext = infofont.render('You need fins to swim', 1, (infocolor))
            screen.blit(Finsinfotext, (infopos))
         
    ### Regulator ###
    if boughtequipment[4]:
        Regulatorprice = 200
        #Regulatortext = pricefont.render('Regulator: $' + str(Regulatorprice), 1, (pricecolor))
        #screen.blit(Regulatortext, (590, 220))
        if equipment[4] == 0:
            ShopRegulator = [pygame.image.load("Regulator.jpg"), 590, 120, 100, 100, 0, 0, True]
            draw(ShopRegulator)
            if fakemoney >= Regulatorprice and clicked(ShopRegulator):
                equipment[4] = 1
                fakemoney = fakemoney - Regulatorprice
        else:
            ShopRegulator = [pygame.image.load("Regulator.jpg"), 590, 600, 50, 50, 0, 0, True]
            draw(ShopRegulator)
            if clicked(ShopRegulator):
                equipment[4] = 0
                fakemoney = fakemoney + Regulatorprice
        if mouseover(ShopRegulator):
            Regulatorinfotext = infofont.render('You need a regulator to breathe', 1, (infocolor))
            screen.blit(Regulatorinfotext, (infopos))   
       
    ### ExtraRegulator ###
    if boughtequipment[5]:
        ExtraRegulatorprice = 200
        #ExtraRegulatortext = pricefont.render('2nd Regulator: $' + str(ExtraRegulatorprice), 1, (pricecolor))
        #screen.blit(ExtraRegulatortext, (590, 560))
        if equipment[5] == 0:
            ShopExtraRegulator = [pygame.transform.flip(pygame.image.load("Regulator.jpg"), True, False), 590, 460, 100, 100, 0, 0, True]
            draw(ShopExtraRegulator)
            if fakemoney >= ExtraRegulatorprice and clicked(ShopExtraRegulator):
                equipment[5] = 1
                fakemoney = fakemoney - ExtraRegulatorprice
        else:
            ShopExtraRegulator = [pygame.transform.flip(pygame.image.load("Regulator.jpg"), True, False), 590, 700, 50, 50, 0, 0, True]
            draw(ShopExtraRegulator)
            if clicked(ShopExtraRegulator):
                equipment[5] = 0
                fakemoney = fakemoney + ExtraRegulatorprice
        if mouseover(ShopExtraRegulator):
            ExtraRegulatorinfotext = infofont.render('You need an extra regulator just in case', 1, (infocolor))
            screen.blit(ExtraRegulatorinfotext, (infopos))
        
    ### AirTank ###
    if boughtequipment[6]:
        AirTankprice = 250
        #AirTanktext = pricefont.render('Air Tank: $' + str(AirTankprice), 1, (pricecolor))
        #screen.blit(AirTanktext, (420, 560))
        if equipment[6] == 0:
            ShopAirTank = [pygame.image.load("AirTank.jpg"), 420 + 25, 460 - 25, 50, 125, 0, 0, True]
            draw(ShopAirTank)
            if fakemoney >= AirTankprice and clicked(ShopAirTank):
                equipment[6] = 1
                fakemoney = fakemoney - AirTankprice
        else:
            ShopAirTank = [pygame.image.load("AirTank.jpg"), 420, 700 - 20, 35, 75, 0, 0, True]
            draw(ShopAirTank)   
            if clicked(ShopAirTank):
                equipment[6] = 0
                fakemoney = fakemoney + AirTankprice  
        if mouseover(ShopAirTank):
            AirTankinfotext = infofont.render('You need an Air Tank for air', 1, (infocolor))
            screen.blit(AirTankinfotext, (infopos)) 

    ### Gauges ###
    if boughtequipment[7]:
        Gaugesprice = 150
        #Gaugestext = pricefont.render('Gauges: $' + str(Gaugesprice), 1, (pricecolor))
        #screen.blit(Gaugestext, (250, 560))
        if equipment[7] == 0:
            ShopGauges = [pygame.image.load("Gauges.jpg"), 250 + 30, 460, 50, 100, 0, 0, True]
            draw(ShopGauges)
            if fakemoney >= Gaugesprice and clicked(ShopGauges):
                equipment[7] = 1
                fakemoney = fakemoney - Gaugesprice
        else:
            ShopGauges = [pygame.image.load("Gauges.jpg"), 250, 700, 25, 50, 0, 0, True]
            draw(ShopGauges)
            if clicked(ShopGauges):
                equipment[7] = 0
                fakemoney = fakemoney + Gaugesprice
        if mouseover(ShopGauges):
            Gaugesinfotext = infofont.render('Gauges display depth and tank pressure', 1, (infocolor))
            screen.blit(Gaugesinfotext, (infopos))
                 
    ### Wetsuit ###
    if boughtequipment[8]:
        Wetsuitprice = 200
        #Wetsuittext = pricefont.render('Wetsuit: $' + str(Wetsuitprice), 1, (pricecolor))
        #screen.blit(Wetsuittext, (101, 280))
        if equipment[8] == 0:
            ShopWetsuit = [pygame.image.load("Wetsuit.jpg"), 101, 180 + 50, 100, 50, 0, 0, True]
            draw(ShopWetsuit)
            if fakemoney >= Wetsuitprice and clicked(ShopWetsuit):
                equipment[8] = 1
                fakemoney = fakemoney - Wetsuitprice
        else:
            ShopWetsuit = [pygame.image.load("Wetsuit.jpg"), 11, 600, 50, 25, 0, 0, True]
            draw(ShopWetsuit)  
            if clicked(ShopWetsuit):
                equipment[8] = 0
                fakemoney = fakemoney + Wetsuitprice
        if mouseover(ShopWetsuit):
            Wetsuitinfotext = infofont.render('Wetsuits prevent cold and scratches', 1, (infocolor))
            screen.blit(Wetsuitinfotext, (infopos)) 
        
    ### Drysuit ###
    if boughtequipment[9]:
        Drysuitprice = 900
        #Drysuittext = pricefont.render('Dry Suit: $' + str(Drysuitprice), 1, (pricecolor))
        #screen.blit(Drysuittext, (101, 480))
        if equipment[9] == 0:
            ShopDrysuit = [pygame.image.load("Drysuit.jpg"), 101, 380 + 50, 100, 50, 0, 0, True]
            draw(ShopDrysuit)
            if fakemoney >= Drysuitprice and clicked(ShopDrysuit):
                equipment[9] = 1
                fakemoney = fakemoney - Drysuitprice
        else:
            ShopDrysuit = [pygame.image.load("Drysuit.jpg"), 11, 650, 50, 25, 0, 0, True]
            draw(ShopDrysuit)  
            if clicked(ShopDrysuit):
                equipment[9] = 0
                fakemoney = fakemoney + Drysuitprice
        if mouseover(ShopDrysuit):
            Drysuitinfotext = infofont.render('Drysuits for extremely cold environments', 1, (infocolor))
            screen.blit(Drysuitinfotext, (infopos)) 
        
    ### Slate ###
    if boughtequipment[10]:
        Slateprice = 10
        #Slatetext = pricefont.render('Slate: $' + str(Slateprice), 1, (pricecolor))
        #screen.blit(Slatetext, (101, 680))
        if equipment[10] == 0:
            ShopSlate = [pygame.image.load("Slate.jpg"), 101, 580, 75, 100, 0, 0, True]
            draw(ShopSlate)
            if fakemoney >= Slateprice and clicked(ShopSlate):
                equipment[10] = 1
                fakemoney = fakemoney - Slateprice
        else:
            ShopSlate = [pygame.image.load("Slate.jpg"), 11, 700, 30, 50, 0, 0, True]
            draw(ShopSlate) 
            if clicked(ShopSlate):
                equipment[10] = 0
                fakemoney = fakemoney + Slateprice  
        if mouseover(ShopSlate):
            Slateinfotext = infofont.render('Slates let you write messages to your buddy', 1, (infocolor))
            screen.blit(Slateinfotext, (infopos)) 

    ### Glowstick ###
    if boughtequipment[12]:
        Glowstickprice = 5
        #Glowsticktext = pricefont.render('Glowstick: $' + str(Glowstickprice), 1, (pricecolor))
        #screen.blit(Glowsticktext, (840, 280))
        if equipment[12] == 0:
            ShopGlowstick = [pygame.image.load("Glowstick.jpg"), 840 + 25, 180, 30, 100, 0, 0, True]
            draw(ShopGlowstick)
            if fakemoney >= Glowstickprice and clicked(ShopGlowstick):
                equipment[12] = 1
                fakemoney = fakemoney - Glowstickprice
        else:
            ShopGlowstick = [pygame.image.load("Glowstick.jpg"), 1024 - 50 - 11, 600, 15, 50, 0, 0, True]
            draw(ShopGlowstick) 
            if clicked(ShopGlowstick):
                equipment[12] = 0
                fakemoney = fakemoney + Glowstickprice
        if mouseover(ShopGlowstick):
            Glowstickinfotext = infofont.render('Glow Sticks let you keep you buddy in sight on night dives', 1, (infocolor))
            screen.blit(Glowstickinfotext, (infopos))  
        
    ### Scooter ###
    if boughtequipment[13]:
        Scooterprice = 2000
        #Scootertext = pricefont.render('Scooter: $' + str(Scooterprice), 1, (pricecolor))
        #screen.blit(Scootertext, (840, 480))
        if equipment[13] == 0:
            ShopScooter = [pygame.image.load("Scooter.jpg"), 840, 380, 100, 100, 0, 0, True]
            draw(ShopScooter)
            if fakemoney >= Scooterprice and clicked(ShopScooter):
                equipment[13] = 1
                fakemoney = fakemoney - Scooterprice
        else:
            ShopScooter = [pygame.image.load("Scooter.jpg"), 1024 - 50 - 11, 650, 50, 50, 0, 0, True]
            draw(ShopScooter)   
            if clicked(ShopScooter):
                equipment[13] = 0
                fakemoney = fakemoney + Scooterprice
        if mouseover(ShopScooter):
            Scooterinfotext = infofont.render('Under water scooters can be a lot of fun', 1, (infocolor))
            screen.blit(Scooterinfotext, (infopos))
            
    ### ExtraFlashlight ###
    if boughtequipment[14]:
        ExtraFlashlightprice = 40
        #ExtraFlashlighttext = pricefont.render('2nd Light: $' + str(ExtraFlashlightprice), 1, (pricecolor))
        #screen.blit(ExtraFlashlighttext, (840, 680))
        if equipment[14] == 0:
            ShopExtraFlashlight = [pygame.transform.flip(pygame.image.load("Flashlight.png"), True, True), 840 + 20, 580, 75, 75, 0, 0, True]
            draw(ShopExtraFlashlight)
            if fakemoney >= ExtraFlashlightprice and clicked(ShopExtraFlashlight):
                equipment[14] = 1
                fakemoney = fakemoney - ExtraFlashlightprice
        else:
            ShopExtraFlashlight = [pygame.transform.flip(pygame.image.load("Flashlight.png"), True, True), 1024 - 50 - 11, 700, 50, 50, 0, 0, True]
            draw(ShopExtraFlashlight)
            if clicked(ShopExtraFlashlight):
                equipment[14] = 0
                fakemoney = fakemoney + ExtraFlashlightprice
        if mouseover(ShopExtraFlashlight):
            ExtraFlashlightinfotext = infofont.render('Carry an extra light on night dives', 1, (infocolor))
            screen.blit(ExtraFlashlightinfotext, (infopos))

    for i in range(15):
        if everequipment[i] == 0:
            if equipment[i] == 1:
                everequipment[i] = 1

  
def Level8():
    global level
    global Islandbutton
    global Shelves
    global boughtequipment
    global MONEY
    global levels
    
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
    
    if boughtequipment[0] == 0 and everequipment[0] == 0:
        ShopSnorkel = [pygame.image.load("Snorkel.png"), 320, 320, 100, 100, 0, 0, True]
        draw(ShopSnorkel)
        if MONEY >= snorkelprice and clicked(ShopSnorkel):
            boughtequipment[0] = 1
            MONEY = MONEY - snorkelprice
    else:
        ShopSnorkel = [pygame.image.load("Snorkel.png"), 320, 650, 50, 50, 0, 0, True]
        draw(ShopSnorkel)
        if clicked(ShopSnorkel) and everequipment[0] == 0:
            boughtequipment[0] = 0
            MONEY = MONEY + snorkelprice
    if mouseover(ShopSnorkel):
        snorkelinfotext = infofont.render('Snorkels conserve air at the surface', 1, (infocolor))
        screen.blit(snorkelinfotext, (infopos))

    ### Goggles ###
    Gogglesprice = 20
    Gogglestext = pricefont.render('Goggles: $' + str(Gogglesprice), 1, (pricecolor))
    screen.blit(Gogglestext, (480, 420))
    if boughtequipment[1] == 0 and everequipment[1] == 0:
        ShopGoggles = [pygame.image.load("Goggles.jpg"), 480, 320, 100, 75, 0, 0, True]
        draw(ShopGoggles)
        if MONEY >= Gogglesprice and clicked(ShopGoggles):
            boughtequipment[1] = 1
            MONEY = MONEY - Gogglesprice
    else:
        ShopGoggles = [pygame.image.load("Goggles.jpg"), 480, 650, 50, 30, 0, 0, True]
        draw(ShopGoggles)
        if clicked(ShopGoggles) and everequipment[1] == 0:
            boughtequipment[1] = 0
            MONEY = MONEY + Gogglesprice
    if mouseover(ShopGoggles):
        Gogglesinfotext = infofont.render('You need goggles to see underwater', 1, (infocolor))
        screen.blit(Gogglesinfotext, (infopos))  
        
    ### Flashlight ###
    flashlightprice = 100
    flashlighttext = pricefont.render('Light: $' + str(flashlightprice), 1, (pricecolor))
    screen.blit(flashlighttext, (640, 420))
    if boughtequipment[11] == 0 and everequipment[11] == 0:
        ShopFlashlight = [pygame.image.load("Flashlight.png"), 640, 320, 100, 100, 0, 0, True] # 11
        draw(ShopFlashlight)
        if MONEY >= flashlightprice and clicked(ShopFlashlight):
            boughtequipment[11] = 1
            MONEY = MONEY - flashlightprice
    else:
        ShopFlashlight = [pygame.image.load("Flashlight.png"), 640, 650, 50, 50, 0, 0, True] # 11
        draw(ShopFlashlight)  
        if clicked(ShopFlashlight) and everequipment[11] == 0:
            boughtequipment[11] = 0
            MONEY = MONEY + flashlightprice
    if mouseover(ShopFlashlight):
        Flashlightinfotext = infofont.render('You need a flashlight when night diving', 1, (infocolor))
        screen.blit(Flashlightinfotext, (infopos))

    ### BCD ###
    BCDprice = 300
    BCDtext = pricefont.render('BCD: $' + str(BCDprice), 1, (pricecolor))
    screen.blit(BCDtext, (250, 220))
    if boughtequipment[2] == 0 and everequipment[2] == 0:
        ShopBCD = [pygame.image.load("BCD.jpg"), 250, 120 - 25, 100, 125, 0, 0, True]
        draw(ShopBCD)
        if MONEY >= BCDprice and clicked(ShopBCD):
            boughtequipment[2] = 1
            MONEY = MONEY - BCDprice
    else:
        ShopBCD = [pygame.image.load("BCD.jpg"), 250, 600, 50, 60, 0, 0, True]
        draw(ShopBCD)   
        if clicked(ShopBCD) and everequipment[2] == 0:
            boughtequipment[2] = 0
            MONEY = MONEY + BCDprice
    if mouseover(ShopBCD):
        BCDinfotext = infofont.render('Buoyancy Control Devices control buoyancy', 1, (infocolor))
        screen.blit(BCDinfotext, (infopos))
        
    ### Fins ###
    Finsprice = 200
    Finstext = pricefont.render('Fins: $' + str(Finsprice), 1, (pricecolor))
    screen.blit(Finstext, (420, 220))
    if boughtequipment[3] == 0 and everequipment[3] == 0:
        ShopFins = [pygame.image.load("Fins.jpg"), 420 - 25, 120, 150, 100, 0, 0, True]
        draw(ShopFins)
        if MONEY >= Finsprice and clicked(ShopFins):
            boughtequipment[3] = 1
            MONEY = MONEY - Finsprice
    else:
        ShopFins = [pygame.image.load("Fins.jpg"), 420, 600, 75, 50, 0, 0, True]
        draw(ShopFins)   
        if clicked(ShopFins) and everequipment[3] == 0:
            boughtequipment[3] = 0
            MONEY = MONEY + Finsprice
    if mouseover(ShopFins):
        Finsinfotext = infofont.render('You need fins to swim', 1, (infocolor))
        screen.blit(Finsinfotext, (infopos))
         
    ### Regulator ###
    Regulatorprice = 200
    Regulatortext = pricefont.render('Regulator: $' + str(Regulatorprice), 1, (pricecolor))
    screen.blit(Regulatortext, (590, 220))
    if boughtequipment[4] == 0 and everequipment[4] == 0:
        ShopRegulator = [pygame.image.load("Regulator.jpg"), 590, 120, 100, 100, 0, 0, True]
        draw(ShopRegulator)
        if MONEY >= Regulatorprice and clicked(ShopRegulator):
            boughtequipment[4] = 1
            MONEY = MONEY - Regulatorprice
    else:
        ShopRegulator = [pygame.image.load("Regulator.jpg"), 590, 600, 50, 50, 0, 0, True]
        draw(ShopRegulator)
        if clicked(ShopRegulator) and everequipment[4] == 0:
            boughtequipment[4] = 0
            MONEY = MONEY + Regulatorprice
    if mouseover(ShopRegulator):
        Regulatorinfotext = infofont.render('You need a regulator to breathe', 1, (infocolor))
        screen.blit(Regulatorinfotext, (infopos))   
       
    ### ExtraRegulator ###
    ExtraRegulatorprice = 200
    ExtraRegulatortext = pricefont.render('2nd Regulator: $' + str(ExtraRegulatorprice), 1, (pricecolor))
    screen.blit(ExtraRegulatortext, (590, 560))
    if boughtequipment[5] == 0 and everequipment[5] == 0:
        ShopExtraRegulator = [pygame.transform.flip(pygame.image.load("Regulator.jpg"), True, False), 590, 460, 100, 100, 0, 0, True]
        draw(ShopExtraRegulator)
        if MONEY >= ExtraRegulatorprice and clicked(ShopExtraRegulator):
            boughtequipment[5] = 1
            MONEY = MONEY - ExtraRegulatorprice
    else:
        ShopExtraRegulator = [pygame.transform.flip(pygame.image.load("Regulator.jpg"), True, False), 590, 700, 50, 50, 0, 0, True]
        draw(ShopExtraRegulator)
        if clicked(ShopExtraRegulator) and everequipment[5] == 0:
            boughtequipment[5] = 0
            MONEY = MONEY + ExtraRegulatorprice
    if mouseover(ShopExtraRegulator):
        ExtraRegulatorinfotext = infofont.render('You need an extra regulator just in case', 1, (infocolor))
        screen.blit(ExtraRegulatorinfotext, (infopos))
        
    ### AirTank ###
    AirTankprice = 250
    AirTanktext = pricefont.render('Air Tank: $' + str(AirTankprice), 1, (pricecolor))
    screen.blit(AirTanktext, (420, 560))
    if boughtequipment[6] == 0 and everequipment[6] == 0:
        ShopAirTank = [pygame.image.load("AirTank.jpg"), 420 + 25, 460 - 25, 50, 125, 0, 0, True]
        draw(ShopAirTank)
        if MONEY >= AirTankprice and clicked(ShopAirTank):
            boughtequipment[6] = 1
            MONEY = MONEY - AirTankprice
    else:
        ShopAirTank = [pygame.image.load("AirTank.jpg"), 420, 700 - 20, 35, 75, 0, 0, True]
        draw(ShopAirTank)   
        if clicked(ShopAirTank) and everequipment[6] == 0:
            boughtequipment[6] = 0
            MONEY = MONEY + AirTankprice  
    if mouseover(ShopAirTank):
        AirTankinfotext = infofont.render('You need an Air Tank for air', 1, (infocolor))
        screen.blit(AirTankinfotext, (infopos)) 

    ### Gauges ###
    Gaugesprice = 150
    Gaugestext = pricefont.render('Gauges: $' + str(Gaugesprice), 1, (pricecolor))
    screen.blit(Gaugestext, (250, 560))
    if boughtequipment[7] == 0 and everequipment[7] == 0:
        ShopGauges = [pygame.image.load("Gauges.jpg"), 250 + 30, 460, 50, 100, 0, 0, True]
        draw(ShopGauges)
        if MONEY >= Gaugesprice and clicked(ShopGauges):
            boughtequipment[7] = 1
            MONEY = MONEY - Gaugesprice
    else:
        ShopGauges = [pygame.image.load("Gauges.jpg"), 250, 700, 25, 50, 0, 0, True]
        draw(ShopGauges)
        if clicked(ShopGauges) and everequipment[7] == 0:
            boughtequipment[7] = 0
            MONEY = MONEY + Gaugesprice
    if mouseover(ShopGauges):
        Gaugesinfotext = infofont.render('Gauges display depth and tank pressure', 1, (infocolor))
        screen.blit(Gaugesinfotext, (infopos))
             
    ### Wetsuit ###
    Wetsuitprice = 200
    Wetsuittext = pricefont.render('Wetsuit: $' + str(Wetsuitprice), 1, (pricecolor))
    screen.blit(Wetsuittext, (101, 280))
    if boughtequipment[8] == 0 and everequipment[8] == 0:
        ShopWetsuit = [pygame.image.load("Wetsuit.jpg"), 101, 180 + 50, 100, 50, 0, 0, True]
        draw(ShopWetsuit)
        if MONEY >= Wetsuitprice and clicked(ShopWetsuit):
            boughtequipment[8] = 1
            MONEY = MONEY - Wetsuitprice
    else:
        ShopWetsuit = [pygame.image.load("Wetsuit.jpg"), 11, 600, 50, 25, 0, 0, True]
        draw(ShopWetsuit)  
        if clicked(ShopWetsuit) and everequipment[8] == 0:
            boughtequipment[8] = 0
            MONEY = MONEY + Wetsuitprice
    if mouseover(ShopWetsuit):
        Wetsuitinfotext = infofont.render('Wetsuits prevent cold and scratches', 1, (infocolor))
        screen.blit(Wetsuitinfotext, (infopos)) 
        
    ### Drysuit ###
    Drysuitprice = 900
    Drysuittext = pricefont.render('Dry Suit: $' + str(Drysuitprice), 1, (pricecolor))
    screen.blit(Drysuittext, (101, 480))
    if boughtequipment[9] == 0 and everequipment[9] == 0:
        ShopDrysuit = [pygame.image.load("Drysuit.jpg"), 101, 380 + 50, 100, 50, 0, 0, True]
        draw(ShopDrysuit)
        if MONEY >= Drysuitprice and clicked(ShopDrysuit):
            boughtequipment[9] = 1
            MONEY = MONEY - Drysuitprice
    else:
        ShopDrysuit = [pygame.image.load("Drysuit.jpg"), 11, 650, 50, 25, 0, 0, True]
        draw(ShopDrysuit)  
        if clicked(ShopDrysuit) and everequipment[9] == 0:
            boughtequipment[9] = 0
            MONEY = MONEY + Drysuitprice
    if mouseover(ShopDrysuit):
        Drysuitinfotext = infofont.render('Drysuits for extremely cold environments', 1, (infocolor))
        screen.blit(Drysuitinfotext, (infopos)) 
        
    ### Slate ###
    Slateprice = 10
    Slatetext = pricefont.render('Slate: $' + str(Slateprice), 1, (pricecolor))
    screen.blit(Slatetext, (101, 680))
    if boughtequipment[10] == 0 and everequipment[10] == 0:
        ShopSlate = [pygame.image.load("Slate.jpg"), 101, 580, 75, 100, 0, 0, True]
        draw(ShopSlate)
        if MONEY >= Slateprice and clicked(ShopSlate):
            boughtequipment[10] = 1
            MONEY = MONEY - Slateprice
    else:
        ShopSlate = [pygame.image.load("Slate.jpg"), 11, 700, 30, 50, 0, 0, True]
        draw(ShopSlate) 
        if clicked(ShopSlate) and everequipment[10] == 0:
            boughtequipment[10] = 0
            MONEY = MONEY + Slateprice  
    if mouseover(ShopSlate):
        Slateinfotext = infofont.render('Slates let you write messages to your buddy', 1, (infocolor))
        screen.blit(Slateinfotext, (infopos)) 

    ### Glowstick ###
    Glowstickprice = 5
    Glowsticktext = pricefont.render('Glowstick: $' + str(Glowstickprice), 1, (pricecolor))
    screen.blit(Glowsticktext, (840, 280))
    if boughtequipment[12] == 0 and everequipment[12] == 0:
        ShopGlowstick = [pygame.image.load("Glowstick.jpg"), 840 + 25, 180, 30, 100, 0, 0, True]
        draw(ShopGlowstick)
        if MONEY >= Glowstickprice and clicked(ShopGlowstick):
            boughtequipment[12] = 1
            MONEY = MONEY - Glowstickprice
    else:
        ShopGlowstick = [pygame.image.load("Glowstick.jpg"), 1024 - 50 - 11, 600, 15, 50, 0, 0, True]
        draw(ShopGlowstick) 
        if clicked(ShopGlowstick) and everequipment[12] == 0:
            boughtequipment[12] = 0
            MONEY = MONEY + Glowstickprice
    if mouseover(ShopGlowstick):
        Glowstickinfotext = infofont.render('Glow Sticks let you keep you buddy in sight on night dives', 1, (infocolor))
        screen.blit(Glowstickinfotext, (infopos))  
        
    ### Scooter ###
    Scooterprice = 2000
    Scootertext = pricefont.render('Scooter: $' + str(Scooterprice), 1, (pricecolor))
    screen.blit(Scootertext, (840, 480))
    if boughtequipment[13] == 0 and everequipment[13] == 0:
        ShopScooter = [pygame.image.load("Scooter.jpg"), 840, 380, 100, 100, 0, 0, True]
        draw(ShopScooter)
        if MONEY >= Scooterprice and clicked(ShopScooter):
            boughtequipment[13] = 1
            MONEY = MONEY - Scooterprice
    else:
        ShopScooter = [pygame.image.load("Scooter.jpg"), 1024 - 50 - 11, 650, 50, 50, 0, 0, True]
        draw(ShopScooter)   
        if clicked(ShopScooter) and everequipment[13] == 0:
            boughtequipment[13] = 0
            MONEY = MONEY + Scooterprice
    if mouseover(ShopScooter):
        Scooterinfotext = infofont.render('Under water scooters can be a lot of fun', 1, (infocolor))
        screen.blit(Scooterinfotext, (infopos))
        
    ### ExtraFlashlight ###
    ExtraFlashlightprice = 40
    ExtraFlashlighttext = pricefont.render('2nd Light: $' + str(ExtraFlashlightprice), 1, (pricecolor))
    screen.blit(ExtraFlashlighttext, (840, 680))
    if boughtequipment[14] == 0 and everequipment[14] == 0:
        ShopExtraFlashlight = [pygame.transform.flip(pygame.image.load("Flashlight.png"), True, True), 840 + 20, 580, 75, 75, 0, 0, True]
        draw(ShopExtraFlashlight)
        if MONEY >= ExtraFlashlightprice and clicked(ShopExtraFlashlight):
            boughtequipment[14] = 1
            MONEY = MONEY - ExtraFlashlightprice
    else:
        ShopExtraFlashlight = [pygame.transform.flip(pygame.image.load("Flashlight.png"), True, True), 1024 - 50 - 11, 700, 50, 50, 0, 0, True]
        draw(ShopExtraFlashlight)
        if clicked(ShopExtraFlashlight) and everequipment[14] == 0:
            boughtequipment[14] = 0
            MONEY = MONEY + ExtraFlashlightprice
    if mouseover(ShopExtraFlashlight):
        ExtraFlashlightinfotext = infofont.render('Carry an extra light on night dives', 1, (infocolor))
        screen.blit(ExtraFlashlightinfotext, (infopos))

                
    moneyfont = pygame.font.SysFont("monospace", 30, "bold")
    moneytext = moneyfont.render('Wallet = $' + str(MONEY), 1, (0, 0, 0))
    screen.blit(moneytext, (350, 5))
    
#def underwavemaker():
#    global underwave
    
def underwavestartup():
    global underwave
    s = 0
    e = 12
    d = 600
    checkersset = True
    for a in range(20):
        if checkersset == True:
            initial_Underwave_x = -100 - windowoffset
            checkersset = False
        else:
            initial_Underwave_x = -400 - windowoffset
            checkersset = True
        for n in range(s, e):
            Underwave[n][3] = 300
            Underwave[n][4] = 100
            Underwave[n][1] = initial_Underwave_x
            Underwave[n][2] = y_min + d - windowoffset
            initial_Underwave_x = initial_Underwave_x + 1000
        a = a
        s = s + 12
        e = e + 12
        d = d + 600
        
def nothing():
    cool = True
    return cool

#### Surface Variables #######################################################################
# list = [image, x, y, x size, y size, x speed, y speed, right]
### Equipment #####
#equipment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
#boughtequipment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
#everequipment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  

equipment = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]  
boughtequipment = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]  
everequipment = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]  


# Snorkel, Goggles, BCD, Fins, Regulator, ExtraRegulator, AirTank, Gauges, Wetsuit, Drysuit, Slate, Flashlight, Glowstick, Scooter, ExtraFlashlight 

Snorkel = [[pygame.transform.rotate(pygame.image.load("Snorkel.png"), -30), 0, 0, 100, 100, 0, 0, True], # 0
           [pygame.transform.rotate(pygame.image.load("Snorkel.png"), -30), 0, 0, 100, 100, 0, 0, True]]

Goggles = [[pygame.image.load("Gogglesdiver.png"), 0, 0, 63, 40, 0, 0, True], # 1
              [pygame.image.load("Gogglesdiver.png"), 0, 0, 63, 40, 0, 0, True]]

BCD = [[pygame.image.load("BCDdiver.png"), 0, 0, 70, 50, 0, 0, True], # 2
              [pygame.image.load("BCDdiver.png"), 0, 0, 70, 50, 0, 0, True]]

Fins = [[pygame.image.load("Finsdiver.png"), 0, 0, 97, 160, 0, 0, True], # 3
              [pygame.image.load("Finsdiver.png"), 0, 0, 97, 160, 0, 0, True]]

Regulator = [[pygame.image.load("Regulatordiver.png"), 0, 0, 45, 20, 0, 0, True], # 4
              [pygame.image.load("Regulatordiver.png"), 0, 0, 45, 20, 0, 0, True]]

ExtraRegulator = [[pygame.image.load("ExtraRegulatordiver.png"), 0, 0, 50, 45, 0, 0, True], # 5
              [pygame.image.load("ExtraRegulatordiver.png"), 0, 0, 50, 45, 0, 0, True]]

AirTank = [[pygame.image.load("AirTankdiver.png"), 0, 0, 70, 25, 0, 0, True], # 6
              [pygame.image.load("AirTankdiver.png"), 0, 0, 70, 25, 0, 0, True]]

Gauges = [[pygame.image.load("Gaugesdiver.png"), 0, 0, 97, 51, 0, 0, True], # 7
              [pygame.image.load("Gaugesdiver.png"), 0, 0, 97, 51, 0, 0, True]]

Wetsuit = [[pygame.image.load("Wetsuitdiver1.png"), 0, 0, 260, 186, 0, 0, True], # 8
           [pygame.image.load("Wetsuitdiver2.png"), 0, 0, 260, 186, 0, 0, True],
           [pygame.image.load("Wetsuitdiver3.png"), 0, 0, 260, 186, 0, 0, True], # 8
           [pygame.image.load("Wetsuitdiver4.png"), 0, 0, 260, 186, 0, 0, True]]

#Drysuit = [[pygame.image.load("Drysuitdiver.png"), 0, 0, 100, 100, 0, 0, True], # 9
#            [pygame.image.load("Drysuitdiver.png"), 0, 0, 100, 100, 0, 0, True]]

#Slate = [[pygame.image.load("Slatediver.png"), 0, 0, 100, 100, 0, 0, True], # 10
#              [pygame.image.load("Slatediver.png"), 0, 0, 100, 100, 0, 0, True]]

Flashlight = [[pygame.image.load("Flashlight.png"), 0, 0, 100, 100, 0, 0, True], # 11
              [pygame.image.load("Flashlight.png"), 0, 0, 100, 100, 0, 0, True]]

#Glowstick = [[pygame.image.load("Glowstickdiver.png"), 0, 0, 100, 100, 0, 0, True], # 12
#              [pygame.image.load("Glowstickdiver.png"), 0, 0, 100, 100, 0, 0, True]]

Scooterdiver = [[pygame.image.load("Scooterdiver.png"), 0, 0, 250, 250, 0, 0, True], # 13
                  [pygame.image.load("Scooterdiver.png"), 0, 0, 250, 250, 0, 0, True]]
    
#ExtraFlashlight = [[pygame.image.load("ExtraFlashlightdiver.png"), 0, 0, 100, 100, 0, 0, True], # 14
#              [pygame.image.load("ExtraFlashlightdiver.png"), 0, 0, 100, 100, 0, 0, True]]


#######################
Orangediver = [pygame.image.load("Orangediver.png"), 200, 200, 260, 186, 10, 10, True]
Orangediverkick = [pygame.image.load("Orangediverkick.png"), 200, 260, 286, 200, 10, 10, True]
Orangediverdead = [pygame.transform.flip(pygame.image.load("Orangediver.png"), False, True), Orangediver[1], Orangediver[2], Orangediver[3], Orangediver[4], Orangediver[5], Orangediver[6], Orangediver[7]]

#Greendiver = [pygame.image.load("Greendiver.png"), 0, 200, 224, 188, 10, 10, True]
#Greendiverkick = [pygame.image.load("Greendiverkick.png"), 0, 200, 224, 188, 10, 10, True]
Greendiver = [pygame.image.load("Greendiver.png"), 0, 200, 260, 186, 10, 10, True]
Greendiverkick = [pygame.image.load("Greendiverkick.png"), 0, 200, 260, 186, 10, 10, True]

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
    
orangeBubbles = [[pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                 [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                 [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                 [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                 [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                 [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                 [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
                 [pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False]]

greenBubbles = [[pygame.image.load("Bubbles.gif"), -1000, -1000, 25, 51, 10, 10, True, False],
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
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False], 
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
          [pygame.image.load("Coral1.png"), 0, 0, 484, 285, 0, 0, True, False],
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

Shipwreck = [[pygame.image.load("Shipwreck.png"), -10000, -10000, 800, 500, 0, 0, True, False]]
Boat = [[pygame.image.load("Boat.png"), 0, 0, 800, 500, 0, 0, True, False]]
Bottle = [[pygame.image.load("Bottle.jpg"), -10000, -10000, 50, 100, 10, 10, True, False]]
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
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False],
        [pygame.image.load("Wave.gif"), 0, 0, 400, 100, 0, 0, True, False]]
########################################################Underwave = [[pygame.image.load("Wave.gif"), 0, 0, 200, 50, 0, 0, True, False]]
#underwavemaker()
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
Introscreen = [pygame.image.load("Introscreen.png"), 150, 0, 756, 791, 0, 0, True]
Endscreen = [pygame.image.load("Endscreen.png"), 0, 0, 1024, 768, 0, 0, True]

Airgauge = [pygame.image.load("Airgauge.png"), 1024 - 200, 0, 200, 200, 0, 0, True]
Depthgauge = [pygame.image.load("Depthgauge.png"), 1024 - 400, 0, 200, 200, 0, 0, True]

Shelves = [pygame.image.load("Shelves.png"), 0, 0, 1024, 768, 0, 0, True]
Closetshelves = [pygame.image.load("Closetshelves.png"), 0, 0, 1024, 768, 0, 0, True]

Clueback = [pygame.image.load("Clueback.png"), 200, 200, 100, 100, 10, 10, True]
Islandbutton = [pygame.image.load("Islandbutton.png"), 200, 200, 100, 100, 10, 10, True]
Menubutton = [pygame.image.load("Menubutton.png"), 200, 200, 100, 100, 10, 10, True]

#aha = pygame.mixer.Sound("Aha.mp3")


#### Surface Variables ###################################################################

pygame.init()
pygame.mixer.init()
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
level_2_initialized = False
level_3_initialized = False
level_4_initialized = False
level_5_initialized = False
level_6_initialized = False
level_7_initialized = False
level_9_initialized = False
level_10_initialized = False
level_11_initialized = False
level_12_initialized = False
#################################################################
### Level 2 Variables ###########################################
level_2_initialized = False
fish_collected = 0
holding_a_fish = False
#################################################################
### Universal Variables #########################################
level = -1
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
gacount = 0
orangedead = False
depth = 0
scroll = 0
myfont = pygame.font.SysFont("monospace", 40, "bold")
#ocean = [135, 206, 250] 
ocean = [0, 100, 255] 
red = [255, 0, 0]

slowbub = 0
slowbubgreen = 0
slowbubtime = 2

bubblecycles = [0, 0, 0, 0, 0, 0, 0, 0] # for more bubbles, add more zeros
numnum = 50

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
MONEY = 1000000000#1300
accel = 0.5

aircap = 200
kk = False
downair = False
greendownair = False
air_step = 1
airdegrees = 0
depthdegrees = 0
real_depth = 0
exreg = 0

#edges = [0, 0, 2000, 1000]
levels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
levelsdone = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
windowoffset = 200

bubblesound = pygame.mixer.Sound('bubblesound.wav')
breathesound = pygame.mixer.Sound('breathesound.wav')
wilhelm = pygame.mixer.Sound('wilhelm.wav')

#################################################################
# -------- Main Program Loop -----------
while done == False:
    keys()
    if level == -2:
        screen.fill(ocean)   
        controlsfont = pygame.font.SysFont("monospace", 30, "bold")
        controlstext1 = controlsfont.render('W, A, S, D = Up, Left, Down, Right', 1, (255, 255, 0))
        screen.blit(controlstext1, (100, 100))
        controlstext2 = controlsfont.render('Spacebar = Restart Level', 1, (255, 255, 0))
        screen.blit(controlstext2, (100, 140))
        controlstext3 = controlsfont.render('Backspace = World Map', 1, (255, 255, 0))
        screen.blit(controlstext3, (100, 180))
    elif level == -1:
        pygame.mouse.set_visible(1)
        screen.fill(ocean)   
        draw(Introscreen)
        if clicked(Introscreen):
            level = 0
    elif level == 100:
        pygame.mouse.set_visible(1)
        screen.fill(ocean)   
        draw(Endscreen)
        #if clicked(Endscreen):
        #    level = 0
    ################# Map Level 0 ###########################
    elif level == 0:
        wintime = 0
        Level0()
    ################# Closet Level 50 ###########################
    elif level == 50:
        Level50()
    ################# Dive Shop Level 8
    elif level == 8:
        Level8()
                
    ############### Game Levels ###################################################
    else:
        if level_initialized == False:
            if equipment[6] and equipment[4]:
                aircap = 3000
            else:
                aircap = 30
            if equipment[13] == 1:
                aircap = 5000
            
            x_min = 0
            y_min = 0
            
            exreg = 0
            ### Level Bounds
            if level == 1:
                x_max = 99*100
                y_max = 99*20
            elif level == 2:
                x_max = 99*100
                y_max = 99*20
            elif level == 3:
                x_max = 99*100
                y_max = 99*30
            elif level == 4:
                x_max = 99*75
                y_max = 99*75
            elif level == 5:
                x_max = 99*50
                y_max = 99*40
            elif level == 6:
                x_max = 99*50
                y_max = 99*120    
            elif level == 7:
                x_max = 99*100
                y_max = 99*100
            elif level == 9:
                x_max = 99*50
                y_max = 99*100  
            elif level == 10:
                x_max = 99*100
                y_max = 99*60
            elif level == 11:
                x_max = 99*50
                y_max = 99*50     
            elif level == 12:
                x_max = 99*120
                y_max = 99*120    
            
            y_min_edge = False
            y_max_edge = False
            x_min_edge = False
            x_max_edge = False
            
            level_initialized = True
            level_complete = False
            
            wintime = 0
            
            Boat = [[pygame.image.load("Boat.png"), 100, -400, 800, 500, 0, 0, True, False]]
            
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
            
            Orangediver = [pygame.image.load("Orangediver.png"), 400, 200, 260, 186, 10, 10, True]
            Orangediverkick = [pygame.image.load("Orangediverkick.png"), 400, 260, 286, 200, 10, 10, True]
            Greendiver = [pygame.image.load("Greendiver.png"), 0, 200, 260, 186, 10, 10, True]
            Orangediver[5] = 0
            Orangediver[6] = 0
            orangedead = False
            greenrise = False
            greenkicking = True
            orangekicking = True
            orangekicking = True
            orangecycles = 0
            orangelength = 20 
            if equipment[9] == 1:
                Orangediver[0] = pygame.image.load("Wetsuitdiverdry1.png")
                Orangediverkick[0] = pygame.image.load("Wetsuitdiverdry2.png")
                Greendiver[0] = pygame.image.load("Wetsuitdiverdry3.png")
                Greendiverkick[0] = pygame.image.load("Wetsuitdiverdry4.png")
                Orangediverdead[0] = pygame.transform.flip(pygame.image.load("Wetsuitdiverdry1.png"), False, True)
                Fins[1][3] = 101
                Fins[3][3] = 101
            elif equipment[8] == 1:
                Orangediver[0] = pygame.image.load("Wetsuitdiver1.png")
                Orangediverkick[0] = pygame.image.load("Wetsuitdiver2.png")
                Greendiver[0] = pygame.image.load("Wetsuitdiver3.png")
                Greendiverkick[0] = pygame.image.load("Wetsuitdiver4.png")
                Orangediverdead[0] = pygame.transform.flip(pygame.image.load("Wetsuitdiver1.png"), False, True)
                Fins[1][3] = 101
                Fins[3][3] = 101
            else:
                Orangediver[0] = pygame.image.load("Orangediver.png")
                Orangediverkick[0] = pygame.image.load("Orangediverkick.png")
                Greendiver[0] = pygame.image.load("Greendiver.png")
                Greendiverkick[0] = pygame.image.load("Greendiverkick.png")
                Orangediverdead[0] = pygame.transform.flip(pygame.image.load("Orangediver.png"), False, True)
                Fins[1][3] = 97
                Fins[3][3] = 97
                
            bubblecycles = [0, 0, 0, 0, 0, 0, 0, 0]
            scroll = Orangediver[1]  
            depth = Orangediver[2]
            
            #edges = [-100, -100, 3500, 1800]
            underwavestartup()
            
            initial_Coral0_x = -100 - windowoffset
            for n in range(33):
                Coral0[n][3] = 600
                Coral0[n][4] = 400
                Coral0[n][1] = initial_Coral0_x
                Coral0[n][2] = y_max + 50 - 100 - 115 + windowoffset
                initial_Coral0_x = initial_Coral0_x + 400
            
            initial_Rock0_y = -windowoffset - 100
            for n in range(60):
                Rock0[n][3] = 400
                Rock0[n][1] = x_min - 200 + 100 - windowoffset
                Rock0[n][2] = initial_Rock0_y
                initial_Rock0_y = initial_Rock0_y + 250
            
            initial_Rock0_y2 = -windowoffset - 100
            for n in range(60, 120):
                Rock0[n][3] = 400
                Rock0[n][1] = x_max + 175  - 100 - 150 + windowoffset
                Rock0[n][2] = initial_Rock0_y2
                initial_Rock0_y2 = initial_Rock0_y2 + 250
                
            initial_Wave_x = -100 - windowoffset
            for n in range(25):
                Wave[n][3] = 600
                Wave[n][4] = 400
                Wave[n][1] = initial_Wave_x
                Wave[n][2] = y_min + 20 - windowoffset
                initial_Wave_x = initial_Wave_x + 536
                
            ########################################
                
            
        ##  Initialized #########################################################3 
        if level == 6 or level == 11 or level == 12:
            screen.fill([100, 90, 150])   
        elif level == 10:
            screen.fill([19, 189, 232])   
        else:
            screen.fill(ocean)   
        justdied = False
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
                ox1 = 155 #129
                ox2 = 160 #160
            else:
                ox1 = 64 #95
                ox2 = 64 #64
            oy1 = 146 #118
            oy2 = 31 #31
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
        ##############################################3
        ################################################
        # Snorkel, Goggles, BCD, Fins, Regulator, ExtraRegulator, AirTank, Gauges, Wetsuit, Drysuit, Slate, Flashlight, Glowstick, Scooter, ExtraFlashlight 

        if orangedead == False:
            if equipment[0] == 1:
                Snorkel[0][7] = Orangediver[7]
                Snorkel[0][3] = 75
                Snorkel[0][4] = 75
                Snorkel[0][2] = Orangediver[2] - 10
            if equipment[1] == 1:
                Goggles[0][7] = Orangediver[7]
                Goggles[0][2] = Orangediver[2] + 8
            if equipment[2] == 1:
                BCD[0][7] = Orangediver[7]
                BCD[0][2] = Orangediver[2] + 50
            if equipment[3] == 1:
                Fins[0][7] = Orangediver[7]
                Fins[0][2] = Orangediver[2] + 58
                Fins[1][7] = Orangediver[7]
                Fins[1][2] = Orangediver[2] + 50
            if equipment[4] == 1:
                Regulator[0][7] = Orangediver[7]
                Regulator[0][2] = Orangediver[2] + 40
            if equipment[5] == 1:      
                ExtraRegulator[0][7] = Orangediver[7]
                ExtraRegulator[0][2] = Orangediver[2] + 40
            if equipment[6] == 1:                
                AirTank[0][7] = Orangediver[7]
                AirTank[0][2] = Orangediver[2] + 34
            if equipment[7] == 1:
                Gauges[0][7] = Orangediver[7]
                Gauges[0][2] = Orangediver[2] + 42
            if equipment[11] == 1:
                Flashlight[0][7] = Orangediver[7]
                Flashlight[0][3] = 60
                Flashlight[0][4] = 40
                Flashlight[0][2] = Orangediver[2] + 145
                
            if Orangediver[7] == True:
                if equipment[0] == 1:
                    Snorkel[0][1] = Orangediver[1] + Orangediver[3] - Snorkel[0][3] - 10
                if equipment[1] == 1:
                    Goggles[0][1] = Orangediver[1] + Orangediver[3] - Goggles[0][3] - 10
                if equipment[2] == 1:
                    BCD[0][1] = Orangediver[1] + Orangediver[3] - BCD[0][3] - 51
                if equipment[3] == 1:
                    Fins[0][1] = Orangediver[1] + Orangediver[3] - Fins[0][3] - 209
                    Fins[1][1] = Orangediver[1] + Orangediver[3] - 97 - 144
                if equipment[4] == 1:
                    Regulator[0][1] = Orangediver[1] + Orangediver[3] - Regulator[0][3] - 27
                if equipment[5] == 1:
                    ExtraRegulator[0][1] = Orangediver[1] + Orangediver[3] - ExtraRegulator[0][3] - 65
                if equipment[6] == 1:
                    AirTank[0][1] = Orangediver[1] + Orangediver[3] - AirTank[0][3] - 70
                if equipment[7] == 1:
                    Gauges[0][1] = Orangediver[1] + Orangediver[3] - Gauges[0][3] - 70
                if equipment[11] == 1:
                    Flashlight[0][1] = Orangediver[1] + Orangediver[3] - Flashlight[0][3] - 56
            else:
                if equipment[0] == 1:
                    Snorkel[0][1] = Orangediver[1] + 10
                if equipment[1] == 1:
                    Goggles[0][1] = Orangediver[1] + 10
                if equipment[2] == 1:
                    BCD[0][1] = Orangediver[1] + 51
                if equipment[3] == 1:
                    Fins[0][1] = Orangediver[1] + 209
                    Fins[1][1] = Orangediver[1] + 144 - 5
                if equipment[4] == 1:
                    Regulator[0][1] = Orangediver[1] + 27
                if equipment[5] == 1:
                    ExtraRegulator[0][1] = Orangediver[1] + 65
                if equipment[6] == 1:
                    AirTank[0][1] = Orangediver[1] + 70
                if equipment[7] == 1:
                    Gauges[0][1] = Orangediver[1] + 70
                if equipment[11] == 1:
                    Flashlight[0][1] = Orangediver[1] + 56
###################### DEAD #############################################################
        else:
            upsdown = 50   
            
            if equipment[0] == 1:
                Snorkel[0][7] = Orangediver[7]
                Snorkel[0][3] = 75
                Snorkel[0][4] = 75
                Snorkel[0][2] = Orangediver[2] - 1 + Orangediver[4] - Snorkel[0][4] + 10
            if equipment[1] == 1:
                Goggles[0][7] = Orangediver[7]
                Goggles[0][2] = Orangediver[2] + 8 + Orangediver[4] - Goggles[0][4] - 15
            if equipment[2] == 1:
                BCD[0][7] = Orangediver[7]
                BCD[0][2] = Orangediver[2] + 88
            if equipment[3] == 1:
                Fins[0][7] = Orangediver[7]
                Fins[0][2] = Orangediver[2] + 41
            if equipment[4] == 1:
                Regulator[0][7] = Orangediver[7]
                Regulator[0][2] = Orangediver[2] + 126
            if equipment[5] == 1:  
                ExtraRegulator[0][7] = Orangediver[7]
                ExtraRegulator[0][2] = Orangediver[2] + 100
            if equipment[6] == 1:
                AirTank[0][7] = Orangediver[7]
                AirTank[0][2] = Orangediver[2] + 124
            if equipment[7] == 1:
                Gauges[0][7] = Orangediver[7]
                Gauges[0][2] = Orangediver[2] + 92
            if equipment[11] == 1:
                Flashlight[0][7] = Orangediver[7]
                Flashlight[0][3] = 60
                Flashlight[0][4] = 40
                Flashlight[0][2] = Orangediver[2]
                
            if Orangediver[7] == True:
                if equipment[0] == 1:
                    Snorkel[0][1] = Orangediver[1] + Orangediver[3] - Snorkel[0][3] - 10
                if equipment[1] == 1:
                    Goggles[0][1] = Orangediver[1] + Orangediver[3] - Goggles[0][3] - 10
                if equipment[2] == 1:
                    BCD[0][1] = Orangediver[1] + Orangediver[3] - BCD[0][3] - 51
                if equipment[3] == 1:
                    Fins[0][1] = Orangediver[1] + Orangediver[3] - Fins[0][3] - 209
                if equipment[4] == 1:
                    Regulator[0][1] = Orangediver[1] + Orangediver[3] - Regulator[0][3] - 27
                if equipment[5] == 1:
                    ExtraRegulator[0][1] = Orangediver[1] + Orangediver[3] - ExtraRegulator[0][3] - 65
                if equipment[6] == 1:
                    AirTank[0][1] = Orangediver[1] + Orangediver[3] - AirTank[0][3] - 70
                if equipment[7] == 1:
                    Gauges[0][1] = Orangediver[1] + Orangediver[3] - Gauges[0][3] - 70
                if equipment[11] == 1:
                    Flashlight[0][1] = Orangediver[1] + Orangediver[3] - Flashlight[0][3] - 56
            else:
                if equipment[0] == 1:
                    Snorkel[0][1] = Orangediver[1] + 10
                if equipment[1] == 1:
                    Goggles[0][1] = Orangediver[1] + 10
                if equipment[2] == 1:
                    BCD[0][1] = Orangediver[1] + 51
                if equipment[3] == 1:
                    Fins[0][1] = Orangediver[1] + 209
                if equipment[4] == 1:
                    Regulator[0][1] = Orangediver[1] + 27
                if equipment[5] == 1:
                    ExtraRegulator[0][1] = Orangediver[1] + 65
                if equipment[6] == 1:
                    AirTank[0][1] = Orangediver[1] + 70
                if equipment[7] == 1:
                    Gauges[0][1] = Orangediver[1] + 70
                if equipment[11] == 1:
                    Flashlight[0][1] = Orangediver[1] + 56
            
        ##############################################################3
        ################################################################
        ##########################################################
        if equipment[0] == 1:
            Snorkel[1][7] = Greendiver[7]
            Snorkel[1][3] = 75
            Snorkel[1][4] = 75
            Snorkel[1][2] = Greendiver[2] - 10
        if equipment[1] == 1:
            Goggles[1][7] = Greendiver[7]
            Goggles[1][2] = Greendiver[2] + 8
        if equipment[2] == 1:
            BCD[1][7] = Greendiver[7]
            BCD[1][2] = Greendiver[2] + 50
        if equipment[3] == 1:
            Fins[2][7] = Greendiver[7]
            Fins[2][2] = Greendiver[2] + 58
            Fins[3][7] = Greendiver[7]
            Fins[3][2] = Greendiver[2] + 50
        if equipment[4] == 1:
            Regulator[1][7] = Greendiver[7]
            Regulator[1][2] = Greendiver[2] + 40
        if equipment[5] == 1:      
            ExtraRegulator[1][7] = Greendiver[7]
            ExtraRegulator[1][2] = Greendiver[2] + 40
        if equipment[6] == 1:                
            AirTank[1][7] = Greendiver[7]
            AirTank[1][2] = Greendiver[2] + 34
        if equipment[7] == 1:
            Gauges[1][7] = Greendiver[7]
            Gauges[1][2] = Greendiver[2] + 42
        if equipment[11] == 1:
            Flashlight[1][7] = Greendiver[7]
            Flashlight[1][3] = 60
            Flashlight[1][4] = 40
            Flashlight[1][2] = Greendiver[2] + 145
            
        if Greendiver[7] == True:
            if equipment[0] == 1:
                Snorkel[1][1] = Greendiver[1] + Greendiver[3] - Snorkel[1][3] - 10
            if equipment[1] == 1:
                Goggles[1][1] = Greendiver[1] + Greendiver[3] - Goggles[1][3] - 10
            if equipment[2] == 1:
                BCD[1][1] = Greendiver[1] + Greendiver[3] - BCD[1][3] - 51
            if equipment[3] == 1:
                Fins[2][1] = Greendiver[1] + Greendiver[3] - Fins[2][3] - 209
                Fins[3][1] = Greendiver[1] + Greendiver[3] - 97 - 144
            if equipment[4] == 1:
                Regulator[1][1] = Greendiver[1] + Greendiver[3] - Regulator[1][3] - 27
            if equipment[5] == 1:
                ExtraRegulator[1][1] = Greendiver[1] + Greendiver[3] - ExtraRegulator[1][3] - 65
            if equipment[6] == 1:
                AirTank[1][1] = Greendiver[1] + Greendiver[3] - AirTank[1][3] - 70
            if equipment[7] == 1:
                Gauges[1][1] = Greendiver[1] + Greendiver[3] - Gauges[1][3] - 70
            if equipment[11] == 1:
                Flashlight[1][1] = Greendiver[1] + Greendiver[3] - Flashlight[1][3] - 56
        else:
            if equipment[0] == 1:
                Snorkel[1][1] = Greendiver[1] + 10
            if equipment[1] == 1:
                Goggles[1][1] = Greendiver[1] + 10
            if equipment[2] == 1:
                BCD[1][1] = Greendiver[1] + 51
            if equipment[3] == 1:
                Fins[2][1] = Greendiver[1] + 209
                Fins[3][1] = Greendiver[1] + 144 - 5
            if equipment[4] == 1:
                Regulator[1][1] = Greendiver[1] + 27
            if equipment[5] == 1:
                ExtraRegulator[1][1] = Greendiver[1] + 65
            if equipment[6] == 1:
                AirTank[1][1] = Greendiver[1] + 70
            if equipment[7] == 1:
                Gauges[1][1] = Greendiver[1] + 70
            if equipment[11] == 1:
                Flashlight[1][1] = Greendiver[1] + 56
   
            
        #####################################################
        rowdraw(Boat, 0)
        rowdraw(Shipwreck, 0)        
        for n in range(25):
            if greenrise == False:
                Wave[n] = rowmovebackground(Wave, n, Orangediver)
            rowdraw(Wave, n)
        for n in range(240):
            if greenrise == False:
                Underwave[n] = rowmovebackground(Underwave, n, Orangediver)
            rowdraw(Underwave, n)
        for n in range(120):
            if greenrise == False:
                Rock0[n] = rowmovebackground(Rock0, n, Orangediver)
            rowdraw(Rock0, n)
        for n in range(33):
            if greenrise == False:
                Coral0[n] = rowmovebackground(Coral0, n, Orangediver)
            rowdraw(Coral0, n)
        if greenrise == False:
            Boat[0] = rowmovebackground(Boat, 0, Orangediver)
            Bottle[0] = rowmovebackground(Bottle, 0, Orangediver)
            Treasurechest[0] = rowmovebackground(Treasurechest, 0, Orangediver)
            Shipwreck[0] = rowmovebackground(Shipwreck, 0, Orangediver)

        for b in range(8):
            if greenrise == False:
                orangeBubbles[b][2] = orangeBubbles[b][2] - orangeBubbles[b][6]
                orangeBubbles[b] = rowmovebackground(orangeBubbles, b, Orangediver)
                
                obubbledepth = depth - (Orangediver[2] - orangeBubbles[b][2])
                if obubbledepth < 0:
                    orangeBubbles[b][2] = -10000 
                gbubbledepth = depth - (Orangediver[2] - greenBubbles[b][2])
                if gbubbledepth < 0:
                    greenBubbles[b][2] = -10000 
                           
            greenBubbles[b][2] = greenBubbles[b][2] - greenBubbles[b][6]
            greenBubbles[b] = rowmovebackground(greenBubbles, b, Orangediver)
            rowdraw(orangeBubbles, b)
            rowdraw(greenBubbles, b)

        #########################################################
        #### Level Initialization and Fish ############
          
        if level == 1: # Outer Banks
            if level_1_initialized == False:
                level_1_initialized = True
                Bottle = [[pygame.image.load("Bottle.jpg"), x_max - x_max/2, y_max + 120, 50, 100, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Dolphin, 4, 3, 100*0.75)
            multifish(Jellyfish, 4, 1, 100*0.75)
            multifish(Shark, 4, 4, 100*0.75)
        
        if level == 2: # Singapore
            if level_2_initialized == False:
                level_2_initialized = True
                for n in range(33):
                    Coral0[n][0] = Coral2[0]
                for n in range(120):
                    Rock0[n][0] = Rock4[0]
            multifish(Eel, 4, 2, 100*16)
            multifish(Clownfish, 4, 5, 100*2)
            multifish(Dolphin, 4, 3, 100*0.75)
            multifish(Shark, 4, 4, 100*0.75)
        
        if level == 3: # Sydney
            if level_3_initialized == False:
                level_3_initialized = True
                Bottle = [[pygame.image.load("Bottle.jpg"), x_max - x_max/2, y_max + 120, 50, 100, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Clownfish, 4, 5, 100*2)
            multifish(Jellyfish, 4, 1, 100*0.75)
            multifish(Shark, 4, 4, 100*0.75)
            
        if level == 4: # Panama
            if level_4_initialized == False:
                level_4_initialized = True
                Bottle = [[pygame.image.load("Bottle.jpg"), x_max - x_max/2, y_max + 120, 50, 100, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Eel, 4, 2, 100*16)
            multifish(Clownfish, 4, 5, 100*2)
            multifish(Dolphin, 4, 3, 100*0.75)
            
        if level == 5: # SanDiego
            if level_5_initialized == False:
                level_5_initialized = True
                Bottle = [[pygame.image.load("Bottle.jpg"), x_max - x_max/2, y_max + 120, 50, 100, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Clownfish, 4, 5, 100*2)
            multifish(Jellyfish, 4, 1, 100*0.75)
            multifish(Shark, 4, 4, 100*0.75)
        
        if level == 6: # Tokyo
            if level_6_initialized == False:
                level_6_initialized = True
                Bottle = [[pygame.image.load("Bottle.jpg"), x_max - x_max/2, y_max + 120, 50, 100, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Eel, 4, 2, 100*16)
            multifish(Clownfish, 4, 5, 100*2)
            multifish(Jellyfish, 4, 1, 100*0.75)
            multifish(Lanturnfish, 4, 2, 100*80)
            multifish(Shark, 4, 4, 100*0.75)
            
        if level == 7: # CapeTown
            if level_7_initialized == False:
                level_7_initialized = True
                Bottle = [[pygame.image.load("Bottle.jpg"), x_max - x_max/2, y_max + 120, 50, 100, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Eel, 4, 2, 100*16)
            multifish(Dolphin, 4, 3, 100*0.75)
            multifish(Jellyfish, 4, 1, 100*0.75)
            
        if level == 9: # Santiago
            if level_9_initialized == False:
                level_9_initialized = True
                Bottle = [[pygame.image.load("Bottle.jpg"), x_max - x_max/2, y_max + 120, 50, 100, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Clownfish, 4, 5, 100*2)
            multifish(Dolphin, 4, 3, 100*0.75)
            multifish(Shark, 4, 4, 100*0.75)
        
        if level == 10: # Antarctica
            if level_10_initialized == False:
                level_10_initialized = True
                Bottle = [[pygame.image.load("Bottle.jpg"), x_max - x_max/2, y_max + 120, 50, 100, 0, 0, True, False]]
                Shipwreck = [[pygame.image.load("Shipwreck.png"), x_max - x_max/7, y_max - 400, 1200, 900, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Eel, 4, 2, 100*16)
            multifish(Jellyfish, 4, 1, 100*0.75)
            multifish(Lanturnfish, 4, 2, 100*30)
            multifish(Shark, 4, 4, 100*0.75)

        if level == 11: # KeyWest
            if level_11_initialized == False:
                level_11_initialized = True
                Bottle = [[pygame.image.load("Bottle.jpg"), x_max - x_max/2, y_max + 120, 50, 100, 0, 0, True, False]]
                Shipwreck = [[pygame.image.load("Shipwreck.png"), x_max/4, y_max - 400, 1200, 900, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Eel, 4, 2, 100*16)
            multifish(Jellyfish, 4, 1, 100*0.75)
            multifish(Lanturnfish, 4, 2, 100*30)
            multifish(Shark, 4, 4, 100*0.75)
            
        if level == 12: # Unknown
            if level_12_initialized == False:
                level_12_initialized = True
                Treasurechest = [[pygame.image.load("Treasurechest.png"), x_max - x_max/2, y_max, 200, 150, 0, 0, True, False]]
                Shipwreck = [[pygame.image.load("Shipwreck.png"), x_max - x_max/3, y_max - 600, 1600, 1200, 0, 0, False, False]]
                #Treasurechest = [[pygame.image.load("Treasurechest.png"), 500, 500, 200, 150, 0, 0, True, False]]
                for n in range(33):
                    Coral0[n][0] = Coral1[0]
                for n in range(120):
                    Rock0[n][0] = Rock5[0]
            multifish(Eel, 4, 2, 100*16)
            multifish(Clownfish, 4, 5, 100*2)
            multifish(Dolphin, 4, 3, 100*0.75)
            multifish(Jellyfish, 4, 1, 100*0.75)
            multifish(Lanturnfish, 4, 2, 100*80)
            multifish(Shark, 4, 4, 100*0.75)
            
        #########################################################
        
        ### Air Gauge stuff ###
        if equipment[7]:
            draw(Airgauge)
        step_step = 5
        air_step = (step_step)*real_depth/33 + step_step
        #5000:-10 2500:90 0:190 -10-190/5000-0=-0.04 y=mx+b y=-0.04x+b b=y+0.04x = 90+0.04*2500 = 190
        airdegrees = -0.04*aircap + 190
        pi = 3.141592653589793238462643383279502884197169399375
        gaugeradius = 200 #radius of gauge, if time try to make that actually use the gauge rect to calculate width
        air_gaugerect = Airgauge[0].get_rect()
        pygame.draw.line(Airgauge[0], (120,0,0), (air_gaugerect.centerx, air_gaugerect.centery), (air_gaugerect.centerx+200, air_gaugerect.centery), 5)
        air_startx = air_gaugerect.centerx
        air_starty = air_gaugerect.centery
        air_endx = 200*math.cos((airdegrees*pi)/180.0) + air_startx
        air_endy = -200*math.sin((airdegrees*pi)/180.0)+ air_starty
        Airgauge[0].fill
        Airgauge[0].set_alpha(255)
        air_gauge_image = pygame.image.load("Airgauge.png") #For redrawing
        Airgauge[0] = air_gauge_image
        pygame.draw.line(Airgauge[0], (120,0,0), (air_startx, air_starty), (air_endx, air_endy), 5)
        
        ### Depth Gauge stuff ###
        if equipment[7]:
            draw(Depthgauge)
        real_depth = depth/100
        #105:0 67:90 27:180 0-180/105-27=-2.31 y=mx+b y=-2.31x+b b=y+2.31x = 90+2.31*67 = 245
        depthdegrees = -2.31*real_depth + 245
        depth_gaugerect = Depthgauge[0].get_rect()
        pygame.draw.line(Depthgauge[0], (120,0,0), (depth_gaugerect.centerx, depth_gaugerect.centery), (depth_gaugerect.centerx+200, depth_gaugerect.centery), 5)
        depth_startx = depth_gaugerect.centerx
        depth_starty = depth_gaugerect.centery
        depth_endx = 200*math.cos((depthdegrees*pi)/180.0) + depth_startx
        depth_endy = -200*math.sin((depthdegrees*pi)/180.0)+depth_starty
        Depthgauge[0].fill
        Depthgauge[0].set_alpha(255)
        depth_gauge_image = pygame.image.load("Depthgauge.png") #For redrawing
        Depthgauge[0] = depth_gauge_image
        pygame.draw.line(Depthgauge[0], (120,0,0), (depth_startx, depth_starty), (depth_endx, depth_endy), 5)

        aircaptext = myfont.render("Air=" + str(aircap), 1, (255, 255, 0))
        #screen.blit(aircaptext, (10, 100))
        depthtext = myfont.render("Y=" + str(real_depth), 1, (255, 255, 0))
        #screen.blit(depthtext, (10, 10))
        scrolltext = myfont.render("X=" + str(scroll), 1, (255, 255, 0))
        #screen.blit(scrolltext, (10, 50))
        
        if equipment[13] == 0:
            for n in range(4):
                if collision(Eel[n], Orangediver, 75):
                    orangedead = True
                    justdied = True
                    eelskilled = True
                    
            for n in range(4):
                if collision(Shark[n], Orangediver, 75):
                    orangedead = True
                    justdied = True
                    sharkskilled = True
                    
            for n in range(4):
                if collision(Jellyfish[n], Orangediver, 75) and equipment[8] == 0 and equipment[9] == 0: # Wetsuit protects against Jellyfish
                    orangedead = True
                    justdied = True
                    jellyskilled = True
                
        #for n in range(4):
        #    if collision(Lanturnfish[n], Orangediver, 75):
        #        orangedead = True
        #        justdied
        #        lanturnskilled = True

        if level_complete == True and orangedead == False:
            winfont = pygame.font.SysFont("monospace", 100, "bold")
            wintext = winfont.render('YOU WIN!', 1, (255, 255, 0))
            screen.blit(wintext, (250, 100))
            if wintime > 75:
                level = 0
                level_initialized = False
                level_1_initialized = False
                level_2_initialized = False
                level_3_initialized = False
                level_4_initialized = False
                level_5_initialized = False
                level_6_initialized = False
                level_7_initialized = False
                level_9_initialized = False
                level_10_initialized = False
                level_11_initialized = False
                level_12_initialized = False
            wintime = wintime + 1
            
        if orangedead == True:
            deadfont = pygame.font.SysFont("monospace", 100, "bold")
            deadtext = deadfont.render('YOU DEAD!', 1, (255, 255, 0))
            screen.blit(deadtext, (250, 100))
        if equipment[13] == 0:
            if equipment[0] == 1: 
                if Orangediver[7]: ## Behind
                    rowdraw(Snorkel, 0)
                if Greendiver[7]: ## Behind
                    rowdraw(Snorkel, 1)
        animatedgreen()
        #movebubbles(Greendiver, 4, numnum/2)
        if greendownair:
            if slowbubgreen > slowbubtime:
                slowbubgreen = 0
                bubblesound.play()
                newbubbles(Greendiver, greenBubbles)
            slowbubgreen = slowbubgreen + 1
        if equipment[13] == 0:
            if equipment[0] == 1:
                if Greendiver[7] == False: ## In front
                    rowdraw(Snorkel, 1)
            if equipment[1] == 1:
                rowdraw(Goggles, 1)
            if equipment[2] == 1:
                rowdraw(BCD, 1)
            #if equipment[3] == 1:
               # rowdraw(Fins, 1)
            if equipment[4] == 1:
                rowdraw(Regulator, 1)
            if equipment[5] == 1:
                rowdraw(ExtraRegulator, 1)
            if equipment[6] == 1:
                rowdraw(AirTank, 1)
            if equipment[7] == 1:
                rowdraw(Gauges, 1)
            if equipment[11] == 1:
                rowdraw(Flashlight, 1)
     
        #######################
        ### Draw Equipment ###
        animatedorange()
        if downair:
            gacount = 0
        gacount = gacount + 1
        if gacount == 10:
            greendownair = True
        else:
            greendownair = False
        if orangedead == False:
            #movebubbles(Orangediver, 0, 0)
            if downair:
                if slowbub > slowbubtime:
                    slowbub = 0
                    breathesound.play()
                    newbubbles(Orangediver, orangeBubbles)
                slowbub = slowbub + 1
                #newbubbles(Greendiver, greenBubbles)
        if equipment[13] == 0:
            if equipment[0] == 1:
                if Orangediver[7] == False: ## In front
                    rowdraw(Snorkel, 0)
            if equipment[1] == 1:
                rowdraw(Goggles, 0)
            if equipment[2] == 1:
                rowdraw(BCD, 0)
          #  if equipment[3] == 1:
               # rowdraw(Fins, 0)
            if equipment[4] == 1:
                rowdraw(Regulator, 0)
            if equipment[5] == 1:
                rowdraw(ExtraRegulator, 0)
            if equipment[6] == 1:
                rowdraw(AirTank, 0)
            if equipment[7] == 1:
                rowdraw(Gauges, 0)
            if equipment[11] == 1:
                rowdraw(Flashlight, 0)
  
        if greenrise == False:
            binddiver()
        if equipment[13] == 0:
            killspeed = -17
        else:
            killspeed = -100000
        if Orangediver[6] < killspeed:
            orangedead = True
            justdied = True
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
        
        
        ##### Equipment Consequences #####
        if equipment[13]:
            Scooterdiver[1][1] = Greendiver[1]
            Scooterdiver[1][2] = Greendiver[2]
            Scooterdiver[1][7] = Greendiver[7]
            rowdraw(Scooterdiver, 1)
            Scooterdiver[0][1] = Orangediver[1]
            Scooterdiver[0][2] = Orangediver[2]
            Scooterdiver[0][7] = Orangediver[7]
            rowdraw(Scooterdiver, 0)
            
            
        if equipment[0] == 1 and depth < 10: #Snorkel lets conserve air at the surface
            aircap = aircap
        elif downair == True:
            aircap = aircap - air_step
            #newbubbles(Orangediver, Bubbles, 0)
        if equipment[1] == 0: # No goggles and you cannot see
            screen.fill(ocean) 
            darkfont = pygame.font.SysFont("monospace", 30, "bold")
            darktext = darkfont.render('Hard to see without goggles.', 1, (255, 255, 0))
            screen.blit(darktext, (250, 450))    
        ### No BCD pulls player down.  See Key accell
        if equipment[3] == 1: # No fins and its hard to move
            accel = 0.5
        else:
            accel = 0.1
        if equipment[13] == 1:
            accel = 2
        
        # Regulator and air tank are required for more air.  Up in level intialization
        # If not gauges, you cannot see your gauges
        
        if aircap < 0:
            aircap = 0
            orangedead = True
            justdied = True
            airdeadfont = pygame.font.SysFont("monospace", 30, "bold")
            airdeadtext = airdeadfont.render('Crap air is gone.', 1, (255, 255, 0))
            screen.blit(airdeadtext, (300, 550))

#### Level Gameplay
################# Outer Banks Level 1 ###############################
        if level == 1:
            if collision(Bottle[0], Orangediver, 50):
                Bottle[0][8] = True
                if greenrise == False:
                    Bottle[0][2] = Orangediver[2] + Orangediver[4]/2 - Bottle[0][4]/2 + 50
                    Bottle[0][3] = 50
                    Bottle[0][4] = 100
                    if Orangediver[7]:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 + 25
                    else:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 - 25
            if level_complete == False and levelsdone[1] == 0:
                rowdraw(Bottle, 0)
            if collision(Boat[0], Orangediver, 0) and Bottle[0][8] == True and levelsdone[1] == 0:
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
                        #Clownfish[f][3] = 150
                        #Clownfish[f][4] = 100
                        if Orangediver[7]:
                            Clownfish[f][1] = Orangediver[1] + Orangediver[3]/2 - Clownfish[f][3]/2 + 25
                        else:
                            Clownfish[f][1] = Orangediver[1] + Orangediver[3]/2 - Clownfish[f][3]/2 - 25
                    rowdraw(Clownfish, f)
                    
            fishfont = pygame.font.SysFont("monospace", 40, "bold")
            fishtext = fishfont.render('You collected ' + str(fish_collected) + ' Clownfish', 1, (255, 255, 0))
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
################# Sydney Level 3 ###############################
        if level == 3:
            if collision(Bottle[0], Orangediver, 50):
                Bottle[0][8] = True
                if greenrise == False:
                    Bottle[0][2] = Orangediver[2] + Orangediver[4]/2 - Bottle[0][4]/2 + 50
                    Bottle[0][3] = 50
                    Bottle[0][4] = 100
                    if Orangediver[7]:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 + 25
                    else:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 - 25
            if level_complete == False and levelsdone[3] == 0:
                rowdraw(Bottle, 0)
            if collision(Boat[0], Orangediver, 0) and Bottle[0][8] == True and levelsdone[3] == 0:
                    level_complete = True  
                    levels[3] = 1
####################################################################
################# Panama Level 4 ###############################
        if level == 4:
            if collision(Bottle[0], Orangediver, 50):
                Bottle[0][8] = True
                if greenrise == False:
                    Bottle[0][2] = Orangediver[2] + Orangediver[4]/2 - Bottle[0][4]/2 + 50
                    Bottle[0][3] = 50
                    Bottle[0][4] = 100
                    if Orangediver[7]:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 + 25
                    else:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 - 25
            if level_complete == False and levelsdone[4] == 0:
                rowdraw(Bottle, 0)
            if collision(Boat[0], Orangediver, 0) and Bottle[0][8] == True and levelsdone[4] == 0:
                    level_complete = True  
                    levels[4] = 1
####################################################################
################# SanDiego level 5 ###############################
        if level == 5:
            if collision(Bottle[0], Orangediver, 50):
                Bottle[0][8] = True
                if greenrise == False:
                    Bottle[0][2] = Orangediver[2] + Orangediver[4]/2 - Bottle[0][4]/2 + 50
                    Bottle[0][3] = 50
                    Bottle[0][4] = 100
                    if Orangediver[7]:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 + 25
                    else:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 - 25
            if level_complete == False and levelsdone[5] == 0:
                rowdraw(Bottle, 0)
            if collision(Boat[0], Orangediver, 0) and Bottle[0][8] == True and levelsdone[5] == 0:
                level_complete = True  
                levels[5] = 1
####################################################################
################# Tokyo Level 6 ####################################
        if level == 6:
            if equipment[14] == 0:
                exreg = exreg + 1
                if exreg > 30:
                    screen.fill([0,0,0]) 
                    darkfont = pygame.font.SysFont("monospace", 30, "bold")
                    darktext = darkfont.render('Wow, it is really dark.', 1, (255, 255, 0))
                    screen.blit(darktext, (250, 400))
                    orangedead = True
                    justdied = True
                    exflashdeadfont = pygame.font.SysFont("monospace", 30, "bold")
                    exflashdeadtext = exflashdeadfont.render('Flashlight broke. No backup!', 1, (255, 255, 0))
                    screen.blit(exflashdeadtext, (200, 300))
            elif equipment[12] == 0:
                exreg = exreg + 1
                if exreg > 100:
                    screen.fill([0,0,0]) 
                    darkfont = pygame.font.SysFont("monospace", 30, "bold")
                    darktext = darkfont.render('Wow, it is really dark.', 1, (255, 255, 0))
                    screen.blit(darktext, (250, 400))
                    orangedead = True
                    justdied = True
                    exflashdeadfont = pygame.font.SysFont("monospace", 30, "bold")
                    exflashdeadtext = exflashdeadfont.render('Both Lights broke. No glow stick!', 1, (255, 255, 0))
                    screen.blit(exflashdeadtext, (200, 300))
            elif equipment[5] == 0:
                exreg = exreg + 1
                if exreg > 30:
                    orangedead = True
                    justdied = True
                    exregdeadfont = pygame.font.SysFont("monospace", 30, "bold")
                    exregdeadtext = exregdeadfont.render('Regulator broke. No backup!', 1, (255, 255, 0))
                    screen.blit(exregdeadtext, (200, 250))
            elif equipment[8] == 0 and equipment[9] == 0:
                exreg = exreg + 1
                if exreg > 30:
                    orangedead = True
                    justdied = True
                    exregdeadfont = pygame.font.SysFont("monospace", 30, "bold")
                    exregdeadtext = exregdeadfont.render('Too cold!', 1, (255, 255, 0))
                    screen.blit(exregdeadtext, (200, 350))
                    
            if equipment[11] == 0:
                screen.fill([0,0,0]) 
                darkfont = pygame.font.SysFont("monospace", 30, "bold")
                darktext = darkfont.render('Wow, it is really dark.', 1, (255, 255, 0))
                screen.blit(darktext, (250, 400))
            for f in range(4):
                if collision(Lanturnfish[f], Orangediver, 50):
                    if holding_a_fish == False:
                        Lanturnfish[f][8] = True
                        holding_a_fish = True              
                if Lanturnfish[f][8] == True:
                    if greenrise == False:
                        Lanturnfish[f][7] = Orangediver[7]
                        Lanturnfish[f][2] = Orangediver[2] + Orangediver[4]/2 - Lanturnfish[f][4]/2 + 50
                        #Lanturnfish[f][3] = 150
                        #Lanturnfish[f][4] = 100
                        if Orangediver[7]:
                            Lanturnfish[f][1] = Orangediver[1] + Orangediver[3]/2 - Lanturnfish[f][3]/2 + 25
                        else:
                            Lanturnfish[f][1] = Orangediver[1] + Orangediver[3]/2 - Lanturnfish[f][3]/2 - 25
                    rowdraw(Lanturnfish, f)
                    
            fishfont = pygame.font.SysFont("monospace", 40, "bold")
            fishtext = fishfont.render('You collected ' + str(fish_collected) + ' Lanternfish', 1, (255, 255, 0))
            screen.blit(fishtext, (250, 767 - 60))
            for f in range(4):
                if collision(Boat[0], Orangediver, 75) and Lanturnfish[f][8] == True:
                    holding_a_fish = False
                    Lanturnfish[f][8] = False
                    Lanturnfish[f][1] = -1000
                    Lanturnfish[f][2] = -1000
                    fish_collected = fish_collected + 1
            if fish_collected == 5:
                level_complete = True
                levels[6] = 1
####################################################################
################# CapeTown Level 7 ###############################
        if level == 7:
            if equipment[5] == 0:
                exreg = exreg + 1
                if exreg > 30:
                    orangedead = True
                    justdied = True
                    exregdeadfont = pygame.font.SysFont("monospace", 30, "bold")
                    exregdeadtext = exregdeadfont.render('Regulator broke. No backup!', 1, (255, 255, 0))
                    screen.blit(exregdeadtext, (200, 250))
            elif equipment[8] == 0 and equipment[9] == 0:
                exreg = exreg + 1
                if exreg > 30:
                    orangedead = True
                    justdied = True
                    exregdeadfont = pygame.font.SysFont("monospace", 30, "bold")
                    exregdeadtext = exregdeadfont.render('Too cold!', 1, (255, 255, 0))
                    screen.blit(exregdeadtext, (200, 350))
            if collision(Bottle[0], Orangediver, 50):
                Bottle[0][8] = True
                if greenrise == False:
                    Bottle[0][2] = Orangediver[2] + Orangediver[4]/2 - Bottle[0][4]/2 + 50
                    Bottle[0][3] = 50
                    Bottle[0][4] = 100
                    if Orangediver[7]:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 + 25
                    else:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 - 25
            if level_complete == False and levelsdone[7] == 0:
                rowdraw(Bottle, 0)
            if collision(Boat[0], Orangediver, 0) and Bottle[0][8] == True and levelsdone[7] == 0:
                    level_complete = True  
                    levels[7] = 1
####################################################################
################# Santiago Level 9 ###############################
        if level == 9:
            if equipment[5] == 0:
                exreg = exreg + 1
                if exreg > 30:
                    orangedead = True
                    justdied = True
                    exregdeadfont = pygame.font.SysFont("monospace", 30, "bold")
                    exregdeadtext = exregdeadfont.render('Regulator broke. No backup!', 1, (255, 255, 0))
                    screen.blit(exregdeadtext, (200, 250))
            for f in range(4):
                if collision(Dolphin[f], Orangediver, 50):
                    if holding_a_fish == False:
                        Dolphin[f][8] = True
                        holding_a_fish = True              
                if Dolphin[f][8] == True:
                    if greenrise == False:
                        Dolphin[f][7] = Orangediver[7]
                        Dolphin[f][2] = Orangediver[2] + Orangediver[4]/2 - Dolphin[f][4]/2 + 50
                        #Dolphin[f][3] = 150
                        #Dolphin[f][4] = 100
                        if Orangediver[7]:
                            Dolphin[f][1] = Orangediver[1] + Orangediver[3]/2 - Dolphin[f][3]/2 + 25
                        else:
                            Dolphin[f][1] = Orangediver[1] + Orangediver[3]/2 - Dolphin[f][3]/2 - 25
                    rowdraw(Dolphin, f)
                    
            fishfont = pygame.font.SysFont("monospace", 40, "bold")
            fishtext = fishfont.render('You collected ' + str(fish_collected) + ' Dolphin', 1, (255, 255, 0))
            screen.blit(fishtext, (250, 767 - 60))
            for f in range(4):
                if collision(Boat[0], Orangediver, 75) and Dolphin[f][8] == True:
                    holding_a_fish = False
                    Dolphin[f][8] = False
                    Dolphin[f][1] = -1000
                    Dolphin[f][2] = -1000
                    fish_collected = fish_collected + 1
            if fish_collected == 2:
                level_complete = True
                levels[9] = 1
####################################################################
################# Antarctica Level 10 ###############################
        if level == 10:
            if equipment[9] == 0:
                exreg = exreg + 1
                if exreg > 30:
                    orangedead = True
                    justdied = True
                    exregdeadfont = pygame.font.SysFont("monospace", 30, "bold")
                    exregdeadtext = exregdeadfont.render('Too cold!', 1, (255, 255, 0))
                    screen.blit(exregdeadtext, (200, 350))
            if collision(Bottle[0], Orangediver, 50):
                Bottle[0][8] = True
                if greenrise == False:
                    Bottle[0][2] = Orangediver[2] + Orangediver[4]/2 - Bottle[0][4]/2 + 50
                    Bottle[0][3] = 50
                    Bottle[0][4] = 100
                    if Orangediver[7]:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 + 25
                    else:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 - 25
            if level_complete == False and levelsdone[10] == 0:
                rowdraw(Bottle, 0)
            if collision(Boat[0], Orangediver, 0) and Bottle[0][8] == True and levelsdone[10] == 0:
                    level_complete = True  
                    levels[10] = 1
####################################################################
################# KeyWest Level 11 ###############################
        if level == 11:
            if equipment[11] == 0:
                screen.fill([0,0,0]) 
                darkfont = pygame.font.SysFont("monospace", 30, "bold")
                darktext = darkfont.render('Wow, it is really dark.', 1, (255, 255, 0))
                screen.blit(darktext, (250, 400))    
            if collision(Bottle[0], Orangediver, 50):
                Bottle[0][8] = True
                if greenrise == False:
                    Bottle[0][2] = Orangediver[2] + Orangediver[4]/2 - Bottle[0][4]/2 + 50
                    Bottle[0][3] = 50
                    Bottle[0][4] = 100
                    if Orangediver[7]:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 + 25
                    else:
                        Bottle[0][1] = Orangediver[1] + Orangediver[3]/2 - Bottle[0][3]/2 - 25
            if level_complete == False and levelsdone[11] == 0:
                rowdraw(Bottle, 0)
            if collision(Boat[0], Orangediver, 0) and Bottle[0][8] == True and levelsdone[11] == 0:
                    level_complete = True  
                    levels[11] = 1
####################################################################
################# Unknown Level 12 ###############################
        if level == 12:
            if equipment[14] == 0:
                exreg = exreg + 1
                if exreg > 30:
                    screen.fill([0,0,0]) 
                    darkfont = pygame.font.SysFont("monospace", 30, "bold")
                    darktext = darkfont.render('Wow, it is really dark.', 1, (255, 255, 0))
                    screen.blit(darktext, (250, 400))
                    orangedead = True
                    justdied = True
                    exflashdeadfont = pygame.font.SysFont("monospace", 30, "bold")
                    exflashdeadtext = exflashdeadfont.render('Flashlight broke. No backup!', 1, (255, 255, 0))
                    screen.blit(exflashdeadtext, (200, 300))
            if equipment[11] == 0:
                screen.fill([0,0,0]) 
                darkfont = pygame.font.SysFont("monospace", 30, "bold")
                darktext = darkfont.render('Wow, it is really dark.', 1, (255, 255, 0))
                screen.blit(darktext, (250, 400))
            if levelsdone.count(1) > 2:
                if collision(Treasurechest[0], Orangediver, 50):
                    Treasurechest[0][8] = True
                    if greenrise == False:
                        Treasurechest[0][2] = Orangediver[2] + Orangediver[4]/2 - Treasurechest[0][4]/2 + 50
                        Treasurechest[0][3] = 200
                        Treasurechest[0][4] = 150
                        if Orangediver[7]:
                            Treasurechest[0][1] = Orangediver[1] + Orangediver[3]/2 - Treasurechest[0][3]/2 + 25
                        else:
                            Treasurechest[0][1] = Orangediver[1] + Orangediver[3]/2 - Treasurechest[0][3]/2 - 25
                if level_complete == False and levelsdone[12] == 0:
                    rowdraw(Treasurechest, 0)
                if collision(Boat[0], Orangediver, 0) and Treasurechest[0][8] == True and levelsdone[12] == 0:
                        level_complete = True  
                        levels[12] = 1
####################################################################

########################################################
        if orangedead and justdied:
            wilhelm.play()
            justdied = False
            Snorkel[0][0] = pygame.transform.flip(Snorkel[1][0], False, True)
            Goggles[0][0] = pygame.transform.flip(Goggles[1][0], False, True)
            BCD[0][0] = pygame.transform.flip(BCD[1][0], False, True)
            Fins[0][0] = pygame.transform.flip(Fins[2][0], False, True)
            Regulator[0][0] = pygame.transform.flip(Regulator[1][0], False, True)
            ExtraRegulator[0][0] = pygame.transform.flip(ExtraRegulator[1][0], False, True) 
            AirTank[0][0] = pygame.transform.flip(AirTank[1][0], False, True)              
            Gauges[0][0] = pygame.transform.flip(Gauges[1][0], False, True)
            Flashlight[0][0] = pygame.transform.flip(Flashlight[1][0], False, True)
        downair = False

        
        if levels[12] == True:
            level = 100

####  END   ############################################   
############################
############################
    pygame.display.flip()
    clock.tick(30)
pygame.quit ()