# Generated by Django 3.2.5 on 2021-07-28 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleTextMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_received', models.BooleanField(default=False)),
                ('is_seen', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='simple_text_message_sents', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='simple_text_message_receiveds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupTextMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('received', models.BooleanField(default=False)),
                ('is_seen', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group')),
            ],
        ),
    ]