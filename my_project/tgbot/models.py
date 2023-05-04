from django.db import models

class bot(models.Model):
    ArticleID = models.CharField('ArticleID', max_length=50, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Боты"
        verbose_name_plural = "Боты"






