# Generated by Django 4.0.2 on 2022-02-08 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0004_notice_watched'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='attachment',
        ),
        migrations.CreateModel(
            name='Notice_Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=300, null=True)),
                ('attachment', models.FileField(null=True, upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.notice')),
            ],
            options={
                'db_table': 'notice_attachment',
            },
        ),
    ]
