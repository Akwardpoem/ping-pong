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
    def update(self):
        global bullet_image, bullets, fire_sound
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.player_speed
        if keys[K_RIGHT]:
            self.rect.x += self.player_speed        
        self.reset()

FPS = 60
clock = time.Clock()

window = display.set_mode((700,500))
display.set_caption('Пинг-понг')

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            run = False

    clock.tick(FPS)
    display.update()







