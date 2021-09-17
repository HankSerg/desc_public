from django.shortcuts import render
# from django.views import generic

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Auto

def auto_list(request):
    return render(request, 'auto/auto_list.html', {})

class AutoListView(ListView):
    # template_name = 'auto/auto_list.html'
    model = Auto

