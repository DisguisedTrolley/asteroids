import pygame
import constants
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clk = pygame.time.Clock()
    dt = 0

    # Define the different groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # add player to both the above defined groups
    Player.containers = (updatable, drawable)
    # Initial player position (Center of the screen)
    Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("#000000")

        for item in drawable:
            item.draw(screen)

        time = clk.tick(60)
        dt = time / 1000

        for item in updatable:
            item.update(dt)

        pygame.display.flip()


if __name__ == "__main__":
    main()
