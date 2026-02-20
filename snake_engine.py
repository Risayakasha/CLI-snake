from collections import deque
import random as r


class SnakeSegment:

    def __init__(self, x: int, y: int, bounds: list):
        self.x = x
        self.y = y

        self.bounds = bounds

        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        self.d = 0  # up, right, down, left

        self.previous = []
        self.body = deque([])

    def move(self):
        delta = self.dir[self.d]
        self.previous = [self.x, self.y]

        self.x += delta[0]
        self.y -= delta[1]

        if len(self.body) > 0:
            self.body.pop()
            self.body.appendleft(self.previous)

    def turn(self, key: int):

        if key == 0:
            self.d += 1
        else:
            self.d -= 1
        self.d %= 4

    def grow(self, last_seg):
        if last_seg is not None:
            x, y = last_seg[0], last_seg[1]
        else:
            x, y = self.previous[0], self.previous[1]

        self.body.append([x, y])

    def colision(self):
        if self.x not in range(self.bounds[0], self.bounds[2]) or self.y not in range(
            self.bounds[1], self.bounds[3]
        ):
            return True
        if [self.x, self.y] in self.body:
            return True
        else:
            return False


class Food:
    def __init__(self, max_x, max_y) -> None:
        self.max_x = max_x
        self.max_y = max_y

    def spawnfood(self):
        self.x = r.randint(5, self.max_x - 5)
        self.y = r.randint(5, self.max_y - 5)
