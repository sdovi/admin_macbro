from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import bottg,botupdate

urlpatterns = [
    path('', views.macbro, name='btn3'),
    path('macbrotwo', views.macbrotwo, name='btn4', ),
    path('macmac', views.macmac, name='btn5', ),
    path('maciphone', views.maciphone, name='btn6', ),
    path('macipad', views.macipad, name='btn7', ),
    path('macwatch', views.macwatch, name='btn8', ),
    path('macairpods', views.macair, name='btn10', ),
    path('macwatchmenu', views.macwatchmenu, name='btn11', ),
    path('maciphonemenu', views.maciphonemenu, name='btn12', ),
    path('macaksesuar', views.macaksesuar, name='btn13', ),
    path('macakustika', views.macakustika, name='btn14', ),
    path('macphone', views.macphone, name='btn15', ),
    path('macsamsung', views.macsamsung, name='btn16', ),
    path('macall', views.macall, name='btn18', ),
    path('macnovosti', views.macnovosti, name='btn19', ),
    path('maccompaniya', views.maccompaniya, name='btn20', ),
    path('macmagazine', views.macmagazine, name='btn21', ),
    path('macvakansi', views.macvakansi, name='btn22', ),
    path('macsell', views.macsell, name='btn23', ),
    path('maceosim', views.maceosim, name='btn24', ),
    path('macdostavka', views.macdostavka, name='btn25', ),
    path('maccontac', views.maccontac, name='btn26', ),
    path('macskidka', views.macskidka, name='btn27', ),
    path('ipadipad',  bottg.as_view()),
    path('ipadipad/<int:pk>/',  botupdate.as_view()),
    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
