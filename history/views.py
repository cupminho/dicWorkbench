from django.views.generic import FormView
from django.shortcuts import render
from django.db.models import Q

from .forms import HistoryForm
from .models import History

class HistoryFormView(FormView):
    form_class = HistoryForm
    template_name = 'history/history_list.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        word_list = History.objects.filter(Q(word__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = word_list

        return render(self.request, self.template_name, context)