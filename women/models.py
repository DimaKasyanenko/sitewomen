from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Category(models.Model):
    title = models.CharField('Категория', max_length=255, db_index=True)
    slug = models.SlugField('Ссылка', max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик',
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Ссылка', max_length=255, unique=True, db_index=True)
    description = models.TextField('Описание', blank=True)
    is_published = models.BooleanField('Опубликовано', choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='posts')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Женщина'
        verbose_name_plural = 'Женщины'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    published = PublishedManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
