# Generated by Django 2.2.1 on 2019-06-06 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='画像')),
            ],
        ),
    ]
