# Generated by Django 3.2.8 on 2021-12-15 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_simpletextmessage_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpletextmessage',
            name='message_code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
