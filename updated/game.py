import pygame
import random
import math

pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('space.jpg')


#title and logo
pygame.display.set_caption("Red Notice")
icon = pygame.image.load('pewdiepie.jpg')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480 
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png')) 
    enemyX.append(random.randint(0,736)) 
    enemyY.append(random.randint(50,150)) 
    enemyX_change.append(4)
    enemyY_change.append(40)

#bullet
#Ready = The state defines where you can't see the bullet on the screen
#Fire = The state defines where you can see the bullet on the screen

bulletImg = pygame.image.load('bullet1.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

#score
score = 0

def player(x,y):
    screen.blit(playerImg , (x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg , (x+16,y+10))

def isCollide(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))

    if distance < 27:
        return True
    else:
        return False


#screen looping
running = True
while running:

    screen.fill((138, 150, 60))
    #background image
    screen.blit(background , (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed check right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready" :
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                    #print("space is pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


#setting boundaries for enemy and player movements in the screen

    playerX += playerX_change

    if playerX <=0:
        playerX=0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <=0:
            enemyX_change[i] = 0.4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.4
            enemyY[i] += enemyY_change[i]


        #collision
        collision = isCollide(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i], i)
      

    #bullet selection fx
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    


   
    player(playerX,playerY)
    
    pygame.display.update()
    

    
   


    




