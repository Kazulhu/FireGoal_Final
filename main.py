import pygame
import sys
from Button import Button
from pygame import mixer
from game import __game__

pygame.init()

# définir une clock qui va permettre de fixer des FPS.

clock = pygame.time.Clock()
FPS = 60

SCREEN = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Menu")
mixer.music.load('assets/squad-infraction-main-version-01-44-13482.mp3')
mixer.music.play(-1)

BG = pygame.image.load("assets/unknown.png")
BG = pygame.transform.scale(BG, (1200, 720))
LOGO = pygame.image.load("assets/logo.png")
LOGO = pygame.transform.scale(LOGO, (170, 140))
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
SCREEN.blit(play_button, (0, 0))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def player2_perso(player2_score, player1_score):
    global player2_choice, player2_gravity

    player2_gravity = 0

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # applique le BG dans une fenêtre spécial

        SCREEN.blit(BG, (0, 00))

        PLAY_TEXT = get_font(18).render("Joueur 2 choisis ton personnage", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=pygame.image.load("DA/icons/shining/back_icon_s.png"), pos=(620, 610),
                           text_input="", font=get_font(75), base_color="White", hovering_color="Green")

        PERSO_TEXT = get_font(18).render("Jerry", True, "Black")
        PERSO_RECT = PERSO_TEXT.get_rect(center=(200, 200))
        SCREEN.blit(PERSO_TEXT, PERSO_RECT)

        PERSO_IMAGE1 = pygame.image.load("DA/players/jerry/jerry.png")
        PERSO_IMAGE = pygame.transform.scale(PERSO_IMAGE1, (100, 200))
        SCREEN.blit(PERSO_IMAGE, (130, 270))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/player.png"), pos=(175, 350),
                             # remplacer l'image par un truc de la même taille que les persos en gros ou sinon prendre les persos déjà de la même forme il faudra voir
                             text_input="", font=get_font(75), base_color="White", hovering_color="Green")

        PERSO_TEXT = get_font(18).render("Red", True, "Black")
        PERSO_RECT = PERSO_TEXT.get_rect(center=(600, 200))
        SCREEN.blit(PERSO_TEXT, PERSO_RECT)

        PERSO_IMAGE1 = pygame.image.load("DA/players/red/red.png")
        PERSO_IMAGE = pygame.transform.scale(PERSO_IMAGE1, (100, 200))
        SCREEN.blit(PERSO_IMAGE, (550, 250))

        PLAY_BUTTON1 = Button(image=pygame.image.load("assets/player.png"), pos=(600, 350),
                              text_input="", font=get_font(75), base_color="White", hovering_color="Green")

        PERSO_TEXT = get_font(18).render("Sanji", True, "Black")
        PERSO_RECT = PERSO_TEXT.get_rect(center=(1000, 200))
        SCREEN.blit(PERSO_TEXT, PERSO_RECT)

        PERSO_IMAGE1 = pygame.image.load("DA/players/sanji/sanji.png")
        PERSO_IMAGE = pygame.transform.scale(PERSO_IMAGE1, (100, 200))
        SCREEN.blit(PERSO_IMAGE, (950, 250))

        PLAY_BUTTON2 = Button(image=pygame.image.load("assets/player.png"), pos=(1000, 350),
                              text_input="", font=get_font(1), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for button in [PERSO_TEXT, PERSO_RECT, PERSO_IMAGE1, PERSO_IMAGE]:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        play()
                    if PLAY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        player2_choice = 1
                        __game__(player1_choice, player2_choice, player2_score, player1_score)
                    if PLAY_BUTTON1.checkForInput(PLAY_MOUSE_POS):
                        player2_choice = 2
                        __game__(player1_choice, player2_choice, player2_score, player1_score)
                    if PLAY_BUTTON2.checkForInput(PLAY_MOUSE_POS):
                        player2_choice = 3
                        __game__(player1_choice, player2_choice, player2_score, player1_score)

        pygame.display.update()
        clock.tick(FPS)


def play():
    global player1_choice, player_gravity

    player_gravity = 0

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # applique le BG dans une fenêtre spécial

        SCREEN.blit(BG, (0, 00))

        PLAY_TEXT = get_font(18).render("Joueur 1 choisis ton personnage", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=pygame.image.load("DA/icons/shining/back_icon_s.png"), pos=(620, 610),
                           text_input="", font=get_font(75), base_color="White", hovering_color="Green")

        PERSO_TEXT = get_font(18).render("Jerry", True, "Black")
        PERSO_RECT = PERSO_TEXT.get_rect(center=(200, 200))
        SCREEN.blit(PERSO_TEXT, PERSO_RECT)

        PERSO_IMAGE1 = pygame.image.load("DA/players/jerry/jerry.png")
        PERSO_IMAGE = pygame.transform.scale(PERSO_IMAGE1, (100, 200))
        SCREEN.blit(PERSO_IMAGE, (130, 270))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/player.png"), pos=(175, 350),
                             # remplacer l'image par un truc de la même taille que les persos en gros ou sinon prendre les persos déjà de la même forme il faudra voir
                             text_input="", font=get_font(75), base_color="White", hovering_color="Green")

        PERSO_TEXT = get_font(18).render("Red", True, "Black")
        PERSO_RECT = PERSO_TEXT.get_rect(center=(600, 200))
        SCREEN.blit(PERSO_TEXT, PERSO_RECT)

        PERSO_IMAGE1 = pygame.image.load("DA/players/red/red.png")
        PERSO_IMAGE = pygame.transform.scale(PERSO_IMAGE1, (100, 200))
        SCREEN.blit(PERSO_IMAGE, (550, 250))

        PLAY_BUTTON1 = Button(image=pygame.image.load("assets/player.png"), pos=(600, 350),
                              text_input="", font=get_font(75), base_color="White", hovering_color="Green")

        PERSO_TEXT = get_font(18).render("Sanji", True, "Black")
        PERSO_RECT = PERSO_TEXT.get_rect(center=(1000, 200))
        SCREEN.blit(PERSO_TEXT, PERSO_RECT)

        PERSO_IMAGE1 = pygame.image.load("DA/players/sanji/sanji.png")
        PERSO_IMAGE = pygame.transform.scale(PERSO_IMAGE1, (100, 200))
        SCREEN.blit(PERSO_IMAGE, (950, 250))

        PLAY_BUTTON2 = Button(image=pygame.image.load("assets/player.png"), pos=(1000, 350),
                              text_input="", font=get_font(1), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        player1_score = 0
        player2_score = 0

        for button in [PERSO_TEXT, PERSO_RECT, PERSO_IMAGE1, PERSO_IMAGE]:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                    if PLAY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        player1_choice = 1
                        player2_perso(player2_score, player1_score)
                    if PLAY_BUTTON1.checkForInput(PLAY_MOUSE_POS):
                        player1_choice = 2
                        player2_perso(player2_score, player1_score)
                    if PLAY_BUTTON2.checkForInput(PLAY_MOUSE_POS):
                        player1_choice = 3
                        player2_perso(player2_score, player1_score)



        pygame.display.update()
        clock.tick(FPS)


def options():
    while True:
        VOLUME = 100
        volumeplus_button = Button(image=pygame.image.load("assets/volume_icon1.png"), pos=(640, 600),
                                   text_input="", font=get_font(89), base_color="#d7fcd4", hovering_color="Green")
        volumeminus_button = Button(image=pygame.image.load("assets/volume_icon2.png"), pos=(740, 600),
                                    text_input="", font=get_font(89), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 00))
        pygame.display.flip

        CONTROLS_TEXT1 = get_font(25).render("CONTROLS PLAYER 1", True, "Black")
        CONTROLS_TEXT2 = get_font(25).render("CONTROLS PLAYER 2", True, "Black")
        CONTROLS_RECT1 = CONTROLS_TEXT1.get_rect(center=(300, 90))
        CONTROLS_RECT2 = CONTROLS_TEXT2.get_rect(center=(900, 90))

        CONTROLS_PLAYER_3 = get_font(25).render("GO LEFT", True, "Black")
        CONTROLS_PLAYER_1 = get_font(25).render("JUMP", True, "Black")
        CONTROLS_PLAYER_2 = get_font(25).render("GO RIGHT", True, "Black")
        CONTROLS_RAYER1 = CONTROLS_PLAYER_1.get_rect(center=(610, 190))
        CONTROLS_RAYER2 = CONTROLS_PLAYER_2.get_rect(center=(610, 330))
        CONTROLS_RAYER3 = CONTROLS_PLAYER_3.get_rect(center=(610, 480))

        UP_PLAYER1 = Button(image=pygame.image.load("assets/z.png"), pos=(290, 190),
                            text_input="", font=get_font(75), base_color="Black", hovering_color="Green")
        UP_PLAYER1.update(SCREEN)
        RIGHT_PLAYER1 = Button(image=pygame.image.load("assets/d.png"), pos=(290, 330),
                               text_input="", font=get_font(75), base_color="Black", hovering_color="Green")
        RIGHT_PLAYER1.update(SCREEN)
        LEFT_PLAYER1 = Button(image=pygame.image.load("assets/q.png"), pos=(290, 480),
                              text_input="", font=get_font(75), base_color="Black", hovering_color="Green")
        LEFT_PLAYER1.update(SCREEN)

        UP_PLAYER2 = Button(image=pygame.image.load("assets/up.png"), pos=(890, 190),
                            text_input="", font=get_font(75), base_color="Black", hovering_color="Green")
        UP_PLAYER2.update(SCREEN)
        RIGHT_PLAYER2 = Button(image=pygame.image.load("assets/right.png"), pos=(890, 330),
                               text_input="", font=get_font(75), base_color="Black", hovering_color="Green")
        RIGHT_PLAYER2.update(SCREEN)
        LEFT_PLAYER2 = Button(image=pygame.image.load("assets/left.png"), pos=(890, 480),
                              text_input="", font=get_font(75), base_color="Black", hovering_color="Green")
        LEFT_PLAYER2.update(SCREEN)

        OPTIONS_BACK = Button(image=pygame.image.load("DA/icons/shining/back_icon_s.png"), pos=(620, 610),
                              text_input="", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        SCREEN.blit(CONTROLS_TEXT1, CONTROLS_RECT1)
        SCREEN.blit(CONTROLS_TEXT2, CONTROLS_RECT2)
        SCREEN.blit(CONTROLS_PLAYER_1, CONTROLS_RAYER1)
        SCREEN.blit(CONTROLS_PLAYER_2, CONTROLS_RAYER2)
        SCREEN.blit(CONTROLS_PLAYER_3, CONTROLS_RAYER3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()


def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0), )
        pygame.display.flip

        CREDITS_TEXT = get_font(70).render(" CREDITS ", True, "Green")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 60))
        CREDITS_TEXT1 = get_font(20).render("Coordinateur pôle codage", True, "Black")
        CREDITS_RECT1 = CREDITS_TEXT1.get_rect(center=(640, 170))
        CREDITS_TEXT12 = get_font(20).render("Guillaume Rousselin", True, "Yellow")
        CREDITS_RECT12 = CREDITS_TEXT12.get_rect(center=(640, 210))

        CREDITS_TEXT2 = get_font(20).render("Coordinateur du département graphique", True, "Black")
        CREDITS_RECT2 = CREDITS_TEXT2.get_rect(center=(640, 250))
        CREDITS_TEXT22 = get_font(20).render("Quentin Rault", True, "Yellow")
        CREDITS_RECT22 = CREDITS_TEXT22.get_rect(center=(640, 290))

        CREDITS_TEXT3 = get_font(20).render("Coordinateur pôle interface", True, "Black")
        CREDITS_RECT3 = CREDITS_TEXT3.get_rect(center=(640, 330))
        CREDITS_TEXT32 = get_font(20).render("Kévin Tran", True, "Yellow")
        CREDITS_RECT32 = CREDITS_TEXT32.get_rect(center=(640, 370))

        CREDITS_TEXT4 = get_font(20).render("Coordinateur de la partie physique", True, "Black")
        CREDITS_RECT4 = CREDITS_TEXT4.get_rect(center=(640, 410))
        CREDITS_TEXT42 = get_font(20).render("Fady Mechlaoui", True, "Yellow")
        CREDITS_RECT42 = CREDITS_TEXT42.get_rect(center=(640, 450))

        CREDITS_TEXT5 = get_font(20).render("Coordinateur pôle artistique", True, "Black")
        CREDITS_RECT5 = CREDITS_TEXT5.get_rect(center=(640, 490))
        CREDITS_TEXT52 = get_font(20).render("Romain Ferigo", True, "Yellow")
        CREDITS_RECT52 = CREDITS_TEXT52.get_rect(center=(640, 530))

        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        SCREEN.blit(CREDITS_TEXT1, CREDITS_RECT1)
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)
        SCREEN.blit(CREDITS_TEXT5, CREDITS_RECT5)
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)
        SCREEN.blit(CREDITS_TEXT4, CREDITS_RECT4)
        SCREEN.blit(CREDITS_TEXT12, CREDITS_RECT12)
        SCREEN.blit(CREDITS_TEXT22, CREDITS_RECT22)
        SCREEN.blit(CREDITS_TEXT32, CREDITS_RECT32)
        SCREEN.blit(CREDITS_TEXT42, CREDITS_RECT42)
        SCREEN.blit(CREDITS_TEXT52, CREDITS_RECT52)

        CREDITS_BACK = Button(image=pygame.image.load("DA/icons/shining/back_icon_s.png"), pos=(620, 630),
                              text_input="", font=get_font(75), base_color="Black", hovering_color="Green")

        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        for event in pygame.event.get():  # ici c'est quand il appuie sur la croix rouge pour quitter directement.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()
        pygame.display.update()


