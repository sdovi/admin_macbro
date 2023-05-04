from rest_framework import generics
from .models import bot
from .serializers import usersbot


class bottg(generics.ListCreateAPIView):
    queryset = bot.objects.all()
    serializer_class = usersbot


class botupdate(generics.RetrieveUpdateAPIView):
    queryset = bot.objects.all()
    serializer_class = usersbot
