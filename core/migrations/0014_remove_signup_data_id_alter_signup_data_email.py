# Generated by Django 4.1.2 on 2022-12-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_donate_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup_data',
            name='id',
        ),
        migrations.AlterField(
            model_name='signup_data',
            name='email',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
