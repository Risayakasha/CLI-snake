from time import sleep
import curses
from curses import wrapper
from snake_engine import SnakeSegment, Food

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.notimeout(True)
stdscr.keypad(True)

curses.start_color()
curses.use_default_colors()
curses.curs_set(0)

message = stdscr.getch()


def main(stdscr):
    print(message)
    stdscr.refresh()

    stdscr.getkey()


if __name__ == "__main__":
    wrapper(main)


curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
