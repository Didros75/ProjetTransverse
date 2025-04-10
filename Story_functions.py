import pygame
import csv
width=900
height=600

def dialog_box(line, screen, skin, index, talker=2):
    dialogs_hero=[13]
    dialogs_reaper=[8, 9, 12]
    if line in dialogs_hero:
        talker=0
    elif line in dialogs_reaper:
        talker=1
    font=pygame.font.SysFont(None, 30)
    box=pygame.transform.scale(pygame.image.load("assets/meni_menu/dialog.png"), (500, 150))

    hero_idle = [pygame.image.load(f"assets/{skin}/l0_sprite_{i}.png") for i in range(1, 5)]
    reaper_idle = [pygame.transform.scale(pygame.image.load(f"assets/Reaper/l0_reaper_idle{i}.png"), (200, 200)) for i in range(1, 5)]

    with open('dialog.csv', newline='', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier, delimiter=';')
        lecteur = list(lecteur)
        ligne=lecteur[line]

        if ligne!=[]:
            if talker==0:
                screen.blit(hero_idle[int(index%4)], (width / 2 - box.get_width() / 2, height - box.get_height() - 100))
            elif talker==1:
                screen.blit(reaper_idle[int(index%4)], (width / 2 + box.get_width() / 2 - 150, height - box.get_height() - 160))
            screen.blit(box, (width / 2 - box.get_width() / 2, height - box.get_height() - 20))

            liste_text=ligne[0].split("/")
            for elem in range(len(liste_text)):
                text_blit = font.render(liste_text[elem], True, (255, 255, 255))
                screen.blit(text_blit, (width / 2 - box.get_width() / 2 + 20, height - box.get_height()+ elem*25))
            return 1
        else:
            return 0
