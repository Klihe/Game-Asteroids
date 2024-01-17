import pygame
from pygame import sprite

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Detection with Mask")

# Create two sprite instances with images
sprite1_image = pygame.image.load("sprite1.png").convert_alpha()
sprite2_image = pygame.image.load("sprite2.png").convert_alpha()

class MySprite(sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

# Create two sprite instances
sprite1 = MySprite(sprite1_image, 65, 0)
sprite2 = MySprite(sprite2_image, 100, 100)

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites

    # Check for collision using mask.overlap_area
    collision_area = sprite1.mask.overlap_area(sprite2.mask, (sprite2.rect.x - sprite1.rect.x, sprite2.rect.y - sprite1.rect.y))
    
    if collision_area > 0:
        print(collision_area)
        print("Collision detected!")

    # Draw sprites
    screen.fill((0, 0, 0))
    screen.blit(sprite1.image, sprite1.rect)
    screen.blit(sprite2.image, sprite2.rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
