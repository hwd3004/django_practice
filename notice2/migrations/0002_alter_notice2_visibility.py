# Generated by Django 4.0.2 on 2022-02-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice2',
            name='visibility',
            field=models.CharField(choices=[('공개', '공개'), ('비공개', '비공개')], max_length=10),
        ),
    ]
