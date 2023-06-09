# Generated by Django 4.1.7 on 2023-03-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='airpods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(null=True, verbose_name='Цена товара')),
                ('photo', models.FileField(blank=True, null=True, upload_to='img')),
            ],
            options={
                'verbose_name': 'наушники',
                'verbose_name_plural': 'наушник',
            },
        ),
        migrations.CreateModel(
            name='ipad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(null=True, verbose_name='Цена товара')),
                ('photo', models.FileField(blank=True, null=True, upload_to='img')),
            ],
            options={
                'verbose_name': 'айпады',
                'verbose_name_plural': 'айпад',
            },
        ),
        migrations.CreateModel(
            name='iphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(null=True, verbose_name='Цена товара')),
                ('photo', models.FileField(blank=True, null=True, upload_to='img')),
                ('photo2', models.FileField(blank=True, null=True, upload_to='img')),
                ('photo3', models.FileField(blank=True, null=True, upload_to='img')),
            ],
            options={
                'verbose_name': 'айфоны',
                'verbose_name_plural': 'айфон',
            },
        ),
        migrations.CreateModel(
            name='mac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(null=True, verbose_name='Цена товара')),
                ('photo', models.FileField(blank=True, null=True, upload_to='img')),
            ],
            options={
                'verbose_name': 'маки',
                'verbose_name_plural': 'мак',
            },
        ),
        migrations.CreateModel(
            name='main_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(null=True, verbose_name='Цена товара')),
                ('photo', models.FileField(blank=True, null=True, upload_to='img')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'главные страницы',
                'verbose_name_plural': 'главная страница',
            },
        ),
        migrations.CreateModel(
            name='menuwatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(max_length=256, null=True, verbose_name='описание')),
                ('size', models.CharField(blank=True, max_length=20, null=True, verbose_name='Размер')),
                ('img', models.ImageField(null=True, upload_to='img')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'меню',
                'verbose_name_plural': 'меню часов',
            },
        ),
        migrations.CreateModel(
            name='watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(null=True, verbose_name='Цена товара')),
                ('photo', models.FileField(blank=True, null=True, upload_to='img')),
            ],
            options={
                'verbose_name': 'часики',
                'verbose_name_plural': 'часы',
            },
        ),
    ]
