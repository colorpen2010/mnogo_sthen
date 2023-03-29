import pygame,model
def control():
    sobitie=pygame.event.get()
    for k in sobitie:
        if k.type==pygame.QUIT:
            exit()
        if k.type == pygame.MOUSEBUTTONDOWN:
            model.rasmer+=5