# Generated by Django 2.2.5 on 2021-05-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.IntegerField(auto_created=True, default=0),
        ),
    ]
