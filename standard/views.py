from django.views.generic import ListView, FormView
from django.db.models import Q
from django.shortcuts import  render

from .models import Standard
from .forms import StandardForm

class StandardFormView(FormView):
    form_class = StandardForm
    template_name = 'standard/standard_list.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        word_list = Standard.objects.filter(Q(word__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = word_list

        return render(self.request, self.template_name, context)
