# Generated by Django 5.1.4 on 2025-01-18 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='update',
            new_name='updated',
        ),
    ]
