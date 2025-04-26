import time
import pygame
import os

class PngPlayer:
    def __init__(self, frames_folder, screen, position=(0, 0), fps=10):
        self.frames_folder = frames_folder
        self.screen = screen
        self.position = position
        self.fps = fps
        self.frames = []
        self.index = 0
        self.playing = True
        self.timer = 0

        self.load_frames()

    def load_frames(self):
        files = sorted(os.listdir(self.frames_folder))
        for file in files:
            if file.endswith('.png'):
                path = os.path.join(self.frames_folder, file)
                image = pygame.image.load(path).convert_alpha()
                image = pygame.transform.scale(image, (900, 600))
                self.frames.append(image)

    def play(self):
        for i in range(len(self.frames)) :
            frame = self.frames[i]
            self.screen.blit(frame, self.position)
            pygame.display.flip()
            time.sleep(3)