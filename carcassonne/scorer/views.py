from django.shortcuts import render
from django.views.generic import FormView
from .models import *
from .forms import *

class PlayerFormView(FormView):
    template_name = "new_player.html"
    form_class = PlayerForm

class GameFormView(FormView):
    template_name = "new_game.html"
    form_class = GameForm

def player(request, username):
    context = {
        'player': Player.objects.get(username = username),
    }
    return render(request, 'player.html', context)

def game(request, game_id):
    context = {
        'game': Game.objects.get(id = game_id),
        'num_features': Feature.objects.filter(game__id = game_id),
        'roads': Road.objects.filter(game__id = game_id),
        'cities': City.objects.filter(game__id = game_id),
        'monasteries': Monastery.objects.filter(game__id = game_id),
    }
    return render(request, 'game.html', context)

def turn(request, game_id):
    return render(request, 'turn.html', {})

def submit_turn(request, game_id):
    pass

def home(request):
    return render(request, 'home.html', {})

def players(request):
    context = {
        'players': Player.objects.all(),
    }
    return render(request, 'players.html', context)

def games(request):
    context = {
        'games': Game.objects.all(),
    }
    return render(request, 'games.html', context)
