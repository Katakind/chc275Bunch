import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

courageboy_img = pygame.image.load('courageboy.jpg').convert()

running = True
x = 0
while running:
    
    screen.blit(courageboy_img, (x, 30))
    x += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()            
