from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from . import models
# Create your views here.

class IndexView(TemplateView):
    template_name='basic/index.html'

class ThListView(ListView):
    model=models.Thetare

class ThDetailView(DetailView):
    context_object_name='obj'
    model=models.Thetare
    template_name = 'basic/thetare_detail.html'

class ThCreateView(CreateView):
    fields=('name','location')
    model=models.Thetare

class ThUpdateView(UpdateView):
    fields=('location',)
    model=models.Thetare

class ThDeleteView(DeleteView):
     model=models.Thetare
     success_url=reverse_lazy("basic:th_list")
