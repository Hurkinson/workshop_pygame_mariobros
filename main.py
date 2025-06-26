import pygame
import sys 
from systems.player_system import move_manager 

pygame.init()

##### Définir le paramètres de notre fenetre ---------------------

pygame.display.set_caption("New player")

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)

##### Paramètre de notre personnage -----------------------------

# Taille et position initiale du personnage
player_width = 24
player_height = 16
player_x = (screen_width - player_width) // 2  # Centré horizontalement
player_y = (screen_height - player_height) // 2  # Centré verticalement

player_speed = 5 # Vitesse de déplacement du personnage

##### Paramètres du jeux ----------------------------------------

clock = pygame.time.Clock()  # Définir la vitesse de rafraîchissement  # <------


##### Boucle principale ------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #### Obtenir les touches pressées ----------------------------
    keys = pygame.key.get_pressed()

    #### Déplacer le personnage à gauche et à droite--------------
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Empêcher le personnage de sortir de l'écran
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width

    player_x,_,_ = move_manager(keys, player_x, player_speed, player_width, screen_width)
    

    ##### Rendering ----------------------------------------------

    screen.fill(WHITE)  # a inverser pour le LC
    
    # Dessiner le personnage
    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

    clock.tick(60)      # Limiter à 60 images par seconde   # <-----
    

    
    pygame.display.flip()

    
pygame.quit()
sys.exit()