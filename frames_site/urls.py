from django.urls import path
from . import views

urlpatterns = [
    path('', views.FramesView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('filter/', views.FrameFilterView.as_view(), name='filter'),
    path('<int:pk>/', views.FrameDetailView.as_view(), name='frame_detail'),
]
