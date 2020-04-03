# coding=utf-8
# Auteur --> BloodyMasth
# Game --> Crazy Car Race
import sys
import pygame
import time
import random


pygame.init()
# Les dimensions et couleurs
gris = (102, 102, 102)
noir = (0, 0, 0)
rouge = (200, 0, 0)
vert = (0, 200, 0)
bleu = (0, 20, 255)
rouge_clair = (255, 0, 0)
vert_clair = (0, 255, 0)
bleu_clair = (0, 100, 255)
display_width = 800
display_height = 600
en_pause = False

gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Crazy Race")
clock = pygame.time.Clock()
car_img = pygame.image.load("voiture perso.png")
background_img = pygame.image.load("bande d'herbe2.png")
petite_bande = pygame.image.load("bande blanche milieu.png")
grande_bande = pygame.image.load("bande blanche.png")
menu_background = pygame.image.load("background.gif")
controle_background = pygame.image.load("beautiful_background2.jpg")
icon = pygame.image.load("sedan-car-front.png")
x_voiture = 56
y_voiture = 125
play = 0

# Musique de fond de la fenètre d'acceuil
def musique_background():
    pygame.mixer.music.load("The Black Eyed Peas - Pump It.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)  # Met le volume à 0.5 (moitié)

# Fenètre du menu
def menu_loop():
    global play
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        pygame.display.set_icon(icon)
        gamedisplay.blit(menu_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        Text_Surf, Text_Rect = text_objects("Crazy Race", largetext)
        Text_Rect.center = (400, 100)
        gamedisplay.blit(Text_Surf, Text_Rect)
        button("Jouer", 100, 520, 150, 50, vert, vert_clair, "play")
        button("Instruction", 300, 520, 200, 50, bleu, bleu_clair, "setting")
        button("Quitter", 550, 520, 150, 50, rouge, rouge_clair, "quit")
        pygame.display.update()
        clock.tick(50)

# Fenètre du menu lors du retour au menu principale
def menu_loop2():
    global play
    menu = True
    musique_background()
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        pygame.display.set_icon(icon)
        gamedisplay.blit(menu_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        Text_Surf, Text_Rect = text_objects("Crazy Race", largetext)
        Text_Rect.center = (400, 100)
        gamedisplay.blit(Text_Surf, Text_Rect)
        button("Jouer", 100, 520, 150, 50, vert, vert_clair, "play")
        button("Instruction", 300, 520, 200, 50, bleu, bleu_clair, "setting")
        button("Quitter", 550, 520, 150, 50, rouge, rouge_clair, "quit")
        pygame.display.update()
        clock.tick(50)

# Fenètre des instructiuon et controles
def instruction():
    global play
    controles = True
    while controles:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(controle_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 80)
        mediumtext = pygame.font.Font("freesansbold.ttf", 50)
        smalltext = pygame.font.Font("freesansbold.ttf", 25)
        intro_text_surf, intro_text_rect = text_objects("Instruction", largetext)
        intro_text_rect.center = (400, 100)
        def_text_Surf, def_text_Rect = text_objects("Dans ce jeu le but est d'éviter les voitures", smalltext)
        def_text_Rect.center = (400, 170)
        def_text_Surf_2, def_text_Rect_2 = text_objects("qui viennent en sens inverse", smalltext)
        def_text_Rect_2.center = (400, 200)
        ctrl_text_surf, ctrl_text_rect = text_objects("Contrôles", mediumtext)
        ctrl_text_rect.center = (400, 270)
        fg_text_surf, fg_text_rect = text_objects("Flêche Gauche : Aller à Gauche", smalltext)
        fg_text_rect.center = (210, 350)
        fd_text_surf, fd_text_rect = text_objects("Flêche Droite : Aller à Droite", smalltext)
        fd_text_rect.center = (200, 400)
        p_text_surf, p_text_rect = text_objects("Touche Espace : Pause", smalltext)
        p_text_rect.center = (200, 450)
        a_text_surf, a_text_rect = text_objects("Touche A : Accélérer", smalltext)
        a_text_rect.center = (200, 500)
        f_text_surf, f_text_rect = text_objects("Touche F : Freiner", smalltext)
        f_text_rect.center = (200, 550)
        gamedisplay.blit(intro_text_surf, intro_text_rect)
        gamedisplay.blit(def_text_Surf, def_text_Rect)
        gamedisplay.blit(def_text_Surf_2, def_text_Rect_2)
        gamedisplay.blit(ctrl_text_surf, ctrl_text_rect)
        gamedisplay.blit(fg_text_surf, fg_text_rect)
        gamedisplay.blit(fd_text_surf, fd_text_rect)
        gamedisplay.blit(p_text_surf, p_text_rect)
        gamedisplay.blit(a_text_surf, a_text_rect)
        gamedisplay.blit(f_text_surf, f_text_rect)
        button("Retour", 600, 450, 100, 50, bleu, bleu_clair, "menu")
        pygame.display.update()
        clock.tick(30)


# Bouton du menu
def button(msg, x, y, button_widht, button_height, inactive_color, activ_color, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + button_widht > mouse[0] > x and y + button_height > mouse[1] > y:
        pygame.draw.rect(gamedisplay, activ_color, (x, y, button_widht, button_height))
        if click[0] == 1 and action is not None:
            if action == "play":
                compte_a_rebours()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "setting":
                instruction()
            elif action == "menu":
                menu_loop()
            elif action == "menu2":
                menu_loop2()
            elif action == "pause":
                ecran_pause()
            elif action == "reprendre":
                reprendre()
    else:
        pygame.draw.rect(gamedisplay, inactive_color, (x, y, button_widht, button_height))
    
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (button_widht / 2)), (y + (button_height / 2)))
    gamedisplay.blit(textsurf, textrect)


# Fenètre de pause
def ecran_pause():
    pygame.mixer.music.pause()
    global en_pause
    en_pause = True
    while en_pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(controle_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        text_surf, text_rect = text_objects("PAUSE", largetext)
        text_rect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(text_surf, text_rect)
        button("Continuer", 150, 450, 150, 50, vert, vert_clair, "reprendre")
        button("Reccomencer", 350, 450, 150, 50, bleu, bleu_clair, "play")
        button("Menu Principal", 550, 450, 180, 50, rouge, rouge_clair, "menu2")
        pygame.display.update()
        clock.tick(30)


# Fonction pour reprendre le jeu
def reprendre():
    global en_pause
    en_pause = False
    pygame.mixer.music.unpause()

def compte_a_rebours_fond():
    font = pygame.font.SysFont(None, 25)
    x = (display_width * 0.6)
    y = (display_height * 0.7)
    gamedisplay.blit(background_img, (0, 0))
    gamedisplay.blit(background_img, (650, 0))
    gamedisplay.blit(petite_bande, (400, 0))
    gamedisplay.blit(petite_bande, (400, 100))
    gamedisplay.blit(petite_bande, (400, 200))
    gamedisplay.blit(petite_bande, (400, 300))
    gamedisplay.blit(petite_bande, (400, 400))
    gamedisplay.blit(petite_bande, (400, 500))
    gamedisplay.blit(petite_bande, (400, 590))
    gamedisplay.blit(grande_bande, (180, 0))
    gamedisplay.blit(grande_bande, (610, 0))
    gamedisplay.blit(car_img, (x, y))
    text = font.render("Eviter : 0" , True, noir)
    score = font.render("Score : 0", True, rouge)
    gamedisplay.blit(text, (0, 50))
    gamedisplay.blit(score, (0, 30))
    # Bouton Pause dans la fenètre de compte a rebourd
    button("Pause", 650, 0, 150, 50, bleu, bleu_clair, "pause")

def compte_a_rebours():
    compte_rebours = True
    while compte_rebours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.fill(gris)
        compte_a_rebours_fond()
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        text_surf, text_rect = text_objects("3", largetext)
        text_rect.center = ((display_width/2), (display_height/2))
        gamedisplay.blit(text_surf, text_rect)
        pygame.display.update()
        clock.tick(1)
        gamedisplay.fill(gris)
        compte_a_rebours_fond()
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        text_surf, text_rect = text_objects("2", largetext)
        text_rect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(text_surf, text_rect)
        pygame.display.update()
        clock.tick(1)
        pygame.mixer.music.fadeout(400)  # Fondu à 400ms de la fin des musiques
        gamedisplay.fill(gris)
        compte_a_rebours_fond()
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        text_surf, text_rect = text_objects("1", largetext)
        text_rect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(text_surf, text_rect)
        pygame.display.update()
        clock.tick(1)
        gamedisplay.fill(gris)
        compte_a_rebours_fond()
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        text_surf, text_rect = text_objects("Let's Go !!", largetext)
        text_rect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(text_surf, text_rect)

        pygame.display.update()
        clock.tick(1)
        game_loop()




# Les voiture en sens inverse
def obstacle_func(obstacle_start_x, obstacle_start_y, obstacle):
    global obstacle_img
    if obstacle == 0:
        obstacle_img = pygame.image.load("voiture 1.png")
    elif obstacle == 1:
        obstacle_img = pygame.image.load("voiture 2.png")
    elif obstacle == 2:
        obstacle_img = pygame.image.load("voiture 3.png")
    elif obstacle == 3:
        obstacle_img = pygame.image.load("voiture 4.png")
    elif obstacle == 4:
        obstacle_img = pygame.image.load("voiture 5.png")
    elif obstacle == 5:
        obstacle_img = pygame.image.load("voiture 6.png")
    gamedisplay.blit(obstacle_img, (obstacle_start_x, obstacle_start_y))


# Foncion du score
def score_systeme(voiture_pass, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Eviter : " + str(voiture_pass), True, noir)
    score = font.render("Score : " + str(score), True, rouge)
    gamedisplay.blit(text, (0, 50))
    gamedisplay.blit(score, (0, 30))


def text_objects(text, font):
    textsurface = font.render(text, True, noir)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    pygame.mixer.music.load("crash voiture.mp3")
    pygame.mixer.music.play()
    message_display("You Crashed")


# Fonction des element de décor
def background():
    gamedisplay.blit(background_img, (0, 0))
    gamedisplay.blit(background_img, (0, 200))
    gamedisplay.blit(background_img, (0, 400))

    gamedisplay.blit(background_img, (650, 0))
    gamedisplay.blit(background_img, (650, 200))
    gamedisplay.blit(background_img, (650, 400))

    gamedisplay.blit(petite_bande, (400, -100))
    gamedisplay.blit(petite_bande, (400, 0))
    gamedisplay.blit(petite_bande, (400, 100))
    gamedisplay.blit(petite_bande, (400, 200))
    gamedisplay.blit(petite_bande, (400, 300))
    gamedisplay.blit(petite_bande, (400, 400))
    gamedisplay.blit(petite_bande, (400, 500))
    gamedisplay.blit(petite_bande, (400, 600))

    gamedisplay.blit(grande_bande, (180, 0))
    gamedisplay.blit(grande_bande, (180, 100))
    gamedisplay.blit(grande_bande, (180, 200))

    gamedisplay.blit(grande_bande, (610, 0))
    gamedisplay.blit(grande_bande, (610, 100))
    gamedisplay.blit(grande_bande, (610, 200))


# Fonction affichage de la voiture du joueur
def car(x, y):
    gamedisplay.blit(car_img, (x, y))


# Foncion du jeu global
def game_loop():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("circulation.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)  # Met le volume à 0.5 (moitié)
    global en_pause
    # Taille de la voiture
    x = (display_width * 0.6)
    y = (display_height * 0.7)
    x_moove = 0
    # Initialisation des obstacles
    obstacle_speed = 11
    obstacle = 0
    obstacle_start_x = random.randrange(200, (display_width - 250))
    obstacle_start_y = -750
    obstacle_width = 56
    obstacle_height = 125
    # Initialisation des scores
    voiture_pass = 0
    level = 0
    score = 0
    # Vitesse du mouvement du fond
    y_moove_background = 7

    launched = False
    while not launched:
        # Clic sur la croix rouge
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Quand le touche est appuyer (keydown)
            if event.type == pygame.KEYDOWN:
                # Déplacement de la voiture du joueur
                # Touche pour aller à gauche avec la voiture
                if event.key == pygame.K_LEFT:
                    x_moove = -5
                # Touche pour aller à droite avec la voiture
                if event.key == pygame.K_RIGHT:
                    x_moove = 5
                # Touche pour accélérer avec la voiture
                if event.key == pygame.K_a:
                    obstacle_speed = obstacle_speed + 2
                # Touche pour freiner avec la voiture
                if event.key == pygame.K_f and obstacle_speed >= 8:
                    obstacle_speed = obstacle_speed - 2
                # Touche pour mettre en pause
                if event.key == pygame.K_SPACE:
                    ecran_pause()
            # Quand la touche n'est pas appuyer (keyup)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_moove = 0
        # Actualisation de la position de la voiture
        x = x + x_moove
        en_pause = True
        # Fond de la fenètre
        gamedisplay.fill(gris)

        # Fond de la fenètre qui bouge
        rel_y = y_moove_background % background_img.get_rect().width
        gamedisplay.blit(background_img, (0, rel_y - background_img.get_rect().width))
        gamedisplay.blit(background_img, (650, rel_y - background_img.get_rect().width))
        if rel_y < 800:
            gamedisplay.blit(background_img, (0, rel_y))
            gamedisplay.blit(background_img, (650, rel_y))

            gamedisplay.blit(petite_bande, (400, rel_y))
            gamedisplay.blit(petite_bande, (400, rel_y + 100))
            gamedisplay.blit(petite_bande, (400, rel_y + 200))
            gamedisplay.blit(petite_bande, (400, rel_y + 300))
            gamedisplay.blit(petite_bande, (400, rel_y + 400))
            gamedisplay.blit(petite_bande, (400, rel_y + 500))
            gamedisplay.blit(petite_bande, (400, rel_y + 600))
            gamedisplay.blit(petite_bande, (400, rel_y - 100))
            gamedisplay.blit(petite_bande, (400, rel_y - 200))

            gamedisplay.blit(grande_bande, (180, rel_y -  200))
            gamedisplay.blit(grande_bande, (180, rel_y + 20))
            gamedisplay.blit(grande_bande, (180, rel_y + 30))
            gamedisplay.blit(grande_bande, (610, rel_y - 200))
            gamedisplay.blit(grande_bande, (610, rel_y + 20))
            gamedisplay.blit(grande_bande, (610, rel_y + 30))

            y_moove_background = y_moove_background + obstacle_speed



        # Affichage des élément de décor

        # Position de départ des obstacle en x, y
        obstacle_start_y = obstacle_start_y - (obstacle_speed / 4)
        obstacle_func(obstacle_start_x, obstacle_start_y, obstacle)
        obstacle_start_y = obstacle_start_y + obstacle_speed
        # Affichage de la voiture du joueur
        car(x, y)
        # Affichage des scores
        score_systeme(voiture_pass, score)
        # Condition d'accident
        # Si la voiture sort de la route
        if x < 180 or x > 620 - x_voiture:
            crash()
        if x > display_width - (x_voiture + 110) or x < 180:
            crash()
        # Si la voiture rencontre une autre voiture
        if y < obstacle_start_y + obstacle_height < y + 250:
            if obstacle_start_x < x < obstacle_start_x + obstacle_width or obstacle_start_x < x + x_voiture < obstacle_start_x + obstacle_width:
                crash()
        # Spawn des obstacles
        if obstacle_start_y > display_height:
            obstacle_start_y = 0 - obstacle_height
            obstacle_start_x = random.randrange(200, (display_width - 220))
            # Choix de la voiture
            obstacle = random.randrange(0, 6)
            # Score du joueur
            voiture_pass = voiture_pass + 1
            score = voiture_pass * 10
            # Passage au niveau suivant
            if int(voiture_pass) % 10 == 0:
                level = level + 1
                obstacle_speed = obstacle_speed + 2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("Niveau : " + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplay.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)
        # Bouton Pause dans la fenètre de jeu
        button("Pause", 650, 0, 150, 50, bleu, bleu_clair, "pause")
        pygame.display.update()
        clock.tick(60)

musique_background()
menu_loop()
game_loop()
pygame.quit()
quit()
