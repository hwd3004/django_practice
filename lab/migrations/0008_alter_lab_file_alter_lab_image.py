# Generated by Django 4.0.2 on 2022-02-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0007_alter_lab_file_alter_lab_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lab',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
