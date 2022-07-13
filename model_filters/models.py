from django.db import models


class Filter(models.Model):
    name = models.CharField('Имя', max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class Genre(Filter):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Date(Filter):
    class Meta:
        verbose_name = 'Время действия'
        verbose_name_plural = 'Времена действий'


class Made(Filter):
    class Meta:
        verbose_name = 'Год производства'
        verbose_name_plural = 'Года производства'


class Ratio(Filter):
    class Meta:
        verbose_name = 'Соотношение стороны'
        verbose_name_plural = 'Соотношение сторон'


class Format(Filter):
    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'


class Color(Filter):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Inter(Filter):
    class Meta:
        verbose_name = 'Интерьер'
        verbose_name_plural = 'Интерьеры'


class Time(Filter):
    class Meta:
        verbose_name = 'Время суток'
        verbose_name_plural = 'Время суток'


class Compos(Filter):
    class Meta:
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'


class Angle(Filter):
    class Meta:
        verbose_name = 'Угол'
        verbose_name_plural = 'Уголы'


class Plans(Filter):
    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'


class Person(Filter):
    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Sex(Filter):
    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пола'


class View(Filter):
    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'


class Focus(Filter):
    class Meta:
        verbose_name = 'Фокус'
        verbose_name_plural = 'Фокусы'


class Light(Filter):
    class Meta:
        verbose_name = 'Свет'
        verbose_name_plural = 'Света'


class Type(Filter):
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Seasons(Filter):
    class Meta:
        verbose_name = 'Время года'
        verbose_name_plural = 'Времена года'
