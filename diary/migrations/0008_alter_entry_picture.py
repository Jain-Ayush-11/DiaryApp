# Generated by Django 3.2.8 on 2021-10-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_alter_entry_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
