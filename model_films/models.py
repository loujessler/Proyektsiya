from django.db import models
import datetime

from django_countries.fields import CountryField
from django_extensions.db.fields import AutoSlugField


class Film(models.Model):
    poster = models.ImageField(verbose_name='ПОСТЕР', upload_to='posters/')
    name = models.CharField(verbose_name='НАЗВАНИЕ', max_length=255)

    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    release_date = models.IntegerField(verbose_name='ГОД СОЗДАНИЯ',
                                       choices=YEAR_CHOICES,
                                       default=datetime.datetime.now().year,
                                       )

    country = CountryField(verbose_name='СТРАНА')
    directed = models.CharField(verbose_name='РЕЖИССЕР', max_length=255)
    cinematographer = models.CharField(verbose_name='ОПЕРАТОР', max_length=255)
    painter = models.CharField(verbose_name='ХУДОЖНИК', max_length=255)

    url = AutoSlugField(populate_from='id')

    def __str__(self, *args, **kwargs):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Actors(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)

    def __str__(self, *args, **kwargs):
        return "%s" % self.first_name

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'
