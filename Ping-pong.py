from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = player_image
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__(player_image,x,y,speed)
        
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.player_speed
        if keys[K_s] and self.rect.y < 375:
            self.rect.y += self.player_speed
        self.reset()

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.player_speed
        if keys[K_DOWN] and self.rect.y < 375:
            self.rect.y += self.player_speed        
        self.reset()

player_image = transform.scale(image.load('rocket.png'),(30,120))
player_left = Player(player_image, 20, 300, 4)
player_right = Player(player_image, 660, 300, 4)


FPS = 60
clock = time.Clock()

window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.png'),(700,500))

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))

    player_left.update_l()
    player_right.update_r()


    clock.tick(FPS)
    display.update()













