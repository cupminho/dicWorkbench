# Generated by Django 3.2.3 on 2021-05-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0002_document_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.IntegerField(auto_created=True, choices=[(0, '신규'), (1, '보류'), (2, '완료')], default=0),
        ),
    ]
