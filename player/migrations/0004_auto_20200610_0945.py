# Generated by Django 3.0.7 on 2020-06-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_auto_20200608_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.ImageField(default='music.jpg', upload_to='tracks/'),
        ),
    ]
