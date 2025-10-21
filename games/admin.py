from django.contrib import admin
from games.models import Match

# Register your models here.


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass
