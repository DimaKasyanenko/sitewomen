# Generated by Django 5.0.1 on 2024-02-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0006_tagpost_alter_category_options_alter_women_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagpost',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.RemoveField(
            model_name='women',
            name='tags',
        ),
        migrations.AddField(
            model_name='women',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to='women.tagpost', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='tagpost',
            name='tag',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(1, 'Опубликовано'), (0, 'Черновик')], default=1, verbose_name='Опубликовано'),
        ),
    ]