from django.contrib import admin
from .models.frame_model import Frame
from model_filters.models import Genre, Date


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    # filter_horizontal = ['actor', 'filter_genre']
    # radio_fields = {'name': admin.VERTICAL}
    # list_display = [
    #     'name',
    #     'frame',
    # ]
    list_display = ['name', 'place']


# admin.site.register(Frame)
admin.site.register(Genre)
admin.site.register(Date)
