# Generated by Django 5.0.1 on 2024-02-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-created_at'], 'verbose_name': 'Женщина', 'verbose_name_plural': 'Женщины'},
        ),
        migrations.AddField(
            model_name='women',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AddIndex(
            model_name='women',
            index=models.Index(fields=['-created_at'], name='women_women_created_bd38eb_idx'),
        ),
    ]
