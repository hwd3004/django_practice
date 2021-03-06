# Generated by Django 4.0.2 on 2022-02-16 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('visibility', models.CharField(choices=[('public', '공개'), ('private', '비공개')], max_length=10)),
                ('password', models.CharField(default=None, max_length=100, null=True)),
                ('content', models.TextField()),
                ('watched', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.user')),
            ],
            options={
                'db_table': 'notice2',
            },
        ),
        migrations.CreateModel(
            name='Notice2_Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=300, null=True)),
                ('path', models.CharField(max_length=300, null=True)),
                ('attachment', models.FileField(null=True, upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice2.notice2')),
            ],
            options={
                'db_table': 'notice2_attachment',
            },
        ),
    ]
