from pygame import *
#music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Maze')
#задай фон сцены
background = transform.scale(image.load('background.jpg'),(700, 500))

clock = time.Clock()
FPS = 60
class GameSprite():
    def __init__ (self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        #self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT] and self.rect.x < 450:
            self.rect.x += 10
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += 10

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 450:
           self.direction = 'right'
        if self.direction == 'right':
            self.rect.x += 3

        if self.rect.x >= 550:
           self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= 3

class Wall(sprite.Sprite):
    def __init__ (self,color_1, color_2, color_3, wall_x, wall_y, wall_width,wall_height):
        super(). __init__()
        self.color1 = color_1
        self.color2 = color_2
        self.color3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
game = True
finish = False
hero = Player('hero.png', 50, 200)
cyborg = Enemy('cyborg.png', 200, 200)
money = GameSprite('treasure.png', 400, 100)
font.init()
font = font.Font(None, 70)
w1 = Wall(255,0,0,10,100,10,200)
w2 = Wall(255,0,0,20,400,10,200)
w3 = Wall(255,0,0,200,100,10,200)

while game:
    

#обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background,(0,0)) 
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()  
    hero.reset()
    cyborg.reset()
    money.reset() 
    if finish != True:
        hero.update()
        cyborg.update()
        if sprite.collide_rect(hero, money):
            kick = mixer.Sound('money.ogg')
            kick.play()
            win = font.render(
                'YOU WIN', True, (255,215,0)
            )
            window.blit(win,(200, 200))
            finish = True
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3):
            kick = mixer.Sound('kick.ogg')
            kick.play()
            lose = font.render(
                'YOU LOSE', True, (255,215,0)
            )
            window.blit(lose,(200, 200))
            finish = True

    
    display.update()
    clock.tick(FPS)

#управление спрайтом с помощью клавиш





