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

    # Gestion du déplacement du joueur
    if pressed[pygame.K_LEFT]: posX -= 2
    if pressed[pygame.K_RIGHT]: posX += 2

    # Affichage joueur
    #  On applique cette position au rectangle du joueur
    playerRect.topleft = (posX, posY)
    # On affiche l'image du joueur dans la fenêtre de jeu
    window.blit(player, playerRect)
    # On dessine / mettre à jour le contenu de l'écran
    pygame.display.flip()

# On quitte pygame
pygame.quit()