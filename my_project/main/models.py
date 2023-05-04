from django.db import models


class mac(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "маки"
        verbose_name_plural = "мак"


class iphone(models.Model):
    title = models.CharField("Название", null=True, max_length=50, blank=True)
    price = models.IntegerField("Цена товара", null=True, blank=True)
    photo = models.FileField(upload_to="img", null=True, blank=True)
    content = models.TextField(
        "описание", null=True, blank=True, max_length=256)
    imgcolor2 = models.ImageField(upload_to="img", null=True, blank=True)
    imgcolor3 = models.ImageField(upload_to="img", null=True, blank=True)
    imgcolor4 = models.ImageField(upload_to="img", null=True, blank=True)
    imgcolor5 = models.ImageField(upload_to="img", null=True, blank=True)
    size = models.CharField("Емкость", max_length=20, null=True, blank=True)
    size2 = models.CharField("Емкость2", max_length=20, null=True,)
    size3 = models.CharField("Емкость3", max_length=20, null=True,)
    size4 = models.CharField("Емкость4", max_length=20, null=True,)
    sim = models.CharField("SIM", max_length=20, null=True, blank=True)
    sim2 = models.CharField("SIM2", max_length=20, null=True, blank=True)
    sim3 = models.CharField("SIM3", max_length=20, null=True, blank=True)
    list = models.TextField("Описание продукта",
                            null=True, blank=True, max_length=2706)
    photoiphone = models.ImageField("фото Айфона", upload_to="img", null=True)
    null = True

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "айфоны"
        verbose_name_plural = "айфон"


class ipad(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", default='http://127.0.0.1:8000/media/img/ipad_GqSrYvD.png')
    ID = models.CharField('ArticleID', max_length=50, primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "айпады"
        verbose_name_plural = "айпад"


class watch(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True)
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "часики"
        verbose_name_plural = "часы"


class airpods(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "наушники"
        verbose_name_plural = "наушник"


class main_card(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "главные страницы"
        verbose_name_plural = "главная страница"


class menuwatch(models.Model):
    title = models.CharField("Название", max_length=50)
    content = models.TextField("описание", null=True, max_length=256)
    size = models.CharField("размер", null=True, blank=True, max_length=20, )
    imgcolor2 = models.ImageField(upload_to="img", null=True)
    imgcolor3 = models.ImageField(upload_to="img", null=True)
    imgcolor4 = models.ImageField(upload_to="img", null=True)
    imgcolor5 = models.ImageField(upload_to="img", null=True)
    imgcolor6 = models.ImageField(upload_to="img", null=True)
    imgcolor7 = models.ImageField(upload_to="img", null=True)
    imgcolor8 = models.ImageField(upload_to="img", null=True)
    imgcolor9 = models.ImageField(upload_to="img", null=True)
    imgcolor10 = models.ImageField(upload_to="img", null=True)
    list = models.TextField("Описание продукта", null=True, max_length=5706)
    photowatch = models.ImageField("фото часов", upload_to="img", null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "меню"
        verbose_name_plural = "меню часов"


class akustika(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Акустика"
        verbose_name_plural = "Акустик"


class aksesuar(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "аксесуар"
        verbose_name_plural = "аксесуары"


class phone(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "телефоны"
        verbose_name_plural = "телефон"


class samsung(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "самсунг"
        verbose_name_plural = "самсунги"


class akustikamain(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "главная акустика"
        verbose_name_plural = "главные акустики"


class aksessuarmain(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "главная аксессуар"
        verbose_name_plural = "главные аксессуаров"


class phonemain(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "главная смартфон"
        verbose_name_plural = "главные смартфоны"


class maintext(models.Model):
    title = models.CharField(
        "Названиеи", max_length=100, null=True, blank=True)
    text0 = models.TextField("текст обычный")
    text1 = models.TextField("текст жирный", max_length=2000, null=True, blank=True)
    text2 = models.TextField("текст обычный", max_length=5000, null=True, blank=True)
    text3 = models.TextField("текст обычный", max_length=8000, null=True, blank=True)
    text4 = models.TextField("текст жирный", max_length=1000, null=True, blank=True)
    text5 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text6 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text7 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text8 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text9 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text10 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text11 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text12 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text13 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text14 = models.TextField("текст жирный", max_length=1000, null=True, blank=True)
    text15 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text16 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text17 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text18 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)
    text19 = models.TextField("текст обычный", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "главный текста"
        verbose_name_plural = "главные тескт"

