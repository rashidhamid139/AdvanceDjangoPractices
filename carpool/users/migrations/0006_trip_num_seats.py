# Generated by Django 3.0.7 on 2020-06-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='num_seats',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
