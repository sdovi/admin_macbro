# Generated by Django 4.1.7 on 2023-04-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_remove_ipad_id_ipad_articleid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipad',
            name='ArticleID',
        ),
        migrations.AddField(
            model_name='ipad',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
