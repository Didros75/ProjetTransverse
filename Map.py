import csv
import pygame

white= pygame.image.load('carrés/jaune.png')
black=pygame.image.load('carrés/vert.png')
color = pygame.image.load('carrés/noir.jpg')

class Tile() :
    def __init__(self, image, x, y) :
        self.image = image
        self.pos_x = y
        self.pos_y = x

    def draw(self, surface) :

        surface.blit(self.image, (self.pos_x, self.pos_y))

class Create_map() :
    def __init__(self, filename, screen) :
        self.size_tile = 20
        self.tiles = self.load_tiles(filename)
        self.surface = screen
        self.load_map()

    def list_map(self, filename) :
        map = []
        file = open(filename, 'r')
        line = file.readline()
        map.append(line.split(","))
        while line != "" :
            if "\n" in map[-1][-1] :
                map[-1][-1] = map[-1][-1][: -1]
            line = file.readline()
            map.append(line.split(","))
        map.pop(-1)
        file.close()
        return map

    def load_tiles(self, filename) :
        tiles = []
        map = self.list_map(filename)
        for x in range(len(map)) :
            for y in range(len(map[x])) :
                if map[x][y] == "-1" :
                    tiles.append(Tile(black, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "1" :
                    tiles.append(Tile(white, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "2" :
                    tiles.append(Tile(color, x * self.size_tile, y * self.size_tile))
        return tiles

    def load_map(self) :
        for i in range(len(self.tiles)) :
            self.tiles[i].draw(self.surface)

    def draw_map(self, surface) :
        surface.blit(self.surface, (0, 0))