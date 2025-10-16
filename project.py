import cv2
import numpy as np
import pygame
import random
import math
print(cv2.__version__)
pygame.init()


def onTrack(val):
    global hueLow
    hueLow = val
def onTrack2(val):
    global hueHigh
    hueHigh = val
def onTrack3(val):
    global satLow
    satLow = val
def onTrack4(val):
    global satHigh
    satHigh = val
def onTrack5(val):
    global valLow
    valLow = val
def onTrack6(val):
    global valHigh
    valHigh = val

def isCollision(enemyX, enemyY, x, y):
    distance = math.sqrt((math.pow(enemyX-x,2)) + (math.pow(enemyY-y, 2)))
    if distance <= 35:
        return True
    else:
        False

height = 360
width = 640
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('My Trackbars')
cv2.moveWindow('My Trackbars', width, 0)
cv2.resizeWindow('My Trackbars', 400,350)

hueLow = 10
hueHigh = 20
satLow = 10
satHigh = 20
valLow = 10
valHigh = 20

cv2.createTrackbar('Hue Low', 'My Trackbars', 10, 179, onTrack)
cv2.createTrackbar('Hue High', 'My Trackbars', 20, 179, onTrack2)
cv2.createTrackbar('Sat Low', 'My Trackbars', 10, 255, onTrack3)
cv2.createTrackbar('Sat High', 'My Trackbars', 20, 255, onTrack4)
cv2.createTrackbar('Val Low', 'My Trackbars', 10, 255, onTrack5)
cv2.createTrackbar('Val High', 'My Trackbars', 20, 255, onTrack6)

# Game setup
# Background
background = pygame.image.load('sea_background.png')
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Fish Game')
# Player 1
fish = pygame.image.load('player1.png')
r_fish = pygame.transform.flip(fish, True, False)
x = 10
y = 10
left = True
right = False
x_2 = 10
player_font = pygame.font.Font('freesansbold.ttf', 16)
# Fish Food 1
fishFood = []
fishFood_turn = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_fishfood = 5
begin = []
enemyTurn_left = []
enemyTurn_right = []

for i in range(number_fishfood):
    fishFood.append(pygame.image.load('redfish36.png'))
    fishFood_turn.append(pygame.transform.flip(fishFood[i], True, False))
    enemyX.append(random.randint(10, 620))
    enemyY.append(random.randint(10, 170))
    enemyX_change.append(2)
    enemyY_change.append(2)
    begin.append(random.randint(0,2))
    enemyTurn_right.append(i)
    enemyTurn_left.append(i)

for i in range(number_fishfood):
    if begin[i] == 0:
        enemyTurn_right[i] = False
        enemyTurn_left[i] = True
    else:
        enemyTurn_right[i] = True
        enemyTurn_left[i] = False

# Fish Food 2
fishFood2 = []
fishFood_turn2 = []
enemyX2 = []
enemyY2 = []
enemyX_change2 = []
enemyY_change2 = []
begin2 = []
enemyTurn_left2 = []
enemyTurn_right2 = []

for i in range(number_fishfood):
    fishFood2.append(pygame.image.load('seahorse36.png'))
    fishFood_turn2.append(pygame.transform.flip(fishFood2[i], True, False))
    enemyX2.append(random.randint(10, 620))
    enemyY2.append(random.randint(10, 170))
    enemyX_change2.append(2)
    enemyY_change2.append(2)
    begin2.append(random.randint(0,2))
    enemyTurn_left2.append(i)
    enemyTurn_right2.append(i)
for i in range(number_fishfood):
    if begin2[i] == 0:
        enemyTurn_right2[i] = False
        enemyTurn_left2[i] = True
    else:
        enemyTurn_right2[i] = True
        enemyTurn_left2[i] = False   

# Bones
fish_bones = []
boneX = []
fish_bones_number = 1
boneY = -5
boneY_index = .5
for i in range(fish_bones_number):
    fish_bones.append(pygame.image.load('fish-bone.png'))
    boneX.append(random.randint(10, 620))

# Score
scor = 0
scor_index = False
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


