import pygame

with open("script.txt","r") as f:
    buffer = f.readlines()
    for i in range(len(buffer)):
        buffer[i] = buffer[i].strip()





pygame.init()
#display
screen_width, screen_height = 1920, 1080
pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("Pygame Visual Novel")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEXTBOX_COLOR = (0, 0, 0, 180)


#loading background, 
screen = pygame.display.set_mode((screen_width, screen_height))
Background_img = pygame.image.load('vnbackground.jpg').convert()
Background_img = pygame.transform.scale(Background_img, (screen_width, screen_height))
clock = pygame.time.Clock()






#font
FONT = pygame.font.SysFont("cabin", 24)
COLOR = (255,255,255)
running = True
x = 0
i = 0
#textbox
Textbox = pygame.image.load('Textboxofdoom.png').convert()



#clicking function
while running:
    text = FONT.render(f"{buffer[i]}",True,COLOR)
    screen.blit(Background_img, (0,0))
    screen.blit(Textbox, (1000, 800))
    screen.blit(text  ,(100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:   
              i += 1
#fps
    pygame.display.flip()
    clock.tick(60)
#loop
    if i ==len(buffer):
        i = 0



#quit function
pygame.quit()            