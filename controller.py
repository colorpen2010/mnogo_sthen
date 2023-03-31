import pygame,model
def control():
    sobitie=pygame.event.get()
    for k in sobitie:
        if k.type==pygame.QUIT:
            exit()
        if k.type == pygame.MOUSEBUTTONDOWN:
            model.rasmer+=5
        if k.type==pygame.KEYDOWN and k.key==pygame.K_ESCAPE:
            model.scena='igra2'