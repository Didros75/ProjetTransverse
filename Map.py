import csv
import pygame

sky = 0
img0 = pygame.image.load('carrés/img.png')
img1 = pygame.image.load('carrés/img_1.png')
img2 = pygame.image.load('carrés/img_2.png')
img8 = pygame.image.load('carrés/img_7.png')
img9 = pygame.image.load('carrés/img_8.png')
img10 = pygame.image.load('carrés/img_3.png')
img16 = pygame.image.load('carrés/img_6.png')
img17 = pygame.image.load('carrés/img_5.png')
img18 = pygame.image.load('carrés/img_4.png')
background=pygame.image.load("assets/fond_test.jpg")
background=pygame.transform.scale(background,(900,600))

class Tile() :
    def __init__(self, image, x, y) :
        self.image = image
        self.pos_x = y
        self.pos_y = x

        self.rectangle = pygame.Rect(y, x, 30, 30)

    def draw(self, surface) :
        surface.blit(self.image, (self.pos_x, self.pos_y))

class Create_map() :
    def __init__(self, filename, screen) :
        self.size_tile = 30
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
                    tiles.append(Tile(sky, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "0":
                    tiles.append(Tile(img0, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "1" :
                    tiles.append(Tile(img1, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "2" :
                    tiles.append(Tile(img2, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "8" :
                    tiles.append(Tile(img8, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "9" :
                    tiles.append(Tile(img9, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "10" :
                    tiles.append(Tile(img10, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "16" :
                    tiles.append(Tile(img16, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "17" :
                    tiles.append(Tile(img17, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "18" :
                    tiles.append(Tile(img18, x * self.size_tile, y * self.size_tile))
        return tiles

    def load_map(self) :
        self.surface.blit(background, (0, 0))
        for i in range(len(self.tiles)) :
            if self.tiles[i].image != sky :
                self.tiles[i].draw(self.surface)
        return self.tiles