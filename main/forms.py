from django import forms


class TestarQuery(forms.Form):
    data_inicial = forms.CharField(help_text='Inserir a query aqui:',widget=forms.Textarea)
