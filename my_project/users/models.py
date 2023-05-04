from django.db import models

class Users(models.Model):
    title = models.CharField("Имя", max_length=50)
    surname = models.CharField("фамилия", max_length=20, null=True,)
    number = models.IntegerField("Номер", max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "юзер"
        verbose_name_plural = "юзеры"
