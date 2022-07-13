from django.shortcuts import render
from .models.frame_model import Frame




def index(request):
    frames = Frame.objects.all()
    context = {
        'title': 'Main page',
        'frames': frames
    }
    return render(request, './frames_site/index.html', context)


def about(request):
    return render(request, './frames_site/about.html')
