# Generated by Django 2.2.4 on 2020-11-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0002_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='isbn',
            field=models.IntegerField(),
        ),
    ]
