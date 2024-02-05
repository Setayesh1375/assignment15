import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 2
        self.score = 0
        self.body = []
        self.color2 = arcade.color.DARK_BLUE

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color
        )

        for count, part in enumerate(self.body):
            if count % 2 == 0:
                arcade.draw_rectangle_filled(
                    part["x"], part["y"], self.width, self.height, self.color2
                )
            else:
                arcade.draw_rectangle_filled(
                    part["x"], part["y"], self.width, self.height, self.color
                )

    def move(self):
        self.body.append({"x": self.center_x, "y": self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)

        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self, food):
        self.score += food.plus
        del food