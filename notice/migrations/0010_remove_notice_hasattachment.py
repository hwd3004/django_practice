# Generated by Django 4.0.2 on 2022-02-09 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0009_notice_hasattachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='hasAttachment',
        ),
    ]
