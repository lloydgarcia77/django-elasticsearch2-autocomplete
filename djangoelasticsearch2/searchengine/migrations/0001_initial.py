# Generated by Django 3.1.5 on 2021-05-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('postId', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
    ]
