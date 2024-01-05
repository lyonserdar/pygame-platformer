from typing import Iterable
import pygame


class PhysicsEntity:
    def __init__(self, img, name: str, pos: Iterable[int], size: Iterable[int]):
        self.img = img
        self.name = name
        self.pos = list(pos)
        self.size = list(size)
        self.velocity = [0, 0]

    def update(self, movement=(0, 0)):
        frame_movement = (
            movement[0] + self.velocity[0],
            movement[1] * self.velocity[1],
        )

        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def render(self, surf):
        surf.blit(self.img, self.pos)
