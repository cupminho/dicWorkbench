# Generated by Django 2.2.5 on 2021-06-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20210605_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.CharField(max_length=120),
        ),
    ]
