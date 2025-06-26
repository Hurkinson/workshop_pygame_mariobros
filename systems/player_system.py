
import pygame

def move_manager(keys, 
                 player_x,
                 player_speed, 
                 player_width, 
                 screen_width, 
                 facing_right=False, 
                 current_frame=0
                 ):
    
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        facing_right = False  # Le personnage fait face à gauche
        current_frame = (current_frame + 1) % 6 # len(frames)
        
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        facing_right = True  # Le personnage fait face à droite
        current_frame = (current_frame + 1) % 6 # len(frames)
 
    # Empêcher le personnage de sortir de l'écran
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width

    return player_x, facing_right, current_frame
