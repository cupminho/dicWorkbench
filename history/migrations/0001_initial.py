# Generated by Django 2.2.5 on 2021-06-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=120)),
                ('original', models.CharField(max_length=120, null=True)),
                ('alias', models.CharField(max_length=120, null=True)),
                ('keyword', models.CharField(max_length=120, null=True)),
                ('area', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
                ('time', models.URLField(null=True)),
            ],
        ),
    ]
