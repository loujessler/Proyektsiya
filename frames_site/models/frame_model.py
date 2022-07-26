from django.db import models
from taggit.managers import TaggableManager

from model_filters import models as filters
from model_films.models import Film, Actors


class Frame(models.Model):
    frame = models.ImageField(verbose_name='Кадр', upload_to="frames/")
    name = models.ForeignKey(Film, verbose_name='Название фильма', on_delete=models.CASCADE)
    # name = models.CharField(verbose_name='Название кадра', max_length=255)
    place = models.CharField(verbose_name='Место действия', max_length=255)
    camera = models.CharField(verbose_name='Камера', max_length=255)
    optics = models.CharField(verbose_name='Оптика', max_length=255)
    actors = models.ManyToManyField(Actors, verbose_name='Актеры')
    tags = TaggableManager()
    #     Filters
    filter_genre = models.ManyToManyField(filters.Genre, verbose_name='Жанр')
    filter_date = models.ManyToManyField(filters.Date, verbose_name='Время действия')

    def __str__(self, *args, **kwargs):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Название кадра'
        verbose_name_plural = 'Кадры'
