from game import Game
from player import Player


def main():
    name1 = input(f"Hi first player please enter your name")
    name2 = input(f"Hi second player please enter your name")
    player1 = Player(name1, 'X')
    player2 = Player(name2, 'O')
    game1 = Game(player1, player2)
    game1.Play()



main()
