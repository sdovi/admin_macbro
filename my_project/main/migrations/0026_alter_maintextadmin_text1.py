# Generated by Django 4.1.7 on 2023-04-04 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_rename_maintext_maintextadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintextadmin',
            name='text1',
            field=models.TextField(max_length=1000, verbose_name='текст обычный'),
        ),
    ]