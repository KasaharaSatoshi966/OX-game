import curses


class GameView():
    def __init__(self):
        self.init_curses()

    def init_curses(self):
        self.strscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.strscr.keypad(True)

    def get_key(self):
        return self.strscr.getkey()

    def display(self, board):
        scr = self.strscr
        scr.clear()
        board_state = board.get_board()
        for y in range(3):
            for x in range(3):
                scr.addstr(x, y, board_state[x][y]) 
        scr.refresh()

    def finish_curses(self):
        curses.nocbreak()
        self.strscr.keypad(False)
        curses.echo()
        curses.endwin()
