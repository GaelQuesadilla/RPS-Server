from games.models import Match
from games.serializers import MatchSerializer

from rest_framework import viewsets, permissions


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MatchSerializer
