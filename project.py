import pygame

with open("script.txt","r") as f:
    buffer = f.readlines()
    for i in range(len(buffer)):
        buffer[i] = buffer[i].strip()





pygame.init()

screen = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("Pygame Visual Novel")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEXTBOX_COLOR = (0, 0, 0, 180)



Background_img = pygame.image.load('vnbackground.jpg').convert()
FONT = pygame.font.SysFont("cabin", 24)
COLOR = (255,255,255)
running = True
x = 0
i = 0



while running:
    text = FONT.render(f"{buffer[i]}",True,COLOR)
    screen.blit(Background_img, (x, 30))
    screen.blit(text,(100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                i += 1
    pygame.display.flip()

    if i ==len(buffer):
        i = 0




pygame.quit()            