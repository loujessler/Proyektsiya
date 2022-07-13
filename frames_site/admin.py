from django.contrib import admin
from .models.frame_model import Frame
from model_filters.models import Genre, Date

admin.site.register(Frame)
admin.site.register(Genre)
admin.site.register(Date)
