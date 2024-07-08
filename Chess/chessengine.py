class gamestate():
    def __init__(self):
        self.board = \
        [["blackrook", "blackknight", "blackbishop", "blackqueen", "blackking", "blackbishop", "blackknight", "blackrook"],
        ["blackpawn", "blackpawn", "blackpawn", "blackpawn", "blackpawn", "blackpawn", "blackpawn", "blackpawn"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["whitepawn", "whitepawn", "whitepawn", "whitepawn", "whitepawn", "whitepawn", "whitepawn", "whitepawn"],
        ["whiterook", "whiteknight", "whitebishop", "whitequeen", "whiteking", "whitebishop", "whiteknight", "whiterook"]]
        self.movefunctions = {"p": self.getpawnmoves, "R": self.getrookmoves, "N": self.getknightmoves, "B": self.getbishopmoves, "Q": self.getqueenmoves, "K": self.getkingmoves}
        self.whitetomove = True
        self.movelog = []

    def makemove(self, move):
        self.board[move.startrow][move.startcolumn] = "--"
        self.board[move.endrow][move.endcolumn] = move.piecemoved
        self.movelog.append(move)
        self.whitetomove = not self.whitetomove

    def undomove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startrow][move.startcolumn] = move.piecemoved
            self.board[move.endrow][move.endcolumn] = move.piececaptured
            self.whitetomove = not self.whitetomove

    def getvalidmoves(self):
        return self.getallpossiblemoves()

    def getallpossiblemoves(self):
        moves = [move((6, 4), (4, 4), self.board)]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.whitetomove) or (turn == "b" and not self.whitetomove):
                    piece = self.board[r][c][1]
                    self.movefunctions[piece](r, c, moves)
                    """if piece == "p":
                        self.getpawnmoves(r, c, moves)
                    elif piece == "r":
                        self.getrookmoves(r, c, moves)"""
        return moves

    def getpawnmoves(self, r, c, moves):
        if self.whitetomove:
            if self.board[r-1][c] == "--":
                moves.append(move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == "--":
                    moves.append(move((r, c), (r-2, c), self.board))
            if c-1 >= 0:
                if self.board[r-1][c-1][0] == "b":
                    moves.append(move((r, c), (r-1, c-1), self.board))
            if c+1 <= 7:
                if self.board[r-1][c+1][0] == "b":
                    moves.append(move((r, c),(r-1, c+1), self.board))
        else:
            if self.board[r+1][c] == "--":
                moves.append(move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == "--":
                    moves.append(move((r, c), (r+2, c), self.board))
            if c-1 >= 0:
                if self.board[r+1][c-1][0] == "w":
                    moves.append(move((r, c), (r+1, c-1), self.board))
            if c+1 <= 7:
                if self.board[r+1][c+1][0] == "w":
                    moves.append(move((r, c), (r+1, c+1), self.board))

    def getrookmoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        enemycolor = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 8):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":
                        moves.append(move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == enemycolor:
                        moves.append(move((r, c), (endrow, endcol), self.board))
                        break
                    else:
                        break
                else:
                    break

    def getknightmoves(self, r, c, moves):
        knightmoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        allycolor = "w" if self.whitetomove else "b"
        for m in knightmoves:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < 8 and 0 <= endcol < 8:
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != allycolor:
                    moves.append(move((r, c), (endrow, endcol), self.board))

    def getbishopmoves(self, r, c, moves):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        enemycolor = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 8):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":
                        moves.append(move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == enemycolor:
                        moves.append(move((r, c), (endrow, endcol), self.board))
                        break
                    else:
                        break
                else:
                    break

    def getqueenmoves(self, r, c, moves):
        pass
    def getkingmoves(self, r, c, moves):
        pass


class move():
    rankstorows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowstoranks = {v: k for k, v in rankstorows.items()}
    filestocolumns = {"a": 0, "b": 1, "c": 2, "d": 3,
                      "e": 4, "f": 5, "g": 6, "h": 7}
    columnstofile = {v: k for k, v in filestocolumns.items()}
    def __init__(self, startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcolumn = startsq[1]
        self.endrow = endsq[0]
        self.endcolumn = endsq[1]
        self.piecemoved = board[self.startrow][self.startcolumn]
        self.piececaptured = board[self.endrow][self.endcolumn]
        self.moveid = self.startrow * 1000 + self.startcolumn * 100 + self.endrow * 10 + self.endcolumn
        print(self.moveid)
    def __eq__(self, other):
        if isinstance(other, move):
            return self.moveid == other.moveid
        return False
    def chessnotation(self):
        return self.rankfile(self.startrow, self.startcolumn) + self.rankfile(self.endrow, self.endcolumn)
    def rankfile(self, r, c):
        return self.columnstofile[c] + self.rowstoranks[r]