from django.db import models
from users.models import Player

# Create your models here.


class Match(models.Model):

    CHOICES = [
        ("R", "Rock"),
        ("P", "Paper"),
        ("S", "Scissors"),
    ]

    RESULTS = [
        ("W", "Win"),
        ("L", "Loss"),
        ("D", "Draw"),
    ]

    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="matches")

    player_choice = models.CharField(
        max_length=1, choices=CHOICES, blank=False)
    machine_choice = models.CharField(
        max_length=1, choices=CHOICES, blank=False)

    # The results of the match for the player
    result = models.CharField(
        max_length=1, choices=RESULTS, blank=False)

    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, blank=False)

    def __str__(self):
        return f"{self.player.username} {self.result} against vs Machine at {self.created_at}"
