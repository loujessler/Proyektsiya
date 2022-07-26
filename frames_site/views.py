from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from taggit.models import Tag
from model_filters import models as filters
from .models.frame_model import Frame
from model_films.models import Film


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
    paginate_by = 5  # Количество пагинаций

    # slug_field = 'name'


class TagsFramesView(ListView):
    model = Frame
    template_name = './frames_site/frame_tag_list.html'

    def get_queryset(self):
        return Frame.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


class FrameDetailView(GetFilters, DetailView):
    model = Frame
    slug_field = 'url'


class FilmDetailView(GetFilters, DetailView):
    model = Film
    slug_field = 'url'
    template_name = './frames_site/film_detail.html'

    def get_context_data(self, **kwargs):
        # xxx will be available in the template as the related objects
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        context['frames'] = Frame.objects.filter(name=self.get_object())
        return context


class FrameFilterView(GetFilters, ListView):
    def get_queryset(self):
        queryset = Frame.objects.filter(
            Q(filter_genre__in=self.request.GET.getlist('genre')) |
            Q(filter_date__in=self.request.GET.getlist('date'))
        ).distinct()
        return queryset


class JsonFrameFilterView(GetFilters, ListView):
    def get_queryset(self):
        queryset = Frame.objects.filter(
            Q(filter_genre__in=self.request.GET.getlist('genre', filters.Genre.objects.all())),
            Q(filter_date__in=self.request.GET.getlist('date', filters.Date.objects.all()))
        ).distinct().values('frame', 'name', 'id')
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        for item in queryset:
            item['name'] = list(Film.objects.filter(id=item['name']).values('name'))[0]['name']
        return JsonResponse({"frames": queryset}, safe=False)


# def index(request):
#     frames = Frame.objects.all()
#     context = {
#         'title': 'Main page',
#         'frames': frames
#     }
#     return render(request, './frames_site/frame_list.html', context)


def about(request):
    return render(request, './frames_site/about.html')
