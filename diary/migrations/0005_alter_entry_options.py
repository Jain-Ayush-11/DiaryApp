# Generated by Django 3.2.8 on 2021-10-23 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_remove_entry_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
