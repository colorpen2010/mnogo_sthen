import pygame,model
screen=pygame.display.set_mode([1000,1000])
pygame.init()
def viewer():
    screen.fill([0,0,0])
    f = pygame.font.SysFont('arial', model.rasmer, True, True)

    d = f.render(str(6), True, [255, 255, 255])
    screen.blit(d, [500, 500])

    pygame.display.flip()
