import pygame
import math
import random

pygame.init()

def isCollision(enemyX, enemyY, x, y):
    distance = math.sqrt((math.pow(enemyX-x,2)) + (math.pow(enemyY-y, 2)))
    if distance <= 35:
        return True
    else:
        False

width = 640
height = 360
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fish Game')

# Background
background = pygame.image.load('sea_background.png')

# Player 1
player1 = pygame.image.load('player1.png')
player1_turn = pygame.transform.flip(player1, True, False)
player1_x = 50
player1_y = 250
velocity = 4
left = True
right = False
player_font = pygame.font.Font('freesansbold.ttf', 16)

# Fish Food 1
fishFood = []
fishFood_turn = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_fishfood = 5
x_1 = []
x_2 = []
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

# Scor
scor = 0
scor_index = False
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

run = True
while run:
    window.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player1_x -= velocity
        window.blit(player1_turn, (player1_x, player1_y))    
        left = True
        right = False
    if key[pygame.K_RIGHT]:
        player1_x += velocity
        window.blit(player1, (player1_x, player1_y))
        left = False
        right = True
    if key[pygame.K_DOWN]:
        player1_y += velocity
    if key[pygame.K_UP]:
        player1_y -= velocity
    
    if left == True:
        window.blit(player1_turn, (player1_x, player1_y))
    if right == True:
        window.blit(player1, (player1_x, player1_y))
    player_identity = player_font.render('Player 1', True, (255,255,255))
    window.blit(player_identity, (player1_x, int(player1_y - 15)))

    # Boundaries
    if player1_x >= int(width-35):
        player1_x = int(width-36)
    if player1_x <= 0:
        player1_x = 1
    if player1_y >= int(height-20):
        player1_y = int(height-21)
    if player1_y <= 0 :
        player1_y = 1

    # Collision
    for i in range(number_fishfood):
        collision = isCollision(enemyX[i], enemyY[i], player1_x, player1_y)
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

    # Enemy
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

    # Collision 2
    for i in range(number_fishfood):
        collision2 = isCollision(enemyX2[i], enemyY2[i], player1_x, player1_y)
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

    # Bones
    for i in range(fish_bones_number):
        boneY += boneY_index
        window.blit(fish_bones[i], (boneX[i],boneY))
    # Bones Collision
    for i in range(fish_bones_number):
        boneCol = isCollision(boneX[i], boneY, player1_x, player1_y)
        if boneCol == True or boneY == 360:
            boneX[i] = random.randint(10, 620)
            boneY = -5
            scor -= 1


    if scor_index == True:
        scor += 1
        print(scor)
        scor_index = False
    score = font.render('Score: ' + str(scor), True, (255,255,255))
    window.blit(score, (textX, textY))

    pygame.display.update()
    window.fill((0,0,0))
    #pygame.time.delay(30)

pygame.quit()



