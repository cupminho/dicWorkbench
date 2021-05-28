from .models import Document
from django.views import generic
from django.urls import reverse_lazy


class DocumentList(generic.ListView):
    model = Document
    ordering = ['id']


class DocumentCreate(generic.CreateView):
    model = Document
    fields = ['title', 'author', 'file']
    success_url = reverse_lazy('index')


class DocumentDetail(generic.DetailView):
    model = Document


class DocumentUpdate(generic.UpdateView):
    model = Document
    fields = ['title', 'author', 'file']
    success_url = reverse_lazy('index')


class DocumentDelete(generic.DeleteView):
    model = Document
    success_url = reverse_lazy('index')