# Generated by Django 4.1.2 on 2022-12-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_addbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='conformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('book', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('passsword', models.CharField(max_length=30)),
            ],
        ),
    ]
