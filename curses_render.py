from time import sleep
import curses
from curses import wrapper
from snake_engine import SnakeSegment, Food

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


def main(stdscr):
    food = Food(width, height)
    head = SnakeSegment(centerx, centery)
    body = [head]

    food_count = 0
    game = True

    food.spawnfood()
    food_count += 1

    while game is True:
        key = stdscr.getch()
        stdscr.clear()

        stdscr.addstr(food.y, food.x, "󰉛")

        if head.x == 0 or head.x == width or head.y == 0 or head.y == height:
            stdscr.clear()
            stdscr.addstr(centery, centerx - 4, "GAME OVER")
            stdscr.nodelay(False)
            game = False
            stdscr.getkey()

        if key == 260:
            head.turn(1)
        if key == 261:
            head.turn(0)

        if head.x == food.x and head.y == food.y:
            body.append(body[-1].grow())
            food_count = 0
            food.spawnfood()
            food_count += 1
        stdscr.addstr(head.y, head.x, "")

        n = 0
        for n in range(len(body)):
            # stdscr.addstr(0, 0, str(n))
            if n == 0:
                continue
            else:
                stdscr.addstr(body[n].y, body[n].x, "")
                body[n].move(body[n - 1].d)
        head.move(head.d)

        stdscr.refresh()
        sleep(0.1)


if __name__ == "__main__":
    wrapper(main)


curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
