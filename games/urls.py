from rest_framework import routers
from games.api import MatchViewSet
from django.urls import include, path
from games.views import Play
router = routers.DefaultRouter()

router.register('matches', MatchViewSet, basename='matches')


urlpatterns = [
    path('play/', Play.as_view(), name='play'),
    path('', include(router.urls))
]
