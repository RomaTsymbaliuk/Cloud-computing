# Generated by Django 5.0 on 2023-12-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_rename_firstname_entry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateField(),
        ),
    ]