# Generated by Django 4.0.2 on 2022-02-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_alter_notice_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='file',
        ),
        migrations.AddField(
            model_name='notice',
            name='attachment',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
