import pygame
import sys   
from systems.player_system import move_manager 

pygame.init()

##### Définir le paramètres de notre fenetre ---------------------

pygame.display.set_caption("Ajout background et sprites")

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)

##### Paramètre du niveau ------------------------------------

background = pygame.image.load('assets/level_11.jpg')

background_width = 6400
background_height = 1800

# Position initiale de la caméra 
camera_x = 0
camera_y = background_height - screen_height  # Placer la caméra en bas de l'image

##### Paramètre de notre personnage -----------------------------

player_width = 24
player_height = 16
player_x = (screen_width - player_width) // 2  
player_y = (screen_height - player_height) // 2

player_sprite_sheet = pygame.image.load('assets/mario_spritesheet_1.png')

# Découper les frames de la sprite sheet
frames = []
for i in range(6):  # Il y a 6 frames
    frame = player_sprite_sheet.subsurface(pygame.Rect(i * player_width, 0, player_width, player_height))
    frames.append(frame)

player_speed = 5 

# Index de la frame actuelle
current_frame = 0


##### Paramètres du jeux ----------------------------------------

clock = pygame.time.Clock()  


##### Boucle principale ------------------------------------------

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #### Obtenir les touches pressées ----------------------------
    keys = pygame.key.get_pressed()

    #### Déplacer le personnage à gauche et à droite--------------

    player_x,_,_ = move_manager(keys, player_x, player_speed, player_width, screen_width)
    

    ##### Rendering ----------------------------------------------

    screen.fill(WHITE) 

    screen.blit(background, (-camera_x, -camera_y))

    # Dessiner le personnage avec la sprite sheet
    screen.blit(frames[current_frame], (player_x, player_y))


    pygame.display.flip()

    clock.tick(60)   
        
pygame.quit()
sys.exit()