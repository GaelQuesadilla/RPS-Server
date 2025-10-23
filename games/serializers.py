from rest_framework import serializers
from games.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "id", "player", "player_choice", "machine_choice", "result", "created_at",
        )
        read_only_fields = (
            "id", "player", "player_choice", "machine_choice", "result", "created_at",
        )


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ["player_choice"]
