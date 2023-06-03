import random
# Importation de pygame
import pygame

# Initialisation de pygame
pygame.init()

# Création de la fenêtre pour afficher le jeu
window = pygame.display.set_mode((800, 600))

# Modifier le titre et l'icone de la fenêtre
pygame.display.set_caption("My space invaders")
windowIcon = pygame.image.load("alien.png")
pygame.display.set_icon(windowIcon)

# On charge l'image du joueur
player = pygame.image.load("player.png")
# On convertie l'image du joueur en rectangle
playerRect = player.get_rect()
#  Position du joueur
posX = 350
posY = 480
# Image de background
bg = pygame.image.load("bg.png")
playerSpeed = 5

# Image pour le laser de notre joueur
laser = pygame.image.load("laser.png")
laserSpeed = 4
posLaserX = 0
posLaserY = -100
canShoot = True

# L'OVNI ennemi
ovni = pygame.image.load("ufoGreen.png")
ovniSpeed = 2
posOvniX = random.randint(1, 750)
posOvniY = 50



# Pour définir les FPS (Frame Per Second) du jeu ou image par secondes sur l'écran
clock = pygame.time.Clock()
# La boucle de jeu
running = True
while running:
    # Couleur de l'écran
    window.fill((0, 0, 0))
    window.blit(bg, (0, 0))
    # On check tous les événements (clavier ou souris)
    for event in pygame.event.get():
        # Est ce que l'utilisateur appuie sur une touche du clavier ?
        pressed = pygame.key.get_pressed()
        # On teste si l'utilisateur click sur la croix de la fenêtre
        if event.type == pygame.QUIT:
            # Si c'est le cas on met la variable running à False
            running = False
        # On teste si l'utilisateur appuie sur une touche du clavier exemple de déplacement cran par cran (pas fluide)
        # On va utiliser une autre méthode pour gérer les touches du clavier
        """if event.type == pygame.KEYDOWN:
            # De quelle touche s'agit-il ?
            if event.key == pygame.K_LEFT:
                # On déplace le joueur vers la gauche
                posX -= 50
            if event.key == pygame.K_RIGHT:
                # On déplace le joueur vers la droite
                posX += 50"""

        # Detection barre d'espace pour tirer un laser
        if event.type == pygame.KEYDOWN:
            # De quelle touche s'agit-il ?
            if event.key == pygame.K_SPACE and canShoot:
                canShoot = False
                # Position du laser
                posLaserX = posX + 45
                # On déplace le laser vers le haut du vaisseau
                posLaserY = posY - 50
            

    # Gestion du déplacement du joueur
    if pressed[pygame.K_LEFT] and posX > 0:  # Si la touche gauche est pressée et que la position en X est supérieur à 0
        posX -= playerSpeed # On déplace le joueur vers la gauche
    if pressed[pygame.K_RIGHT] and posX < 700: # Si la touche droite est pressée et que la position en X est inférieur à 700 donc 800 - 100 (la taille du joueur)
        posX += playerSpeed

    # Affichage joueur
    #  On applique cette position au rectangle du joueur
    playerRect.topleft = (posX, posY)
    # On affiche l'image du joueur dans la fenêtre de jeu
    window.blit(player, playerRect)

    # Gestion du laser
    posLaserY -= laserSpeed
    window.blit(laser, (posLaserX, posLaserY))
    if posLaserY < -40:
        canShoot = True

    # Gestion de l'OVNI
    posOvniX -= ovniSpeed
    window.blit(ovni, (posOvniX, posOvniY))
    if posOvniX < 0 or posOvniX > 710:
        ovniSpeed = -ovniSpeed
        posOvniY += 50

    # On dessine / mettre à jour le contenu de l'écran
    pygame.display.flip()
    clock.tick(60)

# On quitte pygame
pygame.quit()