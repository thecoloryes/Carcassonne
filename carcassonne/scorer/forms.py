from django import forms
from .models import Player, MAX_USERNAME_LENGTH, MAX_PLAYERS

class PlayerForm(forms.Form):
    """Form for creating a new player."""

    icon = forms.ImageField(required=False)
    username = forms.CharField(max_length=MAX_USERNAME_LENGTH, required=True)

class GameForm(forms.Form):
    """Form for creating a new game."""
    players = forms.ModelMultipleChoiceField(
            queryset=Player.objects.all(), 
            widget=forms.CheckboxSelectMultiple,
            label=f"Select up to {MAX_PLAYERS} players for this game")
    using_rivers = forms.BooleanField(label="Using river tiles", required=False)

    def clean_players(self):
        """Make sure there are a valid number of players."""
        p = self.cleaned_data['players']
        if len(p) > MAX_PLAYERS:
            raise forms.ValidationError(f"You can't have more than {MAX_PLAYERS} players.")
        elif len(p) < 2:
            raise forms.ValidationErorr("You must have at least 2 players.")
        return p

