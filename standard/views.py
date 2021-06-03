from .models import Standard
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render


class StandardList(generic.ListView):
    model = Standard
    ordering = ['id']
    paginate_by = 100