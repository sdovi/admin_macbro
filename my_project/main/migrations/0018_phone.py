# Generated by Django 4.1.5 on 2023-03-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_aksesuar'),
    ]

    operations = [
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(null=True, verbose_name='Цена товара')),
                ('photo', models.FileField(blank=True, null=True, upload_to='img')),
            ],
            options={
                'verbose_name': 'телефоны',
                'verbose_name_plural': 'телефон',
            },
        ),
    ]
