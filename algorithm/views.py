from django.shortcuts import render
from django.views import generic

from .models import Combination

class IndexView(generic.ListView):
    template_name = 'algorithm/index.html'
    context_object_name = 'combinations'

    def get_queryset(self):
        return Combination.objects.all()
