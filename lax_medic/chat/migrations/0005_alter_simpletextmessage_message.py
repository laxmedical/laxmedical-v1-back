# Generated by Django 3.2.5 on 2021-07-30 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_grouptextmessage_message_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpletextmessage',
            name='message',
            field=models.CharField(max_length=1000000),
        ),
    ]
