from django.urls import path
from tgbot.views import bottg

urlpatterns = [
    path('get', bottg.as_view()),
]

