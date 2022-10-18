# Generated by Django 4.1.2 on 2022-10-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_rename_registr_date_user_register_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chats',
            name='chat_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AddField(
            model_name='chats',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]