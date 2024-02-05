import random
from typing import Optional
import arcade
from arcade import Texture

from fruit import Apple
from fruit import Pear
from fruit import Poop
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake ver1")
        arcade.set_background_color(arcade.color.KHAKI)

        self.food = Apple(self)
        self.poop = Poop(self)
        self.pear = Pear(self)
        self.snake = Snake(self)
        self.game_over = False
        self.state = 1

    def del_all(self):
        del self.food
        del self.pear
        del self.poop
        self.food = Apple(self)
        self.poop = Poop(self)
        self.pear = Pear(self)

    def on_draw(self):
        arcade.start_render()

        self.food.draw()
        self.pear.draw()
        self.poop.draw()
        self.snake.draw()

        arcade.draw_text(
            str("Score: " + str(self.snake.score)),
            self.width /15,
            15,
            arcade.color.BLACK,
            18,
        )

        if self.state == 0:
            arcade.draw_lrtb_rectangle_filled(
                0, self.width, self.height, 0, arcade.color.BLACK
            )
            arcade.draw_text(
                "GAME OVER!", self.width // 6, self.height // 2, arcade.color.WHITE, 40
            )

        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

    def on_update(self, delta_time: float):
        self.snake.move()

        for count, part in enumerate(self.snake.body):
            for i in range(count + 1, len(self.snake.body)):
                if part['x'] == self.snake.body[i]['x'] and part['y'] == self.snake.body[i]['y']:
                    self.state = 0        

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.score += 1
            self.del_all()
        elif arcade.check_for_collision(self.snake, self.pear):
            self.snake.score += 2
            self.del_all()
            
        elif arcade.check_for_collision(self.snake, self.poop):  
            self.snake.score -= 1
            self.del_all()
        
        if (
            self.snake.center_x < 0
            or self.snake.center_x > 500
            or self.snake.center_y < 0
            or self.snake.center_y > self.height
            or self.snake.score < 0
        ):
            self.state = 0


if __name__ == "__main__":
    game = Game()
    arcade.run()