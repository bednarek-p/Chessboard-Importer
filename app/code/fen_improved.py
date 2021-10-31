# pylint: skip-file
class FenImproved():

    def __init__(self, fen):
        self.fen = fen[:-10]
        self.rows = self.fen.split("/")

    def count_chess_pieces(self):
        self.rows = self.fen.split("/")
        self.number_black_king = self.fen.count('k')
        self.number_black_queen = self.fen.count('q')
        self.number_black_rook = self.fen.count('r')
        self.number_black_bishop = self.fen.count('b')
        self.number_black_knight = self.fen.count('n')
        self.number_black_pawn = self.fen.count('p')
        self.number_white_king = self.fen.count('K')
        self.number_white_queen = self.fen.count('Q')
        self.number_white_rook = self.fen.count('R')
        self.number_white_bishop = self.fen.count('B')
        self.number_white_knight = self.fen.count('N')
        self.number_white_pawn = self.fen.count('P')

    def fen_improve_king(self):

        self.count_chess_pieces()

        if self.number_black_king != 1:
            if self.number_black_king == 0:
                if self.number_black_rook > 2:

                    if self.rows[0].count('r') == 1:
                        new_fen = ""
                        index = self.rows[0].index('r')
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('r', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[0].count('r') == 2:
                        new_fen = ""
                        index = self.rows[0].index('r', 2)
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('r', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[0].count('r') == 3:
                        new_fen = ""
                        index = self.rows[0].index('r', 3)
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('r', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[1].count('r') == 1 and self.fen.count('k') == 0:
                        new_fen = ""
                        index = self.rows[1].index('r')
                        self.rows[1] = self.rows[1][:index] + self.rows[1][index:].replace('r', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[1].count('r') == 2 and self.fen.count('k') == 0:
                        new_fen = ""
                        index = self.rows[1].index('r', 2)
                        self.rows[1] = self.rows[1][:index] + self.rows[1][index:].replace('r', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[1].count('r') == 3 and self.fen.count('k') == 0:
                        new_fen = ""
                        index = self.rows[1].index('r', 3)
                        self.rows[1] = self.rows[1][:index] + self.rows[1][index:].replace('r', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                elif self.number_black_queen > 1:

                    if self.rows[0].count('q') == 1:
                        new_fen = ""
                        index = self.rows[0].index('q')
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('q', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[0].count('q') == 2:
                        new_fen = ""
                        index = self.rows[0].index('q', 4)
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('q', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[1].count('q') == 1 and self.fen.count('k') == 0:
                        new_fen = ""
                        index = self.rows[1].index('q')
                        self.rows[1] = self.rows[1][:index] + self.rows[1][index:].replace('q', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[1].count('q') == 2 and self.fen.count('k') == 0:
                        new_fen = ""
                        index = self.rows[1].index('q')
                        self.rows[1] = self.rows[1][:index] + self.rows[1][index:].replace('q', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                if self.number_black_bishop > 2:

                    if self.rows[0].count('b') == 1:
                        new_fen = ""
                        index = self.rows[0].index('b')
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('b', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[0].count('b') == 2:
                        new_fen = ""
                        index = self.rows[0].index('b', 2)
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('b', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[0].count('b') == 3:
                        new_fen = ""
                        index = self.rows[0].index('b', 3)
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('b', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[1].count('b') == 1 and self.fen.count('k') == 0:
                        new_fen = ""
                        index = self.rows[1].index('b')
                        self.rows[1] = self.rows[1][:index] + self.rows[1][index:].replace('b', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[1].count('b') == 2 and self.fen.count('k') == 0:
                        new_fen = ""
                        index = self.rows[1].index('b', 2)
                        self.rows[1] = self.rows[1][:index] + self.rows[1][index:].replace('b', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[1].count('b') == 3 and self.fen.count('k') == 0:
                        new_fen = ""
                        index = self.rows[1].index('b', 3)
                        self.rows[1] = self.rows[1][:index] + self.rows[1][index:].replace('r', 'k', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                elif self.number_black_rook == 2 and self.fen.count('k') == 0:
                    rook_index =  [i for i, piece in enumerate(self.fen) if piece == 'r'][1]
                    self.fen = self.fen[:rook_index] + self.fen[rook_index:].replace('r', 'k', 1)

                elif self.number_black_rook == 1 and self.fen.count('k') == 0:
                    rook_index = self.fen.index('r')
                    self.fen = self.fen[:rook_index] + self.fen[rook_index:].replace('r', 'k', 1)

                elif self.number_black_queen == 1 and self.fen.count('k') == 0:
                    queen_index = self.fen.index('q')
                    self.fen = self.fen[:queen_index] + self.fen[queen_index:].replace('q', 'k', 1)

                elif self.number_black_bishop == 2 and self.fen.count('k') == 0:
                    bishop_index =  [i for i, piece in enumerate(self.fen) if piece == 'b'][1]
                    self.fen = self.fen[:bishop_index] + self.fen[bishop_index:].replace('b', 'k', 1)

                elif self.number_black_bishop == 1 and self.fen.count('k') == 0:
                    bishop_index = self.fen.index('b')
                    self.fen = self.fen[:bishop_index] + self.fen[bishop_index:].replace('b', 'k', 1)

                elif self.number_white_rook == 2 and self.fen.count('k') == 0:
                    rook_index =  [i for i, piece in enumerate(self.fen) if piece == 'R'][1]
                    self.fen = self.fen[:rook_index] + self.fen[rook_index:].replace('R', 'k', 1)

                elif self.number_white_rook == 1 and  self.fen.count('k') == 0:
                    rook_index = self.fen.index('R')
                    self.fen = self.fen[:rook_index] + self.fen[rook_index:].replace('R', 'k', 1)

            if self.number_black_king == 2:
                if self.number_black_queen == 0:
                    if self.rows[0].count('k') == 2:
                        new_fen = ""
                        index = self.rows[0].index('k', 2)
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('k', 'q', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen
                    else:
                        king_index =  [i for i, piece in enumerate(self.fen) if piece == 'k'][1]
                        self.fen = self.fen[:king_index] + self.fen[king_index:].replace('k', 'q', 1)
                if self.number_black_bishop < 2 and self.fen.count('k') == 2:
                    if self.rows[0].count('k') == 2:
                        new_fen = ""
                        index = self.rows[0].index('k', 2)
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('k', 'b', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen
                    else:
                        king_index =  [i for i, piece in enumerate(self.fen) if piece == 'k'][1]
                        self.fen = self.fen[:king_index] + self.fen[king_index:].replace('k', 'b', 1)
                if self.number_black_rook < 2 and self.fen.count('k') == 2:
                    if self.rows[0].count('k') == 2:
                        new_fen = ""
                        index = self.rows[0].index('k', 2)
                        self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('k', 'r', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen
                    else:
                        king_index =  [i for i, piece in enumerate(self.fen) if piece == 'k'][1]
                        self.fen = self.fen[:king_index] + self.fen[king_index:].replace('k', 'r', 1)

        if self.number_white_king != 1:
            if self.number_white_king == 0:
                if self.number_white_rook > 2:

                    if self.rows[7].count('R') == 1:
                        new_fen = ""
                        index = self.rows[7].index('R')
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('R', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[7].count('R') == 2:
                        new_fen = ""
                        index = self.rows[7].index('R', 2)
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('R', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[7].count('R') == 3:
                        new_fen = ""
                        index = self.rows[7].index('R', 3)
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('R', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[6].count('R') == 1 and self.fen.count('K') == 0:
                        new_fen = ""
                        index = self.rows[6].index('R')
                        self.rows[6] = self.rows[6][:index] + self.rows[1][index:].replace('R', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[6].count('R') == 2 and self.fen.count('K') == 0:
                        new_fen = ""
                        index = self.rows[6].index('R', 2)
                        self.rows[6] = self.rows[6][:index] + self.rows[6][index:].replace('R', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[6].count('R') == 3 and self.fen.count('K') == 0:
                        new_fen = ""
                        index = self.rows[6].index('R', 3)
                        self.rows[6] = self.rows[6][:index] + self.rows[6][index:].replace('R', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                elif self.number_white_queen > 1:

                    if self.rows[7].count('Q') == 1:
                        new_fen = ""
                        index = self.rows[7].index('Q')
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('Q', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[7].count('Q') == 2:
                        new_fen = ""
                        index = self.rows[7].index('Q', 4)
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('Q', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[6].count('Q') == 1 and self.fen.count('K') == 0:
                        new_fen = ""
                        index = self.rows[6].index('Q')
                        self.rows[6] = self.rows[6][:index] + self.rows[6][index:].replace('Q', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[6].count('Q') == 2 and self.fen.count('K') == 0:
                        new_fen = ""
                        index = self.rows[6].index('Q')
                        self.rows[6] = self.rows[6][:index] + self.rows[6][index:].replace('Q', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                if self.number_white_bishop > 2:

                    if self.rows[7].count('B') == 1:
                        new_fen = ""
                        index = self.rows[7].index('B')
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('B', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[7].count('B') == 2:
                        new_fen = ""
                        index = self.rows[7].index('B', 2)
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('B', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[7].count('B') == 3:
                        new_fen = ""
                        index = self.rows[7].index('B', 3)
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('B', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[6].count('B') == 1 and self.fen.count('K') == 0:
                        new_fen = ""
                        index = self.rows[6].index('B')
                        self.rows[6] = self.rows[6][:index] + self.rows[6][index:].replace('B', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[6].count('B') == 2 and self.fen.count('K') == 0:
                        new_fen = ""
                        index = self.rows[6].index('B', 2)
                        self.rows[6] = self.rows[6][:index] + self.rows[6][index:].replace('B', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                    if self.rows[6].count('B') == 3 and self.fen.count('K') == 0:
                        new_fen = ""
                        index = self.rows[6].index('B', 3)
                        self.rows[6] = self.rows[6][:index] + self.rows[6][index:].replace('R', 'K', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen

                elif self.number_white_rook == 2 and self.fen.count('K') == 0:
                    rook_index =  [i for i, piece in enumerate(self.fen) if piece == 'R'][1]
                    self.fen = self.fen[:rook_index] + self.fen[rook_index:].replace('R', 'K', 1)

                elif self.number_white_rook == 1 and self.fen.count('K') == 0:
                    rook_index = self.fen.index('K')
                    self.fen = self.fen[:rook_index] + self.fen[rook_index:].replace('R', 'K', 1)

                elif self.number_white_queen == 1 and self.fen.count('K') == 0:
                    queen_index = self.fen.index('Q')
                    self.fen = self.fen[:queen_index] + self.fen[queen_index:].replace('Q', 'K', 1)

                elif self.number_white_bishop == 2 and self.fen.count('K') == 0:
                    bishop_index =  [i for i, piece in enumerate(self.fen) if piece == 'B'][1]
                    self.fen = self.fen[:bishop_index] + self.fen[bishop_index:].replace('B', 'K', 1)

                elif self.number_white_bishop == 1 and self.fen.count('K') == 0:
                    bishop_index = self.fen.index('B')
                    self.fen = self.fen[:bishop_index] + self.fen[bishop_index:].replace('B', 'K', 1)

                elif self.number_black_rook == 2 and self.fen.count('K') == 0:
                    rook_index =  [i for i, piece in enumerate(self.fen) if piece == 'r'][1]
                    self.fen = self.fen[:rook_index] + self.fen[rook_index:].replace('r', 'K', 1)

                elif self.number_black_rook == 1 and self.fen.count('K') == 0:
                    rook_index = self.fen.index('r')
                    self.fen = self.fen[:rook_index] + self.fen[rook_index:].replace('r', 'K', 1)

            if self.number_white_king == 2:
                if self.number_white_queen == 0:
                    if self.rows[7].count('K') == 2:
                        new_fen = ""
                        index = self.rows[7].index('K', 2)
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('K', 'Q', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen
                    else:
                        king_index =  [i for i, piece in enumerate(self.fen) if piece == 'K'][1]
                        self.fen = self.fen[:king_index] + self.fen[king_index:].replace('K', 'Q', 1)
                if self.number_white_bishop < 2 and self.fen.count('K') == 2:
                    if self.rows[7].count('K') == 2:
                        new_fen = ""
                        index = self.rows[7].index('K', 2)
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('K', 'B', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen
                    else:
                        king_index =  [i for i, piece in enumerate(self.fen) if piece == 'K'][1]
                        self.fen = self.fen[:king_index] + self.fen[king_index:].replace('K', 'B', 1)
                if self.number_white_rook < 2 and self.fen.count('K') == 2:
                    if self.rows[7].count('K') == 2:
                        new_fen = ""
                        index = self.rows[7].index('K', 2)
                        self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('K', 'R', 1)
                        for row in self.rows:
                            new_fen += row + '/'
                        new_fen = new_fen[:-1]
                        self.fen = new_fen
                    else:
                        king_index =  [i for i, piece in enumerate(self.fen) if piece == 'K'][1]
                        self.fen = self.fen[:king_index] + self.fen[king_index:].replace('K', 'R', 1)

    def fen_improve_queen(self):

        self.count_chess_pieces()

        if self.number_black_queen > 1:
            if self.number_black_rook < 2:
                queen_index =  [i for i, piece in enumerate(self.fen) if piece == 'q'][1]
                self.fen = self.fen[:queen_index] + self.fen[queen_index:].replace('q', 'r', 1)

            if self.number_black_bishop < 2 and self.fen.count('q') > 1:
                queen_index =  [i for i, piece in enumerate(self.fen) if piece == 'q'][1]
                self.fen = self.fen[:queen_index] + self.fen[queen_index:].replace('q', 'b', 1)

        if self.number_white_queen > 1:
            if self.number_white_rook < 2 and self.fen.count('Q') > 1:
                queen_index =  [i for i, piece in enumerate(self.fen) if piece == 'Q'][1]
                self.fen = self.fen[:queen_index] + self.fen[queen_index:].replace('Q', 'R', 1)

            if self.number_white_bishop < 2:
                queen_index =  [i for i, piece in enumerate(self.fen) if piece == 'Q'][1]
                self.fen = self.fen[:queen_index] + self.fen[queen_index:].replace('Q', 'B', 1)

    def fen_improve_knight(self):

        self.count_chess_pieces()

        if self.number_black_knight + self.number_black_pawn > 10 or self.number_black_knight > 2:
            if self.rows[0].count('r') < 2 and self.rows[0].count('n') > 0:
                new_fen = ""
                index = self.rows[0].index('n')
                self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('n', 'r', 1)
                for row in self.rows:
                    new_fen += row + '/'
                new_fen = new_fen[:-1]
                self.fen = new_fen
            number_of_pawns = 0
            for i in range(1,7):
                number_of_pawns += self.rows[i].count('p')

            if number_of_pawns < 8:
                knight_index =  [i for i, piece in enumerate(self.fen) if piece == 'n'][2]
                self.fen = self.fen[:knight_index] + self.fen[knight_index:].replace('n', 'p', 1)
            else:
                knight_index =  [i for i, piece in enumerate(self.fen) if piece == 'n'][2]
                self.fen = self.fen[:knight_index] + self.fen[knight_index:].replace('n', 'r', 1)

        if self.number_white_knight + self.number_white_pawn > 10 or self.number_white_knight > 2:
            if self.rows[7].count('R') < 2 and self.rows[7].count('N') > 0:
                new_fen = ""
                index = self.rows[7].index('N')
                self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('N', 'R', 1)
                for row in self.rows:
                    new_fen += row + '/'
                new_fen = new_fen[:-1]
                self.fen = new_fen
            number_of_pawns = 0

            for i in range(1,7):
                number_of_pawns += self.rows[i].count('P')

            if number_of_pawns < 8:
                knight_index =  [i for i, piece in enumerate(self.fen) if piece == 'N'][0]
                self.fen = self.fen[:knight_index] + self.fen[knight_index:].replace('N', 'P', 1)
            elif self.fen.count('N') > 2:
                knight_index =  [i for i, piece in enumerate(self.fen) if piece == 'N'][0]
                self.fen = self.fen[:knight_index] + self.fen[knight_index:].replace('N', 'R', 1)

    def fen_improve_bishop(self):

        self.count_chess_pieces()

        if self.number_black_bishop + self.number_black_pawn > 10 or self.number_black_bishop > 2:
            if self.rows[0].count('r') < 2 and self.rows[0].count('b') > 0:
                new_fen = ""
                index = self.rows[0].index('b')
                self.rows[0] = self.rows[0][:index] + self.rows[0][index:].replace('b', 'r', 1)
                for row in self.rows:
                    new_fen += row + '/'
                new_fen = new_fen[:-1]
                self.fen = new_fen
            number_of_pawns = 0
            for i in range(1,7):
                number_of_pawns += self.rows[i].count('p')
            if number_of_pawns < 8:
                bishop_index =  [i for i, piece in enumerate(self.fen) if piece == 'b'][2]
                self.fen = self.fen[:bishop_index] + self.fen[bishop_index:].replace('b', 'p', 1)
            else:
                bishop_index =  [i for i, piece in enumerate(self.fen) if piece == 'b'][2]
                self.fen = self.fen[:bishop_index] + self.fen[bishop_index:].replace('b', 'r', 1)

        if self.number_white_bishop + self.number_white_pawn > 10 or self.number_white_bishop > 2:
            if self.rows[7].count('R') < 2 and self.rows[0].count('B') > 0:
                new_fen = ""
                index = self.rows[7].index('B')
                self.rows[7] = self.rows[7][:index] + self.rows[7][index:].replace('B', 'R', 1)
                for row in self.rows:
                    new_fen += row + '/'
                new_fen = new_fen[:-1]
                self.fen = new_fen
            number_of_pawns = 0
            for i in range(1,7):
                number_of_pawns += self.rows[i].count('P')
            if number_of_pawns < 8:
                bishop_index =  [i for i, piece in enumerate(self.fen) if piece == 'B'][0]
                self.fen = self.fen[:bishop_index] + self.fen[bishop_index:].replace('B', 'P', 1)
            else:
                bishop_index =  [i for i, piece in enumerate(self.fen) if piece == 'B'][0]
                self.fen = self.fen[:bishop_index] + self.fen[bishop_index:].replace('B', 'R', 1)

    def fen_improve_rook(self):

        self.count_chess_pieces()

        if self.number_black_rook + self.number_black_pawn > 10 or self.number_black_rook > 2:
            if self.rows[0].count('r') > 2:
                if self.rows[0].count('q') == 0:
                    new_fen = ""
                    rook_index =  self.rows[0].index('r', 1)
                    self.rows[0] = self.rows[0][:rook_index] + self.rows[0][rook_index:].replace('r', 'q', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[0].count('n') < 2:
                    new_fen = ""
                    rook_index =  self.rows[0].index('r', 1)
                    self.rows[0] = self.rows[0][:rook_index] + self.rows[0][rook_index:].replace('r', 'n', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[0].count('b') < 2:
                    new_fen = ""
                    rook_index =  self.rows[0].index('r', 1)
                    self.rows[0] = self.rows[0][:rook_index] + self.rows[0][rook_index:].replace('r', 'b', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
            elif self.number_black_pawn < 8 and self.number_black_pawn > 1 and self.fen.count('r') > 2 and self.fen.count('r') > 2 and self.rows[0].count('p') == 0:
                if self.rows[1].count('r') > 0 and self.fen.count('p') < 8:
                    new_fen = ""
                    rook_index =  self.rows[1].index('r')
                    self.rows[1] = self.rows[1][:rook_index] + self.rows[1][rook_index:].replace('r', 'p', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[2].count('r') > 0 and self.fen.count('p') < 8:
                    new_fen = ""
                    rook_index =  self.rows[2].index('r')
                    self.rows[2] = self.rows[2][:rook_index] + self.rows[2][rook_index:].replace('r', 'p', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[3].count('r') > 0 and self.fen.count('p') < 8:
                    new_fen = ""
                    rook_index =  self.rows[3].index('r')
                    self.rows[3] = self.rows[3][:rook_index] + self.rows[3][rook_index:].replace('r', 'p', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[4].count('r') > 0 and self.fen.count('p') < 8:
                    new_fen = ""
                    rook_index =  self.rows[4].index('r')
                    self.rows[4] = self.rows[4][:rook_index] + self.rows[4][rook_index:].replace('r', 'p', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[5].count('r') > 0 and self.fen.count('p') < 8:
                    new_fen = ""
                    rook_index =  self.rows[5].index('r')
                    self.rows[5] = self.rows[5][:rook_index] + self.rows[5][rook_index:].replace('r', 'p', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[6].count('r') > 0 and self.fen.count('p') < 8:
                    new_fen = ""
                    rook_index =  self.rows[6].index('r')
                    self.rows[6] = self.rows[6][:rook_index] + self.rows[6][rook_index:].replace('r', 'p', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen

        if self.number_white_rook + self.number_white_pawn > 10 or self.number_white_rook > 2:
            if self.rows[7].count('R') > 2:
                if self.rows[7].count('Q') == 0:
                    new_fen = ""
                    rook_index =  self.rows[7].index('R', 1)
                    self.rows[7] = self.rows[7][:rook_index] + self.rows[7][rook_index:].replace('R', 'Q', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[7].count('N') < 2:
                    new_fen = ""
                    rook_index =  self.rows[7].index('R', 1)
                    self.rows[7] = self.rows[7][:rook_index] + self.rows[7][rook_index:].replace('R', 'N', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[7].count('B') < 2:
                    new_fen = ""
                    rook_index =  self.rows[7].index('R', 1)
                    self.rows[7] = self.rows[7][:rook_index] + self.rows[7][rook_index:].replace('R', 'B', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen

            elif self.number_white_pawn < 8 and self.number_white_pawn > 1 and self.fen.count('R') > 2 and self.fen.count('R') > 2 and self.rows[7].count('P') == 0:
                if self.rows[6].count('R') > 0 and self.fen.count('P') < 8:
                    new_fen = ""
                    rook_index =  self.rows[6].index('R')
                    self.rows[6] = self.rows[6][:rook_index] + self.rows[6][rook_index:].replace('R', 'P', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[5].count('R') > 0 and self.fen.count('P') < 8:
                    new_fen = ""
                    rook_index =  self.rows[5].index('R')
                    self.rows[5] = self.rows[5][:rook_index] + self.rows[5][rook_index:].replace('R', 'P', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[4].count('R') > 0 and self.fen.count('P') < 8:
                    new_fen = ""
                    rook_index =  self.rows[4].index('R')
                    self.rows[4] = self.rows[4][:rook_index] + self.rows[4][rook_index:].replace('R', 'P', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[3].count('R') > 0 and self.fen.count('P') < 8:
                    new_fen = ""
                    rook_index =  self.rows[3].index('R')
                    self.rows[3] = self.rows[3][:rook_index] + self.rows[3][rook_index:].replace('R', 'P', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[2].count('R') > 0 and self.fen.count('P') < 8:
                    new_fen = ""
                    rook_index =  self.rows[2].index('R')
                    self.rows[2] = self.rows[2][:rook_index] + self.rows[2][rook_index:].replace('R', 'P', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen
                if self.rows[1].count('R') > 0 and self.fen.count('P') < 8:
                    new_fen = ""
                    rook_index =  self.rows[1].index('R')
                    self.rows[1] = self.rows[1][:rook_index] + self.rows[1][rook_index:].replace('R', 'P', 1)
                    for row in self.rows:
                        new_fen += row + '/'
                    new_fen = new_fen[:-1]
                    self.fen = new_fen

    def get_improved_fen(self):
        fen_improved = self.fen + " w - - 0 1"
        return fen_improved
