# Generated by Django 4.0.2 on 2022-02-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0009_alter_lab_file_alter_lab_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='image',
        ),
        migrations.AlterField(
            model_name='lab',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
