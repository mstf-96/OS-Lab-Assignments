import random
import time
import math
import threading
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.3
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 50

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 660
SCREEN_TITLE = "Space War"
BULLET_SPEED = 5
PARTICLE_GRAVITY = 0.05
PARTICLE_FADE_RATE = 8
PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5
PARTICLE_COUNT = 20
PARTICLE_RADIUS = 3
PARTICLE_COLORS = [arcade.color.ALIZARIN_CRIMSON,
                   arcade.color.COQUELICOT,
                   arcade.color.LAVA,
                   arcade.color.KU_CRIMSON,
                   arcade.color.DARK_TANGERINE]
PARTICLE_SPARKLE_CHANCE = 0.02
SMOKE_START_SCALE = 0.25
SMOKE_EXPANSION_RATE = 0.03
SMOKE_FADE_RATE = 7
SMOKE_RISE_RATE = 0.5
SMOKE_CHANCE = 0.25


class SpaceShip(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.set_mouse_visible(False)
  
      
       
        self.img = "images/heart.png"

        self.hp = arcade.SpriteList() 
        self.hp.append(arcade.Sprite(self.img, 0.01 , center_x=40 , center_y=50))
        self.hp.append(arcade.Sprite(self.img, 0.01 , center_x=90 , center_y=50))
        self.hp.append(arcade.Sprite(self.img, 0.01 , center_x=140 , center_y=50))
        self.game_over = arcade.sound.load_sound("game_over.mp3")
        self.ship=Ship();
        self.score=0
        self.explosions_list=arcade.SpriteList() 
        self.enemy_list=[]

        self.flag_thread=False
        self.enemy_thread=threading.Thread(target=self.add_enemy,args=(lambda:self.flag_thread,)) 
        self.enemy_thread.start() 

        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture("images/background.jpg")
    
    def add_enemy(self,stop):
        while True:
            self.enemy_list.append(Enemy())
            self.random = random.randint(2 ,7)
            
            if stop():
                break
            time.sleep(self.random)

    def on_draw(self):
        arcade.start_render()

        if(not(len(self.hp))):
            arcade.draw_text('GAME OVER',SCREEN_WIDTH//2-90,SCREEN_HEIGHT//2,arcade.color.RED,width=20,
            bold=True,font_size=25)
            self.flag_thread=True
            arcade.play_sound(self.game_over,1.0,0.0,False)
            arcade.exit()            
            
        else:
            arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background_image)
            arcade.draw_text(f"SCORE : {self.score}",SCREEN_WIDTH-110 , 30, arcade.color.RED,bold=True)
         
            self.hp.draw()
            self.ship.draw()
            self.ship.bullet_list.draw()
            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()
            self.explosions_list.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ship.fire() 

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.ship.fire() 

        elif symbol == arcade.key.A:
            self.ship.change_angle = 5
            self.ship.rotate()  

        elif symbol == arcade.key.D:
            self.ship.change_angle = -5    
            self.ship.rotate()

    def on_update(self, delta_time):

        self.ship.bullet_list.update()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].update()
        self.end_time = time.time()
        self.explosions_list.update()
        
        for enemy in self.enemy_list:
            if(arcade.check_for_collision(self.ship,enemy)):
                for i in range(PARTICLE_COUNT):
                    particle = Particle(self.explosions_list)
                    particle.position = enemy.position
                    self.explosions_list.append(particle)

                smoke = Smoke(50)
                smoke.position = enemy.position
                self.explosions_list.append(smoke)

                enemy.hit()
                self.enemy_list.remove(enemy)
                hp=self.hp.pop()
                hp.remove_from_sprite_lists()
            if enemy.top < 0:
                self.enemy_list.remove(enemy)
                hp=self.hp.pop()
                hp.remove_from_sprite_lists()


        for bullet in self.ship.bullet_list:

            hit_list = []
            for enemy in self.enemy_list:
                if(arcade.check_for_collision(bullet,enemy)):
                    hit_list.append(enemy)

          
            if len(hit_list) > 0:

                bullet.remove_from_sprite_lists()

            for enemy in hit_list:
                for i in range(PARTICLE_COUNT):
                    particle = Particle(self.explosions_list)
                    particle.position = enemy.position
                    self.explosions_list.append(particle)

                smoke = Smoke(50)
                smoke.position = enemy.position
                self.explosions_list.append(smoke)

                self.enemy_list.remove(enemy)
                self.score += 1

                arcade.sound.play_sound(enemy.hit())

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()



class Bullet(arcade.Sprite):
    
    def __init__(self, shooter): 
        super().__init__(':resources:images/space_shooter/laserRed01.png',0.8)
        arcade.sound.play_sound(shooter.gun_sound)
        self.center_x = shooter.center_x
        self.center_y = shooter.center_y
        self.speed = 8
        self.angle = shooter.angle

    def update(self):
        angle_radious = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_radious)
        self.center_y += self.speed * math.cos(angle_radious)

class Ship(arcade.Sprite):
    def __init__(self):
    
        super().__init__(':resources:images/space_shooter/playerShip3_orange.png'
        ,0.5)
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        
        self.bullet_list =arcade.SpriteList()
       
        self.width = 50
        self.height = 50
        
        self.center_x = SCREEN_WIDTH//2
        self.center_y = 60

        self.speed = 2
        self.angle = 0
        self.change_angle = 0

    def rotate(self):
        self.angle += self.change_angle * self.speed

    def fire(self):
        self.bullet_list.append(Bullet(self))  

    def draw(self):
        return super().draw()

class Enemy(arcade.Sprite):
    
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png',0.3)
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")

        self.speed = 2.5
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = SCREEN_HEIGHT+10  
        self.angle = 180
        self.width = 50
        self.height = 50

    def hit(self):
        arcade.play_sound(self.hit_sound, 1.0, 0.0,False)

    def update(self):
        self.center_y -= self.speed  

class Smoke(arcade.SpriteCircle):
    def __init__(self, size):
        super().__init__(size, arcade.color.LIGHT_GRAY, soft=True)
        self.change_y = SMOKE_RISE_RATE
        self.scale = SMOKE_START_SCALE

    def update(self):
        if self.alpha <= PARTICLE_FADE_RATE:
            self.remove_from_sprite_lists()
        else:
            self.alpha -= SMOKE_FADE_RATE
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.scale += SMOKE_EXPANSION_RATE


class Particle(arcade.SpriteCircle):
    def __init__(self, my_list):
        color = random.choice(PARTICLE_COLORS)

        super().__init__(PARTICLE_RADIUS, color)

        self.normal_texture = self.texture

        self.my_list = my_list
        speed = random.random() * PARTICLE_SPEED_RANGE + PARTICLE_MIN_SPEED
        direction = random.randrange(360)
        self.change_x = math.sin(math.radians(direction)) * speed
        self.change_y = math.cos(math.radians(direction)) * speed

        self.my_alpha = 255

        self.my_list = my_list

    def update(self):
        if self.my_alpha <= PARTICLE_FADE_RATE:
            self.remove_from_sprite_lists()
        else:
            self.my_alpha -= PARTICLE_FADE_RATE
            self.alpha = self.my_alpha
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.change_y -= PARTICLE_GRAVITY

            if random.random() <= PARTICLE_SPARKLE_CHANCE:
                self.alpha = 255
                self.texture = arcade.make_circle_texture(int(self.width),
                                                          arcade.color.WHITE)
            else:
                self.texture = self.normal_texture

            if random.random() <= SMOKE_CHANCE:
                smoke = Smoke(5)
                smoke.position = self.position
                self.my_list.append(smoke)


window = SpaceShip()
window.center_window()
arcade.run()
