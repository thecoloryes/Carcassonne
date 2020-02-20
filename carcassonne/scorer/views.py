from django.shortcuts import render
from .models import *

def player(request, username):
    context = {
        'player': Player.objects.get(username = username),
    }
    return render(request, 'player.html', context)

def new_game(request):
    return render(request, 'new_game.html', {})

def game(request, game_id):
    context = {
        'game': Game.objects.get(id = game_id),
        'num_features': Feature.objects.filter(game__id = game_id).
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
