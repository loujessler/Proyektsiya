from django.contrib import admin
from .models.frame_model import Frame
from model_filters.models import Genre, Date
from model_films.models import Film, Actors


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    filter_horizontal = ['actors', 'filter_genre', 'filter_date']
    # radio_fields = {'name': admin.VERTICAL}
    # list_display = [
    #     'name',
    #     'frame',
    # ]
    list_display = ['name', 'place']


# admin.site.register(Frame)
admin.site.register(Film)
admin.site.register(Actors)
admin.site.register(Genre)
admin.site.register(Date)
