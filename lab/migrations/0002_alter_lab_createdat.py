# Generated by Django 4.0.2 on 2022-02-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='createdAt',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
