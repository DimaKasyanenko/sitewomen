# Generated by Django 5.0.1 on 2024-02-11 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0008_alter_women_managers_rename_tag_women_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Husband',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Муж')),
                ('age', models.PositiveSmallIntegerField(null=True, verbose_name='Возраст')),
            ],
        ),
        migrations.AddField(
            model_name='women',
            name='husband',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wuman', to='women.husband', verbose_name='Муж'),
        ),
    ]
