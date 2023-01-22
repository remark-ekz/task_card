from django.contrib import admin

from .models import Project, Task, Gallery, Photo


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    '''Галерея'''
    list_display = ('name', 'created', 'id')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created',)
    search_fields = ('name', 'created')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    '''Изображения'''
    list_display = ('name', 'created', 'id',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'created',)
    search_fields = ('name', 'created',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    '''Проект'''
    list_display = (
        'id',
        'title',
        'slug',
        'description',
        'author',
        'created',
    )
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created',)
    # list_editable = ('description',)
    empty_value_display = '-пусто-'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    '''Задача'''
    list_display = (
        'id',
        'title',
        'text',
        'project',
        'author',
        'stage',
        'color',
        'file',
        'slug',
        'images',
    )
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('title', 'text', 'stage', 'color')
    empty_value_displaye = '-пусто-'
