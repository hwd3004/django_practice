# Generated by Django 4.0.2 on 2022-02-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0007_rename_master_notice_notice_attachment_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice_attachment',
            name='filename',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
