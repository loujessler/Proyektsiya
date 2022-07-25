from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.FramesView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('filter/', views.FrameFilterView.as_view(), name='filter'),
    path('json-filter/', views.JsonFrameFilterView.as_view(), name='json_filter'),
    path('<int:pk>/', views.FrameDetailView.as_view(), name='frame_detail'),
    path('film/film=<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
