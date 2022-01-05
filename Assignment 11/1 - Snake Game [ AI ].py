import random
import time
import math
import arcade

SCREEN_WIDTH = 680
SCREEN_HEIGHT = 600
OBJECT_DIAMETER = 20

class Object(arcade.Sprite):
    def __init__(self, w, h):
        self.center_x = random.randint(OBJECT_DIAMETER, w - OBJECT_DIAMETER)
        self.center_y = random.randint(OBJECT_DIAMETER, h - OBJECT_DIAMETER)
        self.width = OBJECT_DIAMETER
        self.height = OBJECT_DIAMETER


class Apple(Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.color = arcade.color.RED
        self.img = arcade.Sprite('images/apple.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()


class Pear(Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.img = arcade.Sprite('images/pear.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()


class Poop(Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.img = arcade.Sprite('images/poop.png')
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()


class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.BLEU_DE_FRANCE
        #self.color1 = arcade.color.RED
        #self.color2 = arcade.color.BLACK_OLIVE
        self.speed = 16
        self.center_x = w // 2
        self.center_y = h // 2
        self.width = 16
        self.height = 16
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.body = []
        self.flag = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y,self.width, self.height, self.color)

        for item in self.body:
            arcade.draw_rectangle_filled(item[0],item[1],self.width, self.height,self.color)
        """
        for i in range(len(self.body)):
            if i % 2 == 0:
                arcade.draw_rectangle_filled(self.body[i][0],self.body[i][1],self.width, self.height,self.color2)
            else:
                arcade.draw_rectangle_filled(self.body[i][0],self.body[i][1],self.width, self.height,self.color1)
        """
    def eat(self, item):
        if item == 'apple':
            self.score += 1
            self.body.append([self.center_x, self.center_y])

        if item == 'pear':
            self.score += 2
            self.body.append([self.center_x, self.center_y])

        if item == 'poop':
            self.score -= 1
            if len(self.body)>0:
                self.body.pop()

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
        
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y

        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y

class Game(arcade.Window):
    def __init__(self, width, height):
        arcade.Window.__init__(self, width, height, 'Snake Game')
        self.background = arcade.load_texture('images/Background.png')
        #arcade.set_background_color(arcade.color.GREEN_YELLOW)
        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.pear = Pear(width, height)
        self.poop = Poop(width, height)
        self.flag = 0
        self.exit = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH,SCREEN_HEIGHT, self.background)
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.poop.draw()

        output = f"SCORE : {self.snake.score}"
        arcade.draw_text(output, 10, 20, arcade.color.RED, 20)

        if self.snake.score != 0:
            self.flag = 1

        if self.flag == 1:
            if self.snake.score <= 0:
                arcade.draw_text("Game Over", -90+SCREEN_WIDTH//2, SCREEN_HEIGHT//2, arcade.color.RED, 30)
                self.exit = 1

        if (SCREEN_WIDTH <= self.snake.center_x + self.snake.width//2) or (0 >= self.snake.center_x - self.snake.width//2) or (SCREEN_HEIGHT <= self.snake.center_y + self.snake.height//2) or (0 >= self.snake.center_y - self.snake.height//2):
            arcade.draw_text("Game Over", -90+SCREEN_WIDTH//2, SCREEN_HEIGHT//2, arcade.color.RED, 30)
            self.exit = 1
        

    def on_update(self, delta_time: float):
        
        target_x = 0
        target_y = 0
        distance_apple = math.sqrt((self.snake.center_x - self.apple.center_x)**2 + (self.snake.center_y - self.apple.center_y)**2)
        distance_pear = math.sqrt((self.snake.center_x - self.pear.center_x)**2 + (self.snake.center_y - self.pear.center_y)**2)
        
        if distance_apple < distance_pear:
            target_x = self.apple.center_x
            target_y = self.apple.center_y
        else :
            target_x = self.pear.center_x
            target_y = self.pear.center_y

        collision_range = (self.snake.width//2) + (OBJECT_DIAMETER//2) - 1

        if self.snake.center_x < target_x - collision_range: # right
            self.snake.change_x = 1
            self.snake.change_y = 0
        
        elif self.snake.center_x > target_x + collision_range: # left
            self.snake.change_x = -1
            self.snake.change_y = 0
        
        elif self.snake.center_y < target_y - collision_range: # up
            self.snake.change_x = 0
            self.snake.change_y = 1
        
        elif self.snake.center_y > target_y + collision_range: # down
            self.snake.change_x = 0
            self.snake.change_y = -1

        self.snake.move()

        if self.exit==1:
            #time.sleep(4)
            time1 = int(round(time.time() * 1000))
            while True:
                diff_time_ms = int(round(time.time() * 1000)) - time1
                if(diff_time_ms >= 4000):
                    break

            arcade.exit()
        
        if arcade.check_for_collision(self.snake,self.apple):
            item = 'apple'
            self.snake.eat(item)
            self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)

        if arcade.check_for_collision(self.snake,self.pear):
            item = 'pear'
            self.snake.eat(item)
            self.pear = Pear(SCREEN_HEIGHT, SCREEN_HEIGHT)

        if arcade.check_for_collision(self.snake,self.poop):
            item = 'poop'
            self.snake.eat(item)
            self.poop = Poop(SCREEN_HEIGHT, SCREEN_HEIGHT)
          
            

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()