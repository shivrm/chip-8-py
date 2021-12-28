import pygame

# Define constants
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

class Display:
    def __init__(self) -> None:
        # Initialize display
        pygame.init()
        self.display = pygame.display.set_mode((640, 320))

    def update(self):
        # Update display and handle events
        pygame.display.update()
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()

    def set(self, x, y):
        # Set a pixel on the screen
        pygame.draw.rect(self.display, WHITE, pygame.Rect(x * 10, y * 10, 10, 10))
        pygame.display.update()
        
    def unset(self, x, y):
        # Unset a pixel on the screen
        pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 10, y * 10, 10, 10))
        pygame.display.update()

    def flip(self, x, y):
        # Flip a pixel on the screen.
        # Return true if the pixel was unset
        color = self.display.get_at(x * 10, y * 10)
        
        if color == WHITE:
            pygame.draw.rect(self.display, BLACK, pygame.Rect(x * 10, y * 10, 10, 10))
            return True
        
        else:
            pygame.draw.rect(self.display, WHITE, pygame.Rect(x * 10, y * 10, 10, 10))
            return False

    def quit(self):
        # Close the display
        pygame.quit()
    