from django.db import models

RIVER_TILE_COUNT = 12
BASE_TILE_COUNT = 72 
MAX_USERNAME_LENGTH = 50
MAX_PLAYERS = 5

class Player(models.Model):
    """Represents a particular player."""
    username = models.CharField(
          max_length=MAX_USERNAME_LENGTH, 
          primary_key=True)
    icon = models.ImageField(null=True, blank=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0) 

    def __str__(self):
        return f"Player {self.username}"

class GameOverException(Exception):
    """Raised when the game is over."""
    def __init__(self, *args):
        if args:
            super(GameOverException, self).__init__()
        else:
            self.message = "Maximum turns reached. Game over!"

class Game(models.Model):
    """Represents a particular game."""
    using_rivers = models.BooleanField(default=False)
    turn = models.IntegerField(default=0)

    # Max length of all usernames + delimiters
    length = MAX_USERNAME_LENGTH * MAX_PLAYERS + MAX_PLAYERS
    player_list = models.CharField(max_length=length)

    def max_turns():
        """Calculate the proper number of turns based on game settings."""
        if using_rivers:
            return BASE_TILE_COUNT + RIVER_TILE_COUNT
        else:
            return BASE_TILE_COUNT
   
    def __str__(self):
        return f"Game #{self.id}"
        

class Feature(models.Model):
    """Represents a particular feature, complete or not."""
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    size = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def score(self):
        #Subclasses must implement.
        raise NotImplementedError

class Road(Feature):
    """Represents a Road feature."""
    def score(self):
        return self.size
    
    def __str__(self):
       return f"{self.score}-point road"

class City(Feature):
    """Represents a City feature."""
    coats_of_arms = models.IntegerField(default=0)

    def score(self):
        factor = 2 if self.is_completed else 1
        return self.size * factor + self.coats * factor

    def __str__(self):
       return f"{self.score}-point city"

class Monastery(Feature):
    def score(self):
        return self.size

    def __str__(self):
       return f"{self.score}-point monastery"
