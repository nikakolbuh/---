From pygame import 

class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      super.__init__()

      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y

  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
      
font1 = font.Font(None, 35)
lose1 = font1.render(
    'PLAYER 1 LOSE!', True, (180, 0, 0))
if ball.rect.x < 0:
       finish = True
       window.blit(lose1, (200, 200))

font2 = font.Font(None, 35)
lose2 = font2.render(
    'PLAYER 2 LOSE!', True, (180, 0, 0))
if ball.rect.x < 0:
       finish = True
       window.blit(lose2, (200, 200))
      
speed_x = 3
speed_y = 3

while game:
   if finish != True:
       ball.rect.x += speed_x
       ball.rect.y += speed_y

   if ball.rect.y > win_height-50 
      or ball.rect.y < 0:
           speed_y *= -1
    
   if sprite.collide_rect(racket1, ball) 
     or sprite.collide_rect(racket2, ball):
           speed_x *= -1
   

Back = (200, 255, 255)
Win_width = 600
Win_height = 500
Window = display.set_mode((win_width, win_height))
Window.fill(back)

ball = GameSprite = ('tenis_ball.png', 200, 200, 4, 50, 50)

Clock = time.clock()
FPS = 60
Game = true

While game:
    For e in event.get():
        If e.type == QUIT:
            Game = false
            
    ball.reset()

    display.update()
    clock.tick(FPS)
