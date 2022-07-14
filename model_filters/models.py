from django.db import models

#
# class Filter(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Date(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Время действия'
        verbose_name_plural = 'Времена действий'

#
# class Made(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Год производства'
#         verbose_name_plural = 'Года производства'
#
#
# class Ratio(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Соотношение стороны'
#         verbose_name_plural = 'Соотношение сторон'
#
#
# class Format(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Формат'
#         verbose_name_plural = 'Форматы'
#
#
# class Color(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Цвет'
#         verbose_name_plural = 'Цвета'
#
#
# class Inter(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Интерьер'
#         verbose_name_plural = 'Интерьеры'
#
#
# class Time(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Время суток'
#         verbose_name_plural = 'Время суток'
#
#
# class Compos(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Композиция'
#         verbose_name_plural = 'Композиции'
#
#
# class Angle(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Угол'
#         verbose_name_plural = 'Уголы'
#
#
# class Plans(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'План'
#         verbose_name_plural = 'Планы'
#
#
# class Person(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Персонаж'
#         verbose_name_plural = 'Персонажи'
#
#
# class Sex(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Пол'
#         verbose_name_plural = 'Пола'
#
#
# class View(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Вид'
#         verbose_name_plural = 'Виды'
#
#
# class Focus(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Фокус'
#         verbose_name_plural = 'Фокусы'
#
#
# class Light(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Свет'
#         verbose_name_plural = 'Света'
#
#
# class Type(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Тип'
#         verbose_name_plural = 'Типы'
#
#
# class Seasons(models.Model):
#     name = models.CharField(verbose_name='Имя', max_length=100)
#     url = models.SlugField(max_length=160, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Время года'
#         verbose_name_plural = 'Времена года'
