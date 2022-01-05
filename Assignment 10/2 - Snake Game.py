import random
import time
import arcade

SCREEN_WIDTH = 680
SCREEN_HEIGHT = 600

class Object(arcade.Sprite):
    def __init__(self, w, h):
        self.center_x = random.randint(20, w - 20)
        self.center_y = random.randint(20, h - 20)


class Apple(Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.color = arcade.color.RED
        self.width = 20
        self.height = 20
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
        self.width = 20
        self.height = 20
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()


class Poop(Object):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        Object.__init__(self, w, h)
        self.img = arcade.Sprite('images/poop.png')
        self.width = 20
        self.height = 20
        self.img.center_x = self.center_x
        self.img.center_y = self.center_y

    def draw(self):
        self.img.draw()


class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.BLUE
        self.speed = 3
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

        output = f"Score: {self.snake.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 20)

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

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1            
            

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()