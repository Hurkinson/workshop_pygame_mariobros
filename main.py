import pygame
import sys   

pygame.init()

##### Définir le paramètres de notre fenetre ------------------

pygame.display.set_caption("Affichage d'un écran blanc")

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)

##### Boucle principale ------------------------------------------

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    ##### Rendering ----------------------------------------------

    pygame.display.flip()

    
pygame.quit()
sys.exit()