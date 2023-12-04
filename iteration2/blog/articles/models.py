from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    author = models.CharField(max_length=200, null=True, verbose_name='Автор')


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название поста')
    text = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True, verbose_name='')
    thumb = models.ImageField(default="image.jpg", blank=True, verbose_name='Фотография')
    date = models.DateField(auto_now=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    """models.CASCADE - удаляет все объекты зависимой модели, если удалится объект из главной модели связанный с ними
       models.PROTECT - не даст удалить объекты зависимой модели, связанные с объектом главной модели.
       models.SET_NULL - оставит поля где выбраны объекты из связанных моделей пустыми"""

    """null=True - разрешает добавлять новые поля пустыми в таблице базы данных.
       blank=True - разрешает пропустить поле и не заполнять его при отправке или создании в форме"""


    def snippet(self):
        return self.text[:20] + '...read more'

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    age = models.IntegerField(null=True, verbose_name='Возраст')

    def __str__(self):
        return self.name
