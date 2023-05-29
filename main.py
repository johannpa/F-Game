# Importation de pygame
import pygame

# Initialisation de pygame
pygame.init()

# Création de la fenêtre pour afficher le jeu
window = pygame.display.set_mode((800, 600))


# La boucle de jeu
running = True
while running:
    # On check tous les événements (clavier ou souris)
    for event in pygame.event.get():
        # On teste si l'utilisateur click sur la croix de la fenêtre
        if event.type == pygame.QUIT:
            # Si c'est le cas on met la variable running à False
            running = False


# On quitte pygame
pygame.quit()