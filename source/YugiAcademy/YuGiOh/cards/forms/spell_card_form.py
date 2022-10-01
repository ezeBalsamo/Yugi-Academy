from django import forms


class SpellCardForm(forms.Form):
    name = forms.CharField(label_suffix='', max_length=50)
    type = forms.CharField(label_suffix='', max_length=20)
    image = forms.ImageField(label_suffix='', required=False)
    description = forms.CharField(label_suffix='', max_length=8000, widget=forms.Textarea)
