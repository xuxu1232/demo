# Generated by Django 2.2.1 on 2019-09-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='publish',
            name='num',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='publish',
            name='salled',
            field=models.IntegerField(default=10),
        ),
    ]
