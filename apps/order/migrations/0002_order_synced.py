# Generated by Django 2.0.4 on 2018-04-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='synced',
            field=models.BooleanField(default=False, verbose_name='Synced'),
        ),
    ]
