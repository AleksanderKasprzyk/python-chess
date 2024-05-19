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
        self.whitetomove = True
        self.movelog = []