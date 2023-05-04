from rest_framework import serializers
from .models import ipad


class usersbot(serializers.ModelSerializer):
    class Meta:
        model = ipad
        fields = ['ID','title', 'price', 'photo']