run = True
while run:
    ignore, frame = cam.read()
    ##frame = cv2.flip(frame, 1)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound = np.array([hueLow,satLow,valLow])
    upperBound = np.array([hueHigh,satHigh,valHigh])
    
    myMask = cv2.inRange(frameHSV, lowerBound,upperBound)
    
    countours, junk = cv2.findContours(myMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, countours, -1, (0,0,255), 3)
    for countour in countours:
        area = cv2.contourArea(countour)
        if area >= 100: # The more number, means the more countour. So the higher the better
            myCountour = [countour]
            #cv2.drawContours(frame, myCountour, 0, (0,0,255), 3)
            x,y,wIdth,hEight = cv2.boundingRect(countour)
            #cv2.rectangle(frame, (x,y),(wIdth+x,hEight+y),(0,0,255),3)
            cv2.circle(frame,(int(x+15),int(y+15)),50,(0,0,255),3)

                                    #UPPER ME IS THE X AND Y COORDINATE    


    myObject = cv2.bitwise_and(frame, frame,mask = myMask)
    myObjectSmall = cv2.resize(myObject, (int(width/2), int(height/2)))
    
    cv2.imshow('My Object', myObjectSmall)
    cv2.moveWindow('My Object', 960, 500)
    myMaskSmall = cv2.resize(myMask, (int(width/2), int(height/2)))
    cv2.imshow('My Mask', myMaskSmall)
    cv2.moveWindow('My Mask', 640, 500)
    cv2.imshow('Frame', frame)
    cv2.moveWindow('Frame', 640,0)

    # Game
    # Background
    window.blit(background, (0,0))
    # Player 1
    x_1 = x

    if x_1 > x_2:
        right = True
        left = False
    if x_1 < x_2:
        left = True
        right = False

    if left == True:
        window.blit(r_fish, (x, y))
    if right == True:
        window.blit(fish, (x, y))
    x_2 = x
    player_identity = player_font.render('Player 1', True, (255,255,255))
    window.blit(player_identity, (x, int(y - 15)))

    # Enemy 1
    for i in range(number_fishfood):
        enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]
        if enemyX[i] >= int(width-35):
            enemyX_change[i] = enemyX_change[i] * (-1)
            enemyTurn_right[i] = True
            enemyTurn_left[i] = False
        if enemyX[i] <= 0:
            enemyX_change[i] = enemyX_change[i] * (-1)
            enemyTurn_right[i] = False
            enemyTurn_left[i] = True
        if enemyY[i] >= int(height-20) or enemyY[i] <= 0:
            enemyY_change[i] = enemyY_change[i] * (-1)
    
        if enemyTurn_right[i] == True:
            window.blit(fishFood_turn[i], (enemyX[i], enemyY[i]))
        if enemyTurn_left[i] == True:
            window.blit(fishFood[i], (enemyX[i], enemyY[i]))

    # Collision 1
    for i in range(number_fishfood):
        collision = isCollision(enemyX[i], enemyY[i], x, y)
        if collision == True:
            scor_index = True
            enemyX[i] = random.randint(10, 600)
            enemyY[i] = random.randint(10, 330)
            turn_index = random.randint(0, 1)
            if turn_index == 0:
                enemyTurn_right[i] = False
                enemyTurn_left[i] = True
            if turn_index == 1:
                enemyTurn_left[i] = False
                enemyTurn_right[i] = True

    # Enemy 2
    for i in range(number_fishfood):
        enemyX2[i] += enemyX_change2[i]
        enemyY2[i] += enemyY_change2[i]
        if enemyX2[i] >= int(width-35):
            enemyX_change2[i] = enemyX_change2[i] * (-1)
            enemyTurn_right2[i] = True
            enemyTurn_left2[i] = False
        if enemyX2[i] <= 0:
            enemyX_change2[i] = enemyX_change2[i] * (-1)
            enemyTurn_right2[i] = False
            enemyTurn_left2[i] = True
        if enemyY2[i] >= int(height-20) or enemyY2[i] <= 0:
            enemyY_change2[i] = enemyY_change2[i] * (-1)
        
        if enemyTurn_right2[i] == True:
            window.blit(fishFood_turn2[i], (enemyX2[i], enemyY2[i]))
        if enemyTurn_left2[i] == True:
            window.blit(fishFood2[i], (enemyX2[i], enemyY2[i]))

    # Collision 2
    for i in range(number_fishfood):
        collision2 = isCollision(enemyX2[i], enemyY2[i], x, y)
        if collision2 == True:
            scor_index = True
            enemyX2[i] = random.randint(10, 600)
            enemyY2[i] = random.randint(10, 330)
            turn_index2 = random.randint(0, 1)
            if turn_index2 == 0:
                enemyTurn_right2[i] = False
                enemyTurn_left2[i] = True
            if turn_index2 == 1:
                enemyTurn_left2[i] = False
                enemyTurn_right2[i] = True

    # Bones
    for i in range(fish_bones_number):
        boneY += boneY_index
        window.blit(fish_bones[i], (boneX[i],boneY))
    # Bones Collision
    for i in range(fish_bones_number):
        boneCol = isCollision(boneX[i], boneY, x, y)
        if boneCol == True or boneY == 360:
            boneX[i] = random.randint(10, 620)
            boneY = -5
            scor -= 1

    # Score
    if scor_index == True:
        scor += 1
        print(scor)
        scor_index = False
    score = font.render('Score: ' + str(scor), True, (255,255,255))
    window.blit(score, (textX, textY))

    
    pygame.display.update()
    window.fill((0,0,0))


    if cv2.waitKey(1) & 0xff == ord('q'):
        run = False
        break
cam.release()
pygame.quit()