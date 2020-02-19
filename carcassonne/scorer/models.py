from django.db import models
from django.contrib.auth.models import User

RIVER_TILE_COUNT = 12
BASE_TILE_COUNT = 72

class Player(User):
    icon = models.ImageField()
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
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    size = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def score():
        raise NotImplementedError

class Road(Feature):
    def __init__(self, sz, comp):
        self.size = sz
        self.is_completed = comp

    def score():
        return size

class City(Feature):
    coats_of_arms = models.IntegerField(default=0)

    def __init(self, sz, comp, cts):
        self.size = sz
        self.is_completed = comp
        self.coats_of_arms = cts

    def score():
        factor = 2 if is_completed else 1
        return size * factor + coats * factor

class Monastery(Feature):
    def __init__(self, sz):
        # Completion status can be inferred from size
        if sz > 9 or sz < 1:
            raise ValueError("The size of a monastery must be at least 1 and no more than 9 tiles.")
        elif sz == 9:
            self.size = sz
            self.is_completed = True
        else:
            self.size = sz
            self.is_completed = False

    def score():
        return size
