import pygame
import sys
from systems.player_system import move_manager
from systems.camera_system import camera_manager
from systems.render_system import render_manager
from systems.audio_system import initialize_audio

pygame.init()

##### Définir le paramètres de notre fenetre ---------------------
pygame.display.set_caption("Workshop video_game")

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
WHITE = (255, 255, 255)

##### Paramètre du niveau ------------------------------------

background = pygame.image.load('assets/level_11.jpg')
background_width = 6400
background_height = 1800

camera_x = 0
camera_y = background_height - screen_height 

##### Paramètre de notre personnage -----------------------------

player_width = 24
player_height = 16
player_x = screen_width // 2 - player_width // 2  # Centré horizontalement
player_y = (background_height - 100) - player_height   # Positionné au sol (bas du fond)

facing_right = False  

player_speed = 5
jump_power = -17
player_velocity_x = 0
player_velocity_y = 0

player_state = "land"  # "land" = au sol, "air" = en l'air

player_sprite_sheet = pygame.image.load('assets/mario_spritesheet_1.png')

frames = []
for i in range(6):  # Il y a 6 frames
    frame = player_sprite_sheet.subsurface(pygame.Rect(i * player_width, 0, player_width, player_height))
    frames.append(frame)

# Index de la frame actuelle
current_frame = 0  # Initialisation de l'index des frames pour éviter une erreur

##### Paramètres du jeu ----------------------------------------

sfx_bank = initialize_audio()
clock = pygame.time.Clock()
gravity = 1 

#### Boucle principale du jeu -------------------

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #### inputs -------------------------------------

    keys = pygame.key.get_pressed()

    #### déplacement du personnage ------------------

    player_x, player_y, player_velocity_y, facing_right, current_frame, player_state = move_manager( 
        keys, 
        player_x,
        player_y, 
        player_speed, 
        player_width,
        player_height,
        jump_power,
        gravity,  
        background_width,    #   <---
        background_height,
        facing_right,
        sfx_bank, 
        current_frame,
        player_velocity_x,
        player_velocity_y,
        player_state, 
    )

    #### Camera ------------------------------------------

    camera_x, camera_y, adjusted_player_x, adjusted_player_y = camera_manager(
        player_x, 
        player_y, 
        screen_width, 
        screen_height, 
        background_width, 
        background_height
    )

    #### Render ------------------------------------------

    render_manager(background, screen, facing_right, camera_x, camera_y, frames, current_frame, adjusted_player_x, adjusted_player_y)

    clock.tick(60)


pygame.quit()
sys.exit()