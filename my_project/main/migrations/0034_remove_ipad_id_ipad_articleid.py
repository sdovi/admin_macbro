# Generated by Django 4.1.7 on 2023-04-30 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_remove_ipad_articleid_ipad_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipad',
            name='id',
        ),
        migrations.AddField(
            model_name='ipad',
            name='ArticleID',
            field=models.IntegerField(default=1, max_length=50, primary_key=True, serialize=False, verbose_name='ArticleID'),
            preserve_default=False,
        ),
    ]