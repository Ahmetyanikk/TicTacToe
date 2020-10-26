import pygame
import  random

pygame.init()


screen=pygame.display.set_mode((900,600))
pygame.display.set_caption("Tic Tac Toe")
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0, 0, 128)
RED = (128,0,0)
font = pygame.font.Font('freesansbold.ttf', 32)
Sayac=0;
#7 8 9
#4 5 6
#1 2 3
FirstboxEmpthy=True
SecondboxEmpthy=True
ThirdboxEmpthy=True
FourthboxEmpthy=True
fifthboxEmpthy=True
sixthboxEmpthy=True
seventhboxEmpthy=True
eighthboxEmpthy=True
ninethboxEmpthy=True

FirstboxPCEmpthy=True
SecondboxPCEmpthy=True
ThirdboxPCEmpthy=True
FourthboxPCEmpthy=True
fifthboxPCEmpthy=True
sixthboxPCEmpthy=True
seventhboxPCEmpthy=True
eighthboxPCEmpthy=True
ninethboxPCEmpthy=True

FirstboxUserEmpthy=True
SecondboxUserEmpthy=True
ThirdboxUserEmpthy=True
FourthboxUserEmpthy=True
fifthboxUserEmpthy=True
sixthboxUserEmpthy=True
seventhboxUserEmpthy=True
eighthboxUserEmpthy=True
ninethboxUserEmpthy=True


aiWins = font.render("Ai Wins" , True, (BLACK))
userWins = font.render("User Wins" , True, (BLACK))
#f=first s=second
def drawX(fStartx,fStarty,fFinishx,fFinishy,sStartx,sStarty,sFinishx,sFinishy):
    pygame.draw.line(screen, RED, (fStartx, fStarty), (fFinishx, fFinishy), 10)
    pygame.draw.line(screen, RED, (sStartx, sStarty), (sFinishx, sFinishy), 10)

