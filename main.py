import pygame

pygame.init()


SCREEN_WIDTH =800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Schrooter")




#defining the player actions
moving_left = False
moving_right = False





class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/player/Idle/0.png')
        self.img = pygame.transform.scale(
            img, (int(img.get_width()*scale), (int(img.get_height()*scale))))
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.img, self.rect)
player = Soldier(200, 200, 3)

run = True
while run:

    player.draw()    
    for event in pygame.event.get():
        #quit event 
        if event.type == pygame.QUIT:
            run = False

        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True

            if event.key == pygame.K_d:
                moving_right = True

        #keyboard released
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True

            if event.key == pygame.K_d:
                moving_right = True
    pygame.display.update()

pygame.quit            

