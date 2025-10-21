from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Player(AbstractUser):

    total_wins = models.PositiveIntegerField(
        default=0, blank=False, editable=True)

    total_losses = models.PositiveIntegerField(
        default=0, blank=False, editable=True)

    total_games = models.PositiveIntegerField(
        default=0, blank=False, editable=True)

    def __str__(self):
        return self.username
