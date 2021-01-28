import pygame
# par la même occasion cela importe pygame.locals dans l'espace de nom de Pygame

pygame.init()

ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

continuer = True
page = 0
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    
    
    tableauBG = ['D:/Desktop/BOB/.dist/BomboneEntree.png', 'D:/Desktop/BOB/.dist/test-design-bobone-de-cri-inserer-cubeai.png', 'D:/.Photo/3431885-hollow-knight-review-thumb-nologo.jpg']
    image_fond = pygame.image.load(tableauBG[page])
    fond = image_fond.convert()
    ecran.blit(fond,(0,0))
    pygame.display.flip()
    #bouton
    Text_2_pos = (700, 510)
    font = pygame.font.Font(None, 70)
    Text_2 = font.render("OPTION",1,(10,10,10))
    ecran.blit (Text_2, Text_2_pos)

pygame.quit()