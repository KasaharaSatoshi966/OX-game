from oxgame.board import Board
from oxgame.game_view import GameView


class GameController:
    def __init__(self):
        self.board = Board()
        self.view = GameView()

    def start_game(self):
        while True:
            self.view.display(self.board)
            xy = self.if_key()
            if xy != [-1,-1]:
                self.board.put_piece(xy[0],xy[1])
            self.view.display(self.board)
            if self.board.check_game_over():
                print(f"\n\nWinner is {self.board.another_piece()}")
                print("restart: space  quit: p")
                break
            elif self.board.check_game_end():
                print("restart: space  quit: p")
                break
            else:
                if xy != [-1,-1]:
                    self.board.remove()

    def if_key(self):
        key = self.view.get_key()
        if key=="q":
            return [0,0]
        elif key=="a":
            return [1,0]
        elif key=="z":
            return [2,0]
        elif key=="w":
            return [0,1]
        elif key=="s":
            return [1,1]
        elif key=="x":
            return [2,1]
        elif key=="e":
            return [0,2]
        elif key=="d":
            return [1,2]
        elif key=="c":
            return [2,2]
        else:
            return [-1,-1]
    def will_quit(self):
        while True:
            key = self.view.get_key()
            if key == 'p':
                self.view.finish_curses()
                return True
            elif key == ' ':
                self.board = Board()
                return False
