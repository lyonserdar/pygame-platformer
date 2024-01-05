import pygame

NEIGHBOR_OFFSETS = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2))
PHYSICS_TILES = {"grass", "stone"}


class Tilemap:
    def __init__(self, tile_size: int = 16):
        self.tile_size = tile_size
        self.tiles = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tiles[str(3 + i) + ";10"] = {
                "name": "grass",
                "variant": 1,
                "pos": (3 + i, 10),
            }
            self.tiles["10;" + str(i + 5)] = {
                "name": "stone",
                "variant": 1,
                "pos": (10, i + 5),
            }

    def render(self, surf, assets):
        for tile in self.offgrid_tiles:
            surf.blit(assets[tile["name"]][tile["variant"]], (tile["pos"]))

        for tile in self.tiles.values():
            surf.blit(
                assets[tile["name"]][tile["variant"]],
                (tile["pos"][0] * self.tile_size, tile["pos"][1] * self.tile_size),
            )

    def get_tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = (
                str(tile_loc[0] + offset[0]) + ";" + str(tile_loc[1] + offset[1])
            )

            if check_loc in self.tiles:
                tiles.append(self.tiles[check_loc])

        return tiles

    def get_physics_rects_around(self, pos):
        rects = []
        for tile in self.get_tiles_around(pos):
            if tile["name"] in PHYSICS_TILES:
                rects.append(
                    pygame.Rect(
                        tile["pos"][0] * self.tile_size,
                        tile["pos"][1] * self.tile_size,
                        self.tile_size,
                        self.tile_size,
                    )
                )
        return rects
