import pygame

with open("script.txt","r") as f:
    buffer = f.readlines()
    for i in range(len(buffer)):
        buffer[i] = buffer[i].strip()

pygame.init() 

#display
screen_width, screen_height = 1920, 1080
pygame.display.set_mode((1920, 1080))

#loading background, 
screen = pygame.display.set_mode((screen_width, screen_height))
Background_img1 = pygame.image.load('vnbackground.jpg').convert()
Background_img1 = pygame.transform.scale(Background_img1, (screen_width, screen_height))
clock = pygame.time.Clock()

#loading music
Backgroundmusic1 = pygame.mixer.music.load('Sonic.mp3')
pygame.mixer.music.play(-1)




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

   
   
#blit
    screen.blit(Background_img1, (0,0))
    screen.blit(resizedtextbox, (475, 700))
    screen.blit(text  ,(100,100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                currentline = (currentline + 1) % len(buffer)    
                    
#fps            
    pygame.display.flip()
    clock.tick(60)



pygame.quit()        

