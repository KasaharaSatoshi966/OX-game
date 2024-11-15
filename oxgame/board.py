class Board():

    def __init__(self):
        self.board = [["."]*3 for _ in range(3)]
        self.turn = "O"
        self.X_list = []
        self.O_list = []

    def another_piece(self):
        return "O" if self.turn=="X" else "X"

    def put_piece(self, x, y):
        if self.board[x][y]==".":
            self.board[x][y] = self.turn
            self.turn = self.another_piece()
            if self.another_piece() == "X":
                self.X_list.append([x,y])
            elif self.another_piece() == "O":
                self.O_list.append([x,y])

    def remove(self):
        x_y = []
        if self.another_piece() == "X":
            if len(self.X_list) == 3:
                x_y = self.X_list.pop(0)
                self.board[x_y[0]][x_y[1]] = "."
        if self.another_piece() == "O":
            if len(self.O_list) == 3:
                x_y = self.O_list.pop(0)
                self.board[x_y[0]][x_y[1]] = "."

    def get_board(self):
        return self.board

    def check_game_over(self):
        win_board = [
            #斜め
            [[0,0],[1,1],[2,2]],
            [[2,0],[1,1],[0,2]],
            #横
            [[0,0],[0,1],[0,2]],
            [[1,0],[1,1],[1,2]],
            [[2,0],[2,1],[2,2]],
            #縦
            [[0,0],[1,0],[2,0]],
            [[0,1],[1,1],[2,1]],
            [[0,2],[1,2],[2,2]]]
        for i in win_board:
            if self.board[i[0][0]][i[0][1]]==self.board[i[1][0]][i[1][1]]==self.board[i[2][0]][i[2][1]]!=".":
                return True
        return False

    def check_game_end(self):
        bool_list = []
        for i in self.board:
            for j in i:
                bool_list.append(True if j=="." else False)
        return not any(bool_list)