carryOn = True
while carryOn:
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (300, 0), (300, 600), 1)
    pygame.draw.line(screen, BLACK, (600, 0), (600, 600), 1)
    pygame.draw.line(screen, BLACK, (0, 200), (900, 200), 1)
    pygame.draw.line(screen, BLACK, (0, 400), (900, 400), 1)
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()


    if FirstboxEmpthy== False and FirstboxPCEmpthy==True:
       drawX(0, 600, 300, 400, 0,400, 300, 600)
       FirstboxUserEmpthy = False
    if SecondboxEmpthy == False and SecondboxPCEmpthy==True:
       drawX(300, 600, 600, 400, 300, 400, 600, 600)
       SecondboxUserEmpthy = False
    if ThirdboxEmpthy ==  False and ThirdboxPCEmpthy==True:
       drawX(600, 400, 900, 600, 600, 600, 900, 400)
       ThirdboxUserEmpthy = False
    if FourthboxEmpthy ==  False and FourthboxPCEmpthy==True:
       drawX(0, 200, 300, 400, 0, 400, 300, 200)
       FourthboxUserEmpthy=False
    if fifthboxEmpthy ==  False and fifthboxPCEmpthy==True:
       drawX(300, 400, 600, 200, 300, 200, 600, 400)
       fifthboxUserEmpthy=False
    if sixthboxEmpthy ==  False and sixthboxPCEmpthy==True:
       drawX(600, 400, 900, 200, 600, 200, 900, 400)
       sixthboxUserEmpthy=False
    if seventhboxEmpthy ==  False and seventhboxPCEmpthy==True:
        drawX(0, 200, 300, 0, 0, 0, 300, 200)
        seventhboxUserEmpthy=False
    if eighthboxEmpthy ==  False and eighthboxPCEmpthy==True:
       drawX(300, 0, 600, 200, 300, 200, 600, 0)
       eighthboxUserEmpthy=False
    if ninethboxEmpthy ==  False and ninethboxPCEmpthy==True:
       drawX(600, 0, 900, 200, 600, 200, 900, 0)
       ninethboxUserEmpthy=False



    if  FirstboxPCEmpthy==False:
       pygame.draw.circle(screen, (BLUE), (150, 500), 75, 10)
    if  SecondboxPCEmpthy==False:
       pygame.draw.circle(screen, (BLUE), (450, 500), 75, 10)
    if  ThirdboxPCEmpthy==False:
       pygame.draw.circle(screen, (BLUE), (750, 500), 75, 10)
    if  FourthboxPCEmpthy==False:
       pygame.draw.circle(screen, (BLUE), (150, 300), 75, 10)
    if  fifthboxPCEmpthy==False:
       pygame.draw.circle(screen, (BLUE), (450, 300), 75, 10)
    if sixthboxPCEmpthy==False:
       pygame.draw.circle(screen, (BLUE), (750, 300), 75, 10)
    if  seventhboxPCEmpthy==False:
        pygame.draw.circle(screen, (BLUE), (150, 100), 75, 10)
    if  eighthboxPCEmpthy==False:
       pygame.draw.circle(screen, (BLUE), (450, 100), 75, 10)
    if  ninethboxPCEmpthy==False:
       pygame.draw.circle(screen, (BLUE), (750, 100), 75, 10)

    if FirstboxPCEmpthy == False and SecondboxPCEmpthy==False and ThirdboxPCEmpthy==False:
        screen.blit(aiWins, (450, 300))
        Sayac=2
    if FourthboxPCEmpthy == False and fifthboxPCEmpthy==False and sixthboxPCEmpthy==False:
        screen.blit(aiWins, (450, 300))
        Sayac = 2
    if seventhboxPCEmpthy == False and seventhboxPCEmpthy==False and ninethboxPCEmpthy==False:
        screen.blit(aiWins, (450, 300))
        Sayac = 2
    if FirstboxPCEmpthy == False and FourthboxPCEmpthy==False and seventhboxPCEmpthy==False:
        screen.blit(aiWins, (450, 300))
        Sayac = 2
    if SecondboxPCEmpthy == False and fifthboxPCEmpthy==False and eighthboxPCEmpthy==False:
        screen.blit(aiWins, (450, 300))
        Sayac = 2
    if ThirdboxPCEmpthy == False and sixthboxPCEmpthy==False and ninethboxPCEmpthy==False:
        screen.blit(aiWins, (450, 300))
        Sayac=2
    if FirstboxPCEmpthy == False and fifthboxPCEmpthy==False and ninethboxPCEmpthy==False:
        screen.blit(aiWins, (450, 300))
        Sayac=2
    if ThirdboxPCEmpthy == False and fifthboxPCEmpthy==False and seventhboxPCEmpthy==False:
        screen.blit(aiWins, (450, 300))
        Sayac=2

    if FirstboxUserEmpthy == False and SecondboxUserEmpthy==False and ThirdboxUserEmpthy==False:
        screen.blit(userWins, (450, 300))
        Sayac=2
    if FourthboxUserEmpthy == False and fifthboxUserEmpthy==False and sixthboxUserEmpthy==False:
        screen.blit(userWins, (450, 300))
        Sayac=2
    if seventhboxUserEmpthy == False and seventhboxUserEmpthy==False and ninethboxUserEmpthy==False:
        screen.blit(userWins, (450, 300))
        Sayac=2
    if FirstboxUserEmpthy == False and FourthboxUserEmpthy==False and seventhboxUserEmpthy==False:
        screen.blit(userWins, (450, 300))
        Sayac=2
    if SecondboxUserEmpthy == False and fifthboxUserEmpthy==False and eighthboxUserEmpthy==False:
        screen.blit(userWins, (450, 300))
        Sayac=2
    if ThirdboxUserEmpthy == False and sixthboxUserEmpthy==False and ninethboxUserEmpthy==False:
        screen.blit(userWins, (450, 300))
        Sayac=2
    if FirstboxUserEmpthy == False and fifthboxUserEmpthy==False and ninethboxUserEmpthy==False:
        screen.blit(userWins, (450, 300))
        Sayac=2
    if ThirdboxUserEmpthy == False and fifthboxUserEmpthy==False and seventhboxUserEmpthy==False:
        screen.blit(userWins, (450, 300))
        Sayac=2

    (pcNumber) = random.randint(0, 10)

    if pcNumber == 1 and FirstboxEmpthy == True and Sayac == 1:
        FirstboxEmpthy = False
        FirstboxPCEmpthy = False
        Sayac = 0
    if pcNumber == 2 and SecondboxEmpthy == True and Sayac == 1:
        SecondboxEmpthy = False
        SecondboxPCEmpthy = False
        Sayac = 0
    if pcNumber == 3 and ThirdboxEmpthy == True and Sayac == 1:
        ThirdboxEmpthy = False
        ThirdboxPCEmpthy = False
        Sayac = 0
    if pcNumber == 4 and FourthboxEmpthy == True and Sayac == 1:
        FourthboxEmpthy = False
        FourthboxPCEmpthy = False
        Sayac = 0
    if pcNumber == 5 and fifthboxEmpthy == True and Sayac == 1:
        fifthboxEmpthy = False
        fifthboxPCEmpthy = False
        Sayac = 0
    if pcNumber == 6 and sixthboxEmpthy == True and Sayac == 1:
        sixthboxEmpthy = False
        sixthboxPCEmpthy = False
        Sayac = 0
    if pcNumber == 7 and seventhboxEmpthy == True and Sayac == 1:
        seventhboxEmpthy = False
        seventhboxPCEmpthy = False
        Sayac = 0
    if pcNumber == 8 and eighthboxEmpthy == True and Sayac == 1:
        eighthboxEmpthy = False
        eighthboxPCEmpthy = False
        Sayac = 0
    if pcNumber == 9 and ninethboxEmpthy == True and Sayac == 1:
        ninethboxEmpthy = False
        ninethboxPCEmpthy = False
        Sayac = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn =False
        if pressed1 == True and Sayac==0 :
            Sayac=1
            x,y=pygame.mouse.get_pos()
            if x>300 and y>200:
               if x>600:
                   if y>400 and ThirdboxEmpthy ==True :
                       ThirdboxEmpthy = False
                   elif sixthboxEmpthy==True :
                       sixthboxEmpthy = False
               elif y>400 and SecondboxEmpthy==True  :
                   SecondboxEmpthy =False
               elif  fifthboxEmpthy==True :
                   fifthboxEmpthy=False
            elif x>300 and y<200 :
                if x<600 and eighthboxEmpthy==True:
                    eighthboxEmpthy=False
                elif ninethboxEmpthy==True:
                    ninethboxEmpthy=False
            elif x<300 and y>200:
                if y<400 and FourthboxEmpthy==True:
                    FourthboxEmpthy=False
                elif FirstboxEmpthy==True :
                    FirstboxEmpthy=False
            elif seventhboxEmpthy==True :
                seventhboxEmpthy=False
       





    pygame.display.update()