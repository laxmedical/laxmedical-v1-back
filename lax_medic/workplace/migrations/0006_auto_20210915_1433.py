# Generated by Django 3.2.5 on 2021-09-15 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workplace', '0005_auto_20210908_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordonnace',
            name='note',
        ),
        migrations.AddField(
            model_name='consultation',
            name='data',
            field=models.JSONField(default=None),
        ),
        migrations.AddField(
            model_name='consultation',
            name='type',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='fiche',
            name='is_urgent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fiche',
            name='type',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='ordonnace',
            name='data',
            field=models.JSONField(default=None),
        ),
        migrations.AddField(
            model_name='patient',
            name='blud_group',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='data',
            field=models.JSONField(default=None),
        ),
        migrations.AddField(
            model_name='patient',
            name='is_dead',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Soin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=None, max_length=100)),
                ('data', models.JSONField(default=None)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='soins', to=settings.AUTH_USER_MODEL)),
                ('fiche', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='soins', to='workplace.fiche')),
            ],
        ),
        migrations.CreateModel(
            name='Prelevement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=None, max_length=100)),
                ('data', models.JSONField(default=None)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prelevements', to=settings.AUTH_USER_MODEL)),
                ('fiche', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prelevements', to='workplace.fiche')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=None, max_length=100)),
                ('data', models.JSONField(default=None)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operations', to=settings.AUTH_USER_MODEL)),
                ('fiche', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operations', to='workplace.fiche')),
            ],
        ),
        migrations.CreateModel(
            name='Hospitalisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('type', models.CharField(default=None, max_length=100)),
                ('data', models.JSONField(default=None)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospitalisations', to=settings.AUTH_USER_MODEL)),
                ('fiche', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospitalisations', to='workplace.fiche')),
            ],
        ),
        migrations.CreateModel(
            name='FactureGrid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=None, max_length=100)),
                ('data', models.JSONField(default=None)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facture_grids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=None, max_length=100)),
                ('data', models.JSONField(default=None)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='factures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BonAnalyse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=None, max_length=100)),
                ('data', models.JSONField(default=None)),
                ('consultation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bon_analyses', to='workplace.consultation')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bon_analyses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Analyse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=None, max_length=100)),
                ('analyses', models.JSONField(default=None)),
                ('results', models.JSONField(default=None)),
                ('bon_analyse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='analyses', to='workplace.bonanalyse')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='analyses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=None, max_length=100)),
                ('data', models.JSONField(default=None)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alerts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
