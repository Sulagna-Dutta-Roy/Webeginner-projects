import imp
from json import load
from msilib.schema import Icon
from turtle import Screen, distance
import pygame
import random
import math
from pygame import mixer

# init game
pygame.init()

# screen create
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.png')
# bg sound

#pygame.mixer.music.load
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("SPACE INVADERS")
Icon = pygame.image.load('spaceshipgame.png')
pygame.display.set_icon(Icon)

# player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX =[]
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6

for i in  range(no_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# Bullet
# "Ready", "Fire"

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score :" + str(score_value),True, (255, 255, 255))
    screen.blit(score, (x,y))

# function player


def player(x, y):
    screen.blit(playerImg, (x, y))

# function enemy


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False
def isGameOver(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt(math.pow(enemyX-playerX,2)+math.pow(enemyY-playerY,2))
    if(distance<27):
        return True
    else:
        return False
def dispGameOver():
    end_ = font.render("Game Over",True,(128,128,128))
    screen.blit(end_,(300,300))


def pause():
    running = True
    while running:
        pause_ = font.render("Game Paused",True,(255,255,255))
        screen.blit(pause_,(300,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # keystroke direction check
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    running = False
        pygame.display.update()
            #
        
        
        
        
        
    


# Game loop
running = True
while running:

    #RGB (0,0,0)
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke direction check
        if event.type == pygame.KEYDOWN:
            #print("A keystoke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_p:
                pause()

    # 5 = 5 + -0.1 -> 5 = 5 -0.1
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy boundry set
    for i in range(no_of_enemies):
        

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        if(enemyY[i]>750):
            enemyY[i] = math.random(50,190)

        #GameOver
        if(isGameOver(enemyX[i],enemyY[i],playerX,playerY)):
            dispGameOver()
            running = False
            break

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            #print(score_value)
            enemyX[i] = random.randint(10, 750)
            enemyY[i] = random.randint(50, 190)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
