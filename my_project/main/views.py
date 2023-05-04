
from django.shortcuts import render
from .models import airpods, iphone, watch, ipad, mac, main_card, menuwatch, akustika, aksesuar, phone, samsung, akustikamain, aksessuarmain, phonemain, maintext
from rest_framework import generics
from .models import ipad
from .serializers import usersbot


class bottg(generics.ListCreateAPIView):
    queryset = ipad.objects.all()
    serializer_class = usersbot


class botupdate(generics.UpdateAPIView):
    queryset = ipad.objects.all()
    serializer_class = usersbot


def macipad(request):
    product = ipad.objects.all()
    return render(request, "main/mac_ipad.html", {"product": product})


def macbro(request):
    product = main_card.objects.all()
    akustika = akustikamain.objects.all()
    aksessuar = aksessuarmain.objects.all()
    phone = phonemain.objects.all()
    textfooter = maintext.objects.all()
    return render(request, "main/macbro-glavniy.html", {"product": product,
                                                        "akustika": akustika,
                                                        "aksessuar": aksessuar,
                                                        "phone": phone,
                                                        "text": textfooter})


def macmac(request):
    product = mac.objects.all()
    return render(request, "main/mac_mac.html", {"product": product})


def maciphone(request):
    product = iphone.objects.all()
    return render(request, "main/mac_iphone.html", {"product": product})


def macwatch(request):
    product = watch.objects.all()
    return render(request, "main/mac_watch.html", {"product": product})


def macair(request):
    product = airpods.objects.all()
    return render(request, "main/mac_airpots.html", {"product": product})


def macwatchmenu(request):
    product = menuwatch.objects.all()
    return render(request, "main/mac_watchmenu.html", {"product": product})


def maciphonemenu(request):
    product = iphone.objects.all()
    return render(request, "main/mac_iphonemenu.html", {"product": product})


def macbrotwo(request):
    return render(request, "main/macbro_two.html", )


def macaksesuar(request):
    product = aksesuar.objects.all()
    return render(request, "main/mac_aksesuar.html", {"product": product})


def macakustika(request):
    product = akustika.objects.all()
    return render(request, "main/mac_akustika.html", {"product": product})


def macphone(request):
    product = phone.objects.all()
    return render(request, "main/mac_phone.html",  {"product": product})


def macsamsung(request):
    product = samsung.objects.all()
    return render(request, "main/mac_samsung.html", {"product": product})


def macall(request):
    mac1 = mac.objects.all()
    iphone1 = iphone.objects.all()
    ipad1 = ipad.objects.all()
    watch1 = watch.objects.all()
    airpods1 = airpods.objects.all()
    akustika1 = akustika.objects.all()
    aksesuar1 = aksesuar.objects.all()
    phone1 = phone.objects.all()
    samsung1 = samsung.objects.all()
    return render(request, "main/mac_all.html", {"mac": mac1,
                                                 "iphone": iphone1,
                                                 "ipad": ipad1,
                                                 "watch": watch1,
                                                 "airpods": airpods1,
                                                 "akustika": akustika1,
                                                 "aksessuar": aksesuar1,
                                                 "phone": phone1,
                                                 "samsung": samsung1, })


def macnovosti(request):
    return render(request, "main/mac_novosti.html")


def maccompaniya(request):
    return render(request, "main/mac_companiya.html")


def macmagazine(request):
    return render(request, "main/mac_magazine.html")


def macvakansi(request):
    return render(request, "main/mac_vakansi.html")


def macsell(request):
    return render(request, "main/mac_sell.html")


def maceosim(request):
    return render(request, "main/mac_eosim.html")


def macdostavka(request):
    return render(request, "main/mac_dostavka.html")


def maccontac(request):
    return render(request, "main/mac_contacs.html")


def macskidka(request):
    return render(request, "main/mac_skidka.html")
