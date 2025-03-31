    # Gère la création et l'affichage de la map

import pygame

sky = 0
img0 = pygame.image.load('assets_tiles/top_left_corner.png')
img1 = pygame.image.load('assets_tiles/top_side.png')
img2 = pygame.image.load('assets_tiles/top_right_corner.png')
img8 = pygame.image.load('assets_tiles/left_side.png')
img9 = pygame.image.load('assets_tiles/wall.png')
img10 = pygame.image.load('assets_tiles/right_side.png')
img16 = pygame.image.load('assets_tiles/bottom_left_corner.png')
img17 = pygame.image.load('assets_tiles/bottom_side.png')
img18 = pygame.image.load('assets_tiles/bottom_right_corner.png')
img24 = pygame.image.load('assets_tiles/top_right_in_corner.png')
img26 = pygame.image.load('assets_tiles/top_left_in_corner.png')
img48 = pygame.image.load('assets_tiles/laser.png')
img40 = pygame.image.load('assets_tiles/bottom_left_in_corner.png')
img42 = pygame.image.load('assets_tiles/bottom_right_in_corner.png')
img49 = pygame.image.load('assets_tiles/button.png')
img50 = pygame.image.load('assets_tiles/button_left.png')
img51 = pygame.image.load('assets_tiles/button_bottom.png')
img52 = pygame.image.load('assets_tiles/button_right.png')


#background=pygame.image.load("assets/Design sans titre.png")
#background=pygame.image.load("assets/fond2.jpg")

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
        #self.load_map()

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
                elif map[x][y] == "24" :
                    tiles.append(Tile(img24, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "26" :
                    tiles.append(Tile(img26, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "48" :
                    tiles.append(Tile(img48, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "40" :
                    tiles.append(Tile(img40, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "42" :
                    tiles.append(Tile(img42, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "49" :
                    tiles.append(Tile(img49, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "50" :
                    tiles.append(Tile(img50, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "51" :
                    tiles.append(Tile(img51, x * self.size_tile, y * self.size_tile))
                elif map[x][y] == "52" :
                    tiles.append(Tile(img52, x * self.size_tile, y * self.size_tile))
        return tiles

    def load_map(self, background, laser) :
        self.surface.blit(background, (0, 0))
        if not laser:
            for i in range(len(self.tiles)):
                if self.tiles[i].image == img48:
                    self.tiles[i].image = sky
        for i in range(len(self.tiles)) :
            if self.tiles[i].image != sky :
                self.tiles[i].draw(self.surface)
        return self.tiles

