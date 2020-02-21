"""carcassonne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from scorer import views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players', views.players),
    path('players/<username>', views.player),
    path('game/new', views.GameFormView.as_view()),
    path('game/<game_id>', views.game),
    path('game/<game_id>/turn', views.turn),
    path('game/<game_id>/submit_turn', views.submit_turn),
    path('games', views.games),
    path('', views.home),
    re_path(r'^.*$', RedirectView.as_view(url='/')),
] + static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)
