import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 20,"Hello World!", curses.A_BLINK)
    stdscr.addstr(15, 50,"Barbaross Lives")
    stdscr.addstr(20, 80,"Breakout")
    
    
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
