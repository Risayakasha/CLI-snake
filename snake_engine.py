import random as r

# class Grid:
#   def __init__(self, width: int, height: int) -> None:
#      self.width = width
#     self.height = height
#        self.plane = [[0 for r in range(width)] for c in range(height)]
#
#   def updateScr(self, snakeX, snakeY):
#
#        self.plane[snakeY][snakeX] = 8
#       for i in range(self.height):
#          print(self.plane[i])
#     print("")


class SnakeSegment:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        self.d = 0  # up, right, down, left

    def move(self, d):
        delta = self.dir[d]

        self.previous_coords = [self.x, self.y]

        self.x += delta[0]
        self.y -= delta[1]

    def turn(self, key):
        self.previous_dir = self.d
        # if loop for input

        if key == 0:
            self.d += 1
        else:
            self.d -= 1
        self.d %= 4

    def grow(self):
        x, y = self.previous_coords[0], self.previous_coords[1]

        segment = SnakeSegment(x, y)
        return segment


class Food:
    def __init__(self, max_x, max_y) -> None:
        self.max_x = max_x
        self.max_y = max_y

    def spawnfood(self):
        self.x = r.randint(0, self.max_x)
        self.y = r.randint(0, self.max_y)
