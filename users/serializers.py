from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import serializers, viewsets
from users.models import Player

User = get_user_model()


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            "id", "is_superuser", "username", "total_wins", "total_losses", "total_games"
        )
        read_only_fields = (
            "id", "is_superuser", "username", "total_wins", "total_losses", "total_games"
        )


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
