# Generated by Django 4.1.5 on 2023-04-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='content',
        ),
        migrations.AddField(
            model_name='bot',
            name='name',
            field=models.TextField(blank=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='bot',
            name='phone',
            field=models.TextField(blank=True, verbose_name='Телефон-номер'),
        ),
        migrations.AlterField(
            model_name='bot',
            name='title',
            field=models.CharField(max_length=255, verbose_name='ID'),
        ),
    ]
