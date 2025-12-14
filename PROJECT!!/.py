import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()

    # Set screen size
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Full Screen Image Example")

    try:
        # Load the image
        image = pygame.image.load("vnbackground.jpg")  # Replace with your image path

        # Scale the image to fit the screen
        image = pygame.transform.scale(image, (screen_width, screen_height))
    except pygame.error as e:
        print(f"Error loading image: {e}")
        pygame.quit()
        sys.exit()

    # Main loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the image
        screen.blit(image, (0, 0))

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()