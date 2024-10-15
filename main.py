import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot
import sys

updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable_group, drawable_group)
Asteroid.containers = (asteroids, updatable_group, drawable_group)
AsteroidField.containers = (updatable_group)
Shot.containers = (shots, drawable_group, updatable_group)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astroidfield = AsteroidField()
    points = 0
    points_multiplier = False
    text_font = pygame.font.SysFont("Times New Roman", 15, bold = True)

    def draw_text(text, font, text_color, x, y):
        img = font.render(text, True, text_color)
        screen.blit(img, (x, y))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Player movement
        for obj in updatable_group:
            obj.update(dt)

        for obj in asteroids:
            if player.collision_check(obj):
                sys.exit(f"Game Over! Score: {points:,}")
            for shot in shots:
                if shot.collision_check(obj):
                    obj.split()
                    points += 100
                    if points > 10000:
                        points += 100
                    if points > 100000:
                        points += 300
                    
        
        # Display black screen
        screen.fill((0, 0, 0))
        
        # Display score
        draw_text(f"Score: {points:,}", text_font, (255, 255, 255), 5, 5)

        # Draw objects
        for obj in drawable_group:
            obj.draw(screen)

        # Flip display
        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
