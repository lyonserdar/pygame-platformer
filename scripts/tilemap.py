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
