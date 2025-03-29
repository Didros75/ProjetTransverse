import pygame


class SoundManager:
    def __init__(self, sound=True):
        pygame.mixer.init()
        self.music_file = "assets/musique.mp3"
        self.button_sound_file = "assets/click.mp3"
        self.sound = sound
        self.button_sound = pygame.mixer.Sound(self.button_sound_file)
        if self.sound:
            self.play_music()

    def play_music(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def set_sound(self, sound):
        self.sound = sound
        if self.sound:
            self.play_music()
        else:
            self.stop_music()

    def play_button_sound(self):
        self.button_sound.play()

if __name__ == "__main__":
    pygame.init()
    sound_manager = SoundManager("background_music.mp3", sound=True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
