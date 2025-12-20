import pygame

with open("script.txt","r") as f:
    buffer = f.readlines()
    for i in range(len(buffer)):
        buffer[i] = buffer[i].strip()

#To blit images and music at certain times
Dialougestage = 0
#line to jump to


pygame.init() 

#display
screen_width, screen_height = 1920, 1080
pygame.display.set_mode((1920, 1080))


Sonicmusic = 'Sonic.mp3' 

 



#loading background, 
screen = pygame.display.set_mode((screen_width, screen_height))
Background_img1 = pygame.image.load('vnbackground.jpg').convert()
Background_img1 = pygame.transform.scale(Background_img1, (screen_width, screen_height))
Background_imag2= pygame.image.load('duy-tung-street-night.jpg').convert()
Background_imag2 = pygame.transform.scale(Background_imag2, (screen_width, screen_height))
clock = pygame.time.Clock()
Background_imag3 = pygame.image.load('hellbackground.jpg').convert()
Background_imag3 = pygame.transform.scale(Background_imag3, (screen_width, screen_height))
Background_imag4 = pygame.image.load('Mario is dead.jpg').convert()
Background_imag4 = pygame.transform.scale(Background_imag4, (screen_width, screen_height))
Background_imag5 = pygame.image.load('Mementomori.jpeg').convert()
Background_imag5 = pygame.transform.scale(Background_imag5, (screen_width, screen_height))
Background_imag6 = pygame.image.load('background 6.jpg').convert()
Background_imag6 = pygame.transform.scale(Background_imag6, (screen_width, screen_height))
Background_imag7 = pygame.image.load('yes.jpg').convert()
Background_imag7 = pygame.transform.scale(Background_imag7, (screen_width, screen_height))
#playing music (this was hell to get running OH MY GOD)
if Dialougestage <= 64:
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.load(Sonicmusic)
        pygame.mixer.music.play(-1)    

#loading characters
Luigi1 = pygame.image.load('Luigi_2025.webp').convert()
Mario1 = pygame.image.load('Mario.png').convert()
Luigi2 = pygame.image.load('Luigi2.jpg').convert()
Luigi3 = pygame.image.load('Luigi.gif').convert()
#font
FONT = pygame.font.SysFont("cabin", 24)
COLOR = (255,255,255)
running = True
currentline = 0
#textbox
Textbox = pygame.image.load('Textboxofdoom.png').convert()
resizedtextbox = pygame.transform.smoothscale(Textbox, (1000,300))



while running:  
    
    text = FONT.render(f"{buffer[currentline]}",True,COLOR)
    


    for event in pygame.event.get():
        if Dialougestage <= 22:
            screen.blit(Background_img1, (0,0))
            screen.blit(Luigi1,(500,275))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage == 24:
            screen.blit(Background_imag2, (0,0))
            screen.blit(Luigi2,(500,275))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 55:
            screen.blit(Background_imag2, (0,0))
            screen.blit(Luigi1,(500,275))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 64:
            screen.blit(Background_imag2, (0,0))
            screen.blit(Luigi3,(500,275))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 70:
            screen.blit(Background_imag3, (0,0))
            screen.blit(Luigi3,(500,275))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 91:
            screen.blit(Background_imag3, (0,0))
            screen.blit(Luigi3,(500,275))
            screen.blit(Mario1,(1000,275))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 100:
            screen.blit(Background_imag4, (0,0))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 135:
            screen.blit(Background_imag3, (0,0))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 142:
            screen.blit(Background_imag5, (0,0))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 187:
            screen.blit(Background_imag5, (0,0))
            screen.blit(Mario1,(500,275))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 216:
            screen.blit(Background_imag3, (0,0))
            screen.blit(Luigi3,(1000,275))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))   
        elif Dialougestage <= 225:
            screen.blit(Background_imag6, (0,0))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 243:
            screen.blit(Background_imag7, (0,0))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage <= 250:
            screen.blit(Background_imag7, (0,0))
        elif Dialougestage == 251:
            screen.blit(Background_imag7, (0,0))
            screen.blit(resizedtextbox, (475, 700))
            screen.blit(text  ,(500,750))
        elif Dialougestage == 252:
            running = False
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                currentline = (currentline + 1) % len(buffer)
                Dialougestage += 1    
        

#fps            


    pygame.display.flip()
    clock.tick(60)



pygame.quit()        