def main_menu():
    mixer.music.load('DA/sounds/musics/Head Soccer 95 bpm.mp3')
    mixer.music.play(-1, 0, 10000)
    NO_SOUND = False
    while True:

        SCREEN.blit(BG, (0, 0), )
        SCREEN.blit(LOGO, (553, 30), )
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("FiRE   GOAL", True, "orange""")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("DA/icons/shining/start_icon_s.png"), pos=(640, 300),
                             text_input="", font=get_font(89), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("DA/icons/shining/parameter_icon_s.png"), pos=(640, 540),
                                text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("DA/icons/shining/quit_icon_s.png"), pos=(100, 630),
                             text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SOUND_BUTTON = Button(image=pygame.image.load("DA/icons/shining/music_off_s.png"), pos=(1145, 159),
                              text_input="", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        NOSOUND_BUTTON = Button(image=pygame.image.load("DA/icons/shining/music_on_s.png"), pos=(1145, 70),
                                text_input="", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("DA/icons/shining/info_icon_s.png"), pos=(1100, 630),
                                text_input="", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
        # SOUND_BUTTON1= pygame.image.load("assets/sound_logo.png")
        # SOUND_BUTTON1 = pygame.transform.scale(SOUND_BUTTON1, (4,  10))
        # SCREEN.blit(pygame.transform.scale(SOUND_BUTTON1, (0, 0), SOUND_BUTTON1))
        # pygame.display.flip()

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SOUND_BUTTON, NOSOUND_BUTTON, CREDITS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if SOUND_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.pause()
                if NOSOUND_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.unpause()

        clock.tick(FPS)
        pygame.display.update()


main_menu()
