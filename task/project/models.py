from django.contrib.auth import get_user_model
from django.db import models

NEW = 'nw'
WORK = 'wk'
CHECK = 'ck'
DONE = 'dn'
STAGES = (
    (NEW, 'New'),
    (WORK, 'Work'),
    (CHECK, 'Check'),
    (DONE, 'Done')
)
GREEN = 'gr'
YELLOW = 'yw'
RED = 'rd'
COLOR = (
    (GREEN, '#4bb481'),
    (YELLOW, '#dbc124'),
    (RED, '#d0472f')
)

User = get_user_model()


class Photo(models.Model):
    '''Фото'''
    name = models.CharField('Имя', max_length=50)
    image = models.ImageField('Фото', upload_to='task/')
    created = models.DateTimeField('Дата загрузки', auto_now_add=True)
    slug = models.SlugField('url', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Gallery(models.Model):
    '''Галерея'''
    name = models.CharField('Имя', max_length=100)
    photos = models.ManyToManyField(Photo, verbose_name='Фотографии')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Project(models.Model):
    '''Проект'''
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='project'
    )
    created = models.DateTimeField(
        'Дата создания проекта',
        auto_now_add=True
    )


class Task(models.Model):
    '''Задачи проекта'''
    title = models.CharField('Название', max_length=50)
    text = models.TextField(
        verbose_name='Задача',
        help_text='Введите текст задачи'
    )
    created = models.DateTimeField(
        'Дата создания задачи',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='task'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='task',
        verbose_name='Проект',
        help_text='Проект, к которому относится данная задача'
    )
    stage = models.CharField(
        'Этап',
        max_length=2,
        choices=STAGES,
        default=NEW
    )
    color = models.CharField(
        verbose_name='Важность',
        max_length=2,
        choices=COLOR,
        default=GREEN
    )
    file = models.FileField(
        verbose_name='Файл',
        upload_to='project_file/',
        blank=True,
        null=True
    )
    slug = models.SlugField('url', max_length=200, unique=True)
    images = models.ForeignKey(
        Gallery,
        verbose_name='Изображения',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title


class Comment(models.Model):
    '''Комментарии к задаче'''
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        verbose_name='Комментарий',
        related_name='comments',
    )
    text = models.TextField(
        'Текст комментария',
        help_text='Введите текст комментария'
    )
    created = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text
