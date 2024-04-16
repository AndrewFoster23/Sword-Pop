import pygame

size = width, height = 750, 750

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lock It")
clock = pygame.time.Clock()


#Images
sword = pygame.image.load("swordCenter.png")
sword = pygame.transform.scale(sword, (525, 525))
sword = pygame.transform.rotate(sword, -90)

balloon = pygame.image.load("balloon.png")
balloon = pygame.transform.scale(balloon, (55, 70))

swordRect = sword.get_rect()
swordRect.center = (width // 2, height // 2)

font = pygame.font.SysFont("Arial", 60, bold = True)
popSound = pygame.mixer.Sound("vineboom.wav")

def drawText(text, x, y, color):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def checkPop(popped, angle):    #popped angle is incorrect?
    newAngle = angle
    if angle <= 0:
        newAngle -= 5
    print("Popped Angle: {}".format(newAngle))    
    if popped % 2 == 0:
        #print(newAngle)
        #print(balloonAngles[popped])
        if newAngle >= balloonAngles[popped] - 5 and newAngle <= balloonAngles[popped] + 5:
            print("here")
            popSound.play()
            return True
    else:
        if newAngle <= balloonAngles[popped] + 5 and newAngle >= balloonAngles[popped] - 5:
            popSound.play()
            return True
    return False
    

def drawBalloon(num):
    screen.blit(balloon, balloonCoords[num])

def checkWin(num):
    if num == len(balloonCoords) - 1:
        return True
    else:
        return False


#def calculateBalloonCoords():
    
#Num of coords = 2          (375+275-55-10, 375-35), (375-27.5, 375-275+10)
balloonCoords = [(195, 520), (520, 190), (550, 460), (570, 280), (125, 265), (125, 430)]

#Angle from top
balloonAngles = [-135, 45, -30, 15, -200, -160]


#calculateBalloonCoords()

def gameLoss(popped, angle):
    #print(popped)
    newAngle = angle
    if angle <= 0:
        newAngle -= 5
    
    if popped % 2 == 0:
        #print(newAngle)
        #print(balloonAngles[popped] - 5)
        if newAngle < balloonAngles[popped] - 5:
            #print("Loss here")
            return True
    else:
        if newAngle > balloonAngles[popped] + 5:
            return True
    return False

aWin = 0
angle = 0
fps = 40
balloonsPopped = 0
change = -1
spaceTime = 0



run = True
# Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    
    if balloonsPopped == 5:
        fps = 60
    
    spaceTime += 1
    
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True and spaceTime > 10 :
        pop = checkPop(balloonsPopped, angle)
        print(angle)
        print(pop)
        if pop:
            print("Entered pop loop")
            win = checkWin(balloonsPopped)
            if win:
                aWin = 1
                change = 0
                print("Win detected")
            spaceTime = 0
            balloonsPopped += 1
            if change == -1:
                change = 1
            else:
                change = -1
        else: 
            print("Here?")
            aWin = 2
            change = 0
    
    if balloonsPopped < len(balloonCoords):
        loss = gameLoss(balloonsPopped, angle)
    
    if loss:
        #print("loss")
        aWin = 2
        change = 0
        
    
    screen.fill((182, 213, 227))
    drawText("Pops: {}".format(balloonsPopped), 20, 20, (0, 0, 0))
    
    pygame.draw.circle(screen, (46, 232, 102), [width/2, height/2], 275) 
    
    
    if aWin == 0:
        drawBalloon(balloonsPopped)
        
        angle += change
        sword1 = pygame.transform.rotate(sword, angle)
        swordRect1 = sword1.get_rect()
        swordRect1.center = swordRect.center
    
    
    
    screen.blit(sword1, swordRect1)
    
    #pygame.draw.circle(screen, (255, 255, 255), [width/2, height/2], 6)
    #pygame.draw.circle(screen, (255, 255, 255), [width/2 - 50, height/2], 6)
    #pygame.draw.circle(screen, (255, 255, 255), [width/2 + 50, height/2], 6)
    
    if aWin == 1:
        drawText("You win!", 275, 665, (255, 0, 0))
    elif aWin == 2:
        drawText("You lose", 275, 665, (255, 0, 0))
           
    clock.tick(fps)
    pygame.display.flip()   
    
    
pygame.quit()

#Randomly generate balloon coordinates
#Begin screen, easy or hard mode (maybe blue balloon for easy and red for hard)(easy and hard button enlarge when mouse hovers over it)
#Music that ticks faster as it gets harder and faster
#When loss, push space to play again