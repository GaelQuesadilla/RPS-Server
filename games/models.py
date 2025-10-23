from django.db import models
from users.models import Player
from random import choice
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

    def save(self, *args, **kwargs):

        if not self.machine_choice:
            self.machine_choice = choice(self.CHOICES)[0]

        self.result = self.get_result()

        super().save(*args, **kwargs)

    def get_result(self):

        if self.player_choice == self.machine_choice:
            return "D"  # Draw

        # Rock vs Scissors:
        if self.player_choice == "R" and self.machine_choice == "S":
            return "W"

        # Scissors vs Paper:
        if self.player_choice == "S" and self.machine_choice == "P":
            return "W"

        # Paper vs Rock:
        if self.player_choice == "P" and self.machine_choice == "R":
            return "W"

        return "L"

    def __str__(self):
        return f"{self.player.username} {self.result} against vs Machine at {self.created_at}"
