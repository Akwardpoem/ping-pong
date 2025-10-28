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

class Ball(GameSprite):

    def __init__(self, ball_image, x, y, speed):
        super().__init__(ball_image,x,y,speed)
        self.x_speed = speed
        self.y_speed = speed

    def update(self):
        if self.rect.y < 0 or self.rect.y > 450:
            self.y_speed = -self.y_speed
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.reset()

player_image = transform.scale(image.load('rocket.png'),(30,120))
player_left = Player(player_image, 20, 300, 4)
player_right = Player(player_image, 660, 300, 4)

ball_image = transform.scale(image.load('ball.png'),(50,50))
ball = Ball(ball_image, 350, 250, 3)

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

    if sprite.collide_rect(ball, player_left) or sprite.collide_rect(ball, player_right):
        ball.x_speed = -ball.x_speed

    player_left.update_l()
    player_right.update_r()
    ball.update()

    clock.tick(FPS)
    display.update()







