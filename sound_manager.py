    # Gère les intéractions liées à la musique et au son

import pygame

class SoundManager:
    def __init__(self, sound=True):
        """
        Initialise les paramètres définissant le son

        :param sound: un booléen à True si la musique joue, False sinon
        """
        pygame.mixer.init()
        self.sound = sound
        self.music_file = "assets/Sounds/musique.mp3"
        self.button_sound = pygame.mixer.Sound("assets/Sounds/click.mp3")
        self.tp_sound = pygame.mixer.Sound("assets/Sounds/portal_sound.mp3")
        self.charging_sound = pygame.mixer.Sound("assets/Sounds/charging.mp3")
        self.tp_sound.set_volume(0.2)

        self.tp_channel = pygame.mixer.Channel(1)
        self.charging_channel = pygame.mixer.Channel(2)
        self.charging_playing = False

        # Appelle la fonction qui lance la musique

        if self.sound:
            self.play_music()

    def play_music(self):
        """
        Permet de lancer la musique en définissant le volume, la musique à lanccer etc...
        """
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def pause_music(self):
        """
        Permet de mettre la musique sur pause
        """
        pygame.mixer.music.pause()

    def resume_music(self):
        """
        Permet de rejouer la musique quand elle est mise sur pause
        """
        pygame.mixer.music.unpause()

    def play_button_sound(self):
        """
        Permet de lancer le son que fait un bouton quand on clique dessus
        """
        self.button_sound.play()

    def play_tp_sound(self):
        """
        Permet de lancer le son que fait le joueur quand il se téléporte
        """
        self.tp_channel.play(self.tp_sound)

    def play_charging_sound(self):
        """
        Permet de lancer le son que fait la barre de chargement
        """
        if not self.charging_playing:
            self.charging_channel.play(self.charging_sound)
            self.charging_playing = True

    def stop_charging_sound(self):
        """
        Permet de lancer le son que fait la barre de chargement quand elle atteint sa puissance maximmum
        """
        self.charging_channel.stop()
        self.charging_playing = False