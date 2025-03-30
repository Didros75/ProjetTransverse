import pygame

class SoundManager:
    def __init__(self, sound=True):
        pygame.mixer.init()
        self.music_file = "assets/musique.mp3"
        self.sound = sound
        self.button_sound = pygame.mixer.Sound("assets/click.mp3")
        self.tp_sound = pygame.mixer.Sound("assets/portal_sound.mp3")
        self.charging_sound = pygame.mixer.Sound("assets/charging.mp3")
        self.tp_sound.set_volume(0.2)

        self.tp_channel = pygame.mixer.Channel(1)
        self.charging_channel = pygame.mixer.Channel(2)
        self.charging_playing = False

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

    def play_button_sound(self):
        self.button_sound.play()

    def play_tp_sound(self):
        self.tp_channel.play(self.tp_sound)

    def play_charging_sound(self):
        if not self.charging_playing:
            self.charging_channel.play(self.charging_sound)
            self.charging_playing = True

    def stop_charging_sound(self):
        self.charging_channel.stop()
        self.charging_playing = False
