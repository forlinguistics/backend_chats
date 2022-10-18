# Generated by Django 4.1.2 on 2022-10-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('chat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('chat_name', models.CharField(max_length=30)),
                ('chat_description', models.TextField()),
                ('creation_date', models.DateField()),
                ('chat_icon', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('bio', models.TextField()),
                ('registr_date', models.DateField()),
                ('user_icon', models.URLField()),
                ('chats', models.ManyToManyField(to='chats.chats')),
            ],
        ),
    ]