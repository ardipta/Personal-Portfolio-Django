# Generated by Django 2.2.10 on 2020-09-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]