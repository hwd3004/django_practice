# Generated by Django 4.0.2 on 2022-02-08 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_remove_notice_attachment_notice_attachment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice_attachment',
            old_name='master',
            new_name='master_notice',
        ),
    ]
