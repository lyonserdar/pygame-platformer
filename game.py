import sys
import pygame


class Game:
    """Main game class"""

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("pygame-platformer")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
