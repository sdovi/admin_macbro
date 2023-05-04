# Generated by Django 4.1.7 on 2023-04-30 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0003_remove_bot_is_published_remove_bot_time_create_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='title',
        ),
        migrations.AddField(
            model_name='bot',
            name='ArticleID',
            field=models.CharField(default=1, max_length=50, primary_key=True, serialize=False, verbose_name='ArticleID'),
            preserve_default=False,
        ),
    ]