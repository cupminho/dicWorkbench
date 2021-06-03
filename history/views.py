from .models import History
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render


class HistoryList(generic.ListView):
    model = History
    ordering = ['id']
