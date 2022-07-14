from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from model_filters import models as filters
from .models.frame_model import Frame


class GetFilters:
    @staticmethod
    def get_genre():
        context = {
            'name': filters.Genre._meta.verbose_name,
            'objects': filters.Genre.objects.all()
        }
        return context
        # return filters.Genre.objects.all()

    @staticmethod
    def get_date():
        context = {
            'name': filters.Date._meta.verbose_name,
            'objects': filters.Date.objects.all()
        }
        return context


class FramesView(GetFilters, ListView):
    model = Frame
    queryset = Frame.objects.all()
    template_name = './frames_site/frame_list.html'
    # slug_field = 'name'


class FrameDetailView(GetFilters, DetailView):
    model = Frame
    slug_field = 'url'


class FrameFilterView(GetFilters, ListView):
    # template_name = './frames_site/frame_list.html'

    def get_queryset(self):
        queryset = Frame.objects.filter(
            Q(filter_genre__in=self.request.GET.getlist('genre')) |
            Q(filter_date__in=self.request.GET.getlist('date'))
        ).distinct()
        return queryset


# def index(request):
#     frames = Frame.objects.all()
#     context = {
#         'title': 'Main page',
#         'frames': frames
#     }
#     return render(request, './frames_site/frame_list.html', context)


def about(request):
    return render(request, './frames_site/about.html')
