# Generated by Django 3.1 on 2021-03-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210314_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_meme',
            field=models.BooleanField(default=True),
        ),
    ]
