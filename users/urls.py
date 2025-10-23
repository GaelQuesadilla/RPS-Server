"""
URL configuration for rpsserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from users.views import WhoAmI
from users.api import PlayerViewSet, Register
from rest_framework import routers


router = routers.DefaultRouter()


router.register('player', PlayerViewSet, basename='players')
router.register('register', Register, basename='register')


urlpatterns = [

    path(
        'whoami/',
        WhoAmI.as_view(),
        name='Who_am_I'
    ),

    path('', include(router.urls))

]
