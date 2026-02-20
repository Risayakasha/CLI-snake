from time import sleep
import curses
from curses import wrapper
from snake_engine import SnakeSegment, Food
from collections import deque

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.notimeout(True)
stdscr.keypad(True)
stdscr.nodelay(True)
curses.start_color()
curses.use_default_colors()
curses.curs_set(0)


height, width = stdscr.getmaxyx()
centery, centerx = height // 2, width // 2


def GameOver(s):
    s.clear()
    s.addstr(centery, centerx - 4, "GAY OVER")
    s.nodelay(False)
    s.getkey()


def main(stdscr):
    food = Food(width, height)
    snake = SnakeSegment(centerx, centery, [0, 0, width, height])

    game = True
    tail = None

    food.spawnfood()

    while game is True:
        head = [snake.x, snake.y]
        key = stdscr.getch()
        stdscr.erase()

        stdscr.addstr(food.y, food.x, "󰉛")

        stdscr.addstr(head[1], head[0], "")

        if len(snake.body) > 0:
            n = 0
            while n < len(snake.body):
                stdscr.addstr(snake.body[n][1], snake.body[n][0], "")
                n += 1

            tail = snake.body[-1]

        if snake.colision() is True:
            game = False
            GameOver(stdscr)

        stdscr.noutrefresh()

        snake.move()

        if head[0] == food.x and head[1] == food.y:
            snake.grow(tail)
            food.spawnfood()

        if key == 260:
            snake.turn(1)
        if key == 261:
            snake.turn(0)

        curses.doupdate()
        sleep(0.1)


if __name__ == "__main__":
    wrapper(main)


curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
