# Generated by Django 3.2.15 on 2022-09-09 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
    ]