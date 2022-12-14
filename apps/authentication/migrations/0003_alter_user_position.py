# Generated by Django 3.2.15 on 2022-09-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, choices=[('SYS_ADMIN', 'System admin'), ('SUB_ADMIN', 'Sub admin'), ('HR', 'HR'), ('INQUIRIES', 'Inquiries')], default='INQUIRIES', max_length=150, verbose_name='position'),
        ),
    ]
