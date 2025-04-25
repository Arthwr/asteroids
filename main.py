import pygame
from player import Player
from constants import *


def main():
    print("Starting Asteroids!")

    pygame.init()

    dt = 0
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        updatable_group.update(dt)

        for entity in drawable_group:
            entity.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
