from player import Player


class Board:
    def __init__(self):
       self.boardGame = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __str__(self):
        s = " ------------ \n"
        for i in range(0, 7, 3):
            s += f"| {self.boardGame[i]} | {self.boardGame[i + 1]} | {self.boardGame[i + 2]} | \n"
            s += " ------------ \n"
        return s

    def make_move(self, player, place):
            if place < 0 or place > 8:
                raise TypeError
            elif self.boardGame[place] != ' ':
                raise ValueError
            else:
                self.boardGame[place] = player.marker

    def is_winner(self, marker):
        for i in range(0, 7, 3):
            if self.boardGame[i] == self.boardGame[i+1] == self.boardGame[i+2] == marker:
                return True
        for i in range(3):
            if self.boardGame[i] == self.boardGame[i + 3] == self.boardGame[i + 6] == marker:
                return True
        if self.boardGame[0] == self.boardGame[4] == self.boardGame[8] == marker:
            return True
        if self.boardGame[2] == self.boardGame[4] == self.boardGame[6] == marker:
            return True
        return False

    def is_draw(self):
        flag = True
        for i in range(9):
            if self.boardGame[i] == ' ':
                flag = False
        if flag is True:
            if self.is_winner('X') is True:
                flag = False
            if self.is_winner('O') is True:
                flag = False
        return flag


