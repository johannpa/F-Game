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
laserRect = laser.get_rect()
laserSpeed = 4
posLaserX = 0
posLaserY = -100
canShoot = True

# L'OVNI ennemi
# ovni = pygame.image.load("ufoGreen.png")
# ovniRect = ovni.get_rect()
# posOvniX = random.randint(1, 750)
# posOvniY = 50
# ovniSpeed = 3


ovni = [] # Image
ovniRect = [] # Rect
posOvniX = [] # pos x
posOvniY = [] # pos y
ovniSpeed = [] # tableau de vitesse pour chaque ovni
nbOvni = 4

# Texte
score = 0
font = pygame.font.Font("freesansbold.ttf", 48)
txtPos = 10

# Boucle de génération des OVNI
for i in range(nbOvni):
    ovni.append(pygame.image.load("ufoGreen.png"))
    ovniRect.append(ovni[i].get_rect())
    posOvniX.append(random.randint(1, 750))
    posOvniY.append(random.randint(0, 300))
    ovniSpeed.append(3)


# Fonction de detection de collision
def collision(rectA, rectB):
    if rectB.right < rectA.left:
        # rectB est à gauche
        return False
    if rectB.bottom < rectA.top:
        # rectB est au dessus
        return False
    if rectB.left > rectA.right:
        # rectB est à droite
        return False
    if rectB.top > rectA.bottom:
        # rectB est en dessous
        return False
    # Dans tous les autres cas il y a collision
    return True

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
    laserRect.topleft = (posLaserX, posLaserY)
    window.blit(laser, laserRect)
    if posLaserY < -40:
        canShoot = True

    # Gestion des OVNI
    for i in range(nbOvni):
        posOvniX[i] -= ovniSpeed[i]
        ovniRect[i].topleft = (posOvniX[i], posOvniY[i])
        window.blit(ovni[i], ovniRect[i])
        if posOvniX[i] < 0 or posOvniX[i] > 710:
            ovniSpeed[i] = -ovniSpeed[i]
            posOvniY[i] += 50

        # Detection de collision entre le laser et l'OVNI
        if collision(laserRect, ovniRect[i]):
            posOvniY[i] = 10000
            posLaserY = -500
            score += 1

        # Detection de collision entre le joueur et l'OVNI
        if collision(playerRect, ovniRect[i]):
            posX = -500

    # Affichage du score
    scoreTxt = font.render("Score : " + str(score), True, (255, 255, 255))
    window.blit(scoreTxt, (txtPos, txtPos))

    # On dessine / mettre à jour le contenu de l'écran
    pygame.display.flip()
    clock.tick(60)

# On quitte pygame
pygame.quit()