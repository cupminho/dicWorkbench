from django import forms

class StandardForm(forms.Form):
    search_word = forms.CharField(label='검색어')

    def __init__(self, *args, **kwargs):
        super(StandardForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'