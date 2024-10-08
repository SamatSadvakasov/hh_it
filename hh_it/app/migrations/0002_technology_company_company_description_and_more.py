# Generated by Django 5.1.1 on 2024-09-29 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Changed at')),
                ('technology_name', models.CharField(max_length=255, verbose_name='Технология')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='company',
            name='company_description',
            field=models.TextField(default=None, verbose_name='Текст компании'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Локация компании'),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Веб-сайт компании'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='employment_type',
            field=models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Freelance', 'Freelance')], default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Локация вакансии'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='posted_date',
            field=models.DateField(default=None, verbose_name='Дата поста вакансии'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='technology',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.technology', verbose_name='Технология'),
            preserve_default=False,
        ),
    ]
