# Generated by Django 4.1.2 on 2022-12-05 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_addbook_id_remove_conform_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='conform',
            new_name='confirm',
        ),
    ]