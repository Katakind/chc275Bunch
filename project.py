import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("Pygame Visual Novel")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEXTBOX_COLOR = (0, 0, 0, 180)



courageboy_img = pygame.image.load('vnbackground.jpg').convert()
Textbox = pygame.image.load('Persona.png').convert()


running = True
x = 0
while running:
    
    screen.blit(courageboy_img, (x, 30))
    screen.blit(Textbox, (300,600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
FONT = pygame.font.SysFont("cabin", 24)

script = [
    {"speaker": "Alice", "text": "Hey there! Welcome to our story."},
    {"speaker": "Bob", "text": "Hi Alice! How are you today?"},
    {"speaker": "Alice", "text": "I'm doing great, thanks for asking."},
    {"speaker": "", "text": "The sun sets over the horizon..."},
]
current_line = 0



pygame.quit()            