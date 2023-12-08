from game import Game
from player import Player


name = input("Введите имя первого игрока: ")
player1 = Player(name)
name = input("Введите имя второго игрока: ")
player2 = Player(name)
game = Game(player1, player2)
game.start()
