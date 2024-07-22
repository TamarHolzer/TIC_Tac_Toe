from board import Board
from player import Player


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = Player(player1, 'X')
        self.player2 = Player(player2, 'O')
        self.turn = 1

    def Play(self):
        mark1 = self.player1.marker
        mark2 = self.player2.marker
        while self.board.is_winner(mark1) is False and self.board.is_winner(mark2) is False \
                and self.board.is_draw() is False and self.turn <= 9:
           try:
                if self.turn % 2:
                    place = input(f"{str(self.player2.name)} enter a place ")
                    self.board.make_move(self.player2, int(place)-1)
                else:
                    place = input(f"{str(self.player1.name)} enter a place ")
                    self.board.make_move(self.player1, int(place)-1)
                print(f"{self.board}")
                self.turn = self.turn+1
           except ValueError:
               print("The place is not empty try again")
           except TypeError:
               print("The location is out of range try again")

        if self.board.is_winner(mark1) is True:
            print(f"Hooray {self.player1.name}, you won!🏆")
        elif self.board.is_winner(mark2) is True:
            print(f"Hooray {self.player2.name}, you won!🏆")
        else:
            print("Game over⏳")
