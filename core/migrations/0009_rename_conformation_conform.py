# Generated by Django 4.1.2 on 2022-12-05 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_returnbook_return_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='conformation',
            new_name='conform',
        ),
    ]
