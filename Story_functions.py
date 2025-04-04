import pygame
import csv
width=900
height=600

def dialog_box(line, screen, talker=0):
    font=pygame.font.SysFont(None, 30)
    box=pygame.transform.scale(pygame.image.load("assets/meni_menu/dialog.png"), (500, 150))


    with open('dialog.csv', newline='', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier, delimiter=';')
        for i, ligne in enumerate(lecteur):
            if i == line:
                print(ligne)
                if ligne == [] :
                    return 0
                else :
                    if ligne != ['', '']:
                        screen.blit(box, (width / 2 - box.get_width() / 2, height - box.get_height() - 20))
                    liste_text=ligne[0].split("/")
        try:
            for elem in range(len(liste_text)):
                print(liste_text[elem])
                text_blit = font.render(liste_text[elem], True, (255, 255, 255))
                screen.blit(text_blit, (width / 2 - box.get_width() / 2 + 20, height - box.get_height()+ elem*25))
        except:
            return 1
        return 1



