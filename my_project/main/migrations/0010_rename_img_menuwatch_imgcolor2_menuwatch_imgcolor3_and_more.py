# Generated by Django 4.1.5 on 2023-03-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_iphonemenu_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuwatch',
            old_name='img',
            new_name='imgcolor2',
        ),
        migrations.AddField(
            model_name='menuwatch',
            name='imgcolor3',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='menuwatch',
            name='imgcolor4',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='menuwatch',
            name='imgcolor5',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='menuwatch',
            name='imgcolor6',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='menuwatch',
            name='imgcolor7',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='menuwatch',
            name='imgcolor8',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='menuwatch',
            name='imgcolor9',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='menuwatch',
            name='list',
            field=models.TextField(max_length=2706, null=True, verbose_name='Описание продукта'),
        ),
        migrations.AddField(
            model_name='menuwatch',
            name='photoiphone',
            field=models.ImageField(null=True, upload_to='img', verbose_name='фото Айфона'),
        ),
        migrations.AlterField(
            model_name='menuwatch',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='размер'),
        ),
    ]
