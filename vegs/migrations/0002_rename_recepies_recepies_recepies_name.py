# Generated by Django 5.0.4 on 2024-04-07 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vegs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recepies',
            old_name='recepies',
            new_name='recepies_name',
        ),
    ]
