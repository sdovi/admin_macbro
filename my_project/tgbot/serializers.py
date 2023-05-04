from rest_framework import serializers
from .models import bot


class usersbot(serializers.ModelSerializer):
    class Meta:
        model = bot
        fields = ['ArticleID', 'name', 'phone']
