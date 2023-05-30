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


# La boucle de jeu
running = True
while running:
    # Couleur de l'écran
    window.fill((0, 0, 0))
    # On check tous les événements (clavier ou souris)
    for event in pygame.event.get():
        # On teste si l'utilisateur click sur la croix de la fenêtre
        if event.type == pygame.QUIT:
            # Si c'est le cas on met la variable running à False
            running = False
    # On dessine / mettre à jour le contenu de l'écran
    pygame.display.flip()

# On quitte pygame
pygame.quit()