# Generated by Django 3.2.5 on 2021-09-06 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workplace', '0002_auto_20210904_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(default=None)),
                ('conclusion', models.TextField(default=None)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='constations', to=settings.AUTH_USER_MODEL)),
                ('fiche', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='constations', to='workplace.fiche')),
            ],
        ),
    ]
