from django.db import models
from django.contrib.auth.models import User

RIVER_TILE_COUNT = 12
BASE_TILE_COUNT = 72

class Player(User):
    icon = models.ImageField(null=True, blank=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0) 

class GameOverException(Exception):
    """Raised when the game is over"""
    def __init__(self, *args):
        if args:
            super(GameOverException, self).__init__()
        else:
            self.message = "Maximum turns reached. Game over!"


class Game(models.Model):
    using_rivers = models.BooleanField(default=False)
    turn = models.IntegerField(default=0)

    def max_turns():
        if using_rivers:
            return BASE_TILE_COUNT + RIVER_TILE_COUNT
        else:
            return BASE_TILE_COUNT

class Feature(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    size = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def score():
        raise NotImplementedError

class Road(Feature):
    def score():
        return size

class City(Feature):
    coats_of_arms = models.IntegerField(default=0)

    def score():
        factor = 2 if is_completed else 1
        return size * factor + coats * factor

class Monastery(Feature):
    def score():
        return size
