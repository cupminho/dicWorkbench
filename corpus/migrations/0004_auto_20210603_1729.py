# Generated by Django 2.2.5 on 2021-06-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0003_auto_20210530_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
