# Generated by Django 4.2.16 on 2024-11-28 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
